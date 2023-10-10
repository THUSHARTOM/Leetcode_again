
################################# Learn to use python dicts well
# get() method takes maximum of two parameters:

# key - key to be searched in the dictionary
# value (optional) - Value to be returned if the key is not found. The default value is None
##################################
s = "abcd"
t = "abcda"

count = {}

for c in t:
    count[c] = count.get(c,0) + 1



for c in s:
    count[c] -= 1
    if count[c] ==0:
        del count[c]

print(list(count.keys())[0])