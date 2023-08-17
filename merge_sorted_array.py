class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # use Neetcode's solution
        # start at the end of nums1 array and put values in backwards
        # fashion
        #
        # Runtime: O(n) b/c just need to loop thru nums2 array to merge
        # into nums1 array
        # Space used: O(1) b/c only pointers are needed.

        # p1 ptr --> points to current nums1 index to insert next val at
        # p2 ptr --> points to current nums2 value to merge into nums1
        # n1e --> points to nums1 end value to possibly insert over
        # to p1 index if needed. (You compare btwn the vals at p2 and n1e
        # indices to see which one to insert at p1).

        # don't forget the two edge case checks from brute solution
        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return

        p1 = len(nums1) - 1
        p2 = n - 1
        n1e = m - 1

        while p2 >= 0:
            # ATTENTION --> This one was the 3rd edge case. 
            # if n1e goes out of bounds, then copy nums2 into nums1 
            # from p1 back to index zero (backwards copy)
            if n1e < 0:
                while p1 >= 0:
                    nums1[p1] = nums2[p2]
                    p2 -= 1
                    p1 -= 1
            if nums2[p2] >= nums1[n1e]:
                nums1[p1] = nums2[p2]
                p2 -= 1
                if p2 == -1:
                    return
            else:
                nums1[p1] = nums1[n1e]
                n1e -= 1
            p1 -= 1
        