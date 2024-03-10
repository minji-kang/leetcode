class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        result = []
        
        while matrix != []:
            array = matrix.pop(0)
            i, j = 0, 0

            while j < len(array):
                result.append(array[j])
                j += 1

            while i < len(matrix):
                if matrix == []: break
                if matrix[i] == []: break
                result.append(matrix[i].pop())
                i += 1

            if matrix == []: break
            array = matrix.pop()
            j = len(array) - 1

            while j >= 0:
                result.append(array[j])
                j -= 1

            i = len(matrix) - 1

            while i >= 0:
                if matrix == []: break
                if matrix[i] == []: break
                result.append(matrix[i].pop(0))
                i -= 1
        
        return result