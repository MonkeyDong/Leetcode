class Solution(object):
    def firstMissingPositive(self, nums):
        L=len(nums)
        for m in range(L):
            if nums[m]>L:
                continue
            val = nums[m]-1
            while nums[m]>0 and val<L and nums[val] != nums[m]:
                #小于等于0，大于等于长度的不换。
                nums[m],nums[val]=nums[val],nums[m]
                val = nums[m]-1
        for m in range(len(nums)):
            if nums[m] != m +1:
                return m +1
        return L+1
