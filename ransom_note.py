class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # use two hashtables
        # store ransomnote and magazine's char freq counts in
        # their respective hash tables
        #
        # loop thru ransomnote's hash table and check to see that
        # for each ransomnote char, magazine's hash table char
        # freq count is >= ransomnote char count.
        # Return False at first occurrence of insufficient num
        # of magazine char count available for ransomnote.
        # Else, return True when entire ransomnote is looped thru.
        #
        # Runtime: O(R + M) where R is len(ransomNote) and
        # M is len(magazine)
        # Space used: O(R + M) b/c you store char freq counts
        # of all unique chars in both ransomNote and magazine,
        # with is of size proportional to order of R and M,
        # respectively.  


        ransom_map = dict()
        magazine_map = dict()


        # store ransom note's char freq counts
        for char in ransomNote:
            if char not in ransom_map.keys():
                ransom_map[char] = 1
            else:
                ransom_map[char] += 1
       
        # store magazine's char freq counts
        for char in magazine:
            if char not in magazine_map.keys():
                magazine_map[char] = 1
            else:
                magazine_map[char] += 1


        # loop thru ransom map and make sure adequate
        # char freq counts exists in magazine map
        for char in ransom_map.keys():
            if char not in magazine_map.keys() or\
            magazine_map[char] < ransom_map[char]:
                return False
        return True



