<<<<<<< HEAD
f = open('testapi.txt', "r")
=======
f = open('apikey.txt', "r")
>>>>>>> 2d6a3edbf8752e45521fc09bd984bdc15cb642e1
lines = f.readlines()
f.close()
apikey = lines[0]

print("apikey = " + apikey)
