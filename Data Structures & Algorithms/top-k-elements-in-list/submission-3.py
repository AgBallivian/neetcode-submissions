class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        out_list = []
        sort_count = {c: v for c, v in sorted(count.items(), key=lambda item: item[1])}
        for key in sort_count:
            out_list.append(key)
        out_list=out_list[-k:]
        return out_list