"""
Num: 186. Reverse Words in a String II
Link: https://leetcode.com/problems/reverse-words-in-a-string-ii/
Problem: Given a character array s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.
Your code must solve the problem in-place, i.e. without allocating extra space.

Example 1:
    Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Example 2:
    Input: s = ["a"]
    Output: ["a"]
Constraints:
    1 <= s.length <= 105
    s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
    There is at least one word in s.
    s does not contain leading or trailing spaces.
    All the words in s are guaranteed to be separated by a single space.
"""


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # At first, reverse array
        s.reverse()

        # if the character indicates ' ', change the order
        def reverseWord(s, first, second):
            while first < second:
                s[first], s[second] = s[second], s[first]
                first, second = first + 1, second - 1

        # main
        first, second = 0, 0
        while first < len(s):
            while s[second] != ' ':
                second += 1
                if second == len(s):
                    break

            reverseWord(s, first, second-1)
            first, second = second+1, second+1
