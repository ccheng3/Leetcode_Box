class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # only one valid answer exists --> you're guaranteed that
        #
        # use a hash map 
        # loop thru the array
        # for each int in the array, calc the difference and check if 
        # it exists in the hash map. 
        # if exists, then return the indices of the two numbers 
        # else DNE, so store the int and array index as key : value pair
        # in the hashmap
        # 
        # Runtime: O(N), in worst case last two numbers in array 
        # make up the pair and so you have to scan thru entire array
        # Space used: O(N), same worst case, so you have to store
        # almost entire input array (size N - 1, really) into hash map.

        my_dict = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in my_dict.keys():
                return [my_dict[diff], index]
            else:
                my_dict[num] = index
          