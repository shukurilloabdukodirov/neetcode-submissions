class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        best = 0
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]]+=1
            max_freq = max(max_freq, count[s[r]])
            while((r-left+1)-max_freq>k):
                count[s[left]]-=1
                left+=1
            
            best = max(best,r-left+1)
        return best
