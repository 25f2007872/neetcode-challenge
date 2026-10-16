class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums)//2
        dict1= {}
        for num in nums:
            dict1[num] = dict1.get(num, 0) + 1
        sorted_dict = sorted(dict1.keys() ,key= lambda x: dict1[x], reverse=True)
        return sorted_dict[0]