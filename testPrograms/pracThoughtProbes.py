#set the window resolution and tell it to be full screen
from psychopy import visual, data, core, event, gui

def allThoughtProbes(win):
	# win = visual.Window (size = [1920,1080],fullscr = True)

	#customized marker is a white rectangle
	bar = visual.Rect (win,width = .01, height = .1, fillColor = 'white')

	event.Mouse(visible = True, newPos = (0,0))

	#text for thought probes
	thoughtProbe1Text = "Were you thinking about something other than what you were doing?"
	thoughtprobe2Text = "Were you thinking about your surroundings?"
	thoughtProbe3Text = 'Was your mind moving about freely?'
	thoughtProbe4aText = 'How negative or positive were your thoughts?'
	thoughtProbe4bText = 'How strong was that emotion?'

	#text for the scale and bottom of screen
	lowEndScaleText = 'not at all'
	highEndScaleText = 'very much'
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
	lowEndScale4a = visual.TextStim(win, lowEndScaleText, pos = (-.5,.4))
	highEndScale4a = visual.TextStim(win, highEndScaleText, pos = (.5,.4))
	lowEndScale4b = visual.TextStim(win, lowEndScaleText, pos = (-.5,-.4))
	highEndScale4b = visual.TextStim(win, highEndScaleText, pos = (.5,-.4))
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
		win.flip()
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
		win.flip()
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
		win.flip()
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
		win.flip()   
		if event.getKeys(['escape']):
			core.quit()
	#print the response to the fourth thought probes
	print ratingScale4a.getRating()/100.0
	print ratingScale4b.getRating()/100.0       