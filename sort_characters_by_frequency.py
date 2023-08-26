class Solution:
    def frequencySort(self, s: str) -> str:
        # another solution --> use both a hashmap and a max-heap
        # don't use a sort, but do use two data structures together
        # Runtime is still O(NlogN) b/c of the complete depletion
        # of the maxHeap
        # Space used --> O(N) where N is num unique chars in the string
        #
        # 1) store the char freq counts in the hashmap
        # 2) get a list of tuple pairs (freq count : char) from
        # the hashmap, heapify the list into maxHeap based on 
        # the freq counts. 
        # 3) Completely deplete maxHeap and build up the return string

        import heapq
        hashmap = dict()

        for char in s:
            if char not in hashmap.keys():
                hashmap[char] = 1
            else:
                hashmap[char] += 1
        
        # don't forget the clever (* -1) trick for storing a maxHeap 
        # representation in heapq's default minHeap format. 
        pairs = [tuple([hashmap[key] * -1, key]) for key in hashmap.keys()]
        heapq.heapify(pairs)
        return_string = ""

        while len(pairs) > 0:
            heapTop = heapq.heappop(pairs)
            for _ in range(heapTop[0] * -1):
                return_string += heapTop[1]
        
        return return_string

