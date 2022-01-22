
print("About to import manim...")
from manim import *
print("...manim has been imported")

config.frame_height = 15
config.frame_width = 15

print("Value of config.frame_height when I use my script: %s" % config.frame_height)
print("Value of config.frame_width when I use my script: %s" % config.frame_width)

axes = Axes()

print("")
print("Value of axes.y_length when I actually *call* Axes.__init__: %s" % axes.y_length)
print("Value of axes.x_length when I actually *call* Axes.__init__: %s" % axes.x_length)
