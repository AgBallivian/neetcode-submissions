class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final_results = []
        operations = []
        posi = 0
        for n in nums:
            nums_act = nums.copy()
            nums_act.pop(posi)
            posi+=1
            result = 1
            for num in nums_act:
                result *= num
            final_results.append(result)
        return final_results