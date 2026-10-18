class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        new = ""
        i , j = 0, 0
        while i < m and j < n:
            new+=word1[i] + word2[j]
            i += 1
            j += 1
        while i < m:
            new+=word1[i]
            i += 1

        while j < n:
            new+=word2[j]
            j += 1
        return new