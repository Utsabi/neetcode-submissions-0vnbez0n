class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j=0,len(heights)-1

        result=0

        while i!=j:
            if heights[i]<heights[j]:
                value = (j-i)*heights[i]
                result = max(result,value)
                i+=1
            else:
                value = (j-i)*heights[j]
                result = max(result,value)
                j-=1
        return result