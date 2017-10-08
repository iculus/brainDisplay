''' 
Presentation for Brittany with recording
Designed by Brittany Alperin and Mike Soroka
MIT License, use freely and credit the authors and keep track of changes
2017-10-05

Notes:
2017-10-05 	- Composed functions to handle keyboard events and sound generation MS
BUG 		- spacebar is measured across event types correctly except rolls into start of new block... IMPORTANT MS
ODD 		- The data structure is indexed correctly, but an extra fixation datapoint is added at the end of a block
TODO		- Move the definitions into a library called michoPy 
'''

from psychopy import visual, core, event
import numpy
import random
import pygame
import time
from array import array

pygame.mixer.pre_init(44100, -16, 1, 1024)
pygame.mixer.init()
#pygame.init()

''' CLASS FOR FREQUENCY GENERATION '''
class Note(pygame.mixer.Sound):

    def __init__(self, frequency, volume=.01):
	''' set the |-VOLUME-| here '''
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

''' DEFINITIONS '''
def sendOverPort():
	pass

def pickANumber(thisTrial,maxTrial,position):
	if thisTrial <= maxTrial-position: stim = random.choice([1,2,3,4,5,6,7,8,9])
	if thisTrial > maxTrial-position: stim = random.choice([1,2,4,5,6,7,8,9])
	return stim
		   		
def closeWindowExit(): 
	if event.getKeys(keyList=["escape"]):
		win.close()
		core.quit()

def toneProb(threshold,start,end):
	toneProbability = random.randrange(start,end)
	if toneProbability < threshold: tone = True
	else: tone = False		
	return tone

def playTheSound(startTime, startTone, endTone, sound, toneGo):
# USEAGE - playTheSound(startTime_,startTone,endTone,sound,toneGo)	#return didWeSoundNow
# DEFINITION - set the duration and play a sound for it's entirety
# WONKY - the sound does not begin or end at the right time, it is off by some loading time. Adjust accordingly
	if tone: 
		if time.time()-startTime >= startTone and time.time()-startTime <= endTone:
			sound.play(-1)
			print 'toning'
		else: 
			pygame.mixer.stop()
		didWeSoundNow = True
	if not tone: 
		pygame.mixer.stop()
		didWeSoundNow = False
	return didWeSoundNow

def recordSpaceBar(startTime,maxTime,kpress,RThere):
# USEAGE - recordSpaceBar(startTime_,maxTime,kpress, RThere)	# return kpress, RThere
# DEFINITON - returns the first instance of measured kpress and RThere if previously unmodified
	if event.getKeys(keyList=["space"]):
		print 'keys'
		#we know we are within the timelimit, but why not check
		if time.time() - startTime < maxTime:	
			if kpress == False:	#ensure a single keypress here
				sendOverPort()
				RThere = time.time()-startTime_DigitDraw
				kpress = True
	return kpress, RThere

def changeTheBool(theBool):
	if theBool == True: theBool = 'T'
	else: theBool = 'F'
	return theBool

''' SET UP VARIABLES '''
#set display properties
win = visual.Window (size = [800,600],fullscr = False)
mouse = event.Mouse(visible = False)

#define the fixation as a plus sign
fixation= visual.TextStim(win, text = "+", height = .1)

#set block characteristics
blockNum = 1
maxBlockNum = 3

thisSound = Note(600)

endOfDigit = 0.25


#set up data structure here
DATA_BLOCK_toneParams = []; DATA_BLOCK_ISI = []; DATA_BLOCK_RT = []; DATA_BLOCK_digit = []; DATA_BLOCK_correctness = []

