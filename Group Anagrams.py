from collections import defaultdict
def groupAnagrams(strs):
    anagramy = defaultdict(list)
    n = len(strs)
    for i in range(n):
        key = "".join(sorted(strs[i]))
        anagramy[key].append(strs[i])
    return list(anagramy.values())
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))