#set the window resolution and tell it to be full screen
from psychopy import visual, data, core, event
import pracThoughtProbes

def allThoughtProbes(win):

	# win = visual.Window (size = [800,600],fullscr = False)
	#customized marker is a white rectangle
	bar = visual.Rect (win,width = .01, height = .1, fillColor = 'white')

	# event.Mouse(visible = True, newPos = (0,0))
	
	# port codes for thought probes
	# probe1 = 100
	# probe1Response = 100 + int(round(ratingScale1.getRating()/100.0))
	# probe2 = 200
	# probe2Response = 200 + int(round(ratingScale2.getRating()/100.0))
	# probe3 = 300
	# probe3Response = 300 + int(round(ratingScale3.getRating()/100.0))
	# probe4 = 400
	# probe4aResponse = 400 + int(round(ratingScale4a.getRating()/100.0))
	# probe4bResponse = 450 + int(round(ratingScale4b.getRating()/100.0))


	#text for thought probes
	thoughtProbe1Text = "Were you thinking about something other than what you were doing?"
	thoughtprobe2Text = "Were you thinking about your surroundings?"
	thoughtProbe3Text = 'Was your mind moving about freely?'
	thoughtProbe4aText = 'How negative or positive were your thoughts?'
	thoughtProbe4bText = 'How strong was that emotion?'

	#text for the scale and bottom of screen
	lowEndScaleText = 'not at all'
	highEndScaleText = 'very much'
	lowEndNeg = 'negative'
	highEndPos = 'positive'
	lowEndWeak = 'weak'
	highEndStrong = 'strong'
	spacebarText = "Hit the spacebar to continue"

	#position of text on screen
	thoughtProbe1 = visual.TextStim(win, thoughtProbe1Text, pos = (0,.27), wrapWidth = 2, height = .11, color = [-1,-1,-.2])
	thoughtProbe2 = visual.TextStim(win, thoughtprobe2Text, pos = (0,.27), wrapWidth = 2, height = .11, color = [-1,-1,-.2])
	thoughtProbe3 = visual.TextStim(win, thoughtProbe3Text, pos = (0,.27), wrapWidth = 2, height = .11, color = [-1,-1,-.2])
	thoughtProbe4a = visual.TextStim(win, thoughtProbe4aText, pos = (0,.77), wrapWidth = 2, height = .11, color = [-1,-1,-.2])
	thoughtProbe4b = visual.TextStim(win, thoughtProbe4bText, pos = (0,-.03), wrapWidth = 2, height = .11, color = [-1,-1,-.2])

	lowEndScale = visual.TextStim(win, lowEndScaleText, pos = (-.5,-.1))
	highEndScale = visual.TextStim(win, highEndScaleText, pos = (.5,-.1))
	hitSpace = visual.TextStim(win, spacebarText, pos = (0,-.7))

	#locations of things for the 4th thought probe (two scales on the screen)
	lowEndScale4a = visual.TextStim(win, lowEndNeg, pos = (-.5,.4))
	highEndScale4a = visual.TextStim(win, highEndPos, pos = (.5,.4))
	lowEndScale4b = visual.TextStim(win, lowEndWeak, pos = (-.5,-.4))
	highEndScale4b = visual.TextStim(win, highEndStrong, pos = (.5,-.4))
	hitSpace4 = visual.TextStim(win, spacebarText, pos = (0,-.7))


	ratingScale1 = visual.RatingScale(win,low = 100, high = 700, scale = '',
		tickHeight = 0.0, marker = bar, markerStart = 400, markerColor = 'white', pos = (0,0), 
		showValue = False, labels =  ['',''], acceptKeys = 'space', 
		size = 1.5, showAccept = False, name = 'probeOnTask')

	ratingScale2 = visual.RatingScale(win,low = 100, high = 700, scale = '',
		tickHeight = 0.0, marker = bar, markerStart = 400, markerColor = 'white', pos = (0,0),  
		showValue = False, labels =  ['',''], acceptKeys = 'space', 
		size = 1.5, showAccept = False, name = 'probeSurroundings')

	ratingScale3 = visual.RatingScale(win,low = 100, high = 700, scale = '',
		tickHeight = 0.0, marker = bar, markerStart = 400, markerColor = 'white', pos = (0,0), 
		showValue = False, labels =  ['',''], acceptKeys = 'space', 
		size = 1.5, showAccept = False, name = 'probeFreely')

	ratingScale4a = visual.RatingScale(win,low = 100, high = 700, scale = '',
		tickHeight = 0.0, marker = bar, markerStart = 400, markerColor = 'white', pos = (0,.5), 
		showValue = False, labels =  ['',''], acceptKeys = 'space', 
		size = 1.5, showAccept = False, name = 'probeEmotion')

	ratingScale4b = visual.RatingScale(win,low = 100, high = 700, scale = '',
		tickHeight = 0.0, marker = bar, markerStart = 400, markerColor = 'white', pos = (0,-.3), 
		showValue = False, labels =  ['',''], acceptKeys = 'space', 
		size = 1.5, showAccept = False, name = 'probeArousal')



	#draw the first thought probe
	while ratingScale1.noResponse:
		ratingScale1.draw()
		thoughtProbe1.draw()
		lowEndScale.draw()
		highEndScale.draw()
		hitSpace.draw()
		#send port code
		win.flip()
		#send response port code
		if event.getKeys(['escape']):
			core.quit()
	#print the response to the first thought probe
	print ratingScale1.getRating()/100.0

	#draw the second thought probe
	while ratingScale2.noResponse:
		ratingScale2.draw()
		thoughtProbe2.draw()
		lowEndScale.draw()
		highEndScale.draw()
		hitSpace.draw()
		#send the port code
		win.flip()
		#send the response port code
		if event.getKeys(['escape']):
			core.quit()  
	#print the response to the second thought probe
	print ratingScale2.getRating()/100.0

	#draw the third thought probe
	while ratingScale3.noResponse:
		ratingScale3.draw()
		thoughtProbe3.draw()
		lowEndScale.draw()
		highEndScale.draw()
		hitSpace.draw()
		#send the port code
		win.flip()
		#send the response port code
		if event.getKeys(['escape']):
			core.quit()
	#print the response to the third thought probe
	print ratingScale3.getRating()/100.0

	while ratingScale4a.noResponse and ratingScale4b.noResponse:
		ratingScale4a.draw()
		thoughtProbe4a.draw()
		lowEndScale4a.draw()
		highEndScale4a.draw()
		ratingScale4b.draw()
		thoughtProbe4b.draw()     
		lowEndScale4b.draw()
		highEndScale4b.draw()     
		hitSpace4.draw()
		#send the port code	
		#send the response port code
		#send the other response port code	
		win.flip()   
		if event.getKeys(['escape']):
			core.quit()
	#print the response to the fourth thought probes
	print ratingScale4a.getRating()/100.0
	print ratingScale4b.getRating()/100.0       

	#win.close()

