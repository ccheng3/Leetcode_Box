class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use a hashmap 
        # store the frequency counts of the char in both strings in two separate hash maps
        # loop thru the key chars of string 's' hashmap and verify that the freq count is the 
        # same in string 't' hashmap 
        # return False if EITHER the key char from 's' does not exist in 't' hashmap, or the 
        # freq count is not equal. 
        # return True if you succesfully finish loop thru key chars of string 's' hashmap
        #
        # Runtime: O(M + N) --> the worst case --> s has size M, t has size N, and 
        # s and t are completely different strings so 
        # O(M) time to build s hashmap, O(N) time to build t hashmap, and only 1 comparison
        # required in the loop thru string s hashmap to determine mismatch and return False. 
        #
        # Space used: Worst case --> s and t completely different strings so 
        # 's' size is M, 't' size is N --> O(M + N) total space used. 

        s_dict = dict()
        t_dict = dict()

        # two strings that do not have the same length are automatically not anagrams. Return False.
        if len(s) != len(t):
            return False

        for char in s:
            if char not in s_dict.keys():
                s_dict[char] = 1
            else:
                s_dict[char] += 1
        
        for char in t:
            if char not in t_dict.keys():
                t_dict[char] = 1
            else:
                t_dict[char] += 1

        for char in s_dict.keys():
            if char not in t_dict.keys() or s_dict[char] != t_dict[char]:
                return False
        return True

        