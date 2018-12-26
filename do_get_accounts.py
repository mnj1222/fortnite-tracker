import json
import requests

api_token = '2bcbebe8-e0cb-4f2f-989b-082ec9ef97f2'
api_url_base = 'https://api.fortnitetracker.com/v1/profile/'

headers = {'Content-Type': 'application/json',
           'TRN-Api-Key': (api_token)
           }

platform = 'xbox'
epic_name = 'mnj1222'

def get_account_info():

    api_url = '{}{}/{}'.format(api_url_base, platform, epic_name)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

account_info = get_account_info()

if account_info is not None:
    print("Here's your info: ")
    for k, v in account_info.items():
        print('{0}:{1}'.format(k, v))

else:
    print('[!] Request Failed')
