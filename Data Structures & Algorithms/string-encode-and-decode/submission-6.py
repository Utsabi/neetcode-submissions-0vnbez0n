class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded ="#"
        for item in strs:
            encoded = encoded + str(len(item))+"n" + item +"#"
        return encoded 


    def decode(self, s: str) -> List[str]:
        lst=[]
        st=0
        print(s)
        while st< len(s)-1:
            if s[st] == "#":
                num = ""
                st += 1
                while st < len(s) and s[st].isdigit():  # collect digits
                    num += s[st]
                    st += 1
                length = int(num)   # get length
                if length == 0:
                    word = ""
                else:
                    word = s[st+1 : st+1+length]  # extract word
                lst.append(word)
                st = st + 1 + length    # jump to next #
            else:
                st += 1
        return lst
                




        
       

        
