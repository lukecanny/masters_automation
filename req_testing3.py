from msal import PublicClientApplication
import requests

# Azure AD app information
CLIENT_ID = 'a7230c03-9c28-4953-b70e-bf45b985f57d'

AUTHORITY = 'https://login.microsoftonline.com/common'
SCOPE = ['User.Read', 'Files.Read.All']

# Your image URL
IMAGE_URL = 'https://example.com/image.jpg'

app = PublicClientApplication(CLIENT_ID, authority=AUTHORITY)

# Initiate device code flow
device_flow = app.initiate_device_flow(scopes=SCOPE)
print(device_flow['message'])

# Complete authentication using device code
token = app.acquire_token_by_device_flow(device_flow)

if 'access_token' in token:
    access_token = token['access_token']
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(IMAGE_URL, headers=headers)

    if response.status_code == 200:
        with open('downloaded_image.jpg', 'wb') as f:
            f.write(response.content)
        print("Image downloaded successfully as 'downloaded_image.jpg'")
    else:
        print("Failed to download the image")
else:
    print("Failed to acquire access token")
