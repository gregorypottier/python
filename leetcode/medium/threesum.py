class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        length = len(nums)
        for i, _ in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start, end = i + 1, length - 1

            while start < end:
                total = nums[i] + nums[start] + nums[end] # sum numbers at indices
                # grab i (i), grab number to the right of index i(j), grab last number of list (k)
                # if the sum exceeds 0, move k "down the list"
                # if the sum subceeds 0, move j "up the list until we have a new nums[j] value"
                # if the sum is 0, append to result and increment j
                if total > 0:
                    end -= 1
                elif total < 0:
                    start += 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                else:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1

        return result
