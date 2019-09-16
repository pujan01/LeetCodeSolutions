class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        sol = []
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i-1]:
                target = 0 - nums[i]
                lo = i+1; hi = len(nums)-1
                while (lo < hi):
                    if nums[lo] + nums[hi] == target:
                        sol.append([nums[i], nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == nums[lo+1]  : 
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi-1] :
                            hi -= 1
                        lo += 1; hi -= 1
                    else:
                        if nums[lo] + nums[hi] < target:
                            while lo < hi and nums[lo] == nums[lo+1] : 
                                lo += 1
                            lo += 1
                        else:
                            while lo < hi and nums[hi] == nums[hi-1] :
                                hi -= 1
                            hi -= 1
        return sol