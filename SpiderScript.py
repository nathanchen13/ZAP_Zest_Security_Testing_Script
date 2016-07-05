# https://github.com/zaproxy/zaproxy/wiki/ApiPython
# import sys



import time
from pprint import pprint
from zapv2 import ZAPv2



# Grab API Key from the api.txt file

f = open('apikey.txt', "r")
api = f.read().strip('\n')
f.close()

f = open('ip.txt', "r")
ip = f.readline().strip('inet ').strip('\n')
f.close()

target = 'http://' + ip + '/dvwa/login.php'
zap = ZAPv2()
#The following line must be the ip of where ZAP is, so for us it is localhost:8090
#Also if you are not running ZAP on port 8080 then you must include the line below 
#with the correct port numbers
#zap = ZAPv2(proxies={'http': 'http://localhost:8090', 'https': 'http://localhost:8090'})

zap.context.import_context('/home/centos/ZAP_2.5.0/ZAP_Zest_Security_Testing_Script/InstanceDVWA.context', apikey = api)

print('Accessing target %s' % target)

zap.urlopen(target)
time.sleep(2)

print('Spidering target %s' % target)
dvwa = 'http://' + ip + '/dvwa'
zap.spider.scan_as_user('2', '20', dvwa, subtreeonly = True, apikey = api)


# scanid = zap.spider.scan(target)
# time.sleep(2)

# while(int(zap.spider.status(scanid)) < 100):
# 	print('Spider progress %: ' + zap.spider.status(scanid))
# 	time.sleep(2)

print('Spider completed')
time.sleep(5)

print('Scanning target %s' % target)

zap.ascan.scan_as_user(dvwa, 2, 20, apikey = api)

# scanid = zap.ascan.scan(target)
# while(int(zap.ascan.status(scanid)) < 100):
# 	print('Scan progress %: ' + zap.ascan.status(scanid))
# 	time.sleep(5)

print('Scan completed')
print('Hosts: ' + ', '.join(zap.core.hosts))
print('Alerts: ')
pprint (zap.core.alerts())

f = open('xmlreport.xml','w')
f2 = open('htmlreport.html','w')
f.write(zap.core.xmlreport(apikey = api))
f2.write(zap.core.htmlreport(apikey = api))
f.close()
f2.close()
