import tableauserverclient as TSC
import requests

# Tableau Server information
server = 'https://prod-useast-a.online.tableau.com' # Check the pod you are on
TOKEN_NAME = '' # Create/copy a PAT
TOKEN_VALUE = '' # Paste PAT token value
SITE = '' # Grab your site name

# Create Tableau Server client
tableau_auth = TSC.PersonalAccessTokenAuth(TOKEN_NAME, TOKEN_VALUE, SITE)
s = TSC.Server(server, use_server_version=True)
s.auth.sign_in(tableau_auth)

# Grab values from sign-in request
token = s.auth_token
site_id = s.site_id
print("X-Tableau-Auth: "+token, "\n Site_ID: "+site_id, "\n With User_ID: "+s.user_id)

# Set headers for REST Calls later
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-Tableau-Auth':token
}

# Get all connected apps
connected_apps_url = f"{server}/api/3.21/sites/{site_id}/connected-applications"
connected_apps_response = requests.get(connected_apps_url, headers=headers)
connected_apps = connected_apps_response.json()['connectedApplications']['connectedApplication']

print(connected_apps)

# Iterate through connected apps
for app in connected_apps:
    for secret_entry in app["secret"]:
        secret_id = secret_entry["id"]
        client_id = app['clientId']
        #print("ID:", secret_entry["id"])
        #print("Client ID:", app["clientId"])

        # Delete the secret ID
        delete_secret_url = f"{server}/api/3.21/sites/{site_id}/connected-applications/{client_id}/secrets/{secret_id}"
        requests.delete(delete_secret_url, headers=headers)

        # Generate a new secret ID
        new_secret_url = f"{server}/api/3.21/sites/{site_id}/connected-applications/{client_id}/secrets"
        new_secret_response = requests.post(new_secret_url, headers=headers)
        new_secret = new_secret_response.json()['connectedApplicationSecret']
#
#     # Print information about the connected app and its new secret
    print(f"Connected App ID: {client_id}")
    print("Deleted old secret ID")
    print("New Secret ID:", new_secret)
    print("\n")
