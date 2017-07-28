#sudo pip install metoffer
import metoffer
import time
import urllib
import sys
sys.path.append('/home/ubuntu')
import APIKeyManager
MetDataPointAPIKey = APIKeyManager.MetDataPoint
import pprint

TSbaseURL = 'https://api.thingspeak.com/update?api_key=CA3YNXBUBJTKRLVH'

M = metoffer.MetOffer(MetDataPointAPIKey)
#x = M.nearest_loc_forecast(51.4033, -0.3375, metoffer.THREE_HOURLY)

while 1:
	#Get some observations
	x = M.nearest_loc_obs(51.4033, -0.3375)
	y = metoffer.parse_val(x)
	print(y.data_date)	
	TAmbient = str(y.data[0]["Temperature"][0])
	pAmbient = str(y.data[0]["Pressure"][0])
#	vWind = str(y.data[0]["Pressure"][0])
	pprint(y.data)
	urlstring = TSbaseURL  + "&field1=" + Temp + "&field2=" + Pressure
	f = urllib.urlopen(urlstring)
	print f.read()
	print("Temperature is " + str(y.data[0]["Temperature"][0]))
	time.sleep(20)
