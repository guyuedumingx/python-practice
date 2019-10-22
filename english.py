
with open('u2.txt') as obj:
    words = obj.readlines()

i = 0
key_word = {}

while i < len(words):
    if words[i] == '\n':
        if i < len(words) - 2:
            i = i + 1
        else:
            break
        answer = []
        name = words[i]
        if i < len(words) - 2:
            i = i + 1
        else:
            break
        while words[i] != '\n':
            answer.append(words[i])
            if i < len(words) - 2:
                i = i + 1
            else:
                break
        key_word[name] = answer
    else:
        i = i + 1
print(key_word)