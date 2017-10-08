from psychopy import visual, core, event
import numpy
import random
import pygame
import time


#set the window resolution and tell it to be full screen
win = visual.Window (size = [800,600],fullscr = False)

#get rid of mouse
mouse = event.Mouse(visible = False)

#define the fixation as a plus sign
fixation= visual.TextStim(win, text = "+", height = .1)

#define the number of blocks
blockNumber = 1
maxBlocks = 2

#while the number of blocks is less than or equal to the max number of blocks
while blockNumber <= maxBlocks:
    #display one fixation before starting first trial of a block
    fixation.draw()
    win.flip()
    # I took the easy way out. this one doesn't matter
    # nothing every needs to happen during this fixation
    # so I used a wait
    core.wait(1)

    #define the number of trials shortened for testing(23,69)
    trialNumber = random.randrange(20,22)
    # while within the number of trials present the stimuli
    # this makes it so the number 3 does not show up during the last 10 trials


    for tNumber in range (0,trialNumber):
        #stimulus is a random number between 1 and 9
        if tNumber+1 < trialNumber - 10:
            stimulus = random.randrange (1,9)
        elif tNumber+1 >= trialNumber - 10:
            stimulus = random.choice ([1,2,4,5,6,7,8,9])

        #select a random value between .9 and 1.2 seconds for the ISI
        ISI = random.uniform(0.9,1.2)

        #I'll want to display the random integer on the screen
        digit = visual.TextStim (win, stimulus)

        #setting up to play the sound file. It needs to be in the folder with all of the scripts to run
        pygame.mixer.init()
        pygame.mixer.music.load('tone600hz0dBFS200ms.wav')

        # defining when the onset of the tone should be
        toneOnset = random.uniform(0.4,0.65)
        toneProbability = random.randrange(1,100)

        #grab the current time 
        startOfTime = time.time()
        #start timer at zero
        currentTime = time.time()-startOfTime

        #duration of digit presentation (set to .25)
        endOfDigit = 0.25

        # I need to start a clock at the start of the digit being presented
        # the spacebar will be hit at some point between the digit and the fixation
        # the variables for that time range are endOfDigit and ISI (endOfDigit is set to .25, ISI is a random number selected within a range)
        # I need to know the reaction time (from the start of the digit to the spacebar press)
        # the maximum amount of time they have is to the end of the fixation (endOfDigit+ISI), if they respond after that, it doesn't count. I don't want that logged at all
        # it should only record the first spacebar press (just in case someone accidentally hits it twice or something)
        # basically, a clock needs to start when the digit is presented and run until the spacebar is pressed or until the fixation period is over, whichever happens first
        # more basically, I want their reaction time in response to the digit
        # this should happen for each trial


        #display the digit
        digit.draw()
        win.flip()

        # I think this is keeping track of time?
        while currentTime <= endOfDigit:
            currentTime = time.time()-startOfTime

        #grab the current time again
        startOfTime = time.time()

        startOfISI = 0
        endOfISI = ISI
        startOfTone = startOfISI + toneOnset
        endOfTone = startOfTone + 0.2

        #start timer at zero
        currentTime = time.time()-startOfTime

        # plays a tone if toneProbability (random number 1-100) is <75
        if toneProbability < 75:
            currentTime = time.time()-startOfTime
            # displays the fixation
            fixation.draw()
            win.flip()
            while True:
                currentTime = time.time()-startOfTime
                # if the time is between the start and end of when the tone should play, play the tone
                if currentTime >= startOfTone and currentTime <= endOfTone:
                    currentTime = time.time()-startOfTime
                    pygame.mixer.music.play()
                    break
            while currentTime <= endOfISI:
                currentTime = time.time()-startOfTime

            #if esc is hit, exit task
            if event.getKeys(keyList=["escape"]):
                win.close()
                core.quit()
        # does not play a tone if toneProbability >=75        
        elif toneProbability >=75:
            currentTime = time.time()-startOfTime
            #displays the fixation
            fixation.draw()
            win.flip()
            while currentTime <= endOfISI:
                currentTime = time.time()-startOfTime

            #if esc is hit, exit task
            if event.getKeys(keyList=["escape"]):
                win.close()
                core.quit()

    blockNumber = blockNumber + 1

win.close()
