import urllib
import time
i = 1;
baseURL = 'https://api.thingspeak.com/update?api_key=CA3YNXBUBJTKRLVH'

while 1:
  f = urllib.urlopen("https://api.thingspeak.com/update?key=CA3YNXBUBJTKRLVH&field1=73")
  print f.read()
  time.sleep(16)
  i = i+1
