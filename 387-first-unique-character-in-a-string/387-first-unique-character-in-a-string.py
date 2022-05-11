class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hash_map = {}
        
        for i, letter in enumerate(s):
            if letter not in hash_map: hash_map[letter] = i
            else: hash_map[letter] = -1
        
        for letter in s:
            if hash_map[letter] != -1: return hash_map[letter]
        
        return -1