class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        seen = {}
        start = maxLength = 0

        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= start: # current char has been seen before and it is being seen after the start of the substring
                start = seen[s[i]] + 1 # reinitialize start index
            else:
                maxLength = max(maxLength, i - start + 1) # reinitialize maxLength to itself or previous substring length
            seen[s[i]] = i
        print(seen)
        return maxLength
