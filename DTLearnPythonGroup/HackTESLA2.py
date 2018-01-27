import requests
import teslajsonpy
import bs4
import json


"""
shawn的车 远程 id   ：
20180631175982286
"""

url = 'https://owner-api.teslamotors.com/oauth/token'
MOCkSERVERURL1 = "https://private-anon-944de4b041-timdorr.apiary-mock.com/oauth/token"
params = {
  "grant_type": "password",
  "client_id": "81527cff06843c8634fdc09e8ac0abefb46ac849f38fe1e431c2ef2106796384",
  "client_secret": "c7257eb71a564034f9419ee651c7d0e5f7aa6bfbd18bafb5c5c033b093bb2fa3",
  "email": "Wangxi@tesla.com",
  "password": "Wanx@2wanx"}
request1 = requests.post(url, data= params).content.decode('utf8')

# request1 = request(url, data=params)
print(request1)
print(type(request1))
# print(request1.headers)
# print(request1.content)
print('---------第一步完成啦-----取得token-----')

dic1 = json.loads(request1)
print(dic1)
token_live = dic1['access_token']
print(token_live)
# # token_full = "Authorization", ":", "Bearer "
header_got = {'Authorization': 'Bearer %s' % token_live}
session = requests.Session()
Vurl = "https://owner-api.teslamotors.com/api/1/vehicles"
debug = "https://private-anon-944de4b041-timdorr.apiary-proxy.com/api/1/vehicles"
request2 = session.get(Vurl, headers = header_got).content
print(request2)

print('---------第二步完成啦-----拿到车辆编号-----')
# vehicle  = teslajsonpy.Lock
# v = teslajsonpy.ChargerConnectionSensor.has_battery()

# print(vehicle)
locationURL = "https://owner-api.teslamotors.com/api/1/vehicles/20180631175982286/data_request/vehicle_state"
locationURL2 = "https://owner-api.teslamotors.com/api/1/vehicles/20180631175982286/data_request/drive_state"
locationURL3 = "https://owner-api.teslamotors.com/api/1/vehicles/20180631175982286/data_request/gui_settings"
locationURL4 = "https://owner-api.teslamotors.com/api/1/vehicles/20180631175982286/data_request/charge_state"
locationURL5 = "https://owner-api.teslamotors.com/api/1/vehicles/20180631175982286/data_request/climate_state"
unlock = "https://owner-api.teslamotors.com/api/1/vehicles/20180631175982286/command/door_unlock"
horn = "https://owner-api.teslamotors.com/api/1/vehicles/20180631175982286/command/honk_horn"
flashlight = "https://owner-api.teslamotors.com/api/1/vehicles/20180631175982286/command/flash_lights"
hornMockserver = "https://private-anon-944de4b041-timdorr.apiary-mock.com/api/1/vehicles/20180631175982286/command/honk_horn"
chargeport = "https://owner-api.teslamotors.com/api/1/vehicles/20180631175982286/command/charge_port_door_open"
wakeup = "https://owner-api.teslamotors.com/api/1/vehicles/20180631175982286/wake_up"
remoteStart = "https://owner-api.teslamotors.com/api/1/vehicles/20180631175982286/command/remote_start_drive?password=Wanx@2wanx"
# request3 = session.get(hornMockserver, headers = header_got).content
# print(request3)

print('---------第三步完成啦-----取得车辆状态信息-----')

def VehicleData(url, HEAD):
  request = session.post(url, headers = HEAD)
  print(request.content)
print('------开始玩--------')
print(VehicleData(wakeup, header_got))
print(VehicleData(chargeport, header_got))
print(VehicleData(unlock, header_got))
# print(VehicleData(flashlight, header_got))
print(VehicleData(remoteStart, header_got))
print('------玩够了--------')

#
# eletrlevel = teslajsonpy.Battery.battery_level('20180631175982286')
# print(eletrlevel)
