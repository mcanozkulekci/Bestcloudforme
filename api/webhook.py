import requests
import json


webhook_url = 'https://webhook.site/45801a49-a6f2-4802-bd56-ad8b61a475b7'
data = {'firstname': 'mehmetcan',
        'lastname': 'ozkulekci'}


r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
