class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # use two passes thru the array and a clever
        # 'flip to -1' technique based on index/value relationship.
        #
        # 1) first pass: for every value, flip the corresponding
        # value at index (abs(val) - 1) to -1
        # if not already negative.
        # --> NOTE: need the abs() b/c the
        # val could have already been flipped negative by a
        # value earlier in the array.
        #
        # 2) second pass: for every value, if it is still positive,
        # then the value at (index + 1) is missing from the array.
        # store a running array of all missing values and return it
        # after the second pass.
        #
        # Runtime: O(N) b/c two passes thru array still required.
        # Space used: O(1) b/c we assume returned list does
        # not count as extra space.


        # first pass
        for num in nums:
            corresponding_index = abs(num) - 1
            if nums[corresponding_index] > 0:
                nums[corresponding_index] *= -1
       
        # second pass
        return_list = []
        for index, num in enumerate(nums):
            if num > 0:
                return_list.append(index + 1)
       
        return return_list





