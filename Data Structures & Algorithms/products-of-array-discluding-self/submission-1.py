class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #What does the Q want? 
            # return a list where each value is the product of all the other numbers in the input list 
                # Excluding the number at the current i position 

        #Edges 

        # brute 
        # double for loop 
        result = []
        for i in range(len(nums)):
            product = 1 
            for j in range(0,len(nums), 1): 
                if i != j: # diffrent index position 
                    product *= nums[j]
            
            result.append(product)
        return result
