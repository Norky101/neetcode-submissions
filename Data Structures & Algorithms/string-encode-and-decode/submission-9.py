class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs: 
            result += str(len(s)) + "#" + s
        return result

        # "5#Hello5#World"

    def decode(self, s: str) -> List[str]:

        result = []
        word_chunk = 0 

        while word_chunk < len(s): 
            delimiter = word_chunk

            while s[delimiter] != "#": 
                delimiter +=1 
            
            # hit the delimiter 
            print(word_chunk,delimiter)
            word_len = int(s[word_chunk:delimiter])
            word_start = delimiter + 1 
            word_end = word_start + word_len 

            result.append(s[word_start:word_end])

        
            word_chunk = word_end

        return result





