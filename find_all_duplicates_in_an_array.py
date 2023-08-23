class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # use the same clever 'flip to -1' technique learned
        # from LC 448.
        #
        # perform one scan thru array nums
        # initialize a return list to return
        # 1) for each value, flip the corresponding value at
        # index (abs(val) - 1) to negative if corre. val
        # positive.
        # Otherwise, corre. val already negative --> indicates
        # the curr val already seen and therefore must be a
        # duplicate. Append abs(curr val) to the return list
        #
        # NOTE: don't forget about the abs() operations. You're
        # manipulating the same array that you're scanning thru.
        #
        # Runtime: O(N) b/c one scan thru array
        # Space used: O(1) assuming return list uses no extra space.


        return_list = []
        for num in nums:
            corresponding_index = abs(num) - 1
            if nums[corresponding_index] < 0:
                return_list.append(abs(num))
            else:
                nums[corresponding_index] *= -1
        return return_list

