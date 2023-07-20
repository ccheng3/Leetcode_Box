class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # use two sets 
        # 1) put all of the unique ints from nums1 in set1
        # put all of the unique ints from nums2 in set2
        # 2) find the smaller set
        # loop over the smaller set and find matches in the larger/equal-sized set
        # append the matches to the return array 
        # return the return array 
        #
        # Runtime: O(M + N) --> O(M + N) + O(min(M, N)), where M is size of num1 
        # and N is size of num2
        # In the worst case, num1 and num2 have completely different int values and 
        # the intersection is empty. O(M + N) operations to loop thru both num1 and 
        # num2 to build their sets. Then O(min(M, N)) total checks of each int in the
        # smaller set if exists in the larger set.
        #
        # (REMEMBER: set() is implemented as a hash table which means lookup runs in
        # O(1) time!!!! Python dict() too. )
        #
        # Space used: O(i + k), where i == num unique vals in nums1, same thing for k.
        # Worst case --> nums1 and nums2 both have completely different, all unique 
        # values and so i == M and k == N, and O(M + K) total space used. 

        set1 = set()
        set2 = set()

        for num in nums1:
            if num not in set1:
                set1.add(num)
        for num in nums2:
            if num not in set2:
                set2.add(num)

        return list(set1.intersection(set2))
         