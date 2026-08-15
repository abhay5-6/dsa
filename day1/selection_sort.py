class Solution:
    def selectionSort(self, nums):
        for i in range(0,len(nums)):
            min_index=i

            for j in range(i+1,(len(nums))):

                if nums[min_index]>nums[j]:
                    min_index=j

            nums[min_index],nums[i]=nums[i],nums[min_index]   

        return nums