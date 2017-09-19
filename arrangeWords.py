def splitUpParagraph(workingInstruction, start, lineLength):
	Working = True
	newLines = []
	for i in range (0,20):
		spaces = []
		chars = []
		for position,character in enumerate(workingInstruction[start:lineLength+start]):
			if character == ' ' or character == '\n':
				spaces.append(position+start)
				chars.append(character)
		newlineFound = False
		for location, newline in enumerate(chars):
			if newline == '\n':
				newLineFound = True
		if newLineFound == True:
			end = spaces[location]
		elif newLineFound == False:
			end = spaces[-1]
		print spaces, chars, newLineFound
		newLines.append(workingInstruction[start:end])
		try: start = end+1
		except: start = end
	return newLines


if __name__ == "__main__":
	sentenceFile = open('sentence.mike')

	instructions = []
	for instruction in sentenceFile:
		instructions.append(instruction)
	
	#print instructions
	thisSentence = ''.join(instructions)
	print thisSentence

	smallerWords = splitUpParagraph(thisSentence, 0, 23)

	for i in smallerWords:
		print i

