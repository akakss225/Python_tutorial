def solution(n, words):
    answer = 0
    d = dict()
    for i in range(len(words)):
        if words[i] not in d:
            d[words[i]] = [i%n+1, i // n + 1]
        else:
            return [i%n+1, i // n + 1]
    for i in range(len(words)-1):
        if words[i][-1] != words[i+1][0]:
            return d[words[i+1]]
        else:
            continue
    return [0,0]

# n = 3
# words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))