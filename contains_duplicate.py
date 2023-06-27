class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # use a hashmap, count up frequency counts for each unique int val and store in hashmap
        # loop thru hashmap and return True at first occurrence of a freq count > 1. Else return 
        # False if you made it thru the entire loop without returning True.
        # 
        # Runtime: O(N), in worst case the input array contains only unique values so the entire 
        # input array is scanned thru. 
        # 
        # Space used: O(N), in worst case the input array contains only unique values so the 
        # hashmap occupies size proportional to input size N. 
        
        my_dict = {}
        for num in nums:
            if num not in my_dict.keys():
                my_dict[num] = 1
            else:
                return True
        return False
        
        # for key in my_dict.keys():
        #     if my_dict[key] > 1:
        #         return True
        # return False
    
        # optimization: return True at first occurrence of duplicate encountered, else return 
        # False at end of first loop.