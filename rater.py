#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Using the new (beta) MovieStim2 to play a video file.

Requires: 
  * vlc, matching your python bitness
  * pip install python-vlc
  * pip install opencv
  * opencv itself
    * For Windows, a binary installer is available at
        http://www.lfd.uci.edu/~gohlke/pythonlibs/ # opencv
"""

from __future__ import division

from psychopy import visual, core, event, data, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import time, os, sys

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

psychopyVersion = '3.0.3'
expName = 'video_rater'
expInfo = {'participant': '', 'session': '001'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=_thisDir + '/video_rater.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# Start Code - component code to be run before the window creation

videopath = r'c:\users\fitch\downloads\huge.mp4'
if not os.path.exists(videopath):
    raise RuntimeError("Video File could not be found:" + videopath)

win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess


# Initialize components for "experimenter"
mov = visual.MovieStim2(win, videopath,
    # pos specifies the /center/ of the movie stim location
    pos=[0, 100],
    loop=False)

mov.size = (800, 600)

experimenter_text = visual.TextStim(win, "Press 'space' if this is the correct video,\nand turn the monitor to face the participant.\nPress 'q' to start over.", pos=(0, -250), units = 'pix')


# Initialize components for Routine "instructions"
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='You will see a video of the test.\n\nUse the mouse to rate how positive or negative the speaker is feeling at this point in the video.\n\nClick a mouse button to start.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "iti"
getready = visual.TextStim(win=win, name='getready',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "trial"
trialClock = core.Clock()
prompt_text = visual.TextStim(win=win, name='prompt_text',
    text='How did this person feel while talking?',
    font='Arial',
    pos=(0, -.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
scale = visual.ImageStim(
    win=win, name='scale',
    image='valence_scale_white.png', mask=None,
    ori=0, pos=(0, -.4), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
indicator = visual.Polygon(
    win=win, name='indicator',
    edges=100, size=(.025, .025),
    ori=90, pos=(0, -0.355),
    lineWidth=4, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,0,.2], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)

# Bind mouse
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanks_text = visual.TextStim(win=win, name='thanks_text',
    text='Thank you for participating!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);



# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

def displayText(text, timeLimit=0, mouseClickNext=False):
    t = 0
    continueRoutine = True

    if timeLimit:
        routineTimer.add(timeLimit)

    # update component parameters for each repeat
    resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    components = [text, resp]
    for thisComponent in components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    endExpNow = False
    mouse.clickReset()

    # -------Start display-------
    while continueRoutine and (not timeLimit or (timeLimit and routineTimer.getTime() > 0)):
        # update/draw components on each frame
        
        if t >= 0.0 and text.status == NOT_STARTED:
            text.setAutoDraw(True)
        
        if t >= 0.0 and resp.status == NOT_STARTED:
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')

        if resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                resp.keys = theseKeys[-1]  # just the last key pressed
                continueRoutine = False
            if mouseClickNext:
                buttons = mouse.getPressed()
                if any(buttons):
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    for thisComponent in components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the routine was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()


# ------Prepare to start Routine "experimenter"-------
shouldflip = mov.play()
continueRoutine = True
while continueRoutine:
    # Only flip when a new frame should be displayed.
    if shouldflip:
        # Movie has already been drawn, so just draw text stim and flip
        experimenter_text.draw()
        win.flip()
    else:
        # Give the OS a break if a flip is not needed
        time.sleep(0.001)
    shouldflip = mov.draw()

    for key in event.getKeys():
        if key in ['escape', 'q']:
            # TODO: Let them select a different file?
            win.close()
            core.quit()
        elif key in ['space']:
            continueRoutine = False

mov.pause()
# Reload the movie from the start
mov.seek(0)

mouse.setVisible(False)


# ------Prepare to start Routine "instructions"-------
displayText(instructions_text, mouseClickNext=True)


# ------Prepare to start Routine "iti"-------
displayText(getready, 2.0)


# ------Prepare to start Routine "trial"-------
shouldflip = mov.play()
mouse.getPos()

oldx, oldy = indicator.pos
width = 0.025
left_bound = -0.32
right_bound = 0.32
indicator.pos = (0, oldy)
continueRoutine = True
constrainMouse = False
while mov.status != visual.FINISHED and continueRoutine:
    x, y = mouse.getPos()
    oldx, oldy = indicator.pos
    newx = x

    # constrain mouse position so that user can't move to the other screen accidentally
    if newx < left_bound:
        newx = left_bound
        constrainMouse = True
    if newx > right_bound:
        newx = right_bound
        constrainMouse = True
    if abs(y - oldy) > 0.2:
        constrainMouse = True
    if constrainMouse:
        mouse.setPos([newx, oldy])

    indicator.pos = (newx, oldy)

    # TODO: Save position data

    # Only flip when a new frame should be displayed.
    if shouldflip:
        # Movie has already been drawn, so just draw text stim and flip
        prompt_text.draw()
        scale.draw()
        indicator.draw()
        win.flip()
    else:
        # Give the OS a break if a flip is not needed
        time.sleep(0.001)
    shouldflip = mov.draw()

    for key in event.getKeys():
        if key in ['escape', 'q']:
            win.close()
            core.quit()

# ------Prepare to start Routine "thanks"-------
displayText(thanks_text, mouseClickNext=True)


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)

logging.flush()

# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit

win.close()
core.quit()
