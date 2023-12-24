# https://learn.microsoft.com/en-us/entra/msal/python/

from msal import PublicClientApplication
import requests
import time

clientid = "bbeb8d4a-f4f4-41e6-9ab7-f760a288d966"
authority = "https://login.microsoftonline.com/common"

app = PublicClientApplication(
    clientid,
    authority=authority)

result = None

# We now check the cache to see
# whether we already have some accounts that the end user already used to sign in before.
accounts = app.get_accounts()
if accounts:
    # If so, you could then somehow display these accounts and let end user choose
    print("Pick the account you want to use to proceed:")
    for a in accounts:
        print(a["username"])
    # Assuming the end user chose this one
    chosen = accounts[0]
    # Now let's try to find a token in cache for this account
    result = app.acquire_token_silent(["User.Read"], account=chosen)

if not result:
    # So no suitable token exists in cache. Let's get a new one from Azure AD.
    result = app.acquire_token_interactive(scopes=["User.Read"])
if "access_token" in result:
    print(result["access_token"])  # Yay!

else:
    print(result.get("error"))
    print(result.get("error_description"))
    print(result.get("correlation_id"))  # You may need this when reporting a bug

## Trying to download the page now:
IMAGE_URL = 'https://heavily-just-bee.ngrok-free.app/dashboard/'

if 'access_token' in result:
    access_token = result['access_token']
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(IMAGE_URL, headers=headers, allow_redirects=True)
    time.sleep(6)
    if response.status_code == 200:
        with open('downloaded.html', 'wb') as f:
            f.write(response.content)
            print(response.url)
        print("Image downloaded successfully as 'downloaded_image.png'")
    else:
        print("Failed to download the image")
else:
    print("Failed to acquire access token")
