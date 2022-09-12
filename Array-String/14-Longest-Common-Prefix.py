class Solution:
    def CompareTwoWords(self, common: str, nextWord: str) -> str:

        minLen = min(len(common), len(nextWord))
        for i in range(minLen):
            if common[i] != nextWord[i]:
                return common[:i]

        return common[:minLen]

    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        # At first, set the first word as a common string
        common = strs[0]

        # iterate over the array to find common words
        for nextWord in strs[1:]:
            common = self.CompareTwoWords(common, nextWord)

        return common

# Runtime: 42 ms, faster than 81.64% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.9 MB, less than 50.09% of Python3 online submissions for Longest Common Prefix.
