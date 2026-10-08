class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        need = Counter(s1)
        window = Counter(s2[:len(s1)])

        if need==window:
            return True
        
        for right in range(len(s1),len(s2)):
            left = right - len(s1)

            window[s2[right]]+=1
            window[s2[left]]-=1

            if window[s2[left]]==0:
                del window[s2[left]]

            if window == need:
                return True

        return False
            

