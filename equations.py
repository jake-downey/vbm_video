from manimlib import *
import sys
sys.path.append("C:/Users/thund/Downloads/manim-master/manimprojects")

class QuatEq(Scene):
    
    def construct(self):
        t2c1 = {
            r"\eta" : PINK,
            r"\xi_{1}" : TEAL,
            r"\xi_{2}" : ORANGE,
        }
        quat_eq1 = Tex(r"cos(\eta)e^{i\xi_{1}} + jsin(\eta)e^{i\xi_{2}}", tex_to_color_map = t2c1)
        quat_eq1.shift(UP*2.6).scale(1.5)
        self.add(quat_eq1)
        self.wait()
        first_group = quat_eq1[0:11].copy()
        second_group = quat_eq1[11:].copy()
        quat_eq2 = Tex(r"cos(\eta)(cos(\xi_{1})+isin(\xi_{1}))+jsin(\eta)(cos(\xi_{2})+isin(\xi_{2})", tex_to_color_map = t2c1)
        quat_eq2.next_to(quat_eq1, DOWN*1.2, buff=1)
        quat_eq_left = quat_eq2[0:24].copy()
        quat_eq_right = quat_eq2[24:].copy()
        self.play(
            Transform(first_group, quat_eq_left),
        )
        self.wait()
        self.play(
            Transform(second_group, quat_eq_right),
        )
        self.wait()
        tip_size= 0.5
        arrow1 = ArcBetweenPoints(
            quat_eq2[10].get_top() + np.array([0,0.1,0]),
            quat_eq2[3].get_top() + np.array([0,0.1,0]),
            radius = 8
        ).set_color(YELLOW)
        arrow1.add_tip()
        arrow1.tip.scale(0.5)
        arrow2 = ArcBetweenPoints(
            quat_eq2[19].get_top() + np.array([0,0.1,0]),
            quat_eq2[3].get_top() + np.array([0,0.1,0]),
        ).set_color(YELLOW)
        arrow2.add_tip()
        arrow2.tip.scale(0.5)
        arrow3 = ArcBetweenPoints(
            quat_eq2[36].get_top() + np.array([0,0.1,0]),
            quat_eq2[29].get_top() + np.array([0,0.1,0]),
        ).set_color(YELLOW)
        arrow3.add_tip()
        arrow3.tip.scale(0.5)
        arrow4 = ArcBetweenPoints(
            quat_eq2[45].get_top() + np.array([0,0.1,0]),
            quat_eq2[29].get_top() + np.array([0,0.1,0]),
        ).set_color(YELLOW)
        arrow4.add_tip()
        arrow4.tip.scale(0.5)
        
        self.play(
            ShowCreation(arrow1),
            ShowCreation(arrow2),
            ShowCreation(arrow3),
            ShowCreation(arrow4),
        )

        quat_eq3 = Tex(r"cos(\xi_{1})cos(\eta)+isin(\xi_{1})cos(\eta)+j(cos(\xi_{2})sin(\eta)+ijsin(\xi_{2})sin(\eta)", tex_to_color_map = t2c1)
        quat_eq3.scale(0.9).shift(DOWN*0.5)

        self.wait()
        self.play(Write(quat_eq3))
        quat_eq4 = Tex(r"cos(\xi_{1})cos(\eta)+isin(\xi_{1})cos(\eta)+j(cos(\xi_{2})sin(\eta)+ksin(\xi_{2})sin(\eta)", tex_to_color_map = t2c1)
        quat_eq4.scale(0.9).shift(DOWN*0.5)
        self.wait()
        self.play(
            TransformMatchingTex(quat_eq3, quat_eq4)
        )
        self.wait()
        self.play(
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(arrow3),
            FadeOut(arrow4),
            FadeOut(self.mobjects[3]),
            FadeOut(self.mobjects[2]),
            quat_eq4.animate.shift(UP*1.7)
        )
        self.wait()

        list_4d = Group(
            quat_eq4[0:13].copy(),
            quat_eq4[14:27].copy(),
            quat_eq4[28:42].copy(),
            quat_eq4[43:].copy(),
        )
        list_4d_copy = Group(
            quat_eq4[0:13].copy(),
            quat_eq4[15:28].copy(),
            quat_eq4[31:44].copy(),
            quat_eq4[46:].copy(),
        ).arrange(DOWN).shift(DOWN*1.4+RIGHT*0.5)
        coords_list = Group(
            Tex(r"x_{0}=").scale(0.9),
            Tex(r"x_{1}=").scale(0.9),
            Tex(r"x_{2}=").scale(0.9),
            Tex(r"x_{3}=").scale(0.9),
        ).arrange(DOWN)
        coords_list[0].next_to(list_4d_copy[0],LEFT).shift(DOWN*0.06)
        coords_list[1].next_to(list_4d_copy[1],LEFT).shift(DOWN*0.06)
        coords_list[2].next_to(list_4d_copy[2],LEFT).shift(DOWN*0.06)
        coords_list[3].next_to(list_4d_copy[3],LEFT).shift(DOWN*0.06)
        self.play(
            Transform(list_4d[0], list_4d_copy[0])
        )
        self.play(FadeIn(coords_list[0]))
        self.wait()
        self.play(
            Transform(list_4d[1], list_4d_copy[1]),
            Transform(list_4d[2], list_4d_copy[2]),
            Transform(list_4d[3], list_4d_copy[3]),
            run_time = 1.5
        )
        self.play(
            FadeIn(coords_list[1]),
            FadeIn(coords_list[2]),
            FadeIn(coords_list[3]),
        )
        coords_group = Group(
            coords_list,
            list_4d_copy,
        )
        self.wait()
        self.play(
            FadeOut(quat_eq4),

        )
        self.wait()
        quat_eq5 = Tex(r"q = x_{0} + ix_{1} + jx_{2} + kx_{3}")
        quat_eq5.move_to(quat_eq4).scale(1.3).shift(DOWN*0.2)
        quat_eq5[0].set_color(YELLOW)
        self.play(Write(quat_eq5))
