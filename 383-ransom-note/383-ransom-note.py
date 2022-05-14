class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        hash_map = {}
        
        for letter in magazine:
            if letter not in hash_map: hash_map[letter] = 1
            else: hash_map[letter] += 1
        
        for letter in ransomNote:
            if letter not in hash_map: return False
            if hash_map[letter] == 0: return False
            hash_map[letter] -= 1
        
        return True