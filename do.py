word = []
allc= {}
with open('u2.txt') as words:
	for line in words:
		if line != '\n':
		    word.append(line)
		else:
			word.append('111')
i = 0
while i < len(word):
	answer = []
	if word[i] == '111':
		g = i + 1
		if word[g] != '111':
			name = word[g]
			g += g
			while word[g] != '111':
				answer.append(word[g]) 
				print(answer)
				if g < len(word) - 2:
					g = g + 1
			allc[name] = answer
	i += i
print(allc)
		
		