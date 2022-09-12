"""
Num: 5. Longest Palindromic Substring
Link: https://leetcode.com/problems/longest-palindromic-substring/
Problem: 
    Given a string s, return the longest palindromic substring in s.
Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.
Example 2:
    Input: s = "cbbd"
    Output: "bb"
Constraints:
    1 <= s.length <= 1000
    s consist of only digits and English letters.
"""

# Solution from David


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        is_palindrome = [[False for i in range(n)] for j in range(n)]
        start = 0
        end = 0

        # Length = 1
        for i in range(n):
            is_palindrome[i][i] = True
            start = i
            end = i

        # Length = 2
        for i in range(1, n):
            if s[i - 1] == s[i]:
                is_palindrome[i - 1][i] = True
                start = i - 1
                end = i

        # Length >= 3
        for length in range(2, n):
            i = 0
            j = length

            while j < n:
                if is_palindrome[i + 1][j - 1] and s[i] == s[j]:
                    is_palindrome[i][j] = True
                    if end - start < j - i:
                        start = i
                        end = j

                i += 1
                j += 1

        return s[start:end + 1]
