from collections import deque

def wordLadder(beginWord, endWord, wordList):
    wordSet = set(wordList)

    if endWord not in wordSet:
        return []

    queue = deque()
    queue.append((beginWord, [beginWord]))

    visited = set([beginWord])

    while queue:
        currentWord, path = queue.popleft()

        if currentWord == endWord:
            return path

        for i in range(len(currentWord)):
            for a in range(26):
                letter = chr(ord('a') + a)

                if letter == currentWord[i]:
                    continue

                newWord = currentWord[:i] + letter + currentWord[i+1:]

                if newWord in wordSet and newWord not in visited:
                    queue.append((newWord, path + [newWord]))
                    visited.add(newWord)

    return []


# Run function
result = wordLadder("hit", "cog", ["hot", "lot", "log", "dog", "cog"])

# Print result and total steps
if result:
    print("Path:", result)
    print("Total steps:", len(result))
else:
    print("No transformation found")