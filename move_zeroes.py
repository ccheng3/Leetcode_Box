class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # start both left and right ptrs at index 0 
        # while right is within array bounds:
        #   if right pts to a non-zero element, swap with left
        #   move left one index to the right 
        # always move right one index to the right at each loop iteration
        # 
        # The key is that if left and right are equal and pt to a non-zero
        # element, then that nonzero element swaps with itself (unchanged
        # really, and both left and right move right one index.)
        #
        # Runtime: O(N) b/c right always has to scan thru entire input array
        # Space used: O(1) b/c only 2 ptrs used in the algo irrespective of
        # input size

        left = 0 
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1