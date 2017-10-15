''' 
Presentation for Brittany with recording
Designed by Brittany Alperin and Mike Soroka
MIT License, use freely and credit the authors and keep track of changes
2017-10-14

Notes:
2017-10-05 	- Composed functions to handle keyboard events and sound generation MS
2017-10-14	- Added save to csv file functionality and enhanced the structure 
BUG 		- spacebar is measured across event types correctly except rolls into start of new block... IMPORTANT MS
ODD 		- The data structure is indexed correctly, but an extra fixation datapoint is added at the end of a block
TODO		- Move the definitions into a library called michoPy 
BUG		- THE FILENAMES CAN BE OVERWRITTEN IF THE SAME SUBJECT IS ENTERED ****CHANGE THIS****
'''

from psychopy import visual, core, event
import numpy
import random
import pygame
import time
from array import array
import thoughtProbes
import csv

fmt = '.4f'

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
	if toneGo: 
		if time.time()-startTime >= startTone and time.time()-startTime <= endTone:
			sound.play(-1)
			print 'toning'
		else: 
			pygame.mixer.stop()
		didWeSoundNow = True
	if not toneGo: 
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
				RThere = time.time()-startTime
				kpress = True
	return kpress, RThere

def changeTheBool(theBool):
	if theBool == True: theBool = 'T'
	else: theBool = 'F'
	return theBool

''' SET UP VARIABLES '''
#set block characteristics

def sart(maxBlockNum, noThreePosition, maxTrialLow, maxTrialHigh, win):
	answers = []
	blockNum = 1
	#set display properties
	mouse = event.Mouse(visible = False)

	#define the fixation as a plus sign
	fixation= visual.TextStim(win, text = "+", height = .1)

	thisSound = Note(600)

	endOfDigit = 0.25

	#set up data structure here
	DATA_BLOCK_toneParams = []; DATA_BLOCK_ISI = []; DATA_BLOCK_RT = []; DATA_BLOCK_digit = []; DATA_BLOCK_correctness = []

	''' START OF PROGRAM ENTER BLOCK ZERO DATA FOR BLOCK '''
	while blockNum <= maxBlockNum:
		startTime_Block = time.time()	#set up time keeping for block start

		#define the number of trials shortened for testing(23,69), randoms updated every block start
		maxTrialNumber = random.randrange(maxTrialLow,maxTrialHigh)
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
			stimulus = pickANumber(trialNum,maxTrialNumber,noThreePosition)
		
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
					closeWindowExit()
				
				#format the values
				didWeSound = changeTheBool(didWeSound)
				startOfTone = float(format(startOfTone, fmt))
				endOfTone = float(format(endOfTone, fmt))
				endOfISI = float(format(endOfISI, fmt))
				
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
				closeWindowExit()
		
			''' PRESENT THE FIXATION FOR ISI TIME '''	
			startTime_FixationDraw = time.time()		#set up timekeeping for fixation draw start
			tone = toneProb(75,1,100)
				
			while time.time() - startTime_FixationDraw <= endOfISI:
				sendOverPort()
				fixation.draw()
				win.flip()
				
				keyPress, RT = recordSpaceBar(startTime_DigitDraw,maxKeypressTime,keyPress, RT)	# returns kpress, rthere
				didWeSound = playTheSound(startTime_FixationDraw,startOfTone,endOfTone,thisSound,tone)	#return didWeSoundNow
				closeWindowExit()
			
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
			startOfTone = float(format(startOfTone, fmt))
			endOfTone = float(format(endOfTone, fmt))
			if RT != 'null': RT = float(format(RT, fmt))
			endOfISI = float(format(endOfISI, fmt))

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
			
			trialNum += 1

		#write all data to block array
		DATA_BLOCK_toneParams.append(DATA_TRIAL_toneParams)
		DATA_BLOCK_ISI.append(DATA_TRIAL_ISI)
		DATA_BLOCK_RT.append(DATA_TRIAL_RT)
		DATA_BLOCK_digit.append(DATA_TRIAL_digit)
		DATA_BLOCK_correctness.append(DATA_TRIAL_correctness)

		#place for thought probes
		returnedAnswers = thoughtProbes.allThoughtProbes(win)
		answers.append(returnedAnswers)

		blockNum += 1
	return DATA_BLOCK_toneParams,DATA_BLOCK_ISI,DATA_BLOCK_RT,DATA_BLOCK_digit,DATA_BLOCK_correctness,answers

""" RUN PROGRAM HERE """
if __name__ == "__main__": 
	window = visual.Window (size = [800,600],fullscr = False)
	maxBlock = 2
	noThreePos = 1
	maxTLow = 3
	maxTHigh = 4

	thisName = thoughtProbes.enterSubjectID2(window)
	thoughtProbes.howToDoThis(window)
	toneParams,ISI,RT,digit,correctness,ans = sart(maxBlock,noThreePos,maxTLow,maxTHigh,window)

	''' PRINT TO SCREEN '''
	fName = thisName+'_SART.csv'
	fName2 = thisName+'_PROBES.csv'
	with open(fName, 'wb') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)

		toWrite = ["block","trial","digit","tonePresent","toneStart","toneEnd","RT","ISI","correct"]
		spamwriter.writerow(toWrite)

		for bn,values in enumerate(digit):
			for tn in range(0,len(values)):
				print '\t block :', bn \
					,' trial:', tn \
					,', digit:', digit[bn][tn] \
					,', tone :', toneParams[bn][tn] \
					,', RT :', RT[bn][tn] \
					,', ISI :', ISI[bn][tn] \
					,', correct :', correctness[bn][tn]
				toWrite = [bn,tn,digit[bn][tn],\
					toneParams[bn][tn][0],toneParams[bn][tn][1],toneParams[bn][tn][2],\
					RT[bn][tn],ISI[bn][tn],correctness[bn][tn]]
				spamwriter.writerow(toWrite)
	with open(fName2, 'wb') as csvfile2:
		spamwriter2 = csv.writer(csvfile2, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)

		toWrite = ["probe1","probe2","probe3","probe4a","probe4b"]
		spamwriter2.writerow(toWrite)
		for value in ans:
			print value
			spamwriter2.writerow(value)

		print 'Done'
