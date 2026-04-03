class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # result ={}
        # from collections import defaultdict
        result = defaultdict(list) 
        for word in strs:
            word_sort = "".join(sorted(word))
            result[word_sort].append(word)
        
        return list(result.values())
            