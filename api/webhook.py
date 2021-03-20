import requests
import json


webhook_url = 'https://webhook.site/ce78ca44-ecf6-439e-88a8-c3c46967e7ea'
data = {'firstname': 'mehmetcan',
        'lastname': 'ozkulekci'}


r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