''' START OF PROGRAM ENTER BLOCK ZERO DATA FOR BLOCK '''
while blockNum <= maxBlockNum:
	startTime_Block = time.time()	#set up time keeping for block start

	#define the number of trials shortened for testing(23,69), randoms updated every block start
	maxTrialNumber = random.randrange(5,9)
	THISTRIAL = True	# to start the trial looper
	trialNum = 0		
	
	#set up data structure here
	DATA_TRIAL_toneParams = []; DATA_TRIAL_ISI = []; DATA_TRIAL_RT = []; DATA_TRIAL_digit = []; DATA_TRIAL_correctness = []
	
	''' ENTER TRIAL ZERO DATA FOR TRIAL '''
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
		stimulus = pickANumber(trialNum,maxTrialNumber,1)
	
		digit = visual.TextStim (win, stimulus)

		''' FIX FOR FIXATION START '''
		# Because recording a spacebar event over two timed events sucks
		if trialNum == 0:
			startTime_FixationDraw = time.time()		#set up timekeeping for fixation draw start
			tone = toneProb(75,1,100)
			
			while time.time()- startTime_FixationDraw <= endOfISI:
				sendOverPort()
				fixation.draw()
				win.flip()

				didWeSound = playTheSound(startTime_FixationDraw,startOfTone,endOfTone,thisSound,tone)	#return didWeSoundNow
				#if tone: 
				#	if time.time()-startTime_FixationDraw >= startOfTone and time.time()-startTime_FixationDraw <= endOfTone:
				#		thisSound.play(-1)
				#		print 'toning'
				#	else: 
				#		pygame.mixer.stop()
				#	didWeSound = True
				#f not tone: 
				#	pygame.mixer.stop()
				#	didWeSound = False
				
				closeWindowExit()
				#if event.getKeys(keyList=["escape"]):
				#	win.close()
				#	core.quit()
			
			#format the values
			didWeSound = changeTheBool(didWeSound)
			startOfTone = float(format(startOfTone, '.5f'))
			endOfTone = float(format(endOfTone, '.5f'))
			
			#append data
			DATA_TRIAL_toneParams.append((didWeSound, startOfTone, endOfTone))
			DATA_TRIAL_ISI.append(endOfISI)
			
			
		''' PRESENT THE DIGIT FOR DIGITDRAW TIME '''	
		startTime_Keypress = time.time()
		maxKeypressTime = endOfISI
		startTime_DigitDraw = time.time()		#set up timekeeping for digit draw start
		keyPress = False
		RT = 'null'
		while time.time() - startTime_DigitDraw < endOfDigit:
			sendOverPort()
			digit.draw()
			win.flip()

			keyPress, RT = recordSpaceBar(startTime_DigitDraw,maxKeypressTime,keyPress,RT)	# returns kpress, rthere
			#if event.getKeys(keyList=["space"]):
			#	#we know we are within the timelimit, but why not check
			#	if time.time() - startTime_DigitDraw < maxKeypressTime:	
			#		if keyPress == False:	#ensure a single keypress here
			#			sendOverPort()
			#			RT = time.time()-startTime_DigitDraw
			#			keyPress = True
			
			closeWindowExit()
			#if event.getKeys(keyList=["escape"]):
			#	win.close()
			#	core.quit()
	
		''' PRESENT THE FIXATION FOR ISI TIME '''	
		startTime_FixationDraw = time.time()		#set up timekeeping for fixation draw start
		tone = toneProb(75,1,100)
			
		while time.time() - startTime_FixationDraw <= endOfISI:
			sendOverPort()
			fixation.draw()
			win.flip()
			
			keyPress, RT = recordSpaceBar(startTime_DigitDraw,maxKeypressTime,keyPress, RT)	# returns kpress, rthere
			#if event.getKeys(keyList=["space"]):
			#	#we know we are within the timelimit, but why not check
			#	if time.time() - startTime_DigitDraw < maxKeypressTime:	
			#		if keyPress == False:	#ensure a single keypress here
			#			sendOverPort()
			#			RT = time.time()-startTime_DigitDraw
			#			keyPress = True

			didWeSound = playTheSound(startTime_FixationDraw,startOfTone,endOfTone,thisSound,tone)	#return didWeSoundNow
			##code to play a tone for the durration 75% of the time
			#if tone: 
			#	if time.time()-startTime_FixationDraw >= startOfTone and time.time()-startTime_FixationDraw <= endOfTone:
			#		thisSound.play(-1)
			#		print 'toning'
			#	else: 
			#		pygame.mixer.stop()
			#	didWeSound = True
			#if not tone: 
			#	pygame.mixer.stop()
			#	didWeSound = False
			
			closeWindowExit()
			#if event.getKeys(keyList=["escape"]):
			#	win.close()
			#	core.quit()

		##write relevant data to trial array	
		
		#if they hit it to a 12x456789 it is correct, if they do not hit it it is not correct
		#if it is a 3 they should do the opposite and they should not hit it, if tey do it's incorrect
		correct = 'F'
		if stimulus == 3:
			if RT == 'null': correct = 'T'
			else: correct = 'F'
		else:
			if RT != 'null': correct = 'T'
			else: correct = 'F'
		
		#format the values here	
		didWeSound = changeTheBool(didWeSound)
		startOfTone = float(format(startOfTone, '.5f'))
		endOfTone = float(format(endOfTone, '.5f'))
		if RT != 'null': RT = float(format(RT, '.5f'))
		endOfISI = float(format(endOfISI, '.5f'))

		#save the values here
		DATA_TRIAL_toneParams.append((didWeSound, startOfTone, endOfTone))
		DATA_TRIAL_ISI.append(endOfISI)
		DATA_TRIAL_RT.append(RT)
		DATA_TRIAL_digit.append(stimulus)
		DATA_TRIAL_correctness.append(correct)
			
		#exit conditions
		if trialNum == maxTrialNumber:
			THISTRIAL = False
		closeWindowExit()
		#if event.getKeys(keyList=["escape"]):
		#	win.close()
		#	core.quit()
		
		trialNum += 1

	#write all data to block array
	DATA_BLOCK_toneParams.append(DATA_TRIAL_toneParams)
	DATA_BLOCK_ISI.append(DATA_TRIAL_ISI)
	DATA_BLOCK_RT.append(DATA_TRIAL_RT)
	DATA_BLOCK_digit.append(DATA_TRIAL_digit)
	DATA_BLOCK_correctness.append(DATA_TRIAL_correctness)
	blockNum += 1

''' PRINT TO SCREEN '''
for blockNumber,values in enumerate(DATA_BLOCK_digit):
	for trialNumber in range(0,len(values)):
		print '\t block :', blockNumber \
			,' trial:', trialNumber \
			,', digit:', DATA_BLOCK_digit[blockNumber][trialNumber] \
			,', tone :', DATA_BLOCK_toneParams[blockNumber][trialNumber] \
			,', RT :', DATA_BLOCK_RT[blockNumber][trialNumber] \
			,', ISI :', DATA_BLOCK_ISI[blockNumber][trialNumber] \
			,', correct :', DATA_BLOCK_correctness[blockNumber][trialNumber]
