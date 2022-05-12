class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        hash_map = {}
        result = []
        
        for i, array in enumerate(mat):
            for j, item in enumerate(array):
                if (i + j) not in hash_map: hash_map[i+j] = [item]
                else: hash_map[i+j].append(item)
            
        for key in hash_map.keys():
            if key % 2 == 0: hash_map[key].reverse()
        
        for array in hash_map.values():
            for value in array: result.append(value)
        
        return result