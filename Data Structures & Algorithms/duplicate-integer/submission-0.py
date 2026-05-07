class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        for item in nums:
            if nums.count(int(item)) > 1:
                return True
        return False