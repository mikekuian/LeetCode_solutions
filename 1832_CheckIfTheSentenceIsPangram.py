# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        l_alphabet = [ord(alphabet[i]) - ord('a') + 1 for i in range(26)]

        for char in sentence:
            if l_alphabet[ord(char) - ord('a')]:
                l_alphabet[ord(char) - ord('a')] = 0

        return not sum(l_alphabet)
