class Solution:
    def trailingZeroes(self, n: int) -> int:
        count_five = 0

        for i in range(1, n + 1):
            if i % 5 == 0:
                num_five = 0
                j = i
                while j % 5 == 0:
                    j /= 5
                    num_five += 1
                count_five += num_five 
        
        return count_five