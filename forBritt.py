from psychopy import visual, core, event
import numpy
import random
import pygame
import time
from array import array

pygame.mixer.pre_init(44100, -16, 1, 2)

''' CLASS FOR FREQUENCY GENERATION '''
class Note(pygame.mixer.Sound):

    def __init__(self, frequency, volume=.01):
        self.frequency = frequency
        pygame.mixer.Sound.__init__(self, self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(pygame.mixer.get_init()[0] / self.frequency))
        samples = array("h", [0] * period)
        amplitude = 2 ** (abs(pygame.mixer.get_init()[1]) - 1) - 1
        for time in xrange(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples

''' START OF PROGRAM '''
#set display properties
win = visual.Window (size = [800,600],fullscr = False)
mouse = event.Mouse(visible = False)

#define the fixation as a plus sign
fixation= visual.TextStim(win, text = "+", height = .1)

#set block characteristics
blockNum = 1
maxBlockNum = 2

pygame.mixer.init()

while blockNum <= maxBlockNum:
	startTime_Block = time.time()	#set up time keeping for block start

    #define the number of trials shortened for testing(23,69), randoms updated every block start
	maxTrialNumber = random.randrange(20,22)
	THISTRIAL = True	# to start the trial looper
	trialNum = 0		

	while THISTRIAL:
		startTime_Trial = time.time()		#set up timekeeping for trial start
		
		#set up music files, randoms are updated ever trial start
		toneOnset = random.uniform(0.4,0.65)

		#math for sound, randoms are updated every trial start
		startOfISI = 0
		endOfISI = random.uniform(0.9,1.2)
		startOfTone = startOfISI + toneOnset
		endOfTone = startOfTone + 0.2

		#to check that we are less than 10 trials from the end, randoms are updated every trial start	
		endOf3 = 10
		if trialNum <= maxTrialNumber-endOf3: stimulus = random.choice([1,2,3,4,5,6,7,8,9])
		if trialNum > maxTrialNumber-endOf3: stimulus = random.choice([1,2,4,5,6,7,8,9])
	
		digit = visual.TextStim (win, stimulus)
		endOfDigit = 0.25
	
			
		''' PRESENT THE FIXATION FOR ISI TIME '''	
		startTime_FixationDraw = time.time()		#set up timekeeping for fixation draw start
		currentTime = time.time()
		toneProbability = random.randrange(1,100)
		didWeSound = False
		while currentTime - startTime_FixationDraw <= endOfISI:
			tone = False
			currentTime = time.time()
			fixation.draw()
			win.flip()
			#code to play a tone for the durration 75% of the time
			if currentTime-startTime_FixationDraw >= startOfTone and currentTime-startTime_FixationDraw <= endOfTone:
				if toneProbability < 75 and trialNum > 0: tone = True
				else: tone = False
			else: tone = False

			if tone: 
				Note(600).play(-1)
				didWeSound = True
			if not tone: pygame.mixer.stop()
            
			if event.getKeys(keyList=["escape"]):
				win.close()
				core.quit()
		
		''' PRESENT THE DIGIT FOR ISI TIME '''	
		startTime_DigitDraw = time.time()		#set up timekeeping for digit draw start
		currentTime = time.time()
		keyPress = False
		RT = 'null'
		while currentTime - startTime_DigitDraw < endOfDigit:
			currentTime = time.time()
			digit.draw()
			win.flip()
			if event.getKeys(keyList=["space"]):
				if keyPress == False:	#ensure a single keypress here
					RT = currentTime-startTime_DigitDraw
					keyPress = True
			if event.getKeys(keyList=["escape"]):
				win.close()
				core.quit()
		print "RT: %s \t digit: %d \t trial: %d \t block: %d \t maxTrial: %d \t maxBlock: %d \t ISI: %f \t didWeSound %s" \
		% (RT, stimulus, trialNum, blockNum, maxTrialNumber, maxBlockNum, endOfISI, didWeSound)
			
		#exit conditions
		if trialNum == maxTrialNumber:
			
			''' PRESENT THE FIXATION FOR ISI TIME '''	
			startTime_FixationDraw = time.time()		#set up timekeeping for fixation draw start
			currentTime = time.time()
			while currentTime - startTime_FixationDraw <= endOfISI:
				currentTime = time.time()
				fixation.draw()
				win.flip()
				if event.getKeys(keyList=["escape"]):
					win.close()
					core.quit()
			
			''' END THE TRIAL LOOP '''
			THISTRIAL = False
		if event.getKeys(keyList=["escape"]) or not THISTRIAL:
			win.close()
			core.quit()
		
		trialNum += 1
	blockNum += 1
