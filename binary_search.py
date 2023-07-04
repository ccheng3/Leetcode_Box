class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # implement the binary search iterative algorithm
        # 
        # binary search requires unique values, sorted input array
        # Runtime: O(logN) b/c the binary search eliminates half of the
        # search space with each additional loop. 

        low = 0 
        high = len(nums) - 1
        mid = (low + high) // 2     # double slash for explicit int division aka floor division

        while low <= high:
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                # re-assign high to mid - 1 (effectively removes the half of the array from index (mid+1) to end of array from search space)
                high = mid - 1
                # re-calculate the new mid index value
                mid = (low + high) // 2
            else:
                # re-assign low to mid + 1 (effectively removes the half of the array from index 0 to index (mid-1))
                low = mid + 1
                mid = (low + high) // 2
        # if you didn't return from the while loop, then no match found.
        return -1