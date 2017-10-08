import os
import pygame, sys
from pygame.locals import *

#function to scale the values
def translate(value, leftMin, leftMax, rightMin, rightMax):
	# Figure out how 'wide' each range is
	leftSpan = leftMax - leftMin
	rightSpan = rightMax - rightMin

	# Convert the left range into a 0-1 range (float)
	valueScaled = float(value - leftMin) / float(leftSpan)

	# Convert the 0-1 range into a value in the right range.
	return rightMin + (valueScaled * rightSpan)

# set window size
width = 700
height = 500
#set  slider bar size
tall = 30
wide = 17
lengthS = 100
lengthE = width-lengthS*2
#set line properties
heightMid = height/2
widthMid = width/2
lineWeight = 2
#set userProperties
lowVal = -7
highVal = 7
# initilaise pygame
pygame.init()
windowSurfaceObj = pygame.display.set_mode((width,height),1,16)
redColor = pygame.Color(255,0,0)
blackColor = pygame.Color(0,0,0)
whiteColor = pygame.Color(255,255,255)

#starting position
x = width/2 - wide/2
steps = abs(lowVal)+abs(highVal)
stepSize = lengthE*1.0/steps
for i in range(steps+1):
	pygame.draw.rect(windowSurfaceObj,whiteColor,Rect(lengthS+i*stepSize,height/2-20,lineWeight,40))
pygame.draw.rect(windowSurfaceObj,whiteColor,Rect(lengthS,heightMid-lineWeight/2,lengthE,lineWeight))
pygame.draw.rect(windowSurfaceObj,redColor,Rect(x,height/2-tall/2,wide,tall))
pygame.display.update(pygame.Rect(0,0,width,height))

s = 0
while s == 0:
	button = pygame.mouse.get_pressed()
	if button[0] != 0:
		pos = pygame.mouse.get_pos()
		x = pos[0]
		y = pos[1]
		a = x - wide/2
		if a < 0:
		  a = 0
		if a > width-lengthS-wide/2: a = width-lengthS-wide/2
		if a < lengthS-wide/2: a = lengthS-wide/2
		print translate (a+wide/2,lengthS,width-lengthS,lowVal,highVal)
		pygame.draw.rect(windowSurfaceObj,blackColor,Rect(0,0,width,height))
		for i in range(steps+1):
			pygame.draw.rect(windowSurfaceObj,whiteColor,Rect(lengthS+i*stepSize,height/2-20,lineWeight,40))
		pygame.draw.rect(windowSurfaceObj,whiteColor,Rect(lengthS,heightMid-lineWeight/2,lengthE,lineWeight))
		#pygame.display.update(pygame.Rect(0,0,width,height))
		pygame.draw.rect(windowSurfaceObj,redColor,Rect(a,height/2-tall/2,wide,tall))
		pygame.display.update(pygame.Rect(0,0,width,height))


# check for ESC key pressed, or pygame window closed, to quit
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
