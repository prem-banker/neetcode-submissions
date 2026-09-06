class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tarr = [0] * 52  
        char_count = Counter(t) 
        ans = "X"*1000

        if len(s) < len(t):
            return ""

        for char, count in char_count.items():
            index = ord(char) - ord('a') if 'a' <= char <= 'z' else ord(char) - ord('A') + 26
            tarr[index] = count

        freq = {}
        freqarr = [0]*52
        for i,el in enumerate(s):
            index = ord(el) - ord('a') if 'a' <= el <= 'z' else ord(el) - ord('A') + 26
            freqarr[index]+=1
            if consists(freqarr, tarr):
                # print('here? ', i, el)

                tempans = s[:i+1]
                if len(tempans) < len(ans):
                    ans = tempans
                remove = subtract(freqarr, tarr)
                for j in freq:
                    if consists(remove, freq[j]):
                        tempans = s[j+1:i+1]
                        if len(tempans) < len(ans):
                            ans = tempans
                
            freq[i] = [el1 for el1 in freqarr] 

        if ans == 'X'*1000:
            return ""
        else:
            return ans


def subtract(a, b):
    return [x - y for x, y in zip(a, b)]

def consists(big, small):
    for x,y in zip(big,small):
        if x-y<0:
            return False
    return True