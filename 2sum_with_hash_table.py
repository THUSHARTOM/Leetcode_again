nums = [2,7,11,15]
target = 9

class Solution():
    def twoSum(self, nums,target):
        # Create a hash table
        numMap = {}
        for i, n in enumerate(nums):
            numMap[n] = i # Save value as num:index !!! not the other way around as it is easier to lookup keys than values

        # Check if element adds upto target
        for j, m in enumerate(nums):
            if target-m in numMap and j!=numMap[target-m]:
                return j, numMap[target-m]

S = Solution()

print(S.twoSum(nums,target))

    