class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # what does the Q want? 
        
        # check whether 2 input strings are anagrams 
        # ("exact same characters as another string, 
        # but the order of the characters can be different.")

        # *** same chars = same char + same amount of chars

        # if are the same- return True, else False

        # edges
        if not s and t: 
            return False
        if s and not t: 
            return False
        if s == t: 
            return True 
        if len(s) != len(t): # varying lengths
            return False
        
        
        #steps - brute 
        s = sorted(s) # sorted alphabetically
        t = sorted(t)
        return t == s

        # cat       # act
        # cat       # act
        
        # for i in range( len(s)-1 ):
        #     if s[i] != t[i]:
        #         return False 
        # return True
















         
