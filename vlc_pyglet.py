from __future__ import absolute_import, division, print_function


import time
import os
import sys
import threading
import logging
import ctypes

import vlc
import pyglet
pyglet.options['debug_gl'] = False
GL = pyglet.gl

filename = sys.argv[1]


instance = vlc.Instance()
stream = instance.media_new(filename)
player = instance.media_player_new()
player.set_media(stream)

# Load up the file
stream.parse()
size = player.video_get_size()
width = size[0]
height = size[1]
frame_rate = player.get_fps()
frame_counter = 0

# We assume we can use the RGBA format here
player.video_set_format("RGBA", width, height, width << 2)

# The lock 
pixel_lock = threading.Lock()
pixel_buffer = (ctypes.c_ubyte * width * height * 4)()

# TODO: Why is duration -1 still even after parsing? Newer vlc docs seem to hint this won't work until playback starts
duration = player.get_length()
logging.warning("Video is %ix%i, duration %s, fps %s" % (width, height, duration, frame_rate))

# vlc.CallbackDecorators in python-vlc lib are incorrect and don't match VLC docs
CorrectVideoLockCb = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
CorrectVideoUnlockCb = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))

@CorrectVideoLockCb
def _vlcLockCallback(user_data, planes):
    logging.warning("Locking")
    bork = ctypes.cast(user_data, ctypes.POINTER(ctypes.py_object)).contents.value
    bork.add_blorp()
    logging.warning("Got bork: %s" % bork.blorps)
    pixel_lock.acquire()
    # Tell VLC to take the data and stuff it into the buffer
    planes[0] = ctypes.cast(pixel_buffer, ctypes.c_void_p)

@CorrectVideoUnlockCb
def _vlcUnlockCallback(user_data, picture, planes):
    pixel_lock.release()

@vlc.CallbackDecorators.VideoDisplayCb
def _vlcDisplayCallback(user_data, picture):
    global frame_counter
    frame_counter += 1


class Bork:
    def __init__(self, blorps):
        self.blorps = blorps

    def blorps(self):
        return self.blorps

    def add_blorp(self):
        self.blorps += 1

bork = Bork(1)

# Once you set these callbacks, you are in complete control of what to do with the video buffer
woo = ctypes.cast(ctypes.pointer(ctypes.py_object(bork)), ctypes.c_void_p)
player.video_set_callbacks(_vlcLockCallback, _vlcUnlockCallback, _vlcDisplayCallback, woo)


def bindTexture(pixel_buffer, texture_id):
    """
    Take a given pixel buffer (assumed to be RGBA)
    and cram it into the given GL texture
    """
    GL.glEnable(GL.GL_TEXTURE_2D)
    GL.glBindTexture(GL.GL_TEXTURE_2D, texture_id)
    GL.glPixelStorei(GL.GL_UNPACK_ALIGNMENT, 1)
    interpolation = GL.GL_LINEAR
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, interpolation)
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, interpolation)
    with pixel_lock:
        GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGB,
                        width,
                        height,
                        0, GL.GL_RGBA, GL.GL_UNSIGNED_BYTE,
                        pixel_buffer)
    GL.glDisable(GL.GL_TEXTURE_2D)


class TexturedSquare:
    def __init__(self, width, height, xpos, ypos, texture_id):
        self.xpos = xpos
        self.ypos = ypos
        self.angle = 0
        self.size = 1
        self.texture_id = texture_id
        x = width/2.0
        y = height/2.0
        self.vertex_list = pyglet.graphics.vertex_list(4, ('v2f', [-x,y, x,y, -x,-y, x,-y]), ('t2f', [0,0, 1,0, 0,1, 1,1]))
    def draw(self):
        GL.glPushMatrix()
        GL.glTranslatef(self.xpos, self.ypos, 0)
        GL.glRotatef(self.angle, 0, 0, 1)
        GL.glScalef(self.size, self.size, self.size)
        GL.glColor4f(1,1,1,1)
        GL.glEnable(GL.GL_TEXTURE_2D)
        GL.glBindTexture(GL.GL_TEXTURE_2D, self.texture_id)
        self.vertex_list.draw(GL.GL_TRIANGLE_STRIP)
        GL.glDisable(GL.GL_TEXTURE_2D)
        GL.glPopMatrix()


window = pyglet.window.Window()
frames = pyglet.text.Label('frame count goes here',
                          font_name='Arial', font_size=14, x=10, y=10,
                          anchor_x='left', anchor_y='bottom')

vlc_tex = GL.GLuint()
GL.glGenTextures(1, ctypes.byref(vlc_tex))
video = TexturedSquare(width, height, width/2, height/2, vlc_tex)


@window.event
def on_draw():
    # Bind VLC buffer to GL texture
    bindTexture(pixel_buffer, vlc_tex)

    # Draw it
    video.draw()
    frames.text = str(frame_counter)
    frames.draw()

def update(dummy):
    return

keyboard = pyglet.window.key.KeyStateHandler()
window.push_handlers(keyboard)
pyglet.clock.schedule_interval(update,1/60.0)

player.play()
pyglet.app.run()
