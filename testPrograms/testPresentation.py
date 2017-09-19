import pygame
import random
import time

pygame.init()

#randomly selected block duration in ms
blockDuration = random.randrange(10000, 15000)

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

myfont = pygame.font.SysFont("monospace", 40)
clock = pygame.time.Clock()

CarryOn = True

startTime1 = pygame.time.get_ticks()

def putCharOnScreen(character,waittime):
	#this is a placeholder while keypress is not pressed
	keypress = 'null'
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONUP: pass
		if event.type == pygame.MOUSEBUTTONDOWN: pass
		if event.type == pygame.QUIT:
			CarryOn = False
		if event.type == pygame.KEYDOWN:
			print pygame.KEYDOWN
			#CHallenge, in this spot, put an if stament when the keydown is 'q' then do the indented crap
			#	CarryOn = False
			#	pygame.display.quit()
			#	pygame.quit()
			if character == '3':
				keypress = event
				print 'heyo', event

	#something to check for the display type (ie a + or a number)
	if character == '+':
		print 'we are in a plus display mode'
		#put the sound contrl herek
	elif character != '+':
		print 'we are not in a plus mode, we are in a number mode (1:9)'
	label = myfont.render(character,1, WHITE)
	screen.fill(BLACK)
	screen.blit(label, (screenWidth/2,screenHeight/2))
	pygame.display.flip()
	pygame.time.delay(waittime)
	return keypress

clock.tick(60)
while CarryOn:
	#start a timer
	currentTimeSinceStart = 0

	#while the timer is less than the block duration timer set at the top do the following
	while currentTimeSinceStart <= blockDuration:
		#set the current time
		currentTimeSinceStart = pygame.time.get_ticks() - startTime1

		#set variables for time ranges
		plusTimeRange = random.randrange(900,1200)
		numSelector = random.randrange(1,9)
		thereturned1 = putCharOnScreen('+', plusTimeRange)
		thereturned2 = putCharOnScreen(str(numSelector),250)
		#the folllowing is just to check that timer values work and to check that all variables are accesible here
		print plusTimeRange, '+', thereturned1, '\t', numSelector, thereturned2
		#once you have all the useful info printing above this line code, then pickle, save, transmit on port here
		#import code -- you will have to write this, I can help
		#code
		#import pickle -- this exists 
		#pickle
		#import transmit --- you will have to write this, I will help
		#transmit

	#after the block timer is done, do these things:
	putCharOnScreen('+',random.randrange(900,1200))
	CarryOn = False
	pygame.display.quit()
	pygame.quit()

	