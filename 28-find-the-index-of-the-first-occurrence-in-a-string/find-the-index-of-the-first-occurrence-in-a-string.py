class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 1:
            if haystack == needle: return 0
            else: return -1
        
        i = 0
        j = 0

        while i < len(haystack):
            if haystack[i] != needle[j]:
                i = i - j + 1
                j = 0

            else:
                j += 1
                i += 1
                if j == len(needle): return i - len(needle)
        
        return -1
