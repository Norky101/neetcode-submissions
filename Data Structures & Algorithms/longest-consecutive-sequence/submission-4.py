class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # what does the question want? 
            # return the longest consecutive line of elements
                # ignore duplicates from the length

        # edges 

        # brute force
        if not nums:
            return 0

        if len(nums) ==1: 
            return 1 
        
        nums = sorted(list(set(nums))) # removes any duplicates & sorts
        if len(nums) == 2: 
            prev = nums[1] -1 
            if prev == nums[0]:
                return 2 
            else: 
                return 1 
        
        r = 1 
        res = 0 
        count = 1
        while r < len(nums):
            prev = nums[r] - 1 

            if prev == nums[r-1]:  
                count += 1
                r += 1 
            else: 
                res = max(res, count)
                count = 1
                r += 1
        
        return max(res, count)