import pygame

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

infoObject = pygame.display.Info()
#size = (infoObject.current_w, infoObject.current_h)
# screenWidth = infoObject.current_w
# screenHeight = infoObject.current_h
size =(700,500)
screenWidth = size[0]
screenHeight = size[1]

#screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SART")

fontSize = 40

myfont = pygame.font.SysFont("monospace", fontSize)

CarryOn = True

#what the instructions say
#this throws an error when I put a word between everyone and what... (more than 9 characters there??)
firstInstruction = "these will be more instructions for the task. It is important everyone what they are supposed to do! Click the spacebar to continue."
secondInstruction = "these will be more instructions for the task. It is important that everyone what they are supposed to do! Click the spacebar to continue"
print len (firstInstruction)

def putInstructionsOnScreen (theInstructions):
	#section to divide long string of text into smaller single lines
	import math

	posX = 0
	posY = 0
	position = posX, posY

	#find the rounded up answer of how many lines will be required
	lineLength = 23
	numberLines = math.ceil(len(theInstructions)/(lineLength*1.0))

	words = []
	for line in range(int(numberLines)):
		startPoint = line*lineLength
		endPoint = (line+1)*lineLength
		snip = theInstructions[startPoint:endPoint]
		spaces = []
		for index, letter in enumerate(snip):
			if letter == " ":
				spaces.append(index)
		print spaces
		newLineBreak = spaces[-1]
		print newLineBreak
 		words.append( snip[0:endPoint])

 	fontContainer = []
 	for line in words:
 		fontContainer.append(myfont.render(line,1,WHITE))

 	#print on the screen	
 	screen.fill(BLACK)

 	for line in range(len(fontContainer)):
 		screen.blit(fontContainer[line],(position[0],position[1]+(line*fontSize)))

 	pygame.display.flip()

 	#close when you hit the space bar
 	running = True
 	while running:
 		for event in pygame.event.get():
   			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
   				running = False

putInstructionsOnScreen (firstInstruction)
putInstructionsOnScreen (secondInstruction)