def howToDoThis(win):

	screen_1 = 'tiffs/Instruct1.TIF'
	Instructions1 = visual.ImageStim(win, screen_1, size = [2,2])

	screen_2 = 'tiffs/Instruct2.TIF'
	Instructions2 = visual.ImageStim(win, screen_2, size = [2,2])

	screen_7 = 'tiffs/StartPracScreen.TIF'

	beginPractice = visual.ImageStim(win, screen_7, size = [2,2])

	Instructions1.draw()
	win.flip()
	response = event.waitKeys(keyList = ["space", "escape"])
	if response == ["space"]:
		win.flip()
	elif response == ["escape"]:
		win.close()
		core.quit()

	Instructions2.draw()
	win.flip()
	response = event.waitKeys(keyList = ["space", "escape"])
	if response == ["space"]:
		win.flip()
	elif response == ["escape"]:
		win.close()
		core.quit()

	pracThoughtProbes.allThoughtProbes(win)	

	beginPractice.draw()
	win.flip()
	response = event.waitKeys(keyList = ["space", "escape"])
	if response == ["space"]:
		win.flip()
	elif response == ["escape"]:
		win.close()
		core.quit()

def enterSubjectID():
	# Initial dialog box to collect info on study participant and year
	study_info = {'Participant':0}
	study_info_dialog = gui.DlgFromDict(dictionary=study_info, title="SART")
	if study_info_dialog.OK:
	    # The code below builds the name for each output file. If you want to change the filenames to start with
	    # something other than 'SART' you can change the value in the quotes below
	    output_file_name = 'SART_' + str(study_info['Participant'])
	else:
	    core.quit()  # If you click "cancel" instead of "OK", closes program

def enterSubjectID2(win):
	go = True
	name = []
	while go:
		keyList = ["1","2","3","4","5","6","7","8","9","0"]
		nameDisplay=''.join(name)
		visual.TextStim(win, text = "please enter subject name", height = 0.1).draw()
		visual.TextStim(win, nameDisplay, pos = (0, 0.27), height = 0.1).draw()
		win.flip()
		key = event.getKeys()
		if len(key) > 0:
			if key[0] == "escape":
				win.close()
				core.quit()
			if key[0] == "return":
				go = False
				nameSend = ''.join(name)
			if key[0] in keyList:
				name.append(key[0])
				nameDisplay=''.join(name)
				visual.TextStim(win, text = "please enter subject name", height = 0.1).draw()
				visual.TextStim(win, nameDisplay, pos = (0, 0.27), height = 0.1).draw()
				win.flip()
			if key[0] == 'backspace':
				name.pop(-1)

	return nameSend
	
import time

if __name__ == '__main__':
	win = visual.Window (size = [800,600],fullscr = False)
	thisName = enterSubjectID2(win)
	print thisName
	howToDoThis(win)
