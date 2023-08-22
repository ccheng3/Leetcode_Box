class Solution:
    def romanToInt(self, s: str) -> int:
        # 1) store the roman symbol/val pairs in a hash table
        # 2) scan thru string s and pull out each next
        # int vals, making sure to account for the 6 special cases
        # Add the int vals to a running count
        # Return the running count.


        roman_map = dict()
        symbols = ["I", "V", "X", "L", "C", "D", "M"]
        values = [1, 5, 10, 50, 100, 500, 1000]
        for i in range(len(symbols)):
            roman_map[symbols[i]] = values[i]
       
        # parse thru string s and compute the running sum
        running_sum = 0
        curr = 0
        while curr < len(s):
            curr_symbol = s[curr]
            # if you're looking at the last symbol in the string
            # just add the int val to the running sum and return it
            if curr == len(s) - 1:
                return running_sum + roman_map[curr_symbol]
            # otherwise, check next symbol --> if one of the six
            # special cases is encountered, then we need to add
            # the special int val to running sum, then move
            # curr ptr two indices to the right. Else,
            # not a special case so just add the regular
            # hashed int val to the sum and move curr ptr
            # just one index to the right.
            #
            # NOTE: observe the clever relationship btwn curr and
            # next symbols. If curr sym < next sym, then add their
            # difference to the running sum.
            else:
                next_symbol = s[curr + 1]
                if roman_map[curr_symbol] < roman_map[next_symbol]:
                    running_sum += roman_map[next_symbol] -\
                                roman_map[curr_symbol]
                    curr += 2
                else:
                    running_sum += roman_map[curr_symbol]
                    curr += 1


        # return the sum
        return running_sum

