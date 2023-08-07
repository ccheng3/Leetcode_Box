class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # Write your code here
        # scan thru the 2-d array using a nested for loop
        # start a running count of "lucky numbers" set to zero.
        # for each item, check if it is the min element in its row AND the 
        # max element in its column. If so, then add to the running count and 
        # move on to the next element. 
        # Continue to do so until end of 2-d array, then return the running count
        # 
        # Runtime: O((MN) + M + N) --> O(M * N), b/c you have to scan thru entire matrix.
        # Space used: O(1) b/c only using a running count variable 
        def is_min_in_row(array, target_element):
            min_val = array[0]
            for element in array:
                if element < min_val:
                    min_val = element
            return True if target_element == min_val else False
            
        def is_max_in_col(array, target_element):
            max_val = array[0]
            for element in array:
                if element > max_val:
                    max_val = element
            return True if target_element == max_val else False
        
        lucky_numbers = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                current_element = matrix[i][j]
                current_row = matrix[i]
                current_col = [matrix[i][j] for i in range(len(matrix))]
                if is_min_in_row(current_row, current_element) and\
                is_max_in_col(current_col, current_element):
                    lucky_numbers.append(current_element)
        return lucky_numbers