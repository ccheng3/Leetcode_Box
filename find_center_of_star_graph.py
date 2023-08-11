class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # 1) use a hash table to count up the number of edge relationships
        # that each node has 
        # 2) return the node that has (N - 1) edge relationships 
        #
        # return the center node --> the center node will have a hash table
        # count of exactly (N - 1). 
        #
        # Runtime: O(E) where you have to look at every single edge relationship
        # in the graph. 
        # Space used: O(V), where space used in the hash table is proportional to
        # the total number of nodes (vertices) in the graph. 

        edge_counts = dict()
        for edge in edges:
            start_vertex = edge[0]
            end_vertex = edge[1]
            if start_vertex not in edge_counts.keys():
                edge_counts[start_vertex] = 1
            else:
                edge_counts[start_vertex] += 1
            if end_vertex not in edge_counts.keys():
                edge_counts[end_vertex] = 1
            else:
                edge_counts[end_vertex] += 1
        for node in edge_counts.keys():
            if edge_counts[node] == len(list(edge_counts.keys())) - 1:
                return node