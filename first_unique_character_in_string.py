class Solution:
    def firstUniqChar(self, s: str) -> int:
        # use a hash map
        # this is the algo:
        # 1) loop thru the input string and store the freq. counts for each char (char : count) pairs
        # in the hash map
        # 2) loop thru the string again and find the first char that has a freq count of 1. 
        # This is the first non-repeating char - return its index. 
        # If you don't return the index from the loop in (2) then it doesn't exist and return 
        # -1 as stated in the spec. 
        #
        # Runtime: O(N) b/c you loop thru the string twice, first to store freq. count, second to
        # find and return the index of the first non-repeating char. 
        # Space used: O(N) b/c worst case situation --> all char in the string are unique
        # so hash map uses space equal to the number of unique chars in the string.

        my_dict = dict()
        
        for char in s:
            if char not in my_dict.keys():
                my_dict[char] = 1
            else:
                my_dict[char] += 1

        for index, char in enumerate(s):
            if my_dict[char] == 1:
                return index
        return -1