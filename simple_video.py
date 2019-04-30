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
import time, os, sys, glob

videopath = r'C:\Users\fitch\downloads\huge.mp4'
if not os.path.exists(videopath):
    raise RuntimeError("Video path could not be found: " + videopath)


win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')

experimenter_text = visual.TextStim(win, "IT'S A MOVIE", pos=(0, -450), units = 'pix')

mov = visual.VlcMovieStim(win, videopath,
    units=None,
    pos=(0, 0.15),
    loop=False)

mov.size = (1.0, .5625)

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

