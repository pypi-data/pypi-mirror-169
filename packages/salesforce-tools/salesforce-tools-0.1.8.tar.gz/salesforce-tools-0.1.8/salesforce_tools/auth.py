import json
from requests_oauthlib import OAuth2Session
from oauthlib.common import to_unicode
from oauthlib.oauth2 import WebApplicationClient, BackendApplicationClient
from oauthlib.oauth2.rfc6749.parameters import prepare_token_request
from datetime import datetime, timedelta
import webbrowser
from salesforce_tools.oauth_server import CallbackServer
from urllib.parse import urlsplit, urljoin
import os
from typing import Callable
import jwt

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"
AUTH_URL = 'https://login.salesforce.com'
AUTH_REL_URL = '/services/oauth2/authorize'
TOKEN_REL_URL = '/services/oauth2/token'
TOKEN_LIFE = timedelta(hours=2)


def login(client_id: str = None, client_secret: str = None, token: dict = None,
          token_updater: Callable = lambda x: True, callback_port: int = 8000,
          force_login: bool = False, scope: str = 'refresh_token openid web full',
          auth_url: str = AUTH_URL, redirect_url: str = None, private_key: str = None,
          private_key_filename: str = None):
    auth_code_url = urljoin(auth_url, AUTH_REL_URL)
    token_url = urljoin(auth_code_url, TOKEN_REL_URL)
    redirect_url = redirect_url or f"http://localhost:{callback_port}/callback"
    if private_key or private_key_filename:
        client = SalesforceJWTClient(client_id,
                                     auth_url,
                                     private_key_filename=private_key_filename,
                                     private_key=private_key
                                     )
        salesforce = salesforce_compliance_fix(
            SalesforceOAuth2Session(client=client, auto_refresh_url=token_url, token_updater=token_updater)
        )
        salesforce.fetch_token(token_url)
        if token_updater:
            token_updater(salesforce.token)
    else:
        salesforce = salesforce_compliance_fix(
            SalesforceOAuth2Session(token=token,
                          client=SalesforceOAuthClient(client_id),
                          redirect_uri=redirect_url,
                          scope=scope if not token else None,
                          auto_refresh_url=token_url,
                          auto_refresh_kwargs={k: v for k, v in
                                               {'client_id': client_id,
                                                'client_secret': client_secret}.items()
                                               if v},
                          token_updater=token_updater
                          )
        )
        if force_login or not token or not token.get('refresh_token'):
            authorization_url, state = salesforce.authorization_url(auth_code_url)
            webbrowser.open(authorization_url, new=1)
            authorization_response = CallbackServer().get_auth(port=callback_port)
            ruri = urlsplit(redirect_url)
            ruri_base_url = ruri.scheme + '://' + ruri.netloc
            authorization_response = urljoin(ruri_base_url, authorization_response)
            salesforce.fetch_token(token_url, client_secret=client_secret,
                                   authorization_response=authorization_response)
            if token_updater:
                token_updater(salesforce.token)
    return salesforce


def salesforce_compliance_fix(sess):
    token = ''

    def _compliance_fix(response):
        token = json.loads(response.text)
        if token.get('issued_at'):
            iat = int(token["issued_at"]) / 1000
            token["expires_in"] = (datetime.fromtimestamp(iat) + TOKEN_LIFE - datetime.now()).seconds
        else:
            token["expires_in"] = TOKEN_LIFE.seconds
        fixed_token = json.dumps(token)
        response._content = to_unicode(fixed_token).encode("utf-8")

        return response

    sess.register_compliance_hook("access_token_response", _compliance_fix)
    sess.register_compliance_hook("refresh_token_response", _compliance_fix)

    return sess


class SalesforceOAuthClient(WebApplicationClient):
    def _add_bearer_token(self, uri, http_method='GET', body=None,
                          headers=None, token_placement=None):
        uri, headers, body = super()._add_bearer_token(
            uri,
            http_method=http_method,
            body=body,
            headers=headers,
            token_placement=token_placement
        )

        headers['X-SFDC-Session'] = self.token.get('access_token')
        return uri, headers, body


class SalesforceJWTClient(BackendApplicationClient):
    grant_type = 'urn:ietf:params:oauth:grant-type:jwt-bearer'

    def __init__(self, client_id,
                 audience: str = None,
                 private_key_filename: str = None,
                 private_key: str = None,
                 **kwargs):
        super().__init__(client_id, **kwargs)
        self.audience = audience
        self.private_key = private_key
        if private_key_filename:
            with open(private_key_filename, mode='r') as f:
                self.private_key = ''.join(f.readlines())

    def prepare_refresh_body(self, body: str = '', **kwargs):
        return self.prepare_request_body(body)

    def prepare_request_body(self, body: str = '', **kwargs):
        claims = {"iss": self.client_id,
                  "sub": "arroyo2207@fionta.com",
                  "aud": self.audience,
                  "exp": int(datetime.now().timestamp()) + 60 * 3
                  }

        signed_claims = jwt.encode(claims, self.private_key, "RS256")
        return prepare_token_request(self.grant_type, assertion=signed_claims, format="json", **kwargs)

    def _add_bearer_token(self, uri, http_method='GET', body=None,
                          headers=None, token_placement=None):
        uri, headers, body = super()._add_bearer_token(
            uri,
            http_method=http_method,
            body=body,
            headers=headers,
            token_placement=token_placement
        )

        headers['X-SFDC-Session'] = self.token.get('access_token')
        return uri, headers, body


class SalesforceOAuth2Session(OAuth2Session):
    def __init__(self, instance_url=None, *args, **kwargs):
        super(SalesforceOAuth2Session, self).__init__(*args, **kwargs)
        self.instance_url = instance_url

    def request(self, method, url, *args, **kwargs):
        url = urljoin(self.instance_url, url)
        return super(SalesforceOAuth2Session, self).request(method, url, *args, **kwargs)

