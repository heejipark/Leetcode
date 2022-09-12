"""
Num: 20. Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/
Problem: 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
 Example 1:
    Input: s = "()"
    Output: true
Example 2:
    Input: s = "()[]{}"
    Output: true
Example 3:
    Input: s = "(]"
    Output: false
Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:

        # Open brackets must be closed by the same type of brackets
        # Set dictionary to match each pair
        dic = {')': '(', ']': '[', '}': '{'}

        # In order to check the correct order
        # use stack.
        stack = []

        for char in s[::-1]:
            if len(stack) == 0 and char in dic.values():
                return False
            # if char is closed bracket, simply insert the bracket into stack
            if char in dic.keys():
                stack.append(char)
            else:  # if char is open bracket,
                # check whether the last element of stack is paried with current bracket
                if dic[stack.pop()] != char:
                    return False

        if stack:
            return False
        return True


# Runtime: 61 ms, faster than 21.18% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.8 MB, less than 98.11% of Python3 online submissions for Valid Parentheses.


# The opposite order
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if len(stack) == 0 and char in dic.keys():
                return False
            if char in dic.values():
                stack.append(char)
            else:  # closing brackets
                top = stack.pop()
                if dic[char] != top:
                    return False

        if stack:
            return False
        return True
