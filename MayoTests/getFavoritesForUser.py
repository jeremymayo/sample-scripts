import requests
import xml.etree.ElementTree as ET

url = "http://ec2amaz-4bljnfv/api/3.15/sites/ad791c31-f759-4018-878f-a3c8cde7cb0e/favorites/66fc1f8c-8e09-4923-820a-0ac7cf4fe68c"

payload={}
headers = {
  'X-Tableau-Auth': 'Sn2DviEQSESgDGCOZ9l4Fw|PzXJc37H0Ypx8eDDX6y7gy3pBdAhBZd7'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

xmlDict = {}
root = ET.fromstring(response.content)
# for child in root.iter('*'):
#     print(child.tag)

for sitemap in root:
    children = sitemap.getchildren()
    xmlDict[children[0].text] = children[1].text
print(xmlDict)
