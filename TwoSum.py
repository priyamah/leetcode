


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        res = dict()
        for i in range(len(nums)):
            other = target - nums[i]
            if other in res:
                return (res[other], i)
            res[nums[i]] = i
        return []
        
