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

        # steps 
            # longest = default of 1 due to always being at least 1 value, excpet it len() == 0:
            # using 2 pointers 
            # loop over the sorted and de-duplicated input 
                # check if the previous values == to the left value 
                    # yes-> increment curr_seq_ct
                    # no -> reset curr_seq_ct =1 
                
                #On each turn 
                    # incremenet l, r +1 
                    # check the longest vs curr_seq_ct value 

            # return longest


        if len(nums) == 0: 
            return 0
        
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






        
