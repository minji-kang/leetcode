class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hash_map = {}
        intersection = []
        
        for i, num in enumerate(nums1):
            if num not in hash_map: hash_map[num] = 1
            else: hash_map[num] += 1
        
        for num in nums2:
            if (num in hash_map) and (hash_map[num] > 0):
                intersection.append(num)
                hash_map[num] -= 1
        
        return intersection
            