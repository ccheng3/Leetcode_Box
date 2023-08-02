class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # two steps in this solution
        # 1) reverse all elements in each row using the reverse() method
        # 2) invert all elements (1 to 0, 0 to 1) in the matrix.
        #
        # Runtime: should by O(M * N) b/c of the reverse, then same runtime from inversion.
        # Space used: O(1), no aux space was used. reverse() should be in-place though
        # you should definitely double check the official docs. 
        for row in image:
            row.reverse()
        for i in range(len(image)):
            for j in range(len(image[i])):
                image[i][j] = 1 if image[i][j] == 0 else 0
        return image

