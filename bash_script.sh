# Start DVWA
sudo /opt/lampp/lampp start

cd ~/ZAP_2.5.0/


# Write IP to file inside repo
/sbin/ip addr | grep -Eo 'inet [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' > ip.txt

# Run script to change context to new IP
python change_context.py

mv SpiderScript.py ..
mv ip.txt ..
cd ..

# Generate the random string for the API key
cat /dev/urandom | env LC_CTYPE=C tr -dc 'a-zA-Z0-9' | fold -w 28 | head -n 1 > apikey.txt

# Start ZAP
./zap.sh -daemon -config api.key=`cat apikey.txt` &
sleep 1m

# Run ZAP script
python SpiderScript.py
mv SpiderScript.py ZAP_Zest_Security_Testing_Script

mv htmlreport.html $WORKSPACE
mv xmlreport.xml $WORKSPACE

# Delete apikey.txt
rm apikey.txt

