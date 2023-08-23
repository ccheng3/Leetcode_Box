class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # brute force solution
        # 1) sort the input array in ascending order 
        # 2) calculate subsequence start index = array size - k value
        # 3) loop from start index to end of array, and append the k largest values to
        # temp array
        # loop thru nums again and append k largest values to return array in 
        # subsequence order based on nums array. 
        # 4) return the return array 
        #
        # Runtime: O(NlogN) b/c Python's Timsort runs merge sort/insertion sort hybrid
        # with worst case of NlogN time. 
        # Space used: O(N) b/c merge sort uses auxiliary array of size N. 

        nums_sorted_ascending = sorted(nums)
        k_largest_elements = []
        return_list = []

        start_index = len(nums) - k
        for i in range(start_index, len(nums)):
            k_largest_elements.append(nums_sorted_ascending[i])

        for num in nums:
            if num in k_largest_elements:
                return_list.append(num)
                k_largest_elements.remove(num)

        return return_list
        