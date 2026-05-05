class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # what does Q want? 
        # return i, j index , if (nums[i] + nums[j] == target) AND  (i != j)

        # steps 
        

        # edges 
        if len(nums) == 2: 
            return [ 0,1 ]

        #brute - double for loop 
        
        for i in range(0, len(nums)-1, 1):
            for j in range(i+1, len(nums), 1): # start, stop, skip
                
                if (nums[i] + nums[j] == target) and (i != j):
                    return [ i,j ]


