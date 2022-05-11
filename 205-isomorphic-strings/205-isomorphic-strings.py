class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        map_s_t = {}
        map_t_s = {}
        
        for i in range(len(s)):
            s_letter = s[i]
            t_letter = t[i]
            
            if s_letter not in map_s_t:
                map_s_t[s_letter] = t_letter
            
            if t_letter not in map_t_s: 
                map_t_s[t_letter] = s_letter
            
            if (map_s_t[s_letter] != t_letter) or (map_t_s[t_letter] != s_letter):
                return False
        
        return True