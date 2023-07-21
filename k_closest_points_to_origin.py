class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use a heap! - in this case I want to use a min-heap b/c I want to return 
        # the k closests points to the origin 
        #
        # My algo:
        # 1) loop thru the input array 'points' and calculate each points' distance
        # from the origin, and append that tuple(distance : point) casted pair to an 
        # auxiliary holding array.
        #
        # 2) heapify() the aux holding array, keep as min-heap default. Distances are stored as 
        # first value in the tuples so min-heap ordered by smallest to largest distances. 
        #
        # 3) Pop off the k smallest distances from the min-heap and append their 
        # paired coordinate value to the return list.
        # Return the return list of k closest coordinates to origin.
        #
        # Runtime: O(N) to calculate all point distances, heapify() the aux array to min-heap.
        # Space used: O(N) b/c min-heap is used to order (distance : point) pairs from closest
        # distance to farthest distance. 

        import heapq
        import math

        distances = []
        origin = [0, 0]         # all you have to due is change the origin coordinates to 
                                # scale with another other point
        return_list = []
        for point in points:
            # it was actually the manual math calculation PEMDAS error that was producing 
            # the wrong calculated distances smh 
            a_squared = (abs(point[0]) - origin[0]) ** 2
            b_squared = (abs(point[1]) - origin[1]) ** 2
            distance = math.sqrt(a_squared + b_squared)

            distances.append(tuple([distance, point]))
        
        heapq.heapify(distances)
        for _ in range(k):
            small_dist = heapq.heappop(distances)
            return_list.append(small_dist[1])
        
        return return_list
