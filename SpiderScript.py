#https://github.com/zaproxy/zaproxy/wiki/ApiPython
# import sys



import time
from pprint import pprint
from zapv2 import ZAPv2



#Grab API Key from the api.txt file
f = open('api.txt', "r")
lines = f.readlines()
f.close()
apikey = lines[0]



# target = 'http://192.168.56.101/dvwa/login.php'
# target = 'http://192.168.56.101/dvwa/login.php'
zap = ZAPv2
# zap = ZAPv2(proxies={'http': 'http://192.168.56.101/', 'https': 'http://192.168.56.101/'})


zap.context.import_context('DVWAAdmin.context', apikey)

zap.spider.scan_as_user(2, 20, apikey=apikey)

print('Accessing target %s' % target)

zap.urlopen(target)
time.sleep(2)

print('Spidering target %s' % target)
scanid = zap.spider.scan(target)
time.sleep(2)

# while(int(zap.spider.status(scanid)) < 100):
# 	print('Spider progress %: ' + zap.spider.status(scanid))
# 	time.sleep(2)

print('Spider completed')
time.sleep(5)

print('Scanning target %s' % target)
scanid = zap.ascan.scan(target)
# while(int(zap.ascan.status(scanid)) < 100):
# 	print('Scan progress %: ' + zap.ascan.status(scanid))
# 	time.sleep(5)

print('Scan completed')
print('Hosts: ' + ', '.join(zap.core.hosts))
print('Alerts: ')
pprint (zap.core.alerts())