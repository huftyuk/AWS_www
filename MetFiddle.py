#pip install datapoint
#https://github.com/jacobtomlinson/datapoint-python
import datapoint  
import sys
sys.path.append('/home/ubuntu')
import APIKeyManager


import urllib
import time
i = 1;
baseURL = 'https://api.thingspeak.com/update?api_key=CA3YNXBUBJTKRLVH'

  
apikey = APIKeyManager.MetDataPoint


# Create datapoint connection
conn = datapoint.Manager(api_key=apikey)

# Get nearest site and print out its name
site = conn.get_nearest_site(-0.5935112, 51.2339491)
print site.name

while 1:
  # Get a forecast for the nearest site
  forecast = conn.get_forecast_for_site(site.id, "3hourly")

  # Get the current timestep using now() and print out some info
  now = forecast.now()
  print now.weather.text
  print "%s%s%s" % (now.temperature.value,
                  u'\xb0', #Unicode character for degree symbol
                  now.temperature.units)
  urlstring = "https://api.thingspeak.com/update?key=CA3YNXBUBJTKRLVH&field1=" + str(now.temperature.value)
  f = urllib.urlopen(urlstring)
  print f.read()
  time.sleep(16)
  i = i+1

