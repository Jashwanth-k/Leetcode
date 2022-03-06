class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = j = 0
        vowels = ['a','e','i','o','u']
        currVowels = 0
        maxVowels = float('-inf')
        
        while j < len(s):
            if s[j] in vowels:
                currVowels += 1
            if (j-i+1) == k:
                maxVowels = max(maxVowels,currVowels)
                if s[i] in vowels:
                    currVowels -= 1
                i += 1
            j += 1
        return maxVowels
                    