class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        subs={}
        result= 0
        count=0
        while i < len(s):
            if s[i] not in subs:
                subs[s[i]] = i
                count+=1
                i+=1
                result=max(result,count)
            else:
                i= subs[s[i]]+1
                subs={}
                count=0

        return result
        