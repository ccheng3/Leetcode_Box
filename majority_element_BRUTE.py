class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # brute force solution - use a hash map 
        # record the frequency counts for each unique element in the hashmap
        # key : value ---> unique element is the key, and its freq count is the
        # associated value. 
        #
        # Then, loop thru the hashmap and return the majority element
        # (its freq count is > floor(n / 2) as stated in the spec)
        #
        # May assume that majority element ALWAYS exists in the array.
        #
        # Runtime: O(N) b/c need to loop thru entire input array to record 
        # freq counts in the hash map
        # Space used: O(N), where N equal to the num of unique elements in 
        # the input array 

        my_dict = dict()
        for num in nums:
            if num not in my_dict.keys():
                my_dict[num] = 1
            else:
                my_dict[num] += 1
        
        for key in my_dict.keys():
            if my_dict[key] > len(nums) // 2:
                return key
