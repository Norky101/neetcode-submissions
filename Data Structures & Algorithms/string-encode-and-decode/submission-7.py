class Solution:

    def encode(self, strs: List[str]) -> str:

        result =""
        for s in strs: 
            result += str(len(s)) + "#" + s
        return result

        # "5#hello5#world"
    def decode(self, s: str) -> List[str]:

        chunk_start = 0 
        result = []
        while chunk_start < len(s):
            delimiter_index = chunk_start
            
            while s[delimiter_index] != "#": # keep looping until we hit the delimiter "#"
                delimiter_index +=1 

            #Once we hit a delimiter (start of the next word), extract the word 
            word_len = int(s[chunk_start:delimiter_index] )# none inclusive of delimiter_index, thus = index 0 
            
            word_start = delimiter_index + 1 
            word_end = word_start + word_len # 2+5 = 7 

            word = s[word_start:word_end] # Hello
            result.append(word)
        
            chunk_start = word_end
    
        return result
