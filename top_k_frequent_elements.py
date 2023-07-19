class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # soln: use BOTH a hash map and a max-heap 
        #
        # Note: can assume that one unique soln exists for each sample input per spec.
        #
        # 1) tally up the freq counts of each unique int into a hash map 
        # 2) append freq count values a list, heapify() it with heapq into a max-heap 
        # form (don't forget the * -1 trick to simulate max-heap in heapq's min-heap 
        # implementation)
        # 3) pop off the k most frequent counts from heap, append to temp holding array
        # 4) loop thru hashmap, append each matching count's key to return list and 
        # remove the (key : count) pair from the hashmap
        # 5) Return the return list 
        #
        # Runtime: O(N) run 4 times, steps 1 to 4. 
        # Space used: O(N) b/c of hashmap, heap, temp holding array.
        
        import heapq

        my_dict = {} 
        for num in nums:
            if num not in my_dict.keys():
                my_dict[num] = 1
            else:
                my_dict[num] += 1
        
        max_heap = list(my_dict.values())
        for i in range(len(max_heap)):
            max_heap[i] *= -1
        heapq.heapify(max_heap)

        k_most_freq_counts = []
        for _ in range(k):
            k_most_freq_counts.append(heapq.heappop(max_heap) * -1)
        
        return_list = []
        for key in my_dict:
            if my_dict[key] in k_most_freq_counts:
                return_list.append(key)
                k_most_freq_counts.remove(my_dict[key])
        
        return return_list
