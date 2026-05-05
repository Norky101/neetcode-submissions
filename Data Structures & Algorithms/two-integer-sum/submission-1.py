class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # what does Q want? 
        # return i, j index , if (nums[i] + nums[j] == target) AND  (i != j)

        # edges 
        if len(nums) == 2: 
            return [ 0,1 ]

        # dict 
        # steps 
        # dict num: index 
        # loop over the list using range for val,index
        # if target - curr[num] in dict and (curr index != dict[num])
            # return [dict[target - curr[num]] ,curr index]
        # else: 
            # add the key, index to dict

        seen_nums = {} # dict
      
        for idx ,val in enumerate(nums):
            print(val,idx)
            difference = target - val 

            if difference in seen_nums and idx != seen_nums[difference]: 
                return [seen_nums[difference], idx]

            else: 
                seen_nums[val] = idx
                

                

        


