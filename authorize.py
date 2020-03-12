from requests_oauthlib import OAuth2Session
from temp_token import client_id, client_secret

def get_token():
    
    redirect_uri = 'https://localhost:8080/'

    scope = 'data:read_write,data:delete'

    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)

    authorization_url, state = oauth.authorization_url('https://todoist.com/oauth/authorize')
    print(f'Please go to {authorization_url} and authorize access.')
    authorization_response = input('Enter the full callback URL\n')

    token = oauth.fetch_token(
        'https://todoist.com/oauth/access_token',
        authorization_response=authorization_response,
        client_secret=client_secret)

    return token['access_token']