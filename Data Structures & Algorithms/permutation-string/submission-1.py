class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        have = [0]*26
        need = [0]*26
        if(len(s1)>len(s2)):
            return False
        for i in range(len(s1)):
            need[ord(s1[i]) - ord('a')] += 1
            have[ord(s2[i]) - ord('a')] += 1

        matches = sum(1 for i in range(26) if have[i]==need[i] )

        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = ord(s2[i])-ord('a')
            have[idx]+=1
            if(have[idx]==need[idx]):
                matches+=1
            elif(have[idx]==need[idx]+1):
                matches-=1


            idx = ord(s2[i-len(s1)]) - ord('a')
            have[idx]-=1
            if(have[idx]==need[idx]):
                matches+=1
            elif(have[idx]==need[idx]-1):
                matches-=1    

        return matches==26