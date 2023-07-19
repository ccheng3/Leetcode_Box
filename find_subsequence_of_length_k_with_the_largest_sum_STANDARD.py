class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Standard solution 
        # use a heap!
        # 
        # 1) Multiply each int value by -1 to simulate for max-heap in heapq (heapq default
        # is a min-heap), then heapify() a copy of the input array in O(N) time.
        # 2) Pop off the k largest elements and append to temp holding array 
        # 3) Loop thru the input array and "rebuild" the return order in subsequence order
        # into the return array
        # 4) Return the return array.
        #
        # Runtime: O(N) b/c heapify() runs in O(N), then you pop off k largest elements 
        # and append to temp holding array --> in worst case k == len(nums) so O(N) time
        # again, then loop thru input array and rebuild return array in subseq order,
        # in worst case O(N) again ---> 3 * O(N) reduces down to O(N).
        #
        # Space used: Same, in worst case k == len(nums) so 3 * O(N) --> 3 aux. space
        # used --> the max-heap, the temp holding array, and the return array. 
        #
        # You could actually just return nums if k == len(nums) but same 'worst-case'
        # idea applies to k == (len(nums) - 1) situation, really.  

        import heapq
        import copy

        max_heap = copy.deepcopy(nums)
        # multiply each int val by -1 to "simulate" max-heap in heapq
        for i in range(len(max_heap)):
            max_heap[i] *= -1
        heapq.heapify(max_heap)

        k_largest_ints = []
        for _ in range(k):
            k_largest_ints.append(heapq.heappop(max_heap) * -1)

        return_list = []
        for num in nums:
            if num in k_largest_ints:
                return_list.append(num)
                k_largest_ints.remove(num)
        
        return return_list