class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack 
        # loop thru the entire input string
        # push every open bracket onto the stack 
        # if you encounter a closing bracket, pop top off stack and 
        # make a comparison. If valid pair, then continue. 
        # Else return false.
        # 
        # Edge cases:
        # 1) You encounter a closing bracket but the stack is empty. Return false. 
        # 2) You loop thru the entire input string but the stack still 
        # contains open brackets. Return false. 
        # 
        # Runtime: O(N) b/c the worst case is an input string with only
        # open brackets. You have to loop thru the entire input string.
        # Space used: O(N). Same worst case - input string contains only
        # open brackets. You use extra space proportional to the size of
        # this input string. 

        my_stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                my_stack.append(char)
            else:
                # must be a closing bracket, b/c prompt says the string
                # contains only open or closing brackets.
                if len(my_stack) == 0:
                    return False
                top = my_stack.pop()
                if top == '(' and char != ')' or\
                top == '{' and char != '}' or\
                top == '[' and char != ']':
                    return False
        return False if len(my_stack) > 0 else True
