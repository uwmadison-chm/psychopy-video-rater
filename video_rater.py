#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Using the new (beta) MovieStim2 to play a video file.

Requires: 
  * vlc, matching your python bitness
  * pip install python-vlc
"""

from __future__ import absolute_import, division

from psychopy import visual, core, event, data, logging, monitors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import time, os, sys, glob, csv, re


video_folder = r'C:\My Experiments\AFCHRON\biopac_data'
if not os.path.exists(video_folder):
    raise RuntimeError("Video folder could not be found: " + video_folder)

if len(sys.argv) > 1:
	video = sys.argv[1]
else:
	videos = glob.glob(video_folder + '\*.mp4')
	video = max(videos, key=os.path.getctime)

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

psychopyVersion = '3.0.6'
expName = 'video_rater'
expInfo = {}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion



win = visual.Window(
    screen=1,
    fullscr=True,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')


mov = visual.VlcMovieStim(win, video,
    units=None,
    pos=(0, 0.15),
    size=(1.0, .5625),
    loop=False)


match = re.search("afc_(\d+)", video)
if match:
    expInfo['participant'] = match.group(1)
    experimenter_text = visual.TextStim(win, "Press 'space' if this is the correct video and participant is number %s.\n\nThen, turn the monitor to face the participant.\n\nIf this is incorrect, press 'q' or 'Esc' to start over and check %s for correct video." % (expInfo['participant'], video_folder), pos=(0, -0.2), height=0.02)
else:
    expInfo['participant'] = "UNKNOWN"
    experimenter_text = visual.TextStim(win, "WARNING: No participant id found in latest video %s.\n\nPress 'q' or 'Esc' and check in folder %s for video." % (video, video_folder), pos=(0, -0.2), height=0.02)


# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file



instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='You will see a video of yourself performing the stress test.\n\nYou will use the trackball to rate how stressed you were DURING the test, not how you are currently feeling while watching the video.\n\nPlease move the trackball now to practice.\n\nLet me know when when you\'re ready to watch your video and rate how you felt AT THAT TIME.',
    font='Arial',
    pos=(0, 0.15), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


getready = visual.TextStim(win=win, name='getready',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


prompt_text = visual.TextStim(win=win, name='prompt_text',
    text='How stressed were you feeling at this time?',
    font='Arial',
    pos=(0, -.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
scale = visual.ImageStim(
    win=win, name='scale',
    image='scale_stressed.png',
    pos=(0, -.37), size=(1.8, 0.24075),
    opacity=1, interpolate=True)
indicator = visual.Polygon(
    win=win, name='indicator',
    edges=100, size=(.025, .025),
    ori=90, pos=(0, -0.363),
    lineWidth=4, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,0,.2], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)

# Mouse and indicator setup
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
mouse.setVisible(False)
mouse.getPos()
left_bound = -0.85
right_bound = 0.85
oldx, oldy = indicator.pos
indicator.pos = (0, oldy)

thanksClock = core.Clock()
thanks_text = visual.TextStim(win=win, name='thanks_text',
    text='Thank you for your participation!\n\nYou have finished the task. Please retrieve the experimenter from the hallway.',
    font='Arial',
    pos=(0, 0), height=0.08, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 


def moveIndicator():
    x, y = mouse.getPos()
    oldx, oldy = indicator.pos
    newx = x
    constrainMouse = False

    # constrain mouse position so that user can't move to the other screen accidentally
    if newx < left_bound:
        newx = left_bound
        constrainMouse = True
    if newx > right_bound:
        newx = right_bound
        constrainMouse = True
    if abs(y - oldy) > 0.1:
        constrainMouse = True
    if constrainMouse:
        mouse.setPos([newx, oldy])

    indicator.pos = (newx, oldy)
    indicator.draw()
    return newx


def displayText(text, timeLimit=0, mouseClickNext=False, showScale=False):
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
    mouse.setPos([0, 0])
    mouse.clickReset()

    # -------Start display-------
    while continueRoutine and (not timeLimit or (timeLimit and routineTimer.getTime() > 0)):
        # update/draw components on each frame
        if showScale:
            scale.draw()
            moveIndicator()
            indicator.draw()

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


# INSTRUCTIONS
displayText(instructions_text, mouseClickNext=False, showScale=True)


rate = 0.005

oldx, oldy = indicator.pos
indicator.pos = (0, oldy)

trialClock = core.Clock()
oldtime = 0.0

# Jump into the movie
mov.seek(0)
# Yes, this is ugly, but force the vlc clock to reset
mov._vlc_clock.reset()
shouldflip = mov.play()
continueRoutine = True

with open(filename+'.tsv', 'w', newline='') as csvfile:
    output = csv.writer(csvfile, delimiter="\t")
    output.writerow(['id', 'clock', 'vlc_time', 'frame_number', 'mouse'])

    # MAIN TRIAL
    while mov.status != visual.FINISHED and continueRoutine:
        newx = moveIndicator()

        newtime = trialClock.getTime()
        if newtime - oldtime >= rate:
            # Save mouse position data
            output.writerow(
                [expInfo['participant'],
                newtime,
                mov.getCurrentFrameTime(),
                mov.getCurrentFrameNumber(),
                newx / right_bound # Regularize to -1.0, 1.0
                ])
        oldtime = newtime

        # Only flip when a new frame should be displayed.
        if shouldflip:
            # Movie has already been drawn, so just draw text stim and flip
            scale.draw()
            prompt_text.draw()
            indicator.draw()
            win.flip()
        else:
            # Give the OS a break if a flip is not needed
            time.sleep(0.001)
        shouldflip = mov.draw()

        for key in event.getKeys():
            if key in ['escape', 'q']:
                continueRoutine = False


mov.pause()

# ------Prepare to start Routine "thanks"-------
displayText(thanks_text, mouseClickNext=False)

logging.flush()

win.close()
core.quit()
