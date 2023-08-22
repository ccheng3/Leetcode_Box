class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 1) store p's char freq. counts in a hashmap
        # 2) run sliding window thru s with window length
        # equal to the length of p, check every sliding
        # window substring for anagram status.
        # append all anagram starting index to return array
        # Return the return array
        #
        # --> clever optimization improves runtime from O(s * p) to O(s) by
        # removing left char from curr window map and adding new right char to
        # curr window map.
        #
        # Runtime: O(s) where s is len(s).
        # Space used: O(2*p) --> reduces to O(p) --> one map for p, the other map constantly updated 
        # thru sliding window for all substrings in s.
        # Sliding window length is bounded by len(p). 


        # edge case --> len(p) > len(s)
        if len(p) > len(s):
            return []


        # edge case --> len(p) == 0, so all indices of
        # s would be an anagram of p.
        if len(p) == 0:
            return [i for i in range(len(s))]


        p_map = dict()
        return_list = []


        # store char freq count of p
        for char in p:
            if char not in p_map.keys():
                p_map[char] = 1
            else:
                p_map[char] += 1
       
        # run sliding window thru s with two ptrs
        # left --> substring starting index
        # right --> substring end index
        #
        # initialize substring hashmap once, bootstrap
        # with first substring
        #
        # everytime left and right are moved to the right,
        # left char needs to be removed from the hashmap,
        # and right char needs to be added to the hashmap
        #
        # This algo is the more optimal soln compared to the
        # brute force. Brute force runs in O(s * p), while this
        # algorithm runs in O(s) --> b/c you're not looping
        # thru p chars at every sliding window and initializing
        # a hash map at every window instance --> you would also
        # be storing redundant, already-seen
        # char freq counts in the 'core'
        # sliding window substring at each new window, which is
        # wasteful.
        left = 0
        right = len(p) - 1
        curr_window_map = dict()


        # bootstrap the sliding window with the first substring
        # and make the first comparison
        for i in range(left, right + 1):
            char = s[i]
            if char not in curr_window_map.keys():
                curr_window_map[char] = 1
            else:
                curr_window_map[char] += 1


        last_valid_start_window_index = len(s) - len(p)
        while left <= last_valid_start_window_index:
            # compare with p map and append left index
            # if anagrams
            if curr_window_map == p_map:
                return_list.append(left)


            # the tricky thing:
            # - left ptr --> delete left char from curr window
            # hashmap, THEN move left up one index
            #
            # - right ptr --> move right up one index, THEN
            # add right char to curr window hashmap
            #
            # (Their operations are reverse-sequences!!)


            # remove left char from curr window hashmap
            curr_window_map[s[left]] -= 1
            # if removal of left char from curr window hashmap
            # results in zero count, then remove the key from
            # the hashmap.
            if curr_window_map[s[left]] == 0:
                del curr_window_map[s[left]]


            # move left up one index
            left += 1
            # need to make this check --> left is at the
            # last valid index, then moves up one more,
            # and now you NEED to stop the loop, otherwise
            # right would be going out of bounds in s.
            if left > last_valid_start_window_index:
                return return_list


            # move right up one index
            right += 1


            # add right char to curr window hashmap
            if s[right] not in curr_window_map.keys():
                curr_window_map[s[right]] = 1
            else:
                curr_window_map[s[right]] += 1


        return return_list

