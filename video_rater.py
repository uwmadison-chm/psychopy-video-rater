#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.3),
    on Wed Feb 13 08:54:42 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.3'
expName = 'video_rater'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/njvack/movie-playback/video_rater.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
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

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='You will see a series of videos.\n\nUse the mouse to rate how positive or negative the speaker is feeling at this point in the video.\n\nPress space to start.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "iti"
itiClock = core.Clock()
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
    pos=(0, -.25), height=0.06, wrapWidth=None, ori=0, 
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
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

indicator = visual.Polygon(
    win=win, name='indicator',
    edges=100, size=(.025, .025),
    ori=90, pos=(0, -0.345),
    lineWidth=4, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,0,.2], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)

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

# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instructions_resp = event.BuilderKeyResponse()
mouse.setVisible(False)
# keep track of which components have finished
instructionsComponents = [instructions_text, instructions_resp]
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_text* updates
    if t >= 0.0 and instructions_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_text.tStart = t
        instructions_text.frameNStart = frameN  # exact frame index
        instructions_text.setAutoDraw(True)
    
    # *instructions_resp* updates
    if t >= 0.0 and instructions_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_resp.tStart = t
        instructions_resp.frameNStart = frameN  # exact frame index
        instructions_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instructions_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instructions_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instructions_resp.keys = theseKeys[-1]  # just the last key pressed
            instructions_resp.rt = instructions_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instructions_resp.keys in ['', [], None]:  # No response was made
    instructions_resp.keys=None
thisExp.addData('instructions_resp.keys',instructions_resp.keys)
if instructions_resp.keys != None:  # we had a response
    thisExp.addData('instructions_resp.rt', instructions_resp.rt)
thisExp.nextEntry()

# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trial_list.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values

for thisTrial in trials:
    currentLoop = trials
    
    # ------Prepare to start Routine "iti"-------
    t = 0
    itiClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    mouse.setVisible(False)
    # keep track of which components have finished
    itiComponents = [getready]
    for thisComponent in itiComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "iti"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = itiClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *getready* updates
        if t >= 0.0 and getready.status == NOT_STARTED:
            # keep track of start time/frame for later
            getready.tStart = t
            getready.frameNStart = frameN  # exact frame index
            getready.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if getready.status == STARTED and t >= frameRemains:
            getready.setAutoDraw(False)
        
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in itiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "iti"-------
    for thisComponent in itiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    gotValidClick = False  # until a click is received
    mouse.setVisible(False)
    # mouse.setPos((1,1))
    mouse.getPos()
    
    _oldx, oldy = indicator.pos
    indicator.pos = (0, oldy)
    movie = visual.MovieStim3(
        win=win, name='movie',
        noAudio = False,
        filename=thisTrial['moviefile'],
        ori=0, pos=(0,100), opacity=1,
        depth=-5.0,
        )
    # keep track of which components have finished
    trialComponents = [prompt_text, scale, mouse, indicator, movie]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prompt_text* updates
        if t >= 0.0 and prompt_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            prompt_text.tStart = t
            prompt_text.frameNStart = frameN  # exact frame index
            prompt_text.setAutoDraw(True)
        
        # *scale* updates
        if t >= 0.0 and scale.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale.tStart = t
            scale.frameNStart = frameN  # exact frame index
            scale.setAutoDraw(True)
        # something
        width = 0.025
        left_bound = -0.385
        right_bound = 0.385
        oldx, oldy = indicator.pos
        dx, _dy = mouse.getRel()
        newx = oldx + dx
        if newx < left_bound:
            newx = left_bound
        if newx > right_bound:
            newx = right_bound
        indicator.pos = (newx, oldy)
        
        # *indicator* updates
        if t >= 0.0 and indicator.status == NOT_STARTED:
            # keep track of start time/frame for later
            indicator.tStart = t
            indicator.frameNStart = frameN  # exact frame index
            indicator.setAutoDraw(True)
        
        # *movie* updates
        if t >= 0.0 and movie.status == NOT_STARTED:
            # keep track of start time/frame for later
            movie.tStart = t
            movie.frameNStart = frameN  # exact frame index
            movie.setAutoDraw(True)
        if movie.status == FINISHED:  # force-end the routine
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
thanks_resp = event.BuilderKeyResponse()
mouse.setVisible(False)
# keep track of which components have finished
thanksComponents = [thanks_text, thanks_resp]
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks_text* updates
    if t >= 0.0 and thanks_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanks_text.tStart = t
        thanks_text.frameNStart = frameN  # exact frame index
        thanks_text.setAutoDraw(True)
    
    # *thanks_resp* updates
    if t >= 0.0 and thanks_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanks_resp.tStart = t
        thanks_resp.frameNStart = frameN  # exact frame index
        thanks_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(thanks_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if thanks_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            thanks_resp.keys = theseKeys[-1]  # just the last key pressed
            thanks_resp.rt = thanks_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if thanks_resp.keys in ['', [], None]:  # No response was made
    thanks_resp.keys=None
thisExp.addData('thanks_resp.keys',thanks_resp.keys)
if thanks_resp.keys != None:  # we had a response
    thisExp.addData('thanks_resp.rt', thanks_resp.rt)
thisExp.nextEntry()

# the Routine "thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()




# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
