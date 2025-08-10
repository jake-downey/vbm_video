from manimlib import *
import sys
sys.path.append("C:/Users/thund/Downloads/manim-master/manimprojects")
from diamond_funcs import *
from vbm_funcs import *
from dots_example import *

class Playground(Scene):
    def construct(self):

        frame = self.camera.frame
        axes = ThreeDAxes(
            x_range = (-5,5,1),
            y_range = (-5,5,1),
            z_range = (-5,5,1),
        ).apply_depth_test()
        self.add(axes)
        
        angle = ValueTracker(0)
        curve_function = lambda u: np.array([-np.sin(u),np.cos(u),0])


        arc = ParametricCurve(
            curve_function,
            color = WHITE,
            t_range = np.array([0, angle.get_value(), 0.01])
        )
        arrow_tip = ArrowTip().scale(0.5)

        def get_tangent(curve_func, t, dt=1e-5):
            p1 = curve_func(t)
            p2 = curve_func(t + dt)
            return normalize(p2 - p1)

        def update_arrow(mob):
            end_point = arc.get_end()
            tangent_vector = get_tangent(curve_function, angle.get_value())
            ang = angle_of_vector(tangent_vector)
            mob.move_to(end_point)
            mob.rotate(ang - mob.get_angle())

        arrow_tip.add_updater(update_arrow)
        arc.add_updater(lambda m: m.become(
                ParametricCurve(
                curve_function,
                color = WHITE,
                t_range = np.array([0, angle.get_value(), 0.01])
            )

        ))

        self.add(arc)
        self.wait()
        self.play(FadeIn(arrow_tip), run_time = 0.2)
        self.play(angle.animate.set_value((2/9)*PI))