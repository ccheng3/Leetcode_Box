class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # clever solution 
        # 1) reverse the entire array 
        # 2) reverse the two individual subdivisions 
        # first partition --> [0 : k-1]
        # second partition --> [k : N-1]

        # start and end INDICES
        def reverse(input_array, start, end):
            # size of the array
            N = end - start + 1
            for i in range(N // 2):
                left = start + i
                right = end - i
                input_array[left], input_array[right] =\
                        input_array[right], input_array[left]
        
        # need to compute the num of unique k shifts. 
        unique_k = k % len(nums)
        
        # reverse the entire array 
        reverse(nums, 0, len(nums) - 1)

        # reverse the first subdivision -> interval [0, k-1]
        reverse(nums, 0, unique_k - 1)

        # reverse the second subdivision -> interval [k, N-1]
        reverse(nums, unique_k, len(nums) - 1)
