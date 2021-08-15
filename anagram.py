"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dics ={}

        for word in strs:
            sorted_words  ="".join(sorted(word))

            if sorted_words not in dics:
                dics[sorted_words] = [word]
            else:
                dics[sorted_words].append(word)

        
        result =[]
        
        for item in dics.values():
            result.append((i))

        return result
        
