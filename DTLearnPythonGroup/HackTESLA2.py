import requests
import teslajsonpy

url = 'https://owner-api.teslamotors.com/oauth/token'
MOCSERVERURL = "https://private-anon-944de4b041-timdorr.apiary-mock.com/oauth/token"
params = {"grant_type":"password","OWNERAPI_CLIENT_ID": "81527cff06843c8634fdc09e8ac0abefb46ac849f38fe1e431c2ef2106796384",
  "OWNERAPI_CLIENT_SECRET": "c7257eb71a564034f9419ee651c7d0e5f7aa6bfbd18bafb5c5c033b093bb2fa3", "email":"Wangxi@tesla.com", "password":"Wanx@2wanx" }
request1 = requests.post(MOCSERVERURL, data= params)
print(request1.headers)
print(request1.content)
Vurl = "https://owner-api.teslamotors.com/api/1/vehicles"

vehicle  = requests.get(Vurl, )
# v = teslajsonpy.ChargerConnectionSensor.has_battery()
#
print(vehicle)