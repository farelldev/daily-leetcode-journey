class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList: return 0

        neighbor = collections.defaultdict(list)
        if beginWord not in wordList: wordList.append(beginWord)
        visited = {beginWord}
        q = deque([beginWord])
        res = 1

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbor[pattern].append(word)

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord: return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in neighbor[pattern]:
                        if neiWord == word or (neiWord in visited): continue
                        q.append(neiWord)
                        visited.add(neiWord)
            res += 1

        return 0