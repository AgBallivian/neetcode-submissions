class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_indx = 0
        for n in nums:
            search = target - n
            search_indx = 0
            for s in nums:
                if search == s and search_indx != n_indx:
                    return [n_indx, search_indx]
                search_indx += 1    
            n_indx += 1     
            