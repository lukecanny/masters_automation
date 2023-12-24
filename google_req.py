from google_auth_oauthlib.flow import InstalledAppFlow

# Replace with your client ID and scopes
CLIENT_ID = 'your_client_id'
SCOPES = ['scope1', 'scope2']  # Replace with the required scopes

# Set up the flow without a client secret
flow = InstalledAppFlow.from_client_config(
    {'installed': {'client_id': CLIENT_ID}}, scopes=SCOPES)

# Get authorization URL
auth_url, _ = flow.authorization_url(access_type='offline', prompt='consent')

# Redirect the user to auth_url and get the authorization code (manual step)

# Exchange authorization code for access token
code = 'authorization_code_received_from_redirect'  # Replace with the received authorization code
flow.fetch_token(code=code)

# Use the access token to make requests to the website's API
access_token = flow.credentials.token
# Make API requests using the obtained access token
