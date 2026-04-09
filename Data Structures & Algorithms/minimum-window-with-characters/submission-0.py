class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        for char in t:
            freq[char] = freq.get(char, 0) + 1

        l = 0
        res = ""
        need = len(t) 

        for r in range(len(s)):
            if s[r] in freq:
                if freq[s[r]] > 0:
                    need -= 1      
                freq[s[r]] -= 1

            while need == 0:   
                if res == "" or r - l + 1 < len(res):
                    res = s[l:r+1]
                if s[l] in freq:
                    freq[s[l]] += 1
                    if freq[s[l]] > 0:
                        need += 1 
                l += 1

        return res






        