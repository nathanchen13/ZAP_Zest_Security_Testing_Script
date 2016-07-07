# Start DVWA
sudo /opt/lampp/lampp start

# Write IP to file inside repo
/sbin/ip addr | grep -Eo 'inet [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' > ~/ZAP_2.5.0/ip.txt

# Run script to change context to new IP
python change_context.py

# Generate the random string for the API key
cat /dev/urandom | env LC_CTYPE=C tr -dc 'a-zA-Z0-9' | fold -w 28 | head -n 1 > /home/centos/jenkins_root/workspace/ZAP/apikey.txt
cat /dev/urandom | env LC_CTYPE=C tr -dc 'a-zA-Z0-9' | fold -w 28 | head -n 1 > ~/ZAP_2.5.0/apikey.txt

# Start ZAP
cd ~/ZAP_2.5.0/
./zap.sh -daemon -config api.key=`cat apikey.txt` &
sleep 1m
cd $WORKSPACE

# Run ZAP script
python SpiderScript.py

mv htmlreport.html $WORKSPACE
mv xmlreport.xml $WORKSPACE

# Delete apikey.txt
rm apikey.txt
