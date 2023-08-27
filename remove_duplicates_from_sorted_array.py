class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # solution --> use two ptrs, left and right 
        # left pts to the position that the next unique val in the list will be stored at
        # right scans thru the array and finds the next unique val to store at left. 
        # if right goes out of bounds, then we can stop the loop and return left. 
        # 
        # Runtime: O(N) b/c left and right scan thru the array once. 
        # Space used: O(1) b/c only maintain two ptrs. 
        #
        # NOTE: the important thing to remember about this soln
        # is that the right ptr only scans thru the array one time total.
        # This fact + sorted array property --> is what allows the 
        # duplicates to be skipped and then the next unique val is placed
        # at left ptr index. 
        #
        # Definitely draw this one out again and rewatch Neetcode's example. 

        left = 1
        right = 1
        if left == len(nums):
            return left
        while right < len(nums):
            if nums[right] == nums[right - 1]:
                right += 1
            else:
                nums[left] = nums[right]
                left += 1
                right += 1
        return left


        