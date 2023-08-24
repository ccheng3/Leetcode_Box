class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Neetcode's solution --> use two ptrs 
        #
        # the brute force is still the nested for loop, except 
        # there's a tweak --> input array is sorted 
        # in the brute force nested loop --> if you find a pair
        # that sums > target, then you don't need to continue
        # in that nested loop anymore since anything after will
        # also have sum > target value. 
        #
        # two ptr technique takes advantage of this idea
        # left and right ptrs --> start left at first array index
        # and right at last array index 
        # 
        # Guaranteed a soln for every test input 
        #
        # Therefore --> run an infinite loop and check
        # sum(left, right). If sum > target, then move right 
        # to the left one index --> b/c the array is sorted,
        # the sum will then decrease. Else if sum < target, then move
        # left to the right one index --> b/c the array is sorted,
        # the sum will then increase. 
        # Else, sum == target, therefore return the 1-based indices
        # of left and right 
        #
        # Runtime: O(N) b/c worst-case the entire array is fully-scanned
        # thru only one time
        # Space used: O(1) b/c only two ptrs used

        left = 0
        right = len(numbers) - 1

        while True:
            sum = numbers[left] + numbers[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [left + 1, right + 1]