import requests
import teslajsonpy
import bs4

url = 'https://owner-api.teslamotors.com/oauth/token'
MOCkSERVERURL1 = "https://private-anon-944de4b041-timdorr.apiary-mock.com/oauth/token"
params = {
  "grant_type": "password",
  "client_id": "81527cff06843c8634fdc09e8ac0abefb46ac849f38fe1e431c2ef2106796384",
  "client_secret": "c7257eb71a564034f9419ee651c7d0e5f7aa6bfbd18bafb5c5c033b093bb2fa3",
  "email": "Wangxi@tesla.com",
  "password": "Wanx@2wanx"}
request1 = requests.post(url, data= params)

# request1 = request(url, data=params)
print(request1)
print(request1.headers)
print(request1.content)

# header_got = {'Server': 'Cowboy', 'Connection': 'keep-alive', 'X-Apiary-Ratelimit-Limit': '120', 'X-Apiary-Ratelimit-Remaining': '119', 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'OPTIONS,GET,HEAD,POST,PUT,DELETE,TRACE,CONNECT', 'Access-Control-Max-Age': '10', 'X-Apiary-Transaction-Id': '5a6c17a08e065007006b247c', 'Content-Length': '139', 'Date': 'Sat, 27 Jan 2018 06:09:36 GMT', 'Via': '1.1 vegur'}
# mockserverurl2= "https://private-anon-944de4b041-timdorr.apiary-mock.com/api/1/vehicles"
# Vurl = "https://owner-api.teslamotors.com/api/1/vehicles"
#
# request2 = requests.get(Vurl, params=header_got)
#
# print(request2.content)

# vehicle  = teslajsonpy.Lock
# v = teslajsonpy.ChargerConnectionSensor.has_battery()

# print(vehicle)