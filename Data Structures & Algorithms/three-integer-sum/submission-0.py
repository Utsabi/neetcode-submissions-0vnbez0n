class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        i=0
        nums.sort()

        while i<len(nums):
            j,k=i+1,len(nums)-1
            target= (-nums[i])
            while j < k:
                if j==i:
                    j+=1
                if k==i:
                    k-=1
                if nums[j]+nums[k]==target:
                    if [nums[j],nums[i],nums[k]] not in result:
                        result.append([nums[j],nums[i],nums[k]])
                    j+=1
                elif nums[j]+nums[k]<target:
                    j+=1
                else:
                    k-=1
            i+=1


        return result


