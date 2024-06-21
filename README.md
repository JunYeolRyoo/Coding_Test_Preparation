# Leetcode_practice

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        longest = 0
        cur,startInd = 0,0
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
                cur += 1
            else:   # Found Duplicate
                if cur > longest: longest = cur 
                cur = i - dic[s[i]] # Update the current length
                for j in range(dic[s[i]],startInd,-1):  # ex, xyzoqao -> qao (q is now startInd)
                    dic.pop(s[j-1])
                startInd = dic[s[i]] + 1
                dic[s[i]] = i   # Update to found repeating character's index
        if cur > longest:
            return cur
        return longest
