class Solution:
    def findMin(self, nums: List[int]) -> int:
        low ,high = 0,len(nums)-1

        while nums[low]>nums[high]:
            mid = (low+high)//2

            if nums[mid-1]>nums[mid] and nums[mid] <nums[mid+1]:
                return nums[mid]
            elif nums[mid-1]<nums[mid] and nums[mid-1]<nums[high]:
                high = mid -1
            else:
                low = mid + 1
        return nums[low]