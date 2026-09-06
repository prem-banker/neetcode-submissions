class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = {}
        for ch in s1:
            map1[ch] = map1.get(ch,0) + 1
    
        

        i = 0
        j = len(s1)
        ans = len(s1)
        
        for ch in s2[i:j]:
            if ch in map1:
                map1[ch]-=1
                if map1[ch]== 0:
                    del map1[ch]
            else:
                map1[ch] = -1
        if map1 == {}:
            return True
        else:
            print(map1)
            for i in range(1, len(s2) - len(s1) + 1):
                left = s2[i-1]
                right = s2[i + len(s1)-1]
                print(map1, left, right)
                if left in map1:
                    map1[left]+=1
                    if map1[left] == 0:
                        del map1[left]
                else:
                    map1[left] = 1
                
                if right in map1:
                    map1[right]-=1
                    if map1[right] == 0:
                        del map1[right]
                else:
                    map1[right]=-1
            
                if map1 == {}:
                    return True

  
        return False