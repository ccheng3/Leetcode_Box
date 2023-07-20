class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use a min-heap
        # find the length of the longest consecutive elements sequence by heapifying
        # input array and continuously pop() the min value off the heap and run a 
        # running count of the longest length seen so far 
        #
        # 1) heapify() nums array into a min-heap
        # 2) initialize longest length seen so far to zero 
        # initialize first prev_val to pop() of the min-heap
        # set the first sequence's running length to zero
        # 
        # while heap not empty:
        #   curr_val is assigned the pop() of the min-heap
        #   if curr_val is equal to prev_val + 1:
        #       add 1 to the running length and continue the loop again 
        #   else curr_val is not a consecutive element:
        #       set prev_val to curr_val 
        #       update longest length seen to running length if running length is larger
        #       than longest length seen so far
        #       reset running length counter back to zero and continue the loop again
        #       (now starting a new count for the next consecutive elements sequence.)
        #
        # update longest length seen to running length if running length is larger (this is
        # the last consecutive elements sequence in the input array and could be 
        # the longest cons. elements seq actually, so need to compare ONE MORE TIME.)
        #
        # return the longest length seen 
        #
        # Runtime: O(N) for heapify() + O(NlogN) for the heapsort-like heap deletion check
        # = O(NlogN) time.
        # Space used: O(N) b/c of the min-heap. 
        # 
        # Note: This soln therefore does not satisfy the algo runtime constraint from 
        # spec. --> Hash table soln gives the O(N) runtime for future reference. 

        import heapq

        heapq.heapify(nums) 
        
        # edge cases of len(nums) being zero or one.
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        longest_length_seen = 0
        prev_val = heapq.heappop(nums)
        running_length = 1

        while len(nums) > 0:
            curr_val = heapq.heappop(nums)
            # this is the case that I WAS NOT thinking about -> basically, if prev and 
            # curr are the same value, then you don't increment the running length, you just
            # skip over this duplicate value. 
            if curr_val == prev_val:
                continue
            elif curr_val == prev_val + 1:
                running_length += 1
            else: 
                if running_length > longest_length_seen:
                    longest_length_seen = running_length
                running_length = 1
            prev_val = curr_val
        
        if running_length > longest_length_seen:
                    longest_length_seen = running_length
        
        return longest_length_seen
        
