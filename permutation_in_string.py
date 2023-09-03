class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # use Neetcode's optimal soln 
        # - b/c guaranteed lower case english chars --> store hashmaps as arrays
        # 1) store s1 char comp
        # 2) store a running count 'matches' that stores num matches
        # btwn s1 and s2 hashmaps --> when matches == 26, then return True
        # 3) run sliding window thru s2 and find the perm, if it exists.
        # return False if OOB and didn't return True inside loop.
        #
        # Runtime: O(s1 + s2) --> O(N) where N = s1 + s2 
        # Space used: O(26) --> used two arrays as char freq count hashmap b/c 
        # guaranteed lower case English letters as input char.  
 
        # edge case: s1 > s2 --> no possible perm of s1 inside s2. 
        if len(s1) > len(s2):
            return False

        s1_comp = [0 for _ in range(26)]
        s2_comp = [0 for _ in range(26)]
        matches = 0

        # store s1 char comp
        for char in s1:
            char_index = ord(char) - ord('a')
            s1_comp[char_index] += 1
        
        # store first sliding window char comp in s2 
        for i in range(len(s1)):
            char = s2[i]
            char_index = ord(char) - ord('a')
            s2_comp[char_index] += 1

        # run thru both char comp arrays only one time and 
        # compute num matches at the start of the algo. 
        for i in range(len(s1_comp)):
            if s1_comp[i] == s2_comp[i]:
                matches += 1

        # print(s1_comp, s2_comp)
        
        # run the sliding window algo and return True when
        # matches == 26. if window goes OOB then return False. 
        left = 0
        right = len(s1) - 1
        while True:
            # return True if matches == 26.
            print(f"left, right, matches: {left, right, matches}") 
            if matches == 26:
                return True 
            # Else, remove the left ptr char from the s2 char comp,
            # then increment left.
            # Then increment right, and add right ptr char to s2 
            # char comp. 
            left_char_index = ord(s2[left]) - ord('a')
            s2_comp[left_char_index] -= 1
            if s2_comp[left_char_index] == s1_comp[left_char_index]:
                matches += 1
            # NOTE: This "only first occurence" check is the hardest 
            # part of the algo to understand, but it makes sense once you 
            # understand this:
            #
            #  --> you do not continue to decrement num
            # matches if you continue to knock a char that you have ALREADY
            # seen out of equality.
            #
            # decrement num matches ONLY ON THE FIRST OCCURENCE of 
            # the char's s2_comp mismatch with its s1_comp. 
            elif s2_comp[left_char_index] + 1 == s1_comp[left_char_index]:
                    matches -= 1
            left += 1

            right += 1
            # return False if sliding window went OOB on right-side
            if right == len(s2):
                return False
            right_char_index = ord(s2[right]) - ord('a')
            s2_comp[right_char_index] += 1
            if s2_comp[right_char_index] == s1_comp[right_char_index]:
                matches += 1
            else:
                # decrement num matches ONLY ON THE FIRST OCCURENCE of 
                # the char's s2_comp mismatch with its s1_comp 
                # (Reasoning --> as in, you DO NOT decrement num matches
                # again if you add another occurence of the same char
                # already in mismatch to the s2_comp.)
                if s2_comp[right_char_index] == s1_comp[right_char_index] + 1:
                    matches -= 1
