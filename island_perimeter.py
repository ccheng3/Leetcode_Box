class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # brute force soln 
        # use a nested for loop and scan thru the entire grid 
        # hold a total perimeter counter variable 
        # visit each cell and for each island cell, you need to figure out 
        # what its single perimeter sum is
            # hold a single cell perimeter counter var = 4
            # hold a single cell num neighbor sides counter var
            # check each of the 4 sides (North, East, South, West) 
            # if any side is connected to a neighboring island cell, then add to num neighbor
            # sides counter
            # EDGE CASE: First and Last rows in the grid are special in a sense
                # first row's cells do not have a North side to check 
                # last row's cells do not have a South side to check 
            # subtract num neighbor sides counter from single cell perimeter counter
            # add single cell perimeter counter to total perimeter counter 
        # return total perimeter counter 
        #
        # Runtime: O(M * N) where M is num rows and N is num cols. All M * N nodes in the grid are visited, which makes this a bit slow. 
        # Space used: O(1) b/c only one total perimeter counter var is used. 

        total_perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # you only want to look at island cells, so skip all of the water cells.
                if grid[i][j] != 1:
                    continue
                cell_perimeter = 4
                num_neighbor_islands = 0
                if i != 0:
                    # check the cell's North side for an island contact
                    if grid[i-1][j] == 1:
                        num_neighbor_islands += 1
                if i != len(grid) - 1:
                    # check the cell's South side for an island contact 
                    if grid[i+1][j] == 1:
                        num_neighbor_islands += 1
                if j != 0:
                    # check the cell's West side for an island contact
                    if grid[i][j-1] == 1:
                        num_neighbor_islands += 1
                if j != len(grid[i]) - 1:
                    # check the cell's East side for an island contact
                    if grid[i][j+1] == 1:
                        num_neighbor_islands += 1
                total_perimeter += (cell_perimeter - num_neighbor_islands)
        return total_perimeter