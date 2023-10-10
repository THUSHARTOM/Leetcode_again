
s = "Let's take LeetCode contest"

words = []
for i in s.split():
    words.append(i)
    # print(i)

s =""
new_string =[]

for word in words:
    # print(s)
    s = "".join(word[::-1])
    new_string.append(s)

s = " ".join(new_string)
print(s)


####### One liner
# print (" ".join([w[::-1] for w in s.split()]))