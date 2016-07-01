f = open('api.txt', "r")
lines = f.readlines()
f.close()
apikey = lines[0]

print("apikey = " + apikey)