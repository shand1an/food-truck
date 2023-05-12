import requests
import json

url = "https://api.yelp.com/v3/businesses/search"

querystring = {"latitude":"37.3533530886479","longitude":"-122.013784749846","radius":""}

payload = "{\n\theaders: {\n\t\t\"Authorization\": \"Bearer UOG4x25kRFF6bWtb-Sq8wP2J3mD9NZfSKbKdweHWO0nC7C-A5-ROuVH30RQ7_2tQrYpIAvOuIjI9OBtON8BtUb49la3UGXmc0B_tgTddC14pp0ceMTSHY_xxnyhtWXYx\"\n\t},\n\tquery: {\n\t\tlocation: \"mountain view,ca\"\n\t}\n}"
headers = {
    'content-type': "application/json",
    'authorization': "Bearer 8YforbPtNAm3KCKY3EnxohSVsa-tbLMFNOjlLQkSMxycC8vbnvy-jT79OhSW__fSZEcpUxEGuJ4kZu_RhA_QSCvKSn5QUnQpNCIoMWP5DcYo5ytu36GYEn36Xml2WXYx",
    'cache-control': "no-cache",
    'postman-token': "f86e26d4-c0d1-dc93-86a7-fded08320b90"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

#print(response.text)

#response = response.replace("'", '"')
response = json.loads(response.text)
for truck in response['businesses']:
    print(str(truck['id']),str(truck['coordinates']['latitude']),str(truck['coordinates']['longitude']))
