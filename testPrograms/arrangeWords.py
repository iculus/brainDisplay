def splitUpParagraph(fileLocation, start, lineLength):
	workingInstruction = prepareInstructionFile(fileLocation)	
	Working = True
	signature = '^'
	#first break up the instruction at line breaks defined by the user
	firstPassList = []
	tempParagraph = []
	#since the prgram uses a signature character, check that this char is not in use
	#send an error if it is!
	for letter in workingInstruction:
		if letter == signature:
			print 'error: do not use the', signature, \
			'character in the instruction or change the', \
			'signature character in splitUpParagraph'
			quit()
	for letter in workingInstruction:
		if letter != '\n':
			tempParagraph.append(letter)
			
		if letter == '\n':
			#add an ending signature
			tempParagraph.append(signature)
			thisParagraph = ''.join(tempParagraph)
			firstPassList.append(thisParagraph)
			tempParagraph = []
	#at this point the variable firstPassList has the user line break formatting
	#there is one list entry per user paragraph
			
	#with firstPassList populated, for each list item check for line lengh requirements
	newLines = []
	newLinesFormatted = []
	lineLengthHere = 0
	exitCondition = False
	for paragraph in firstPassList:
		newLinesThisParagraph = []
		start = 0
		if len(paragraph) <= lineLength: lineLengthHere = len(paragraph) 
		if len(paragraph) > lineLength: lineLengthHere = lineLength
		for i in range (0,100):
			initialChunk = paragraph[start:lineLengthHere+start]
			spaces = []
			chars = []
			for position, char in enumerate(initialChunk):
				if char == ' ' or char == signature:
					spaces.append(position+start)
					chars.append(char)
					if char == signature:
						exitCondition = True
			end = spaces[-1]
			finalChunk = paragraph[start:end]
			if finalChunk[0:1] == ' ':
				finalChunk = finalChunk[1:]
			start = end
			if len(finalChunk) > 0:
				newLinesThisParagraph.append(finalChunk)
		newLines.append(newLinesThisParagraph)
	for entry in newLines:
		if len(entry) > 0:
			for word in entry:
				newLinesFormatted.append(word)
		if len(entry) == 0:
			newLinesFormatted.append('')
	
	
	return newLinesFormatted

def prepareInstructionFile(fileToOpen):
	openFile = open(fileToOpen)
	instructions = []
	for instruction in openFile:
		instructions.append(instruction)
	
	thisSentence = ''.join(instructions)

	return thisSentence
	

if __name__ == "__main__":
	fileLocation = 'instructions/sentence.mike'
	smallerWords = splitUpParagraph(fileLocation, 0, 23)

	print smallerWords

	for i in smallerWords:
		print i

