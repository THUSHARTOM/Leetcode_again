
nums = [1,2,3,1,1,3,1,1]

count = 0
count_map ={}

for i,n in enumerate(nums):
    if n in count_map:
        count += count_map[n]
        count_map[n]+=1
    else:
        count_map[n]=1
    
print(count)