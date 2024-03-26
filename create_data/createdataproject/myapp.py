# Consider this data is coming from frontend/ client data

import requests
from rest_framework.utils import json

URL = "http://127.0.0.1:8000/stucreate/"

# this data is in python
data = {
    'name': 'Priyanka',
    'roll': 101,
    'city': 'Pune'
}
# convert into json

json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
# r= return request("post", url, data=data)
data = r.json()
print(data)
