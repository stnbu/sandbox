
import os
import math
import hashlib
import pickle
import subprocess
from decimal import Decimal

import sys, io
sys.stdout = open(os.devnull, 'w')  # SHUT
import manim
sys.stdout = sys.__stdout__  # ...UUP!

phi = (1 + math.sqrt(5)) / 2

def do_config():
    manim.config.verbosity = "ERROR"
    manim.config.quality = "low_quality"
    manim.config.media_dir = os.path.expanduser("~/.optigraph")

def fdrange(start, stop, step):
    start = Decimal(start)
    stop = Decimal(stop)
    step = Decimal(step)
    while start < stop:
        yield start
        start += step

def graph_parameterized(func, t_range):
    do_config()
    name = "optigraph_" + hashlib.sha224(pickle.dumps((t_range))).hexdigest()  # meh
    class Scene_(manim.Scene):
        pass
    Scene_.__name__ = name
    scene = Scene_()
    start, stop, step = t_range

    points = []
    for t in fdrange(start, stop, step):
        x, y = func(t)
        x = float(x)
        y = float(y)
        points.append((x, y, 0))

    get_x = lambda point: point[0]
    get_y = lambda point: point[1]
    x_range = min(points, key=get_x)[0], max(points, key=get_x)[0], 1
    y_range = min(points, key=get_y)[1], max(points, key=get_y)[1], 1

    if abs((x_range[1] - x_range[0]) - (y_range[1] - y_range[0])) > phi:
        if x_range[1] - x_range[0] <= y_range[1] - y_range[0]:
            y_range = x_range[0] * phi, x_range[1] * phi, 1
        else:
            x_range = y_range[0] * phi, y_range[1] * phi, 1

    plane = manim.Axes(
        x_range=x_range,
        y_range=y_range,
        tips=False,
        axis_config={"include_numbers": True},
    )
    line = manim.VGroup()
    line.set_points_as_corners(points)
    graph = manim.VGroup(plane, line)
    scene.add(graph)
    scene.render()

    # FIXME: make the image_file_path/scene_name depend only upon input; no redoing entire files.
    subprocess.Popen(["qlmanage", "-p", scene.renderer.file_writer.image_file_path],
                     stdout=subprocess.DEVNULL,
                     stderr=subprocess.DEVNULL)

if __name__ == "__main__":

    graph_parameterized(lambda t: (t, t**2), [-5, 5, 0.1])
