class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        visited = set()
        is_present = False # flag for checking if endword is in the wordlist dict or not
        for word in wordList:
            if word == endWord:
                is_present = True
            visited.add(word)

        if not is_present:
            return 0

        queue = deque()
        queue.append(beginWord)
        depth = 0
        # going for until queue is empty
        while queue:

            depth += 1
            Q_size = len(queue)
            # for all the words at the same level (matched possible words)
            for _ in range(Q_size):
                curr = queue.popleft()
                # going for all the chars in each word
                for i in range(len(curr)):
                    temp = list(curr)
                    # checking for all transforming , each character at a time replaced by digits from a-z (26 times, constant loop)
                    for c in range(97, 123):
                        temp[i] = chr(c)

                        if "".join(temp) == curr:
                            continue
                        if "".join(temp) == endWord:
                            return depth + 1

                        if "".join(temp) in visited:
                            queue.append("".join(temp))
                            visited.remove("".join(temp))

        return 0
