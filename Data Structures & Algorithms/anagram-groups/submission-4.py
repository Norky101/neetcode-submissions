class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         # what does the Q want? 

         # return all anagrams into sublists - any order

         # anagrams - same chars as another string + same freq of chars

         # edges
        if len(strs) == 1: 
            return [strs]
        if not strs:  
            return [strs]
        
        # steps
        # dict key=sorted string : [value=original string]
            # - sort the input list
            # add to dict

        # create empty dict
        # loop over the input list 
        # check if curr sorted string is in dict: 
            # yes - add to the values list in unsorted form
        
        # No- add sorted curr string to key & unsorted curr string to val 

        # end - loop over the dict values and add them to a list - return that list

        # challenge - sort the list, whilst also retaining original string
            # A - Tuple

        #strs.sort() # inplace 
        char_dict = {}

        for string in strs: 
            sorted_characters = sorted(string) # list
            sorted_string = "".join(sorted_characters)

            if sorted_string not in char_dict: 
                char_dict[sorted_string] = [string]
            
            else: 
                char_dict[sorted_string].append(string)
            
        return list(char_dict.values())
    


