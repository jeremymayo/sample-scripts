import tableauserverclient as TSC
import requests
import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level="INFO")

TOKEN_NAME = 'PAT-0'
TOKEN_VALUE = 'edduiKuERgmpzvfGUW3Hpg==:vumBWqoS0Y2rqGq34a8GCbjMB8HP9ARj'
SITENAME = 'murrayslanding'
SERVER = 'https://prod-useast-a.online.tableau.com'

tableau_auth = TSC.PersonalAccessTokenAuth(TOKEN_NAME, TOKEN_VALUE, SITENAME)
server = TSC.Server(SERVER, use_server_version=True)
server.auth.sign_in(tableau_auth)
token = server.auth_token

print("X-Tableau-Auth: "+server.auth_token, "\n Site_ID: "+server.site_id, "\n With User_ID: "+server.user_id)

url = "https://prod-useast-a.online.tableau.com/api/3.21/sites/51a8938b-b42f-49a1-8f73-0d9f78bde5ce/connected-applications/"

payload = {}
headers = {
  'X-Tableau-Auth':token}

response = requests.request("GET", url, headers=headers, data=payload)
r=response.text

print(r)

xml_response = ET.fromstring(r)
total_CA = xml_response.findall('.//t:secret id', namespaces=xmlns)

print(total_CA)

