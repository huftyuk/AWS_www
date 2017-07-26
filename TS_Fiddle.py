import urllib2
import time
i = 1;
baseURL = 'https://api.thingspeak.com/update?api_key=CA3YNXBUBJTKRLVH'

while 1:
  f = urllib2.urlopen(baseURL + 'field1=73')
  time.sleep(16)
  i = i+1
