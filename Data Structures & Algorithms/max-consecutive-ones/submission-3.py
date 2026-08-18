class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        result = 0

        for num in nums:
            count = count + 1 if num == 1 else 0
            result = max(result, count)

        return result