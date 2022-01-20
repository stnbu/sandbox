from manim import *

G = 9.832

class Ball(Scene):
    def construct(self):
        time = ValueTracker(0)
        axes = Axes(x_range=[0, 11, 1], y_range=[0, 11, 1]).add_coordinates()
        ball = Circle(radius=0.2, color=RED, fill_opacity=1).move_to(axes.coords_to_point(0, 10))
        ball_orig = ball.copy()

        def move_ball(mobj):
            current_time = time.get_value()
            mobj.become(ball_orig.copy()).move_to(axes.coords_to_point(current_time, 10 - (G * current_time ** 2)))

        ball.add_updater(move_ball)

        spintangle = Square(color=GREEN)

        def spin(mobj):
            current_time = time.get_value()
            mobj.rotate(angle=current_time / 10)

        spintangle.add_updater(spin)

        self.add(axes, ball, spintangle)
        self.play(time.animate.set_value(30), run_time=30)

