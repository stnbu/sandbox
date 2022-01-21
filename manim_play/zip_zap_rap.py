from manim import *
from decimal import Decimal


class W(Scene):
    def construct(self):
        modulus = 10
        axis_config = {"scaling": WrappedScale(Decimal(modulus))}
        t_range = [-10, 10, 1]
        ax = Axes(
            x_range=t_range,
            y_range=t_range,
            x_length=modulus,
            y_length=modulus,
            x_axis_config=axis_config,
            y_axis_config=axis_config
        ).add_coordinates()
        #graph = ax.plot(lambda x: x ** 2, x_range=[0.001, 30, 0.5], use_smoothing=False)
        self.add(ax)
        m = 100
        for n in range(int(0.01*m), int(30*m), int(0.2*m)):
            x = n / 100
            y = x ** 2
            dot = Circle(radius=0.01, color=RED, fill_opacity=1).move_to(ax.coords_to_point(x, y))
            # self.add(dot)
            # self.wait(0.1)
            self.play(dot.animate.become(dot.copy().set_color(BLUE)), run_time=0.1)
        # graph = ax.plot(lambda x: x ** 2, x_range=[0.001, 30, 0.5], use_smoothing=False)
        # self.add(ax, graph)
        # dot = Circle(radius=0.2, color=RED, fill_opacity=1).move_to(RIGHT*2)
