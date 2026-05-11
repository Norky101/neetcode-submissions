class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # What does the question want? 

            # return a list of nums where each index is the product of all the other nums, 
            # except the num at that index 
        
        #Edges 
        if len(nums) ==2: 
            return[nums[1], nums[0]]

        #Steps
        # brute force 
            # loop over the input (i)
                # loop over from start again (j)
                    # check for if current index j == older index i 
                        # avoid that num 
                    # else: 
                        # multiple it by current product 
                
             #add the cur_prodoct to results list 
        # return result list 

        result = []
        for i in range(len(nums)):
            curr_product = 1
            for j in range(len(nums)):
                if i != j: 
                    curr_product *= nums[j]
                else: 
                    continue 
            
            result.append(curr_product)
        return result