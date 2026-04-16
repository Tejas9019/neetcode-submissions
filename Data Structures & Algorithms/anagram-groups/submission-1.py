from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            # Sort the word
            key = "".join(sorted(word))

            # Add the word to the hashmap
            anagram_map[key].append(word)

        return list(anagram_map.values())
            

        