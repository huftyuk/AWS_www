#sudo pip install metoffer
import metoffer
import sys
sys.path.append('/home/ubuntu')
import APIKeyManager
MetDataPointAPIKey = APIKeyManager.MetDataPoint
import pprint

M = metoffer.MetOffer(MetDataPointAPIKey)
x = M.nearest_loc_forecast(51.4033, -0.3375, metoffer.THREE_HOURLY)
x = M.nearest_loc_obs(51.4033, -0.3375)


y = metoffer.parse_val(x)

print(y.data_date)
print(y.dtype)


pprint.pprint(y.data)

for i in y.data:
	print("{} - {}".format(i["timestamp"][0].strftime("%d %b, %H:%M"), metoffer.WEATHER_CODES[i["Weather Type"][0]]))

print("Temperature is " + str(y.data[0]["Temperature"][0]))
print("Visbility Code is " + str(y.data[0]["Visibility"][0]))
	
#metoffer.VISIBILITY[y.data[0]["Visibility"][0]]
#metoffer.guidance_UV(y.data[0]["Max UV Index"][0])
