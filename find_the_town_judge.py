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
    

    # class Solution: ---> Improved solution 
    # def findJudge(self, n: int, trust: List[List[int]]) -> int:
    #     # think like a graph 
    #     # use two dicts 
    #     # first dict --> for each node in graph, stores number of outgoing edges
    #     # second dict --> for each node in graph, stores number of incoming edges
    #     # -> town judge: the node has zero outgoing edges and also has 
    #     # (N - 1) incoming edges
    #     #
    #     # 1) loop thru trust array and count number of outgoing edges for 
    #     # each node (a_i)
    #     # 2) loop thru trust array and count number of incmoing edges for 
    #     # each node (b_i) 
    #     # 3) loop thru the first dict and find a match in the second dict
    #     # if exists, else return -1 

    #     # loop thru 'n' and populate the both dictionaries with key 
    #     # 'n' value and value initialized 0 
    #     # Runtime: O(V + E) b/c all vertices looked at to populate the dictionaries
    #     # and all directed edges looked at to count up each vertex's total 
    #     # num of incoming and outgoing edges. 
    #     # Space used: O(V) where dictionary sizes are proportional to total num
    #     # of vertices in the graph. (V key:value pairs in each dict.)

    #     incoming_edges = dict()
    #     outgoing_edges = dict()

    #     for i in range(1, n + 1):
    #         incoming_edges[i] = 0
    #         outgoing_edges[i] = 0
        
    #     for relationship in trust:
    #         outgoing_edges[relationship[0]] += 1
    #         incoming_edges[relationship[1]] += 1
        
    #     for node in incoming_edges.keys():
    #         if incoming_edges[node] == n - 1 and outgoing_edges[node] == 0:
    #             return node 
    #     return -1