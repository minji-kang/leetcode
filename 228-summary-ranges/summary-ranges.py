class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []: return nums

        string = str(nums[0])
        output = []
        prev = nums[0]
        start = str(nums[0])

        for i in nums[1:]:
            if i != prev + 1:
                prev = i
                output.append(string)
                string = str(i)
                start = str(i)
            
            else:
                string = start + "->" + str(i)
                prev = i
        
        output.append(string)
        return output