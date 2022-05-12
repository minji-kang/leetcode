class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        sums = [0]
        
        for i, num in enumerate(nums):
            sums.append(sums[i] + num)
        
        for i, num in enumerate(nums):
            left_sum = sums[i]
            
            right_sum = sums[-1] - left_sum - num
            
            if left_sum == right_sum: return i
        
        return -1