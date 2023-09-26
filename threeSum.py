class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # practicing the 3sum problem again 
        # gist: brute force soln runs 3 nested loops and finds
        # all matching combos, but it's slow. O(N^3) runtime. 
        #
        # optimal soln runs two sum part two soln inside a loop 
        # that anchors at the next new 'a' value.
        #
        # threeSum = 'a' + 'b' + 'c'
        #
        # two sum part two soln --> sort the array then run a two ptr
        # soln and find all matching 'b' and 'c' twoSum pairs. 
        #
        # Optimal soln runtime --> O(NlogN) + O(N^2) b/c of the sort, then run the nested loop
        # O(N^2) dominates at scale. 
        # 
        # Space used: O(1) b/c only maintain 3 ptrs. i, left and right 
        # (i points to 'a', left to 'b', right to 'c')

        return_list = []
        nums.sort()

        for i,a in enumerate(nums):
            # skip all duplicate 'a' values b/c already seen 
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1 
            right = len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    return_list.append([a, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return return_list
        