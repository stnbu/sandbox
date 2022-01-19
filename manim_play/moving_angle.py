from manim import *

class MovingAngle(Scene):
    def construct(self):
        rotation_center = LEFT

        theta_tracker = ValueTracker(110)
        blue_line = Line(LEFT, RIGHT).set_color(BLUE)
        green_line = Line(LEFT, RIGHT).set_color(GREEN)
        red_line = green_line.copy().set_color(RED)
        green_line.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )
        arc = Angle(blue_line, green_line, radius=0.5, other_angle=False).set_color(ORANGE)
        tex = MathTex(r"\theta").move_to(
            Angle(
                blue_line, green_line, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        ).set_color(PURPLE)

        self.add(blue_line, green_line, arc, tex)
        self.wait()

        green_line.add_updater(
            lambda x: x.become(red_line.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        arc.add_updater(
            lambda x: x.become(Angle(blue_line, green_line, radius=0.5, other_angle=False))
        )
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    blue_line, green_line, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )

        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.increment_value(140))
        self.play(tex.animate.set_color(RED), run_time=0.5)
        self.play(theta_tracker.animate.set_value(350))
    