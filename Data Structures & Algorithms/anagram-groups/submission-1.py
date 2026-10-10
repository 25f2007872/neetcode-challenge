class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <=1:
            return [strs]
        else:
            newdict = defaultdict(list)
            for word in strs:
                sortedword = "".join(sorted(word))
                newdict[sortedword].append(word)
    
        return list(newdict.values())