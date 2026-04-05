class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)

        st =[]

        for item in nums:
            if item - 1 not in nums:
                st.append(item)
        
        result=0
        for item in st:
            count=1
            while item+1 in nums:
                count +=1
                item = item+1
            if result< count:
                result= count
        
        return result






        