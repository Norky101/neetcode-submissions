class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0 
        curr_ct = 0 
        last_idx = 0
        for i in range(len(nums)):
            if nums[i] == 0: 
                res = max(res, curr_ct)
                curr_ct = 0
                last_idx = i
            else: 
                # hit a 1 
                if last_idx == 0 or last_idx == i-1: # first 1 we have ever hit and at index 0
                    curr_ct += 1 
                    last_idx = i
            
            res = max(res, curr_ct)
        
        return res 
                    

                
            


