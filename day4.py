from __future__ import print_function
import md5
key = "bgvyzdsv"
num = 0
hsh = md5.new(key + str(num))
while(hsh.hexdigest()[0:5] != "00000"):
    print("Checking " + str(num), end='\r')
    num += 1
    hsh = md5.new(key + str(num))
print("\nPart 1 Answer: " + str(num))

num = 0
hsh = md5.new(key + str(num))
while(hsh.hexdigest()[0:6] != "000000"):
    print("Checking " + str(num), end='\r')
    num += 1
    hsh = md5.new(key + str(num))
print("\nPart 2 Answer: " + str(num))
