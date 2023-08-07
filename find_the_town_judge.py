class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # use two hash tables 
        # This is the idea:
        # 1) Scan thru the array "trust" and record two things in two separate 
        # hash tables: 
        #   - the number of outgoing edges from the node in current relationship (a_i)
        #   - the number of incoming edges from the node in current relationship node (b_i)
        # Then, scan thru the outgoing edges hash table and look for the 
        # node that has ZERO outgoing edges and (N-1) incoming edges, and 
        # return that node. 
        # Otherwise you will scan thru the entire hash table and not find a 
        # accompanying match, so return a -1.
        #
        # Runtime: O(N) b/c every single person in the town is added into both the
        # incoming and outgoing edges hashmaps. Then you scan thru the entire
        # town in the outgoing hashmap and cross-check with the incoming hashmap 
        # to look for the existence of the town judge. 
        # Space used: O(2N) --> O(N) b/c two hashmaps are used in the process.  

        num_outgoing_edges = dict()
        num_incoming_edges = dict()

        for i in range(1, n + 1):
            num_outgoing_edges[i] = 0
            num_incoming_edges[i] = 0

        for relationship in trust:
            outgoing_edge = relationship[0]
            incoming_edge = relationship[1]
            
            if outgoing_edge in num_outgoing_edges.keys():
                num_outgoing_edges[outgoing_edge] += 1
            else:
                num_outgoing_edges[outgoing_edge] = 1
            
            if incoming_edge in num_incoming_edges.keys():
                num_incoming_edges[incoming_edge] += 1
            else:
                num_incoming_edges[incoming_edge] = 1
            
        for edge in num_outgoing_edges.keys():
            if num_outgoing_edges[edge] == 0 and\
            num_incoming_edges[edge] == n - 1:
                return edge
        return -1