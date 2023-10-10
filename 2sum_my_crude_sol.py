class Solution:
    def twoSum(self, nums, target: int):
        for i,n in enumerate(nums):
            j = i+1
            for k, m in enumerate(nums): 
                k = k+j
                if k == len(nums):
                    break
                if n+nums[k] == target :
                    print("n", n)
                    print("nums[k]", nums[k])
                    return [i,k]
            print(">>>>>>>>>>>")
        # print(target)