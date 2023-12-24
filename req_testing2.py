from flask import Flask, request, redirect
import requests
from msal import PublicClientApplication

# Azure AD app information
CLIENT_ID = 'bbeb8d4a-f4f4-41e6-9ab7-f760a288d966'
AUTHORITY = ' https://login.microsoftonline.com/common'
SCOPE = ['User.Read']
REDIRECT_PATH = '/get_token'

# Your image URL
IMAGE_URL = 'https://coherent-toad-bursting.ngrok-free.app/static/base/images/logo.png?v=a2a176ee3cee251ffddf5fa21fe8e43727a9e5f87a06f9c91ad7b776d9e9d3d5e0159c16cc188a3965e00375fb4bc336c16067c688f5040c0c2d4bfdb852a9e4'

app = Flask(__name__)

@app.route('/')
def login():
    pca = PublicClientApplication(CLIENT_ID, authority=AUTHORITY)
    login_url = pca.get_authorization_request_url(scopes=SCOPE, redirect_uri=request.url_root[:-1] + REDIRECT_PATH)
    return redirect(login_url)

@app.route(REDIRECT_PATH)
def get_token():
    pca = PublicClientApplication(CLIENT_ID, authority=AUTHORITY)
    token = pca.acquire_token_by_authorization_code(request.args['code'], scopes=SCOPE, redirect_uri=request.url_root[:-1] + REDIRECT_PATH)
    if 'access_token' in token:
        access_token = token['access_token']
        headers = {'Authorization': 'Bearer ' + access_token}
        response = requests.get(IMAGE_URL, headers=headers)
        if response.status_code == 200:
            with open('downloaded_image.jpg', 'wb') as f:
                f.write(response.content)
            return 'Image downloaded successfully as "downloaded_image.jpg"'
    return 'Failed to download the image'

if __name__ == '__main__':
    app.run(debug=True)
