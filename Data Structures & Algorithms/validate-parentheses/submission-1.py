class Solution:
    def isValid(self, s: str) -> bool:
        
        brac={
            ')' : '(',
            '}' : '{',
            ']' :'['
        }
        st=[]

        for item in s:
            if item in brac.values():
                st.append(item)
            elif item in brac.keys() and st and st[-1] == brac[item]:
                st.pop()
            else:
                return False
        
        if len(st)==0:
            return True
        else:
            return False
        