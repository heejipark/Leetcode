"""
Num: 49. Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/
Problem: 
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
    Input: strs = [""]
    Output: [[""]]
Example 3:
    Input: strs = ["a"]
    Output: [["a"]]
"""

# Solution 1: Using sorted()


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = collections.defaultdict(list[str])

        for word in strs:
            sorted_word = ''.join(sorted(word))
            dic[sorted_word].append(word)

        return dic.values()

# Runtime: 110 ms, faster than 89.93% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.9 MB, less than 59.86% of Python3 online submissions for Group Anagrams.


# Solution 2: Improeved time complexity O(nk)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

# Runtime: 110 ms, faster than 89.93% of Python3 online submissions for Group Anagrams.
# Memory Usage: 19.9 MB, less than 21.60% of Python3 online submissions for Group Anagrams.
