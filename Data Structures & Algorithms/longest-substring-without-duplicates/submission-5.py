class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        subs=set()
        result= 0
        # s="thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsovert"

        for right in range(len(s)):
            while s[right] in subs:
                subs.remove(s[left])
                left+=1
            subs.add(s[right])
            result = max(result, right-left+1)

            
        return result
        