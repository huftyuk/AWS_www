#sudo pip install metoffer
import metoffer
import time
import datetime
import urllib
import sys
sys.path.append('/home/ubuntu')
import APIKeyManager
MetDataPointAPIKey = APIKeyManager.MetDataPoint
import pprint

TSbaseURL = 'https://api.thingspeak.com/update?api_key=CA3YNXBUBJTKRLVH'

M = metoffer.MetOffer(MetDataPointAPIKey)
#x = M.nearest_loc_forecast(-0.5935112, 51.2339491, metoffer.THREE_HOURLY)
lasttime = datetime.datetime.now()
print lasttime

while 1:
	#Get some observations
	x = M.nearest_loc_obs(51.4033, -0.3375)
	y = metoffer.parse_val(x)
	print(y.data_date)	
	if lasttime == y.data_date:
		print "No new data, keep going"
	else:		
		TAmbient = str(y.data[0]["Temperature"][0])
		pAmbient = str(y.data[0]["Pressure"][0])
		vWind = str(y.data[0]["Wind Speed"][0])
		TDewPoint = str(y.data[0]["Dew Point"][0])
		rHumidity = str(y.data[0]["Screen Relative Humidity"][0])
		NWeather = str(y.data[0]["Weather Type"][0])
		xVisibility = str(y.data[0]["Visibility"][0])
		#vWindGust = str(y.data[0]["Wind Gust"][0])
		#pprint.pprint(y.data)
		urlstring = TSbaseURL  + "&field1=" + TAmbient + "&field2=" + pAmbient + "&field3=" + vWind + "&field4=" + TDewPoint + "&field5=" + rHumidity + "&field6=" + NWeather + "&field7=" + xVisibility
		print urlstring
		f = urllib.urlopen(urlstring)
		print f.read()
		print("Temperature is " + str(y.data[0]["Temperature"][0]))
		lasttime = y.data_date	
	time.sleep(20)
