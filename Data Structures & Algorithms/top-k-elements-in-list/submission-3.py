from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # what does the Q want? 
        # return the top K most frquent nums

        # edges 
        #steps
        # collect the most frequent nums 

        # allow us to sort 

        # loop over the dict 
            # add each key to the keys index in the list
        
        #iterate backkward over the bucket to collect top K amount
    
        dict_freq = Counter(nums) # key=num, val=freq
        bucket = [[]] * (len(nums)+1) # [[],[],[],[]...]

        for num, freq in dict_freq.items():
            if bucket[freq]: 
                bucket[freq].append(num)
            else: 
                bucket[freq] = [num]

        result = []
        k_ct = 0
        for i in range(len(bucket)-1, 0,-1): # start,stop,skip 
            for num in bucket[i]: # each num in the current highest bucket
                result.append(num)
                k_ct += 1 
                if k_ct == k:
                    return result
                else:
                    continue
        return result
            


