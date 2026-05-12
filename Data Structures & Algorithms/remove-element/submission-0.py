class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # what does the Q want? 

            # return every appearance of VAL  in-place

            # return 

        saved_nums = []
        excluded_ct = 0
        for i in range(len(nums)):
            if nums[i] != val: 
                saved_nums.append(nums[i])
            else:
                excluded_ct += 1
            
        for i in range(len(saved_nums)):    
            nums[i] = saved_nums[i]

        return len(nums) - excluded_ct


