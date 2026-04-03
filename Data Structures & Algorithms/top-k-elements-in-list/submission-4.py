class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        for item in nums:
            map[item] = map.get(item, 0) + 1
        result = sorted(map, key=lambda x:map[x], reverse=True)[:k]
        return result
        