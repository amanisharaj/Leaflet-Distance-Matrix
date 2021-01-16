import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api'
data = {
    'origin':'umcc hyderabad',
    'destination':'thrissur kerala'
}
r=requests.get(BASE_URL+ENDPOINT, data=json.dumps(data))
data=r.json()
print('Origin: ',data['origin_addresses'][0])
print('Destination: ',data['destination_addresses'][0])
print('Distance: ',data['rows'][0]['elements'][0]['distance']['text'])
print('Time: ',data['rows'][0]['elements'][0]['duration']['text'])

