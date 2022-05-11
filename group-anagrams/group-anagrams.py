class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = {}
        
        for i, string in enumerate(strs):
            sorted_str = tuple(sorted(string))
            
            if sorted_str not in hash_map: hash_map[sorted_str] = [string]
            else: hash_map[sorted_str].append(string)
        
        return hash_map.values()