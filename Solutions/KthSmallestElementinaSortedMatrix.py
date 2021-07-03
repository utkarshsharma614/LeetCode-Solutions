class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l = matrix[0][0]
        r = matrix[n-1][n-1]
        
        while l < r:
            mid = (l + r) // 2
            if self.count(mid, matrix) < k:
                l = mid + 1
            else:
                r = mid
        return r
    
    def count(self, i, matrix):
        r = 0
        c = len(matrix[0]) - 1
        count = 0
        while r < len(matrix) and c >= 0:
            if matrix[r][c] <= i:
                count += (c + 1)
                r += 1
            else:
                c -= 1
        return count