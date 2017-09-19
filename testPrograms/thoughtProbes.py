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

onTask = "Were yout thinking about something other than what you were doing?"
stimulusDependent = "where you thinking about your surroundings?"
freelyMoving = "Was your mind moving about freely?"

margin = 0

border = 200
numBoxes = 7
sWidth = size[0]-border
sHeight = size[1]-border
calculatedBoxHeight = sHeight/numBoxes - margin
calculatedBoxWidth = calculatedBoxHeight

calculatedMarginWidth = sWidth-sHeight



for column in range(0+margin, sHeight, calculatedBoxWidth+margin):
    for row in range(0+margin, sHeight, calculatedBoxHeight+margin):
        pygame.draw.rect(screen, WHITE, [column+(calculatedMarginWidth/2)+(border/2),row+(border/2),calculatedBoxWidth,calculatedBoxHeight])

pygame.display.flip()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				running = False