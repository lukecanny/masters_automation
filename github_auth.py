from flask import Flask, request, redirect, jsonify
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

app = Flask(__name__)

# GitHub OAuth details
client_id = '8f51fc9d0680a505043c'
redirect_uri = 'https://bd33-89-127-10-188.ngrok-free.app/callback'  # Local callback URL
scope = ['read:user']  # Adjust scopes as needed for your use case
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'


@app.route('/')
def index():
    # Redirect to GitHub for authorization
    github = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
    authorization_url, state = github.authorization_url(authorization_base_url)
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    # Handle the callback from GitHub
    github = OAuth2Session(client_id, redirect_uri=redirect_uri)
    token = github.fetch_token(token_url, client_secret=None, authorization_response=request.url)
    
    # Use the access token for authenticated requests
    headers = {
        'Authorization': f"Bearer {token['access_token']}",
        'Accept': 'application/json'
    }
    
    user_info_response = github.get('https://api.github.com/user', headers=headers)
    
    if user_info_response.status_code == 200:
        user_info = user_info_response.json()
        return jsonify(user_info)
    else:
        return f"Error: {user_info_response.status_code} - {user_info_response.text}"

if __name__ == '__main__':
    app.run(debug=True)
