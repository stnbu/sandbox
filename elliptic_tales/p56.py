
from optigraph import graph_parameterized
from manim import *

def get_homothetic_transform(func, z):
    return lambda x, y: func(x, y, z)


hyperbola = lambda x, y, z: y*z - x**3

graph = ImplicitFunction(
    get_homothetic_transform(hyperbola, 20000),
    color=YELLOW
)
scene = Scene()
scene.add(graph)
scene.render()
