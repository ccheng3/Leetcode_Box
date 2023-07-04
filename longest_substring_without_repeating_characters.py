class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use sliding window technique 
        # I personally consider sliding-window to be a flavor of 
        # two-pointer technique
        # sliding window consists of the LEFT and RIGHT ptrs 
        #
        #
        # first check empty string edge case - return 0 if input 
        # string is empty 
        #
        # initialize and start left and right ptrs both at index 0
        # initialize a "holding" variable to store longest substring 
        # int length seen so far in the sliding window scan
        # initialize a counter variable to store current working 
        # substring's length  
        #
        # initialize a set; a set stores only unique values 
        # while True:
        #   if right == len of string then you're out of bounds of string,
        #   so update "holding" var if this tail-end substring is longer
        #   and return holding var's value.
        #
        #   if right pts to a value not in the set:
        #       add the value to the set
        #       increment the counter variable
        #       move right one index to the right 
        #   else:
        #       move left one index to the right 
        #       reset right back to pt to where left is at
        #       update "holding" var if current working length > holding
        #       var's length 
        #       clear the set for the next working substring scan
        #       reset counter back to zero.
        #
        # Runtime: O(N) b/c you scan thru the entire input string
        # Space used: O(N) b/c the worst case is a input string with
        # all unique chars, as one large substring, and the set will
        # store all the chars

        if len(s) == 0:
            return 0
        else:
            left = 0
            right = 0
            holding = 0
            counter = 0
            my_set = set()

            while True:
                if right == len(s):
                    if counter > holding:
                        holding = counter
                    return holding 
                if s[right] not in my_set:
                    my_set.add(s[right])
                    counter += 1
                    right += 1
                else:
                    left += 1
                    right = left 
                    if counter > holding:
                        holding = counter
                    my_set.clear()
                    counter = 0
