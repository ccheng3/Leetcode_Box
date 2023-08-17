class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # use two hash tables
        # first table to stores num incoming edges
        # second table to store num outgoing edges
        # the destination city to return will be the city
        # with 1 incoming edge and 0 outgoing edges 
        # --> that is to say, the destination city is the 
        # city 'key' that exists in incoming hashtable and 
        # does not exist in outgoing hashtable. 
        #
        # Runtime: O(N) b/c need to loop thru paths array
        # Space used: O(N) b/c need to use to hash tables

        num_incoming = dict()
        num_outgoing = dict()
        
        for path in paths:
            if path[0] not in num_outgoing.keys():
                num_outgoing[path[0]] = 1
            if path[1] not in num_incoming.keys():
                num_incoming[path[1]] = 1
        
        for city in num_incoming.keys():
            if city not in num_outgoing.keys():
                return city

        