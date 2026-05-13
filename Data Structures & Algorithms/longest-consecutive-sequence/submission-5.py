class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # What does the Q want? 
            # return the longest consecutive sequence of numbers 

        # constraints/ considerations: 
            # unsorted 
            # duplicates 
            # Linear time 
        
        
        # [2,3,4,4,5,10,20] # sorted 
        # [2,3,4,5,10,20] # duplicates removed

        # [0,1,2,3,4,5,6]

        if len(nums) == 0: 
            return 0
        # if len(nums) == 2 and nums[0] == 0 and nums[1] ==0:
        #     return 1 
        
        nums = sorted(set(nums)) 
        curr_ct = 1 
        longest_ct = 1
        l = 0 
        r = 1 

        while r < len(nums):
            prev = nums[r] - 1 # desired left val 
            if prev == nums[l]:
                curr_ct +=1   
            else: 
                curr_ct = 1 # default reset val
        
            longest_ct = max(longest_ct, curr_ct)
            l +=1 
            r +=1
        
        return longest_ct






        
