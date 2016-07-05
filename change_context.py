f = open('ip.txt', "r")
f.readline()
ip = f.readline().strip('inet ').strip('\n')
f.close()

f = open('InstanceDVWA.context', 'r')
filedata = f.read()
f.close()

filedata = filedata.replace("<incregexes>http://172.31.2.169/dvwa.*</incregexes>","<incregexes>http://"+ip+"/dvwa.*</incregexes>")
filedata = filedata.replace("<loginurl>http://172.31.2.169/dvwa/login.php</loginurl>","<loginurl>http://"+ip+"/dvwa/login.php</loginurl>")

f = open('InstanceDVWA.context','w')
f.write(filedata)
f.close()