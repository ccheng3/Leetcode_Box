class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # optimal solution -> use two ptr technique 
        # 
        # start left ptr at front of array, right ptr at end of array
        # while left and right are not equal, compare
        # the two and store the larger abs() value's squared val in the 
        # return array in backwards fashion. 
        #
        # Runtime: O(N) b/c you only scan thru the entire array once 
        # and stop when left and right pting to same index 
        #
        # Space used: O(N) b/c return array has size equal to 
        # input array 

        # return list
        return_list = [0 for _ in range(len(nums))]
        left = 0
        right = len(nums) - 1
        # curr stores curr index to store curr larger val at in return list
        curr = len(nums) - 1

        while left < right:
            if abs(nums[left]) > abs(nums[right]):
                return_list[curr] = nums[left] ** 2
                left += 1
            else:
                return_list[curr] = nums[right] ** 2
                right -= 1
            curr -= 1
        # no matter what, you get to a point where left and right
        # are equal (last value from input array to store)
        return_list[curr] = nums[left] ** 2
        return return_list

