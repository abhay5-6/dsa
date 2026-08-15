class Solution:
    def insertionSort(self, nums):
        for i in range(1, len(nums)):
            key = nums[i]
            k = i

            for j in range(i):
                if nums[j] > key:
                    k = j
                    break

            for j in range(i - 1, k - 1, -1):
                nums[j + 1] = nums[j]

            nums[k] = key

        return nums