class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_d = {}
        for num in nums:
            num_d[num] = num_d.get(num, 0) + 1
        sorted_ls = sorted(num_d.keys(), key=lambda x: num_d[x], reverse = True)
        return sorted_ls[:k]