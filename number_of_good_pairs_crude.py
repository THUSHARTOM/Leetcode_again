#######################################
# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
######################################


nums = [1,2,3,1,1,3]
count = 0
hash_table = {}

for i, n in enumerate(nums):
    hash_table[n] = i

for j, m in enumerate(nums):
    for k, w in enumerate(nums):
        if j<k:
            if m == w:
                count +=1



print(count)  