class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        wordListMap = {}
        for word in strs:
            charCount = {}
            for letter in word:
                if letter in charCount:
                    charCount[letter] += 1
                else:
                    charCount[letter] = 1
            key = tuple(sorted(charCount.items()))
            if key in wordListMap:
                wordListMap[key].append(word)
            else:
                wordListMap[key] = [word]
        for wordList in wordListMap.values():
            output.append(wordList)
        return output

