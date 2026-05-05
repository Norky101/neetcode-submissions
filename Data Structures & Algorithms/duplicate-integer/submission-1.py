class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # edges 
        if not nums: 
            return False 
        if len(nums) == 1: 
            return False


        #steps Brute 

        # set() to track each unique num
        # loop over the nums 
            # if curr num is in our set:
                # return True # hit a duplicate 
            #else: 
                # add curr num to our set
        
        # return False

        seen = set() 
        for num in nums: 
            if num in seen: 
                return True 
            else: 
                seen.add(num)
        return False
