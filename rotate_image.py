class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1) transpose the matrix in place
        # you're guaranteed that the matrix is always square
        #
        # ------------IMPORTANT ----------
        # You need to draw out the example matrices, indicate the diagonal,
        # and look at the how the reciprocal [i][j] and [j][i] index values
        # relate for the transposition. Also - the matrix is guaranteed
        # to be square so you only need to scan thru the upper diagonal
        # for the in-place swap. 
        #
        # 2) then reverse all items in each row 
        #
        # Runtime: O(M * N) b/c the algo visits all nodes above the 
        # matrix diagonal, and then the reverse() will visit N/2 nodes in
        # each row for all rows which reduces down also to M * N.
        # 
        # Space used: O(1) space used - matrix is transposed in-place,
        # and reverse() presumably reverses in-place too by scanning
        # thru the first half of the array and swapping with the 
        # value at the reciprocal off the array middle index 
        # (basically the concept from the reverse array problem).
        for i in range(len(matrix[0]) - 1):
            for j in range(i+1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
        
        