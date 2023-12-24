from msal import PublicClientApplication
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    chosen = accounts[0]  # Select the first account as an example
    # Now let's try to find a token in cache for this account
    result = app.acquire_token_silent(["User.Read"], account=chosen)

if not result:
    # So no suitable token exists in cache. Let's get a new one from Azure AD.
    result = app.acquire_token_interactive(scopes=["User.Read"])

if "access_token" in result:
    print(result["access_token"])  # Yay!

    # Use Selenium to download the page now:
    IMAGE_URL = 'https://coherent-toad-bursting.ngrok-free.app/static/base/images/logo.png?v=a2a176ee3cee251ffddf5fa21fe8e43727a9e5f87a06f9c91ad7b776d9e9d3d5e0159c16cc188a3965e00375fb4bc336c16067c688f5040c0c2d4bfdb852a9e4'

    # Create a new instance of a Chrome webdriver (you'll need chromedriver installed)
    driver = webdriver.Chrome()

    driver.get(IMAGE_URL)

    # Load the page with headers containing the access token
    # driver.get(IMAGE_URL)
    # driver.add_cookie({'name': 'access_token', 'value': result["access_token"]})
    
    # Explicitly wait for the document.readyState to be complete
    wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
    wait.until(EC.presence_of_element_located((By.XPATH, '//body123')))  # Wait for the body to be present
    
    
    # Save the HTML content of the page
    with open('downloaded.html', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)
    print("Page downloaded successfully as 'downloaded.html'")
    
    # Close the browser session
    driver.quit()
else:
    print("Failed to acquire access token")
