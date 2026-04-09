class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        ch={}

        for r in range(len(s)):    
            ch[s[r]]= ch.get(s[r], 0) + 1

            if (r-l+1)-max(ch.values())>k:
                
                ch[s[l]]-=1
                l+=1
            
            res=max(res,r-l+1)

        return res





