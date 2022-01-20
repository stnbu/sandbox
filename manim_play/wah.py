from manim import *

class Graphing(Scene):
    def construct(self):
        axes = Axes(x_range=[0, 5, 1], y_range= [0, 3, 1], x_length = 5, y_length = 3)
        axes.to_edge(UR)
        graph = axes.plot(lambda x: x * 2)
        self.play(DrawBorderThenFill(axes))
        self.add(graph)
        self.wait()