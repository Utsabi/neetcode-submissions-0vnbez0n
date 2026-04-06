class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''.join(c for c in s.lower() if c.isalnum())

        st, end = 0, len(word)-1

        while st <= end:
            if word[st]!= word[end]:
                return False
            st +=1
            end -=1
            
        return True