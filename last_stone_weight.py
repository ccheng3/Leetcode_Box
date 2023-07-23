class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use a heap - a max-heap in this case
        #
        # This question ENTIRELY models double-pop() from a max-heap, calculate a value,
        # then push onto max-heap again or not depending on val. Rinse and repeat 
        # until the heap either contains only one last element or is empty. 
        #
        # Remember: heapq's heap implementation is a min-heap --> so, the clever way to 
        # simulate as a max-heap with heapq is to multiply every node val by -1 before push()
        # into the heap, and then multiply again by -1 after pop() from the heap to get the 
        # original value. 
        #
        #
        # Runtime: O(N) --> O(N) time to heapify() the input array of ints + O(N) time to pop 
        # off the N or (N-1) heaviest nodes in the max-heap. 
        # Situation wise - you will either end up with 0 or 1 stone left --> You just need to 
        # return the weight of the last stone if 1 stone left, or return 0 if no stones left. 
        #
        # Space used: O(N) b/c you heapify() the input array into a max-heap. 

        import heapq

        stones_max_heap = [stone * -1 for stone in stones]

        heapq.heapify(stones_max_heap)

        while len(stones_max_heap) > 1:
            stone1 = heapq.heappop(stones_max_heap) * -1
            stone2 = heapq.heappop(stones_max_heap) * -1
            if stone1 == stone2:
                continue
            else:
                heapq.heappush(stones_max_heap, abs(stone1 - stone2) * -1)
        
        return heapq.heappop(stones_max_heap) * -1 if len(stones_max_heap) == 1 else 0


