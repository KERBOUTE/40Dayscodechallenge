class Solution:

    def compare(self, word1, word2, order_map):

        for i in range(min(len(word1), len(word2))):
            if word1[i] != word2[i]:
                if order_map[word1[i]] > order_map[word2[i]]:
                    return False
                break

        else:
            if len(word1) > len(word2):
                return False

        return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:

        order_map = {key:value for value, key in enumerate(order)}

        for i in range(1, len(words)):
            if not self.compare(words[i - 1], words[i], order_map):
                return False

        return True
