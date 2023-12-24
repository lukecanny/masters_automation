import requests
import webbrowser
from msal import PublicClientApplication

# Your Azure AD app information
client_id = 'a7230c03-9c28-4953-b70e-bf45b985f57d'
authority = 'https://login.microsoftonline.com/f8cdef31-a31e-4b4a-93e4-5f571e91255a'
scope = ['User.Read']

# Your image URL
image_url = 'https://coherent-toad-bursting.ngrok-free.app/static/base/images/logo.png?v=a2a176ee3cee251ffddf5fa21fe8e43727a9e5f87a06f9c91ad7b776d9e9d3d5e0159c16cc188a3965e00375fb4bc336c16067c688f5040c0c2d4bfdb852a9e4'

# Create a PublicClientApplication instance
app = PublicClientApplication(client_id)

# Get the URL for interactive login
login_url = app.get_authorization_request_url(scopes=scope)

# Open a browser for user login
print(login_url)
webbrowser.open(login_url)

# Wait for the user to finish the login process and get the redirect URL
redirect_response = input("Enter the redirect URL: ")

# Get the access token using the redirect URL
result = app.acquire_token_by_authorization_code(redirect_response, scopes=scope)

# If successful, download the image using the access token
if 'access_token' in result:
    access_token = result['access_token']
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(image_url, headers=headers)

    # Save the image if the download is successful
    if response.status_code == 200:
        with open('downloaded_image.jpg', 'wb') as f:
            f.write(response.content)
        print("Image downloaded successfully as 'downloaded_image.jpg'")
    else:
        print("Failed to download the image")
else:
    print("Login unsuccessful")
