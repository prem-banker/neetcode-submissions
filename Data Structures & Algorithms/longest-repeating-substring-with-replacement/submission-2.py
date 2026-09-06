class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        maxval = 0
        for ch in alp:
            if k == 0:
                maxval = max(maxval, max_consecutive_char(s, ch) )
            else:
                si = 0
                ei = 0
                i = 0
                replacements = []
                while(i < len(s)):
                    # print(replacements, si, ei, i, maxval)
                    if s[i] == ch:
                        
                        ei=i
                        maxval = max(maxval, (ei-si) + 1)
                    else:
                        if len(replacements) < k:
                            replacements.append(i)
                            ei=i
                            maxval = max(maxval, (ei-si) + 1)
                        else:
                            lastind = replacements.pop(0)
                            replacements.append(i)
                            si = lastind+1
                            ei=i
                            maxval = max(maxval, (ei-si) + 1)
                
                    i+=1
        return maxval 

def max_consecutive_char(s, c):
    max_len = 0  
    current_len = 0  
    
    for char in s:
        if char == c:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 0  
    
    return max_len
        