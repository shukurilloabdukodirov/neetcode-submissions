class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}   # -> yopuvchi: ochuvchi
        stack = []

        for ch in s:
            if ch in pairs:                      # -> yopuvchi qavs
                if not stack or stack.pop() != pairs[ch]:
                    return False                 # -> bo'sh yoki mos kelmadi
            else:                                # -> ochuvchi qavs
                stack.append(ch)

        return not stack                         # -> bo'sh bo'lsa True


