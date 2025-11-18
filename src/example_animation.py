from manimlib import *
import os, sys
sys.path.insert(0, os.path.dirname(__file__))   # ensures the script's folder is on sys.path
from vbm_funcs import *
from diamond_funcs import *


### FINISHED DRAFTS

class TitleScreen(Scene):
    def construct(self):
        frame = self.camera.frame
        symbol = vbm_symbol().scale(2)
        numbers = vbm_numbers(1,9,1.4,2.6).set_color(WHITE)
        circle = Circle().scale(2).set_color(WHITE)
        dots = vbm_dots(1,9,1,2)
        vbm_group = Group(symbol, numbers, circle, dots).shift(DOWN*0.5)
        title = Tex(r"\textsc{Vortex Based Mathmatics}").scale(1.5)
        chapter = Tex(r"\textsc{Chapter 1: VBM and Modular Arithmetic}").next_to(title, DOWN, buff = 0.5).shift(UP*0.3)
        self.add(title)
        self.wait(2)
        self.play(
            title.animate.shift(UP*0.3),
            FadeIn(chapter),
        )
        self.wait(2)
        self.play(
            FadeOut(chapter),
        )
        self.play(
            title.animate.shift(UP*3),
        )
        self.wait(2)
        self.play(
            ShowCreation(symbol[0]),
        )
        self.wait(2)
        for num in numbers:
            self.play(
                Write(num),
                run_time = 0.4
            )
        self.wait(2)
        self.play(
            ShowCreation(symbol[2]),
        )
        self.wait(2)
        self.play(
            ShowCreation(symbol[1]),
        )
        self.wait(2)
        self.play(
            ShowCreation(symbol[3]),
            ShowCreation(symbol[4]),
        )
        
        numbers_new = vbm_numbers(1,9,1.4,2.6).shift(DOWN*0.5)
        self.wait(2)
        self.play(FadeIn(numbers_new))

        plus_group = Group()
        minus_group = Group()
        for i in numbers_new:
            plus = Tex(r"+").scale(0.5).next_to(i, LEFT, buff = 0.1)
            minus = Tex(r"-").scale(0.5).next_to(i, RIGHT, buff = 0.1)
            plus_group.add(plus)
            minus_group.add(minus)

        self.wait(2)
        self.play(
            FadeIn(plus_group),
            FadeIn(minus_group),
        )
            
        rad = 2.4
        stroke = 1
        circle_emination = Circle().set_stroke(width=5)
        arrow1 = Arrow(
            start = np.array([np.sin((10/12)*TAU), np.cos((10/12)*TAU), 0]),
            end = np.array([rad * np.sin((10/12)*TAU), rad * np.cos((10/12)*TAU), 0]),
        ).set_stroke(width=stroke)
        arrow2 = Arrow(
            start = np.array([np.sin((9/12)*TAU), np.cos((9/12)*TAU), 0]),
            end = np.array([rad * np.sin((9/12)*TAU), rad * np.cos((9/12)*TAU), 0]),
        ).set_stroke(width=stroke)
        arrow3 = Arrow(
            start = np.array([np.sin((8/12)*TAU), np.cos((8/12)*TAU), 0]),
            end = np.array([rad * np.sin((8/12)*TAU), rad * np.cos((8/12)*TAU), 0]),
        ).set_stroke(width=stroke)

        arrow4 = Arrow(
            start = np.array([np.sin((2/12)*TAU), np.cos((2/12)*TAU), 0]),
            end = np.array([rad * np.sin((2/12)*TAU), rad * np.cos((2/12)*TAU), 0]),
        ).set_stroke(width=stroke)
        arrow5 = Arrow(
            start = np.array([np.sin((3/12)*TAU), np.cos((3/12)*TAU), 0]),
            end = np.array([rad * np.sin((3/12)*TAU), rad * np.cos((3/12)*TAU), 0]),
        ).set_stroke(width=stroke)
        arrow6 = Arrow(
            start = np.array([np.sin((4/12)*TAU), np.cos((4/12)*TAU), 0]),
            end = np.array([rad * np.sin((4/12)*TAU), rad * np.cos((4/12)*TAU), 0]),
        ).set_stroke(width=stroke)
        center_emination = Group(
            circle_emination, 
            arrow1, arrow2, arrow3, arrow4, arrow5, arrow6
        ).set_color(YELLOW).scale(0.25).shift(DOWN*1.2)

        self.wait(2)
        self.play(FadeIn(center_emination))
        self.wait(2)

        hexagon = RegularPolygon(n=6).scale(0.42).set_color(GREEN)
        triangle_up = RegularPolygon(n=3).scale(0.5).set_color(GREEN)
        triangle_down = RegularPolygon(n=3).scale(0.5).set_color(GREEN)
        rhombus = Polygon(
            [0,1,0],
            [0.7,0,0],
            [0,-1,0],
            [-0.7,0,0],
        ).scale(0.45).set_color(PURPLE)
        hexagon.move_to(numbers[6])
        triangle_up.move_to(numbers[3]).shift(UP*0.1)
        rhombus.move_to(numbers[0])
        shapes = Group(hexagon, triangle_up, rhombus)
        self.play(
            FadeIn(shapes)
        )
        self.wait(2)
        self.play(
            frame.animate.scale(0.001).shift(DOWN*1.2),
            run_time = 5
        )
        self.wait(2)

class SymbolBreakdown(Scene):
    def construct(self):
        frame = self.camera.frame
        symbol = vbm_symbol().scale(2)
        numbers = vbm_numbers(1,9,1.2,2.5)
        circle = Circle().scale(2).set_color(WHITE)
        dots = vbm_dots(1,9,1,2)
        vbm_group = Group(dots, circle, numbers)

        left_shift = 3
        self.wait()
        self.play(
            ShowCreation(circle),
        )
        self.wait()
        for i in range(0,len(numbers)):
            self.play(
                Write(numbers[i]),
                FadeIn(dots[i]),
                run_time=0.3
            )
        self.wait()

        vertical = DashedLine(circle.get_top(), circle.get_bottom())
        vertical.set_color(PURPLE)
        self.play(ShowCreation(vertical))
        self.wait()

        mid_18 = np.array([0,dots[1].get_center()[1],0])
        mid_72 = np.array([0,dots[7].get_center()[1],0])
        mid_45 = np.array([0,dots[4].get_center()[1],0])
        mid_36 = np.array([0,dots[3].get_center()[1],0])
        horizontal_1 = DashedLine(dots[1],mid_18).set_color(RED)
        horizontal_8 = DashedLine(dots[8],mid_18).set_color(BLUE)
        horizontal_7 = DashedLine(dots[7], mid_72).set_color(RED)
        horizontal_2 = DashedLine(dots[2], mid_72).set_color(BLUE)
        horizontal_4 = DashedLine(dots[4], mid_45).set_color(RED)
        horizontal_5 = DashedLine(dots[5], mid_45).set_color(BLUE)
        horizontal_3 = DashedLine(dots[3], mid_36).set_color(GREEN)
        horizontal_6 = DashedLine(dots[6], mid_36).set_color(GREEN)
        lines = Group(
            horizontal_1, 
            horizontal_2, 
            horizontal_3,
            horizontal_4, 
            horizontal_5, 
            horizontal_6,
            horizontal_7, 
            horizontal_8, 
            vertical,
        )
        adds_18 = Tex(r"1 + 8 = 9")
        adds_72 = Tex(r"7 + 2 = 9")
        adds_45 = Tex(r"4 + 5 = 9")
        adds_36 = Tex(r"3 + 6 = 9")
        adds_99 = Tex(r"9 + 9 = 9?")
        adds = Group(adds_18, adds_72, adds_36, adds_45, adds_99)
        adds.arrange(DOWN, buff= 0.3).shift(RIGHT*4.6)
        eighteen = Tex(r"18").scale(0.8).next_to(adds_99[1], DOWN, buff = 0.3)
        adds_mod = Tex(r"1 + 8 = 9").scale(0.8).next_to(adds_99, DOWN, buff = 0.3)
        
        self.play(
            Indicate(numbers[1]),
            Indicate(numbers[8]),
        )
        self.play(
            Indicate(numbers[2]),
            Indicate(numbers[7]),
        )
        self.play(
            Indicate(numbers[3]),
            Indicate(numbers[6]),
        )
        self.play(
            Indicate(numbers[4]),
            Indicate(numbers[5]),
        )
        self.play(
            Indicate(numbers[0]),
        )
        self.wait(2)

        self.play(
            ShowCreation(horizontal_1),
            ShowCreation(horizontal_8),
            Write(adds_18),
        )
        self.wait()
        self.play(
            ShowCreation(horizontal_7),
            ShowCreation(horizontal_2),
            Write(adds_72),
        )
        self.wait()
        self.play(
            ShowCreation(horizontal_3),
            ShowCreation(horizontal_6),
            Write(adds_36),
        )
        self.wait()
        self.play(
            ShowCreation(horizontal_4),
            ShowCreation(horizontal_5),
            Write(adds_45),
        )
        self.wait()
        self.play(
            Write(adds_99)
        )
        self.wait()
        self.play(
            FadeIn(eighteen)
        )
        self.wait()
        self.play(
            ReplacementTransform(eighteen, adds_mod)
        )
        self.wait()
        self.play(
            FadeOut(adds_mod),
            FadeOut(eighteen),
            FadeOut(adds),
            FadeOut(lines)
        )
        self.wait()
        t2c = {
            "1":RED, "4":RED, "7":RED,
            "2":BLUE, "5":BLUE, "8":BLUE,
            "3":GREEN, "6":GREEN, "9":GREEN,
        }





    ######## RING
        def base10_numbers(begin,font_scale, radius):
            number_group = Group()
            for i in range(begin,begin+9):
                number = Tex(str(i)).scale(font_scale)
                number.shift(
                    [
                        radius*np.sin(TAU * (i/9)),
                        radius*np.cos(TAU * (i/9)),
                        0
                    ]            
                )
                number_group.add(number)

            return number_group
               
        first_ring = base10_numbers(10, 0.8, 3.2)
        self.play(Write(first_ring[0]))
        self.wait()
        eq_for_10 = Tex(r"1+0=1").next_to(first_ring[0],UR, buff = 0.5)
        self.play(Write(eq_for_10))
        self.wait()
        self.play(FadeOut(eq_for_10))
        self.wait()


        for ring in first_ring:
            self.play(Write(ring))
        self.wait()

        second_ring = base10_numbers(19, 0.8, 3.8)
        self.play(Write(second_ring[0]))
        self.wait()

        nineteen = Tex(r"1+9 = 10")
        ten = Tex(r"1+0=1")
        ex_19 = Group(nineteen, ten).arrange(DOWN)
        ex_19.next_to(second_ring[0], RIGHT, buff = 1)
        self.play(Write(nineteen))
        self.wait()
        self.play(Write(ten))
        self.wait()
        self.play(FadeOut(ex_19))

        for second in second_ring:
            self.play(Write(second))
        self.wait()
        self.play(frame.animate.scale(3.2))
        all_rings = Group(first_ring, second_ring)
        for i in range(0, 13):
            for j in range(0,9):
                new_ring = base10_numbers(28 + (9*i), 0.8, 4.4 + (0.6 * i))
                all_rings.add(new_ring)
                self.add(new_ring[j])
                self.wait(0.04)
        indicator_rectangle = SurroundingRectangle(all_rings[-1][2])
        self.play(ShowCreation(indicator_rectangle))
        self.wait()
        adds_138 = Tex(r"138 = 3")
        mods_138 = Tex(r"1+3+8 = 12")
        mods_12 = Tex(r"1+2=3")
        group_138 = Group(adds_138, mods_138, mods_12).arrange(DOWN).scale(3.2)
        group_138.next_to(indicator_rectangle, DR, buff=0.2)
        self.play(Write(adds_138))
        self.wait()
        self.play(Write(mods_138))
        self.wait()
        self.play(Write(mods_12))
        self.wait()
        self.play(
            FadeOut(group_138),
            FadeOut(all_rings),
            frame.animate.scale(1/3.2),
        )
        self.wait()

        self.play(vbm_group.animate.shift(LEFT*3.2))
        eisel = Rectangle(width=6.2,height=10,color=BLACK)
        eisel.move_to(4*RIGHT).set_fill(BLACK).set_opacity(1.0)
        self.play(FadeIn(eisel))

        text_scale = 1.3
        family_title = Tex(r"\text{Number Colors}").scale(1.5).move_to(eisel).shift(UP*3)
        plus_three_1 =  Tex(r"+3").scale(0.6).scale(text_scale)
        plus_three_2 =  Tex(r"+3").scale(0.6).scale(text_scale)
        plus_three_x =  Tex(r"+3").scale(0.6).scale(text_scale)
        plus_six_1 =  Tex(r"+6").scale(0.6).scale(text_scale)
        plus_six_2 =  Tex(r"+6").scale(0.6).scale(text_scale)
        plus_six_x =  Tex(r"+6").scale(0.6).scale(text_scale)
        family_1 = Tex(r"1", tex_to_color_map = t2c).scale(text_scale)
        family_4 = Tex(r"4", tex_to_color_map = t2c).scale(text_scale)
        family_7 = Tex(r"7", tex_to_color_map = t2c).scale(text_scale)
        family_147 = Group(family_1, plus_three_1, family_4, plus_three_2, family_7).arrange(RIGHT, buff=0.3*text_scale)
        
        plus_three_3 =  Tex(r"+3").scale(0.6).scale(text_scale)
        plus_three_4 =  Tex(r"+3").scale(0.6).scale(text_scale)
        family_2 = Tex(r"2", tex_to_color_map = t2c).scale(text_scale)
        family_5 = Tex(r"5", tex_to_color_map = t2c).scale(text_scale)
        family_8 = Tex(r"8", tex_to_color_map = t2c).scale(text_scale)
        family_258 = Group(family_2, plus_three_3, family_5, plus_three_4, family_8).arrange(RIGHT, buff=0.3*text_scale)
        plus_three_5 =  Tex(r"+3").scale(0.6).scale(text_scale)
        plus_three_6 =  Tex(r"+3").scale(0.6).scale(text_scale)
        family_3 = Tex(r"3", tex_to_color_map = t2c).scale(text_scale)
        family_6 = Tex(r"6", tex_to_color_map = t2c).scale(text_scale)
        family_9 = Tex(r"9", tex_to_color_map = t2c).scale(text_scale)
        family_369 = Group(family_3, plus_three_5, family_6, plus_three_6, family_9).arrange(RIGHT, buff=0.3*text_scale)

        family_group = Group(family_147, family_258, family_369).arrange(DOWN, buff=0.7*text_scale)
        family_group.next_to(family_title, DOWN, buff=1.5*text_scale)

        arrow_3 = Arrow(ORIGIN, RIGHT*3).scale(text_scale)
        arrow_3_title = Tex(r"+3").scale(0.6).scale(text_scale)
        arr3 = Group(arrow_3, arrow_3_title).arrange(UP, buff=0.1*text_scale).next_to(family_147, UP, buff=0.4*text_scale)
        arrow_6 = Arrow(ORIGIN, LEFT*3).scale(text_scale)
        arrow_6_title = Tex(r"+6").scale(0.6).scale(text_scale)
        arr6 = Group(arrow_6, arrow_6_title).arrange(DOWN, buff=0.1*text_scale).next_to(family_147, DOWN, buff=0.4*text_scale)

        line14 = Line(dots[1], dots[4]).set_color(RED)
        line47 = Line(dots[4], dots[7]).set_color(RED)
        line71 = Line(dots[7], dots[1]).set_color(RED)
        line41 = Line(dots[4], dots[1]).set_color(RED)
        line74 = Line(dots[7], dots[4]).set_color(RED)
        line17 = Line(dots[1], dots[7]).set_color(RED)
        line_147 = Group(line14, line47, line71, line17, line74, line41)
        line25 = Line(dots[2], dots[5]).set_color(BLUE)
        line58 = Line(dots[5], dots[8]).set_color(BLUE)
        line82 = Line(dots[8], dots[2]).set_color(BLUE)
        line_258 = Group(line25, line58, line82)
        line36 = Line(dots[3], dots[6]).set_color(GREEN)
        line69 = Line(dots[6], dots[0]).set_color(GREEN)
        line93 = Line(dots[0], dots[3]).set_color(GREEN)
        line_369 = Group(line36, line69, line93)
        t2c = {
            "1":RED, "4":RED, "7":RED,
            "2":BLUE, "5":BLUE, "8":BLUE,
            "3":GREEN, "6":GREEN, "0":GREEN,
        }
        eq_for_14 = Tex(r"1+3=4", tex_to_color_map = t2c).next_to(family_147,DOWN,buff=2).scale(0.9*text_scale)
        eq_for_47 = Tex(r"4+3=7", tex_to_color_map = t2c).next_to(family_147,DOWN,buff=2).scale(0.9*text_scale)
        eq_for_71 = Tex(r"7+3=10=1", tex_to_color_map = t2c).next_to(family_147,DOWN,buff=2).scale(0.9*text_scale)
        eq_for_71[4].set_color(WHITE)
        eq_for_71[5].set_color(WHITE)
        self.play(FadeIn(family_title))
        self.wait()
        self.play(FadeIn(family_147[0]))
        self.wait()
        self.play(
            FadeIn(family_147[1]),
            FadeIn(family_147[2]),
            ShowCreation(line_147[0]),
            Write(eq_for_14),
        )
        self.wait()

        self.play(
            FadeOut(family_147[1]),
            FadeIn(family_147[3]),
            FadeIn(family_147[4]),
            ShowCreation(line_147[1]),
            FadeOut(eq_for_14),
            Write(eq_for_47),
        )
        self.wait()

        plus_three_x.next_to(family_147, RIGHT, buff = 0.3*text_scale)
        self.play(
            FadeOut(family_147[3]),
            FadeIn(plus_three_x),
            ShowCreation(line_147[2]),
            FadeOut(eq_for_47),
            Write(eq_for_71),
        )
        self.wait()
        self.play(
            FadeIn(arr3),
            FadeOut(plus_three_x),
        )
        self.wait()
        self.play(
            FadeOut(line_147[0]),
            FadeOut(line_147[1]),
            FadeOut(line_147[2]),
            FadeOut(eq_for_71),
        )
        self.wait()

        plus_six_1.next_to(family_147, LEFT, buff = 0.3*text_scale)
        plus_six_2.move_to(family_147[3])
        plus_six_x.move_to(family_147[1])
        self.play(
            FadeIn(arr6),
            FadeIn(plus_six_1),
            ShowCreation(line_147[3]),
        )
        self.wait()
        self.play(
            FadeOut(plus_six_1),
            FadeIn(plus_six_2),
            ShowCreation(line_147[4]),
        )
        self.wait()
        self.play(
            FadeOut(plus_six_2),
            FadeIn(plus_six_x),
            ShowCreation(line_147[5]),
        )
        self.wait()
        self.play(
            FadeOut(plus_six_x),
            arr6.animate.next_to(family_258, DOWN, buff=0.4)
        )
        self.wait()

        self.play(
            FadeIn(family_258[0]),
            FadeIn(family_258[2]),
            FadeIn(family_258[4]),
            FadeIn(line_258),
        )
        self.wait()
        self.play(
            arr6.animate.next_to(family_369, DOWN, buff=0.4)
        )
        self.wait()
        self.play(
            FadeIn(family_369[0]),
            FadeIn(family_369[2]),
            FadeIn(family_369[4]),
            FadeIn(line_369),
        )
        self.wait()
        
        fng_title = Tex(r"\text{Family Number Groups}").scale(1.1).move_to(family_title)
        self.play(
            Uncreate(family_title),
            Write(fng_title),
        )
        self.wait(2)
        self.play(
            Transform(line_147, line_258),
            Transform(line_258, line_147),
        )
        self.wait()

        self.play(
            Indicate(line_369)
        )
        self.wait()

        self.play(
            FadeOut(family_147[0]),
            FadeOut(family_147[2]),
            FadeOut(family_147[4]),
            FadeOut(line_147),
            FadeOut(family_369[0]),
            FadeOut(family_369[2]),
            FadeOut(family_369[4]),
            FadeOut(line_369),
            FadeOut(family_258[0]),
            FadeOut(family_258[2]),
            FadeOut(family_258[4]),
            FadeOut(line_258),
            FadeOut(arr3),
            FadeOut(arr6),
            FadeOut(fng_title),
            FadeOut(eisel),
        )
        self.play(
            vbm_group.animate.shift(RIGHT*3.2),
        )
        self.wait()
        doubling_circuit = doubling_sequence(9,2,1,2).set_color(RED)
        doubling_title = Tex(r"\text{Doubling}").set_color(RED).shift(RIGHT*5+UP*2.5)
        doubling_nums = Group(
            Tex(r"1"),
            Tex(r"2"),
            Tex(r"4"),
            Tex(r"8"),
            Tex(r"16"),
            Tex(r"32"),
            Tex(r"64"),
            Tex(r"128"),
            Tex(r"256"),
            Tex(r"512"),
        ).arrange(DOWN).scale(0.8)
        doubling_mods = Group(
            Tex(r"1"),
            Tex(r"2"),
            Tex(r"4"),
            Tex(r"8"),
            Tex(r"7"),
            Tex(r"5"),
            Tex(r"1"),
            Tex(r"2"),
            Tex(r"4"),
            Tex(r"8"),
        ).arrange(DOWN).scale(0.8)
        doubling_group = Group(doubling_nums, doubling_mods).arrange(RIGHT, buff=1)
        doubling_group.next_to(doubling_title, DOWN, buff=0.5)
        arrow_doub = Arrow(ORIGIN, DOWN*2).scale(0.4).next_to(doubling_nums,DOWN)
        arrow_mod = Arrow(ORIGIN, DOWN*2).scale(0.4).next_to(doubling_mods,DOWN)
        self.play(FadeIn(doubling_circuit))
        self.wait()
        self.play(FadeOut(doubling_circuit))
        self.wait()
        doubling_title.shift(RIGHT*0.1)
        self.play(FadeIn(doubling_title))
        self.wait()
        self.play(Write(doubling_nums[0]))
        self.wait()
        self.play(
            ShowCreation(doubling_circuit[0]),
            Write(doubling_nums[1]),
        )
        self.wait()
        self.play(
            ShowCreation(doubling_circuit[1]),
            Write(doubling_nums[2]),
        )
        self.wait()
        self.play(
            ShowCreation(doubling_circuit[2]),
            Write(doubling_nums[3]),
        )
        self.wait()
        self.play(Write(doubling_nums[4]))
        self.wait()
        for i in range(0,4):
            self.play(Write(doubling_mods[i]))
        self.wait()
        self.play(
            ShowCreation(doubling_circuit[3]),
            Write(doubling_mods[4]),
        )
        self.wait()
        self.play(
            ShowCreation(doubling_circuit[4]),
            Write(doubling_nums[5]),
            Write(doubling_mods[5]),
        )
        self.wait()
        self.play(
            ShowCreation(doubling_circuit[5]),
            Write(doubling_nums[6]),
            Write(doubling_mods[6]),
        )
        self.wait()
        self.play(
            ShowCreation(doubling_circuit[0]),
            Write(doubling_nums[7]),
            Write(doubling_mods[7]),
        )
        self.wait()
        self.play(
            ShowCreation(doubling_circuit[1]),
            Write(doubling_nums[8]),
            Write(doubling_mods[8]),
        )
        self.wait()
        self.play(
            ShowCreation(doubling_circuit[2]),
            Write(doubling_nums[9]),
            Write(doubling_mods[9]),
        )
        self.wait()
        self.play(
            ShowCreation(arrow_doub),
            ShowCreation(arrow_mod),
        )
        self.play(FadeOut(doubling_circuit))
        self.wait()

        halving_circuit = halving_sequence(9,2).set_color(BLUE)
        halving_title = Tex(r"\text{Halving}").set_color(BLUE).shift(LEFT*5+UP*2.5)
        halving_nums = Group(
            Tex(r"1"),
            Tex(r".5"),
            Tex(r".25"),
            Tex(r".125"),
            Tex(r".0625"),
            Tex(r".03125"),
            Tex(r".01562..."),
            Tex(r".00781..."),
            Tex(r".00390..."),
            Tex(r".00195..."),
        ).arrange(DOWN).scale(0.8)
        halving_mods = Group(
            Tex(r"1"),
            Tex(r"5"),
            Tex(r"7"),
            Tex(r"8"),
            Tex(r"4"),
            Tex(r"2"),
            Tex(r"1"),
            Tex(r"5"),
            Tex(r"7"),
            Tex(r"8"),
        ).arrange(DOWN).scale(0.8)

        halving_group = Group(halving_nums, halving_mods).arrange(RIGHT, buff=1)
        halving_group.next_to(halving_title, DOWN, buff=0.5)
        arrow_halv = Arrow(ORIGIN, DOWN*2).scale(0.4).next_to(halving_nums,DOWN)
        arrow_mod1 = Arrow(ORIGIN, DOWN*2).scale(0.4).next_to(halving_mods,DOWN)

        halving_title.shift(RIGHT*0.3)
        self.play(FadeIn(halving_title))
        self.wait()
        self.play(
            Write(halving_nums[0]),
            Write(halving_mods[0]),
        )
        self.wait()
        self.play(
            ShowCreation(halving_circuit[0]),
            Write(halving_nums[1]),
            Write(halving_mods[1]),
        )
        self.wait()
        self.play(
            ShowCreation(halving_circuit[1]),
            Write(halving_nums[2]),
            Write(halving_mods[2]),
        )
        self.wait()
        self.play(
            ShowCreation(halving_circuit[2]),
            Write(halving_nums[3]),
            Write(halving_mods[3]),
        )
        self.wait()
        self.play(
            ShowCreation(halving_circuit[3]),
            Write(halving_nums[4]),
            Write(halving_mods[4]),
        )
        self.wait()
        self.play(
            ShowCreation(halving_circuit[4]),
            Write(halving_nums[5]),
            Write(halving_mods[5]),
        )
        self.wait()
        self.play(
            ShowCreation(halving_circuit[5]),
            Write(halving_nums[6]),
            Write(halving_mods[6]),
        )
        self.play(
            ShowCreation(halving_circuit[0]),
            Write(halving_nums[7]),
            Write(halving_mods[7]),
        )
        self.play(
            ShowCreation(halving_circuit[1]),
            Write(halving_nums[8]),
            Write(halving_mods[8]),
        )
        self.play(
            ShowCreation(halving_circuit[2]),
            Write(halving_nums[9]),
            Write(halving_mods[9]),
        )
        self.play(
            ShowCreation(arrow_halv),
            ShowCreation(arrow_mod1),
        )
        double_group = Group(
            doubling_mods[0].copy(),
            doubling_mods[1].copy(),
            doubling_mods[2].copy(),
            doubling_mods[3].copy(),
            doubling_mods[4].copy(),
            doubling_mods[5].copy(),
        )
        half_group = Group(
            halving_mods[0].copy(),
            halving_mods[1].copy(),
            halving_mods[2].copy(),
            halving_mods[3].copy(),
            halving_mods[4].copy(),
            halving_mods[5].copy(),
        )
        self.wait()
        double_rect = SurroundingRectangle(double_group).set_color(RED)
        half_rect = SurroundingRectangle(half_group).set_color(BLUE)
        self.play(
            FadeIn(double_rect),
            FadeIn(half_rect),
        )
        self.wait()
        self.add(double_group, half_group)
        double_group.add(double_rect)
        half_group.add(half_rect)
        self.play(
            double_group.animate.scale(1/0.8).next_to(circle, RIGHT*9),
            half_group.animate.scale(1/0.8).next_to(circle, LEFT*9),
            FadeOut(doubling_nums),
            FadeOut(doubling_mods),
            FadeOut(halving_nums),
            FadeOut(halving_mods),
            FadeOut(arrow_doub),
            FadeOut(arrow_halv),
            FadeOut(arrow_mod),
            FadeOut(arrow_mod1),
            FadeOut(halving_circuit),
            FadeOut(halving_title),
            FadeOut(doubling_title),
        )
        self.wait()
        self.play(
            Indicate(numbers[0]),
            Indicate(numbers[3]),
            Indicate(numbers[6]),
        )
        vert_9 = DashedLine(circle.get_top(), circle.get_bottom()).set_color(GREEN)
        vert_1 = vert_9.copy().shift([dots[1].get_center()[0],0,0]).set_color(RED)
        vert_2 = vert_9.copy().shift([dots[2].get_center()[0],0,0]).set_color(BLUE)
        vert_3 = vert_9.copy().shift([dots[3].get_center()[0],0,0]).set_color(GREEN)
        vert_4 = vert_9.copy().shift([dots[4].get_center()[0],0,0]).set_color(RED)
        vert_5 = vert_9.copy().shift([dots[5].get_center()[0],0,0]).set_color(BLUE)
        vert_6 = vert_9.copy().shift([dots[6].get_center()[0],0,0]).set_color(GREEN)
        vert_7 = vert_9.copy().shift([dots[7].get_center()[0],0,0]).set_color(RED)
        vert_8 = vert_9.copy().shift([dots[8].get_center()[0],0,0]).set_color(BLUE)

        vert_group = Group(vert_7,vert_6,vert_8,vert_5,vert_9,vert_4,vert_1,vert_3,vert_2)
        for vert in vert_group:
            self.play(
                ShowCreation(vert)
            )
        self.wait()
        dashed_3 = DashedLine(
            dots[3].get_center(), 
            [dots[3].get_center()[0],-dots[3].get_center()[1],0],
        ).set_color(GREEN)
        dashed_6 = DashedLine(
            dots[6].get_center(), 
            [dots[6].get_center()[0],-dots[6].get_center()[1],0],
        ).set_color(GREEN)
        self.add(dashed_3, dashed_6)
        self.play(
            FadeOut(vert_1),
            FadeOut(vert_2),
            FadeOut(vert_4),
            FadeOut(vert_8),
            FadeOut(vert_7),
            FadeOut(vert_5),
            FadeOut(vert_3),
            FadeOut(vert_6),
        )
        
        foward_group = Group(
            Tex(r"3"),
            Tex(r"3"),
            Tex(r"9"),
            Tex(r"6"),
            Tex(r"6"),
            Tex(r"9"),
        ).arrange(DOWN).next_to(double_group, RIGHT).shift(DOWN*0.3).set_color(GREEN)
        backward_group = Group(
            Tex(r"9"),
            Tex(r"6"),
            Tex(r"6"),
            Tex(r"9"),
            Tex(r"3"),
            Tex(r"3"),
        ).arrange(DOWN).next_to(half_group, RIGHT).shift(DOWN*0.3).set_color(GREEN)
        indicator_circuit = doubling_sequence(9,2,1,2)

        indicator_9 = Line(circle.get_top(), circle.get_bottom(), stroke_width=7).set_color(GREEN)
        indicator_3 = Line(
            dots[3].get_center(),
            [dots[3].get_center()[0],-dots[3].get_center()[1],0],
            stroke_width=7,
        ).set_color(GREEN)
        indicator_6 = Line(
            dots[6].get_center(),
            [dots[6].get_center()[0],-dots[6].get_center()[1],0],
            stroke_width=7,
        ).set_color(GREEN)
        self.play(
            ShowCreation(indicator_circuit[0]),
            Write(foward_group[0]),
            FadeIn(indicator_3),
        )
        self.play(FadeOut(indicator_3))
        self.wait()
        self.play(
            ShowCreation(indicator_circuit[1]),
            Write(foward_group[1]),
            FadeIn(indicator_3),
        )
        self.play(FadeOut(indicator_3))
        self.wait()
        self.play(
            ShowCreation(indicator_circuit[2]),
            Write(foward_group[2]),
            FadeIn(indicator_9),
        )
        self.play(FadeOut(indicator_9))
        self.wait()
        self.play(
            ShowCreation(indicator_circuit[3]),
            Write(foward_group[3]),
            FadeIn(indicator_6),
        )
        self.play(FadeOut(indicator_6))
        self.wait()
        self.play(
            ShowCreation(indicator_circuit[4]),
            Write(foward_group[4]),
            FadeIn(indicator_6),
        )
        self.play(FadeOut(indicator_6))
        self.wait()
        self.play(
            ShowCreation(indicator_circuit[5]),
            Write(foward_group[5]),
            FadeIn(indicator_9),
        )
        self.play(FadeOut(indicator_9))
        self.wait()
        self.play(
            FadeOut(indicator_circuit),
        )
        self.wait()

        backward_circuit = halving_sequence(9,2)
        
        self.play(
            ShowCreation(backward_circuit[0]),
            Write(backward_group[0]),
            FadeIn(indicator_9),
        )
        self.play(FadeOut(indicator_9))
        self.play(
            ShowCreation(backward_circuit[1]),
            Write(backward_group[1]),
            FadeIn(indicator_6),
        )
        self.play(FadeOut(indicator_6))
        self.play(
            ShowCreation(backward_circuit[2]),
            Write(backward_group[2]),
            FadeIn(indicator_6),
        )
        self.play(FadeOut(indicator_6))
        self.play(
            ShowCreation(backward_circuit[3]),
            Write(backward_group[3]),
            FadeIn(indicator_9),
        )
        self.play(FadeOut(indicator_9))
        self.play(
            ShowCreation(backward_circuit[4]),
            Write(backward_group[4]),
            FadeIn(indicator_3),
        )
        self.play(FadeOut(indicator_3))
        self.play(
            ShowCreation(backward_circuit[5]),
            Write(backward_group[5]),
            FadeIn(indicator_3),
        )
        self.play(FadeOut(indicator_3))
        self.play(FadeOut(double_rect))
        self.play(
            FadeOut(double_group[0]),
            FadeOut(double_group[1]),
            FadeOut(foward_group[0]),
            FadeOut(foward_group[1]),
        )
        double_group.remove(double_rect, double_group[0], double_group[1])
        foward_group.remove(foward_group[0], foward_group[1])
        self.remove(foward_group[0], foward_group[1])

        self.play(
            double_group.animate.shift(UP*1.12),
            foward_group.animate.shift(UP*1.12)
        )
        self.wait()
        replace_doub1 = Tex(r"1").next_to(double_group, DOWN)
        replace_doub2 = Tex(r"2").next_to(replace_doub1, DOWN)
        replace_fow1 = Tex(r"3").next_to(foward_group, DOWN).set_color(GREEN)
        replace_fow2 = Tex(r"3").next_to(replace_fow1, DOWN).set_color(GREEN)
        double_group.add(replace_doub1, replace_doub2)
        foward_group.add(replace_fow1, replace_fow2)
        self.play(
            FadeIn(replace_doub1),
            FadeIn(replace_doub2),
            FadeIn(replace_fow1),
            FadeIn(replace_fow2),
        )
        self.play(FadeIn(double_rect))
        double_group.add(double_rect)

        self.wait()
        self.play(
            FadeOut(backward_circuit),
        )
        self.play(
            dashed_3.animate.shift(RIGHT*2.5),
            dashed_6.animate.shift(RIGHT*2.5),
            vert_9.animate.shift(RIGHT*2.5),
            vbm_group.animate.shift(RIGHT*2.5),
            half_group.animate.shift(LEFT*0.3),
            backward_group.animate.set_color(WHITE).shift(RIGHT*0.3),
            double_group.animate.next_to(half_group, RIGHT, buff = 1.5),
            FadeOut(foward_group),
        )
        backward_rect = SurroundingRectangle(backward_group).set_color(GREEN)
        self.play(FadeIn(backward_rect))
        left_arrow = Arrow([0,0,0],[1,0,0]).next_to(half_group[0], LEFT)
        right_arrow = Arrow([0,0,0],[-1,0,0]).next_to(double_group[0], RIGHT)
        self.wait()
        self.play(FadeIn(left_arrow), FadeIn(right_arrow))
        self.wait()
        indicator_circuit.shift(RIGHT*2.5)
        backward_circuit.shift(RIGHT*2.5)
        indicator_3.shift(RIGHT*2.5)
        indicator_6.shift(RIGHT*2.5)
        indicator_9.shift(RIGHT*2.5)
        self.play(
            ShowCreation(indicator_circuit[2]),
            ShowCreation(backward_circuit[0]),
            FadeIn(indicator_9),
            left_arrow.animate.next_to(half_group[1], LEFT),
            right_arrow.animate.next_to(double_group[1], RIGHT),
        )
        self.wait()
        self.remove(indicator_circuit[2],backward_circuit[0])
        self.add(indicator_circuit[5],backward_circuit[3])
        self.play(
            Uncreate(indicator_circuit[5]),
            Uncreate(backward_circuit[3]),
            FadeOut(indicator_9),
        )

        self.wait()
        self.play(
            ShowCreation(indicator_circuit[3]),
            ShowCreation(backward_circuit[1]),
            FadeIn(indicator_6),
            left_arrow.animate.next_to(half_group[2], LEFT),
            right_arrow.animate.next_to(double_group[2], RIGHT),
        )
        self.wait()
        self.remove(indicator_circuit[3],backward_circuit[1])
        self.add(indicator_circuit[4],backward_circuit[2])
        self.play(
            Uncreate(indicator_circuit[4]),
            Uncreate(backward_circuit[2]),
            FadeOut(indicator_6),
        )
        indicator_circuit = doubling_sequence(9,2,1,2).shift(RIGHT*2.5)
        backward_circuit = halving_sequence(9,2).shift(RIGHT*2.5)

        self.wait()
        self.play(
            ShowCreation(indicator_circuit[4]),
            ShowCreation(backward_circuit[2]),
            FadeIn(indicator_6),
            left_arrow.animate.next_to(half_group[3], LEFT),
            right_arrow.animate.next_to(double_group[3], RIGHT),
        )
        self.wait()
        self.remove(indicator_circuit[4],backward_circuit[2])
        self.add(indicator_circuit[3],backward_circuit[1])
        self.play(
            Uncreate(indicator_circuit[3]),
            Uncreate(backward_circuit[1]),
            FadeOut(indicator_6),
        )

        self.wait()
        self.play(
            ShowCreation(indicator_circuit[5]),
            ShowCreation(backward_circuit[3]),
            FadeIn(indicator_9),
            left_arrow.animate.next_to(half_group[4], LEFT),
            right_arrow.animate.next_to(double_group[4], RIGHT),
        )
        self.wait()
        self.remove(indicator_circuit[5],backward_circuit[3])
        self.add(indicator_circuit[2],backward_circuit[0])
        self.play(
            Uncreate(indicator_circuit[2]),
            Uncreate(backward_circuit[0]),
            FadeOut(indicator_9),
        )

        self.wait()
        self.play(
            ShowCreation(indicator_circuit[0]),
            ShowCreation(backward_circuit[4]),
            FadeIn(indicator_3),
            left_arrow.animate.next_to(half_group[5], LEFT),
            right_arrow.animate.next_to(double_group[5], RIGHT),
        )
        self.wait()
        self.remove(indicator_circuit[0],backward_circuit[4])
        self.add(indicator_circuit[1],backward_circuit[5])
        self.play(
            Uncreate(indicator_circuit[1]),
            Uncreate(backward_circuit[5]),
            FadeOut(indicator_3),
        )
        indicator_circuit = doubling_sequence(9,2,1,2).shift(RIGHT*2.5)
        backward_circuit = halving_sequence(9,2).shift(RIGHT*2.5)
        self.wait()
        self.play(
            ShowCreation(indicator_circuit[1]),
            ShowCreation(backward_circuit[5]),
            FadeIn(indicator_3),
            left_arrow.animate.next_to(half_group[0], LEFT),
            right_arrow.animate.next_to(double_group[0], RIGHT),
        )
        self.wait()
        self.remove(indicator_circuit[1],backward_circuit[5])
        self.add(indicator_circuit[0],backward_circuit[4])
        self.play(
            Uncreate(indicator_circuit[0]),
            Uncreate(backward_circuit[4]),
            FadeOut(indicator_3),
        )
        self.wait()

        pos_green_circs = Group(
            Circle().set_color(GREEN).scale(0.25).move_to(backward_group[1]),
            Circle().set_color(GREEN).scale(0.25).move_to(backward_group[3]),
            Circle().set_color(GREEN).scale(0.25).move_to(backward_group[5]),
        )
        pos_red_circs = Group(
            Circle().set_color(RED).scale(0.25).move_to(double_group[0]),
            Circle().set_color(RED).scale(0.25).move_to(double_group[2]),
            Circle().set_color(RED).scale(0.25).move_to(double_group[4]),
        )
        pos_blue_circs = Group(
            Circle().set_color(BLUE).scale(0.25).move_to(half_group[1]),
            Circle().set_color(BLUE).scale(0.25).move_to(half_group[3]),
            Circle().set_color(BLUE).scale(0.25).move_to(half_group[5]),
        )

        neg_green_circs = Group(
            Circle().set_color(WHITE).scale(0.25).move_to(backward_group[0]),
            Circle().set_color(WHITE).scale(0.25).move_to(backward_group[2]),
            Circle().set_color(WHITE).scale(0.25).move_to(backward_group[4]),
        )
        neg_red_circs = Group(
            Circle().set_color(WHITE).scale(0.25).move_to(double_group[1]),
            Circle().set_color(WHITE).scale(0.25).move_to(double_group[3]),
            Circle().set_color(WHITE).scale(0.25).move_to(double_group[5]),
        )
        neg_blue_circs = Group(
            Circle().set_color(WHITE).scale(0.25).move_to(half_group[0]),
            Circle().set_color(WHITE).scale(0.25).move_to(half_group[2]),
            Circle().set_color(WHITE).scale(0.25).move_to(half_group[4]),
        )

        self.play(
            FadeOut(left_arrow),
            FadeOut(right_arrow),
            FadeOut(backward_rect),
            FadeOut(double_rect),
            FadeOut(half_rect),
        )
        self.wait()
        self.play(
            FadeIn(pos_green_circs),
            FadeIn(pos_red_circs),
            FadeIn(pos_blue_circs),
        )
        self.wait()
        self.play(
            FadeIn(neg_green_circs),
            FadeIn(neg_red_circs),
            FadeIn(neg_blue_circs),
        )
        # self.play(
        #     FadeOut(half_group),
        #     FadeOut(double_group),
        #     FadeOut(backward_group),

        #     FadeOut(dashed_3),
        #     FadeOut(dashed_6),
        #     FadeOut(vert_9),
        #     FadeOut(backward_rect),
        # )

class VBMBasic(Scene):
    def construct(self):
    #OPENING
    #region
        symbol = vbm_symbol().scale(2)
        numbers = vbm_numbers(1,9,1,2.5)
        circle = Circle().scale(2).set_color(WHITE)
        dots = vbm_dots(1,9,1,2)

        self.play(
            FadeIn(numbers),
            FadeIn(circle),
            FadeIn(dots),
        )
        doubling2s = doubling_sequence(9,2,1,1).scale(2)
        doubling3s = doubling_sequence(9,2,3,2)
        doubling6s = doubling_sequence(9,2,6,2)
        scale = 2
        scene_group = Group(numbers, circle, dots)
        doubling_group = Group(doubling2s, doubling3s, doubling6s).shift(LEFT*3)
        self.wait()
        self.play(scene_group.animate.shift(LEFT*3))
        eisel = Rectangle(width=6,height=10,color=BLACK)
        eisel.move_to(4*RIGHT).set_fill(BLACK).set_opacity(1.0)
        self.wait()
        self.play(FadeIn(eisel))
        title = Tex(r"Doubling \ Sequences")
        one = Tex(r"1").set_color(RED)
        two = Tex(r"2").set_color(BLUE)
        four = Tex(r"4").set_color(RED)
        eight = Tex(r"8").set_color(BLUE)
        seven = Tex(r"7").set_color(RED)
        five = Tex(r"5").set_color(BLUE)
        three = Tex(r"3").set_color(GREEN)
        six = Tex(r"6").set_color(GREEN)
        nine = Tex(r"9").set_color(GREEN)
        title_dub_2s = Group(one,two,four,eight,seven,five).arrange(buff=0.6)
        title_dub_3s = Group(three,six,three.copy(),six.copy(),three.copy(),six.copy()).arrange(buff=0.6)
        title_dub_9s = Group(nine.copy(),nine.copy(),nine.copy(),nine.copy(),nine.copy(),nine.copy()).arrange(buff=0.6)
        title.move_to(eisel).shift(UP*3)
        title_dub_2s.next_to(title,DOWN,buff=1)
        title_dub_3s.next_to(title_dub_2s,DOWN,buff=1)
        title_dub_9s.next_to(title_dub_3s,DOWN,buff=1)

#endregion
   
    # ADDITION SEQUENCE
    #region 
        self.wait()
        title = Tex(r"\text{Multiples \ / \ Addition}")
        title.move_to(eisel).shift(UP*3)
        self.play(FadeIn(title))

        title_add_1s = Group(
            one.copy(),two.copy(),three.copy(),
            four.copy(),five.copy(),six.copy(),
            seven.copy(),eight.copy(),nine.copy(),
        ).arrange(buff=0.4)

        title_add_2s = Group(
            two.copy(),four.copy(),six.copy(),
            eight.copy(),one.copy(),three.copy(),
            five.copy(),seven.copy(),nine.copy(),
        ).arrange(buff=0.4)
        
        title_add_3s = Group(
            three.copy(),six.copy(),nine.copy(),
            three.copy(),six.copy(),nine.copy(),
            three.copy(),six.copy(),nine.copy(),
        ).arrange(buff=0.4)

        title_add_4s = Group(
            four.copy(),eight.copy(),three.copy(),
            seven.copy(),two.copy(),six.copy(),
            one.copy(),five.copy(),nine.copy(),
        ).arrange(buff=0.4)
        
        title_add_5s = Group(
            five.copy(),one.copy(),six.copy(),
            two.copy(),seven.copy(),three.copy(),
            eight.copy(),four.copy(),nine.copy(),
        ).arrange(buff=0.4)

        title_add_6s = Group(
            six.copy(),three.copy(),nine.copy(),
            six.copy(),three.copy(),nine.copy(),
            six.copy(),three.copy(),nine.copy(),
        ).arrange(buff=0.4)

        title_add_7s = Group(
            seven.copy(),five.copy(),three.copy(),
            one.copy(),eight.copy(),six.copy(),
            four.copy(),two.copy(),nine.copy(),
        ).arrange(buff=0.4)

        title_add_8s = Group(
            eight.copy(),seven.copy(),six.copy(),
            five.copy(),four.copy(),three.copy(),
            two.copy(),one.copy(),nine.copy(),
        ).arrange(buff=0.4)

        title_add_9s = Group(
            nine.copy(),nine.copy(),nine.copy(),
            nine.copy(),nine.copy(),nine.copy(),
            nine.copy(),nine.copy(),nine.copy(),
        ).arrange(buff=0.4)
        
        title_add_group = Group(
            title_add_1s, title_add_2s, title_add_3s,
            title_add_4s, title_add_5s, title_add_6s,
            title_add_7s, title_add_8s, title_add_9s
        ).arrange(DOWN,buff=0.3).scale(0.8).next_to(title,DOWN,buff=1)
        table = Group(
            Line([-0.5,0,0],[5,0,0]),
            Line([0,0.5,0],[0,-5,0]),
            Tex(r"\times").move_to([-0.3,0.3,0])
        ).next_to(title, DOWN)
        run = title_add_1s.copy().set_color(WHITE)
        rise = Group(
            one.copy(),two.copy(),three.copy(),
            four.copy(),five.copy(),six.copy(),
            seven.copy(),eight.copy(),nine.copy(),
        ).arrange(DOWN, buff=0.304).scale(0.8).set_color(WHITE)
        run.next_to(table[2], RIGHT, buff = 0.45)
        rise.next_to(table[2], DOWN, buff = 0.45)
        
        self.wait()
        self.play(
            FadeIn(run),
            FadeIn(rise),
            FadeIn(table),
        )
        self.wait()

        adder = addition_sequence(9,1,0,2).shift(LEFT*3)
        for i in range(0,9):
            self.wait(0.1)
            self.play(
                ShowCreation(adder[i]),
                Indicate(dots[(i*1+1)%9]),
                Indicate(numbers[(i*1+1)%9]),
                FadeIn(title_add_1s[i])
            )
        self.play(FadeOut(adder))

        adder = addition_sequence(9,2,0,2).shift(LEFT*3)
        for i in range(0,9):
            self.wait(0.1)
            self.play(
                ShowCreation(adder[i]),
                Indicate(dots[(i*2+2)%9]),
                Indicate(numbers[(i*2+2)%9]),
                FadeIn(title_add_2s[i])
            )
        self.play(FadeOut(adder))

        adder = addition_sequence(9,3,0,2).shift(LEFT*3)
        for i in range(0,9):
            self.wait(0.1)
            self.play(
                ShowCreation(adder[i%3]),
                Indicate(dots[(i*3+3)%9]),
                Indicate(numbers[(i*3+3)%9]),
                FadeIn(title_add_3s[i])
            )
        self.play(FadeOut(adder))

        
        adder = addition_sequence(9,4,0,2).shift(LEFT*3)
        for i in range(0,9):
            self.wait(0.1)
            self.play(
                ShowCreation(adder[i]),
                Indicate(dots[(i*4+4)%9]),
                Indicate(numbers[(i*4+4)%9]),
                FadeIn(title_add_4s[i])
            )
        self.play(FadeOut(adder))


        adder = addition_sequence(9,5,0,2).shift(LEFT*3)
        for i in range(0,9):
            self.wait(0.1)
            self.play(
                ShowCreation(adder[i]),
                Indicate(dots[(i*5+5)%9]),
                Indicate(numbers[(i*5+5)%9]),
                FadeIn(title_add_5s[i])
            )
        self.play(FadeOut(adder))


        adder = addition_sequence(9,6,0,2).shift(LEFT*3)
        for i in range(0,9):
            self.wait(0.1)
            self.play(
                ShowCreation(adder[i%3]),
                Indicate(dots[(i*6+6)%9]),
                Indicate(numbers[(i*6+6)%9]),
                FadeIn(title_add_6s[i])
            )
        self.play(FadeOut(adder))


        adder = addition_sequence(9,7,0,2).shift(LEFT*3)
        for i in range(0,9):
            self.wait(0.1)
            self.play(
                ShowCreation(adder[i]),
                Indicate(dots[(i*7+7)%9]),
                Indicate(numbers[(i*7+7)%9]),
                FadeIn(title_add_7s[i])
            )
        self.play(FadeOut(adder))


        adder = addition_sequence(9,8,0,2).shift(LEFT*3)
        for i in range(0,9):
            self.wait(0.1)
            self.play(
                ShowCreation(adder[i]),
                Indicate(dots[(i*8+8)%9]),
                Indicate(numbers[(i*8+8)%9]),
                FadeIn(title_add_8s[i])
            )
        self.play(FadeOut(adder))

        for i in range(0,9):
            self.wait(0.1)
            self.play(
                Indicate(dots[0]),
                Indicate(numbers[0]),
                FadeIn(title_add_9s[i])
            )
        box_1 = Rectangle(
            width = title_add_1s.get_width()+0.2,
            height = title_add_1s.get_height()+0.2,
            color = YELLOW
        ).move_to(title_add_1s)
        box_8 = Rectangle(
            width = title_add_8s.get_width()+0.2,
            height = title_add_8s.get_height()+0.2,
            color = YELLOW
        ).move_to(title_add_8s)
        self.wait()
        self.play(
            FadeIn(box_1),
            FadeIn(box_8),
        )
        self.wait(2)
        numbers_27 = vbm_numbers(7,9,1,2.5).shift(LEFT*3)
        self.play(
            Uncreate(numbers),
        )
        self.play(
            box_1.animate.move_to(title_add_2s),
            box_8.animate.move_to(title_add_7s),
        )
        self.play(
            ShowCreation(numbers_27),
        )
        self.wait(2)
        numbers_45 = vbm_numbers(4,9,1,2.5).shift(LEFT*3)
        self.play(
            Uncreate(numbers_27),
        )
        self.play(
            box_1.animate.move_to(title_add_4s),
            box_8.animate.move_to(title_add_5s),
        )
        self.play(
            ShowCreation(numbers_45),
        )
        self.wait(2)
        vbm_45 = Group(numbers_45, circle, dots)
        self.play(
            FadeOut(title),
            FadeOut(title_add_group),
            FadeOut(run),
            FadeOut(rise),
            FadeOut(table),
            FadeOut(box_1),
            FadeOut(box_8),
            FadeOut(eisel),
            vbm_45.animate.scale(0.7).shift(RIGHT*3)
        )
        numbers_18 = vbm_numbers(1,9,1,2.5)
        circle_18 = Circle().scale(2).set_color(WHITE)
        dots_18 = vbm_dots(1,9,1,2)
        vbm_18 = Group(numbers_18, circle_18, dots_18).scale(0.7).shift(LEFT*4.5)

        numbers_27 = vbm_numbers(7,9,1,2.5)
        circle_27 = Circle().scale(2).set_color(WHITE)
        dots_27 = vbm_dots(1,9,1,2)
        vbm_27 = Group(numbers_27, circle_27, dots_27).scale(0.7).shift(RIGHT*4.5)

        counting_title = Tex(r"\textsc{Unique Counting Circles}").scale(1.5)
        self.wait()
        self.play(FadeIn(counting_title.next_to(TOP,DOWN, buff=0.4)))
        self.wait()
        self.play(
            FadeIn(vbm_18),
            FadeIn(vbm_27),
        )

        label_18 = Tex(r"(1,8)").next_to(vbm_18, DOWN, buff=0.8)
        label_27 = Tex(r"(7,2)").next_to(vbm_27, DOWN, buff=0.8)
        label_45 = Tex(r"(4,5)").next_to(vbm_45, DOWN, buff=0.8)
        doubling_18 = doubling_sequence(9,2,1,2).scale(0.7).shift(LEFT*4.5).shift(UP*0.1)
        doubling_27 = doubling_sequence(9,2,1,2).scale(0.7).shift(RIGHT*4.5).shift(UP*0.1)
        doubling_45 = doubling_sequence(9,2,1,2).scale(0.7).shift(UP*0.1)

        self.wait()
        self.play(
            FadeIn(doubling_18),
            FadeIn(doubling_27),
            FadeIn(doubling_45),
        )
        self.wait()
        self.play(
            FadeIn(label_18)
        )
        self.wait()
        self.play(
            FadeIn(label_45),
        )
        self.wait()
        self.play(
            FadeIn(label_27)
        )
        self.wait()




#endregion

    # EXPONENTIALS SEQUENCE
    #region
        self.play(
            FadeOut(label_18),
            FadeOut(label_27),
            FadeOut(label_45),
            FadeOut(counting_title),
            FadeOut(vbm_18),
            FadeOut(vbm_27),
            FadeOut(doubling_18),
            FadeOut(doubling_27),
            FadeOut(doubling_45),
        )
        self.play(
            vbm_45.animate.scale(1/0.7).shift(LEFT*3),
            FadeIn(eisel),
        )
        self.wait()
        self.play(
            Uncreate(numbers_45)
        )
        numbers = vbm_numbers(1,9,1,2.5).shift(LEFT*3)
        self.play(
            ShowCreation(numbers)
        )
        self.wait()
        title = Tex(r"\text{Exponentials}")
        title.move_to(eisel).shift(UP*3)
        self.play(FadeIn(title))
        exp_group = Group()
        for i in range(1,9):
            label = Tex(str(i) + r"^{n}:")
            exp_group.add(label)
        exp_group.arrange(DOWN,buff=0.4).next_to(title,DL,buff=0.5)
        


        iso = ["1","2","3","4","8","7","5","6","9",r"\bar{9}"]
        two_n = Tex(r"\left(1,2,4,8,7,5\right)",isolate=iso).scale(0.6)
        two_3n = Tex(r"\left(3,6\right)",isolate=iso).scale(0.6)
        three_1n = Tex(r"\left(1,3,\bar{9}\right)",isolate=iso).scale(0.6)
        three_2n = Tex(r"\left(2,6,\bar{9}\right)",isolate=iso).scale(0.6)
        three_4n = Tex(r"\left(4,3,\bar{9}\right)",isolate=iso).scale(0.6)
        three_5n = Tex(r"\left(5,6,\bar{9}\right)",isolate=iso).scale(0.6)
        three_7n = Tex(r"\left(7,3,\bar{9}\right)",isolate=iso).scale(0.6)
        three_8n = Tex(r"\left(8,6,\bar{9}\right)",isolate=iso).scale(0.6)
        three_39n = Tex(r"\left(3,\bar{9}\right)",isolate=iso).scale(0.6)
        three_69n = Tex(r"\left(6,\bar{9}\right)",isolate=iso).scale(0.6)
        three_9n = Tex(r"\left(9\right)",isolate=iso).scale(0.6)

        def exponentials(mult):
            exp = Group()
            for i in range(0,9):
                exp.add(doubling_sequence(9,mult,i,2))
            return exp
        def set_parts(tex_obj):
            colors = [GREEN,RED,BLUE]
            for i in range(0,10):
                tex_obj.select_parts(str(i)).set_color(colors[i%3])
            return tex_obj

        expo2 = exponentials(2).shift(LEFT*3)
        expo3 = exponentials(3).shift(LEFT*3)
        expo4 = exponentials(4).shift(LEFT*3)
        expo5 = exponentials(5).shift(LEFT*3)
        expo6 = exponentials(6).shift(LEFT*3)
        expo7 = exponentials(7).shift(LEFT*3)
        expo8 = exponentials(8).shift(LEFT*3)
        twos = Group(
            set_parts(two_n),
            set_parts(two_3n)
        ).arrange().next_to(exp_group[1],RIGHT)
        threes_up = Group(
            set_parts(three_1n),
            set_parts(three_7n),
            set_parts(three_4n),
            set_parts(three_39n)
        ).arrange()
        threes_down = Group(
            set_parts(three_8n),
            set_parts(three_2n),
            set_parts(three_5n),
            set_parts(three_69n)
        ).arrange()
        threes = Group(threes_up,threes_down).arrange(DOWN,buff=0.1)
        threes.next_to(exp_group[2],RIGHT)
        set_parts(three_9n)
        three_9n.next_to(threes,RIGHT)

        loop_one = Tex(r"\left(1\right)").scale(0.6)
        loop_two = Tex(r"\left(2\right)").scale(0.6)
        loop_three = Tex(r"\left(3\right)").scale(0.6)
        loop_four = Tex(r"\left(4\right)").scale(0.6)
        loop_five = Tex(r"\left(5\right)").scale(0.6)
        loop_six = Tex(r"\left(6\right)").scale(0.6)
        loop_seven = Tex(r"\left(7\right)").scale(0.6)
        loop_eight = Tex(r"\left(8\right)").scale(0.6)
        loop_nine = Tex(r"\left(9\right)").scale(0.6)
        loops = Group(
            set_parts(loop_one),
            set_parts(loop_two),
            set_parts(loop_three),
            set_parts(loop_four),
            set_parts(loop_five),
            set_parts(loop_six),
            set_parts(loop_seven),
            set_parts(loop_eight),
            set_parts(loop_nine)
        ).arrange(buff=0.2)
        loops.next_to(exp_group[0])
#ONES
        self.play(FadeIn(exp_group))
        self.play(
            Indicate(dots[1]),
            Indicate(numbers[1]),
            FadeIn(loops[0])
        )
        self.wait()
        self.play(
            Indicate(dots[2]),
            Indicate(numbers[2]),
            FadeIn(loops[1])
        )
        self.wait()
        self.play(
            Indicate(dots[3]),
            Indicate(numbers[3]),
            FadeIn(loops[2])
        )
        self.wait()
        self.play(
            Indicate(dots[4]),
            Indicate(numbers[4]),
            FadeIn(loops[3])
        )
        self.wait()
        self.play(
            Indicate(dots[5]),
            Indicate(numbers[5]),
            FadeIn(loops[4])
        )
        self.wait()
        self.play(
            Indicate(dots[6]),
            Indicate(numbers[6]),
            FadeIn(loops[5])
        )
        self.wait()
        self.play(
            Indicate(dots[7]),
            Indicate(numbers[7]),
            FadeIn(loops[6])
        )
        self.wait()
        self.play(
            Indicate(dots[8]),
            Indicate(numbers[8]),
            FadeIn(loops[7])
        )
        self.wait()
        self.play(
            Indicate(dots[0]),
            Indicate(numbers[0]),
            FadeIn(loops[8])
        )
        self.wait()
#TWOS
        
        self.wait(0.1)
        self.play(
            ShowCreation(expo2[1]),
            FadeIn(twos[0])
        )
        self.wait()
        self.play(FadeOut(expo2[1]))
        self.wait()
        self.play(
            ShowCreation(expo2[3]),
            FadeIn(twos[1])
        )
        self.wait()
        self.play(FadeOut(expo2[3]))
        self.wait()

#THREES
        self.play(
            ShowCreation(expo3[1]),
            ShowCreation(expo3[8]),
            FadeIn(threes[0][0]),
            FadeIn(threes[1][0])
        )
        self.wait()
        self.play(FadeOut(expo3[1]),FadeOut(expo3[8]))
        self.wait()
        self.play(
            ShowCreation(expo3[2]),
            ShowCreation(expo3[7]),
            FadeIn(threes[0][1]),
            FadeIn(threes[1][1])
        )
        self.wait()
        self.play(FadeOut(expo3[2]),FadeOut(expo3[7]))
        self.wait()
        self.play(
            ShowCreation(expo3[4]),
            ShowCreation(expo3[5]),
            FadeIn(threes[0][2]),
            FadeIn(threes[1][2])
        )
        self.wait()
        self.play(FadeOut(expo3[4]),FadeOut(expo3[5]))
        self.wait()
        self.play(
            ShowCreation(expo3[3]),
            ShowCreation(expo3[6]),
            FadeIn(threes[0][3]),
            FadeIn(threes[1][3])
        )

        self.wait()
        self.play(
            FadeIn(expo3[1]),
            FadeIn(expo3[2]),
            FadeIn(expo3[4]),
            FadeIn(expo3[5]),
            FadeIn(expo3[7]),
            FadeIn(expo3[8]),
        )
        self.wait()
        self.play(FadeIn(three_9n))

        self.wait()
        self.play(
            FadeOut(expo3[1]),
            FadeOut(expo3[2]),
            FadeOut(expo3[4]),
            FadeOut(expo3[5]),
            FadeOut(expo3[7]),
            FadeOut(expo3[8]),
            FadeOut(expo3[3]),
            FadeOut(expo3[6])
        )
#FOURS
        fours_1n = Tex(r"\left(1,4,7\right)",isolate=iso).scale(0.6)
        fours_2n = Tex(r"\left(2,8,5\right)",isolate=iso).scale(0.6)
        fours_3n = Tex(r"\left(3\right)",isolate=iso).scale(0.6)
        fours_6n = Tex(r"\left(6\right)",isolate=iso).scale(0.6)
        fours_9n = Tex(r"\left(9\right)",isolate=iso).scale(0.6)
        fours = Group(
            set_parts(fours_1n),
            set_parts(fours_2n),
            set_parts(fours_3n),
            set_parts(fours_6n),
            set_parts(fours_9n),
        ).arrange()
        fours.next_to(exp_group[3],RIGHT)

        self.wait()
        self.play(
            ShowCreation(expo4[1]),
            FadeIn(fours[0])
        )
        self.play(FadeOut(expo4[1]))
        self.wait()

        self.wait()
        self.play(
            ShowCreation(expo4[2]),
            FadeIn(fours[1])
        )
        self.play(FadeOut(expo4[2]))

        self.wait()
        self.play(
            Indicate(dots[3]),
            Indicate(dots[6]),
            Indicate(dots[0]),
            FadeIn(fours[2]),
            FadeIn(fours[3]),
            FadeIn(fours[4]),
        )
        self.wait()
#FIVES
        fives_2n = Tex(r"\left(1,5,7,8,4,2\right)",isolate=iso).scale(0.6)
        fives_6n = Tex(r"\left(6,3\right)",isolate=iso).scale(0.6)
        fives_9n = Tex(r"\left(9\right)",isolate=iso).scale(0.6)
        fives = Group(
            set_parts(fives_2n),
            set_parts(fives_6n),
            set_parts(fives_9n),
        ).arrange()
        fives.next_to(exp_group[4],RIGHT)

        self.wait(0.1)
        self.play(
            ShowCreation(expo5[1]),
            FadeIn(fives[0])
        )
        self.wait()
        self.play(FadeOut(expo5[1]))
        self.wait()
        self.play(
            ShowCreation(expo5[6]),
            FadeIn(fives[1])
        )
        self.wait()
        self.play(FadeOut(expo5[6]))

        self.wait()
        self.play(
            Indicate(dots[0]),
            FadeIn(fives[2])
        )
        self.wait()
# SIXES

        six_1n = Tex(r"\left(1,6,\bar{9}\right)",isolate=iso).scale(0.6)
        six_2n = Tex(r"\left(2,3,\bar{9}\right)",isolate=iso).scale(0.6)
        six_4n = Tex(r"\left(4,6,\bar{9}\right)",isolate=iso).scale(0.6)
        six_5n = Tex(r"\left(5,3,\bar{9}\right)",isolate=iso).scale(0.6)
        six_7n = Tex(r"\left(7,6,\bar{9}\right)",isolate=iso).scale(0.6)
        six_8n = Tex(r"\left(8,3,\bar{9}\right)",isolate=iso).scale(0.6)
        six_39n = Tex(r"\left(6,\bar{9}\right)",isolate=iso).scale(0.6)
        six_69n = Tex(r"\left(3,\bar{9}\right)",isolate=iso).scale(0.6)
        six_9n = Tex(r"\left(9\right)",isolate=iso).scale(0.6)

        sixes_up = Group(
            set_parts(six_1n),
            set_parts(six_7n),
            set_parts(six_4n),
            set_parts(six_39n)
        ).arrange()
        sixes_down = Group(
            set_parts(six_8n),
            set_parts(six_2n),
            set_parts(six_5n),
            set_parts(six_69n)
        ).arrange()
        sixes = Group(sixes_up,sixes_down).arrange(DOWN,buff=0.1)
        sixes.next_to(exp_group[5],RIGHT)
        set_parts(six_9n)
        six_9n.next_to(sixes,RIGHT)
        
        self.wait(0.1)
        self.play(
            ShowCreation(expo6[1]),
            ShowCreation(expo6[8]),
            FadeIn(sixes[0][0]),
            FadeIn(sixes[1][0])
        )
        self.wait()
        self.play(FadeOut(expo6[1]),FadeOut(expo6[8]))
        self.wait()
        self.play(
            ShowCreation(expo6[2]),
            ShowCreation(expo6[7]),
            FadeIn(sixes[0][1]),
            FadeIn(sixes[1][1])
        )
        self.wait()
        self.play(FadeOut(expo6[2]),FadeOut(expo6[7]))
        self.wait()
        self.play(
            ShowCreation(expo6[4]),
            ShowCreation(expo6[5]),
            FadeIn(sixes[0][2]),
            FadeIn(sixes[1][2])
        )
        self.wait()
        self.play(FadeOut(expo6[4]),FadeOut(expo6[5]))
        self.wait()
        self.play(
            ShowCreation(expo6[3]),
            ShowCreation(expo6[6]),
            FadeIn(sixes[0][3]),
            FadeIn(sixes[1][3])
        )

        self.wait()
        self.play(
            FadeIn(expo6[1]),
            FadeIn(expo6[2]),
            FadeIn(expo6[4]),
            FadeIn(expo6[5]),
            FadeIn(expo6[7]),
            FadeIn(expo6[8]),
        )
        
        self.wait()
        self.play(
            FadeOut(expo6[1]),
            FadeOut(expo6[2]),
            FadeOut(expo6[4]),
            FadeOut(expo6[5]),
            FadeOut(expo6[7]),
            FadeOut(expo6[8]),
            FadeOut(expo6[3]),
            FadeOut(expo6[6])
        )
        self.wait()
        self.play(
            Indicate(dots[0]),
            FadeIn(six_9n)
        )

#SEVENS
        sevens_1n = Tex(r"\left(1,7,4\right)",isolate=iso).scale(0.6)
        sevens_2n = Tex(r"\left(2,5,8\right)",isolate=iso).scale(0.6)
        sevens_3n = Tex(r"\left(6\right)",isolate=iso).scale(0.6)
        sevens_6n = Tex(r"\left(3\right)",isolate=iso).scale(0.6)
        sevens_9n = Tex(r"\left(9\right)",isolate=iso).scale(0.6)
        sevens = Group(
            set_parts(sevens_1n),
            set_parts(sevens_2n),
            set_parts(sevens_3n),
            set_parts(sevens_6n),
            set_parts(sevens_9n),
        ).arrange()
        sevens.next_to(exp_group[6],RIGHT)

        self.wait()
        self.play(
            ShowCreation(expo7[1]),
            FadeIn(sevens[0])
        )
        self.play(FadeOut(expo7[1]))
        self.wait()

        self.wait()
        self.play(
            ShowCreation(expo7[2]),
            FadeIn(sevens[1])
        )
        self.play(FadeOut(expo7[2]))

        self.wait()
        self.play(
            Indicate(dots[3]),
            Indicate(dots[6]),
            Indicate(dots[0]),
            FadeIn(sevens[2]),
            FadeIn(sevens[3]),
            FadeIn(sevens[4]),
        )
        self.wait()

#EIGHTS
        eight_1n = Tex(r"\left(1,8\right)",isolate=iso).scale(0.6)
        eight_2n = Tex(r"\left(7,2\right)",isolate=iso).scale(0.6)
        eight_4n = Tex(r"\left(4,5\right)",isolate=iso).scale(0.6)
        eight_3n = Tex(r"\left(3,6\right)",isolate=iso).scale(0.6)
        eight_9n = Tex(r"\left(9\right)",isolate=iso).scale(0.6)

        eights = Group(
            set_parts(eight_1n),
            set_parts(eight_2n),
            set_parts(eight_4n),
            set_parts(eight_3n),
            set_parts(eight_9n),
        ).arrange()
        eights.next_to(exp_group[7],RIGHT)
        
        self.wait(0.1)
        self.play(
            ShowCreation(expo8[1]),
            FadeIn(eights[0]),
        )
        self.wait()
        self.play(FadeOut(expo8[1]))
        self.wait()
        self.play(
            ShowCreation(expo8[2]),
            FadeIn(eights[1]),
        )
        self.wait()
        self.play(FadeOut(expo8[2]))
        self.wait()

        self.play(
            ShowCreation(expo8[4]),
            FadeIn(eights[2]),
        )
        self.wait()
        self.play(FadeOut(expo8[4]))

        self.wait()
        self.play(
            ShowCreation(expo8[3]),
            FadeIn(eights[3]),
        )
        self.wait()
        self.play(FadeOut(expo8[3]))

        self.wait()
        self.play(
            FadeIn(expo8[1]),
            FadeIn(expo8[2]),
            FadeIn(expo8[4]),
            FadeIn(expo8[3]),
        )
        
        self.wait()
        self.play(
            FadeOut(expo8[1]),
            FadeOut(expo8[2]),
            FadeOut(expo8[4]),
            FadeOut(expo8[3]),
        )
        self.wait()
        self.play(
            Indicate(dots[0]),
            FadeIn(eight_9n)
        )
#endregion

class SymbolSummary(Scene):
    def construct(self):
        frame = self.camera.frame
        
        numbers = vbm_numbers(1,9,1.2,2.5)
        circle = Circle().scale(2).set_color(WHITE)
        dots = vbm_dots(1,9,1,2)
        vbm_group = Group(dots, circle, numbers)

        neg_numbers = vbm_numbers(1,9,1.2,2.5).set_color(WHITE)
        neg_circle = Circle().scale(2).set_color(WHITE)
        neg_dots = vbm_dots(1,9,1,2).set_color(WHITE)
        neg_vbm_group = Group(neg_dots, neg_circle, neg_numbers)

        left_shift = 3.2
        title = Tex(r"\textsc{Polarity of Space}").scale(1.5).next_to(TOP, DOWN)
        self.add(vbm_group)
        self.wait()
        self.play(
            FadeIn(title),
        )
        self.wait()
        self.add(neg_vbm_group)
        self.play(
            vbm_group.animate.shift(LEFT*left_shift),
            neg_vbm_group.animate.shift(RIGHT*left_shift),
            run_time = 2,
        )
        self.wait()
        pos_pols = number_polarities_pos(numbers, 0.7).set_color(WHITE)
        neg_pols = number_polarities_neg(neg_numbers, 0.7)
        self.play(
            FadeIn(pos_pols),
            FadeIn(neg_pols),
        )
        self.wait()
        space_label = Tex(r"\text{Space}").next_to(circle, DOWN, buff=1.1)
        counterspace_label = Tex(r"\text{Counter-Space}").next_to(neg_circle, DOWN, buff=1.1)
        self.play(
            FadeIn(space_label),
        )
        self.wait()
        self.play(
            FadeIn(counterspace_label),
        )
        self.wait()
        self.play(
            FadeOut(pos_pols),
            FadeOut(neg_pols),
        )
        self.wait()
        symbol_pols = symbol_polarities_pos(numbers, 0.7).set_color(WHITE)
        neg_symbol_pols = symbol_polarities_neg(neg_numbers, 0.7)
        self.play(
            FadeIn(symbol_pols),
            FadeIn(neg_symbol_pols),
        )
        pos_space_label = Tex(r"\bullet").next_to(circle, UR)
        neg_space_label = Tex(r"\circ").next_to(neg_circle, UR)
        self.wait()
        self.play(
            FadeOut(symbol_pols),
            FadeOut(neg_symbol_pols),
            FadeIn(pos_space_label),
            FadeIn(neg_space_label),
        )
        self.wait()
        self.play(
            FadeOut(pos_space_label),
            FadeOut(neg_space_label),
        )
        self.wait()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait()

class ModularArithmetic(Scene):
    def construct(self):
        frame = self.camera.frame
        title = Tex(r"\textsc{Modular Arithmetic}").scale(1.5).shift(UP*3)
        wrap_around = Tex(r"\text{Numbers ``wrap around'' in a loop}").next_to(title, DOWN, buff=0.5)
        self.add(title)
        self.wait()
        self.play(
            FadeIn(wrap_around)
        )
        def vbm_dashes(mult, divisions,dot_scale,radius,dash_length):
            dash_group = Group()
            for i in range(0,divisions):
                dash = Line(
                    np.array([
                        radius*np.sin(TAU * (i/divisions)),
                        radius*np.cos(TAU * (i/divisions)),
                        0
                    ]),
                    np.array([
                        (radius*dash_length)*np.sin(TAU * (i/divisions)),
                        (radius*dash_length)*np.cos(TAU * (i/divisions)),
                        0
                    ]),
                )
                dash_group.add(dash)
            return dash_group

        divs = 12
        hour = ValueTracker(1)
        minute = ValueTracker()
        hour_hand = Line(
            np.array([0,0,0]),
            np.array([
                (1.2)*np.sin(TAU * (hour.get_value()/divs)),
                (1.2)*np.cos(TAU * (hour.get_value()/divs)),
                0
            ]),
        )
        minute_hand = Line(
            np.array([0,0,0]),
            np.array([
                (1.6)*np.sin(TAU * (minute.get_value()/divs)),
                (1.6)*np.cos(TAU * (minute.get_value()/divs)),
                0
            ]),
        )
        numbers = vbm_numbers(1,12,1,2.4).set_color(WHITE)
        circle = Circle().scale(2).set_color(WHITE)
        dashes = vbm_dashes(1,12,1,2,0.86).set_color(WHITE)
        vbm_group = Group(numbers, circle, dashes, hour_hand, minute_hand).shift(DOWN)
        vbm_group.scale(0.9)


        self.wait()
        self.play(
            FadeIn(circle)
        )
        self.wait()
        self.play(
            FadeIn(numbers),
            FadeIn(dashes),
            FadeIn(hour_hand),
            FadeIn(minute_hand),
        )
        self.wait()
        self.play(
            vbm_group.animate.shift(LEFT*2)
        )
        time_tex = Tex(r"\text{Time: 1:00}")
        hour_tex = Tex(r"\text{Hours: 1 hour}")
        time_hour = Group(time_tex, hour_tex).arrange(DOWN, buff=0.5).shift(RIGHT*2.5+DOWN)
        self.wait()
        self.play(
            FadeIn(time_hour)
        )
        self.wait()
        
        for i in range(1,28):
            if i%12 == 0:
                self.remove(time_hour)
                self.remove(hour_hand)
                hour.set_value(i)
                time_tex = Tex(r"\text{Time: "+str(12)+r":00}")
                hour_tex = Tex(r"\text{Hours: "+str(i)+r"}")
                time_hour = Group(time_tex, hour_tex).arrange(DOWN, buff=0.5).shift(RIGHT*2.5+DOWN)
                hour_hand = Line(
                    np.array([0,0,0]),
                    np.array([
                        (1.2*0.9)*np.sin(TAU * (hour.get_value()/divs)),
                        (1.2*0.9)*np.cos(TAU * (hour.get_value()/divs)),
                        0
                    ]),
                ).shift(LEFT*2+DOWN)
                self.add(hour_hand)
                self.add(time_hour)
                self.wait(0.5)  
            else:
                self.remove(time_hour)
                self.remove(hour_hand)
                hour.set_value(i)
                time_tex = Tex(r"\text{Time: "+str(i%12)+r":00}")
                hour_tex = Tex(r"\text{Hours: "+str(i)+r"}")
                time_hour = Group(time_tex, hour_tex).arrange(DOWN, buff=0.5).shift(RIGHT*2.5+DOWN)
                hour_hand = Line(
                    np.array([0,0,0]),
                    np.array([
                        (1.2*0.9)*np.sin(TAU * (hour.get_value()/divs)),
                        (1.2*0.9)*np.cos(TAU * (hour.get_value()/divs)),
                        0
                    ]),
                ).shift(LEFT*2+DOWN)
                self.add(hour_hand)
                self.add(time_hour)
                self.wait(0.5)  

        self.wait()
        self.play(
            time_hour.animate.shift(UP*0.7)
        )
        self.wait()
        mod_example = Tex(r"27(\textup{mod}\; 12)=3").next_to(time_hour, DOWN, buff=0.7)
        self.play(
            FadeIn(mod_example)
        )
        self.wait()
        self.play(
            FadeOut(hour_tex),
            FadeOut(mod_example),
        )
        self.wait()
        minute_tex = Tex(r"\text{Minutes: 0}")
        minute_hour = Group(time_tex, minute_tex).arrange(DOWN,buff=0.5).shift(RIGHT*2.5+DOWN)
        minute_hour.shift(UP*0.7)       
        mod_mins = Tex(r"0 (\textup{mod}\; 60)= 0").next_to(minute_hour,DOWN,buff=0.7)
        minute_dashes = vbm_dashes(1,60,1,2,0.92).scale(0.9).shift(LEFT*2+DOWN)
        self.play(
            FadeIn(minute_dashes),
            FadeIn(minute_tex),
            FadeIn(mod_mins),
        )
        self.wait()

        divs = 60
        for i in range(1,24):
            self.remove(minute_tex)
            self.remove(mod_mins)
            self.remove(minute_hand)
            self.remove(time_tex)
            minute.set_value(i)
            time_tex = Tex(r"\text{Time: 2:}"+'%02d'%((60-i)%60))
            minute_tex = Tex(r"\text{Minutes: -}"+str(i))
            mod_mins = Tex(r"-"+str(i)+r"(\textup{mod}\; 60)="+str((60-i)%60)).next_to(minute_hour,DOWN,buff=0.7)
            minute_hour = Group(time_tex, minute_tex).arrange(DOWN,buff=0.5).shift(RIGHT*2.5+DOWN)
            minute_hour.shift(UP*0.7)
            minute_hand = Line(
                np.array([0,0,0]),
                np.array([
                    (1.6*0.9)*np.sin(-TAU * (minute.get_value()/divs)),
                    (1.6*0.9)*np.cos(-TAU * (minute.get_value()/divs)),
                    0
                ]),
            ).shift(LEFT*2+DOWN)
            self.add(minute_hand)
            self.add(minute_tex)
            self.add(mod_mins)
            self.add(time_tex)
            self.wait(0.3)  
        
        self.wait()

class DigitalRoot(Scene):
    def construct(self):
        frame = self.camera.frame
        title = Tex(r"\textsc{Modular Arithmetic}").scale(1.5).shift(UP*3)
        wrap_around = Tex(r"\text{Mod 9 and Digital Roots}").next_to(title, DOWN, buff=0.5)
        self.add(title)
        self.wait()
        self.play(
            FadeIn(wrap_around)
        )
        def vbm_dashes(mult, divisions,dot_scale,radius,dash_length):
            dash_group = Group()
            for i in range(0,divisions):
                dash = Line(
                    np.array([
                        radius*np.sin(TAU * (i/divisions)),
                        radius*np.cos(TAU * (i/divisions)),
                        0
                    ]),
                    np.array([
                        (radius*dash_length)*np.sin(TAU * (i/divisions)),
                        (radius*dash_length)*np.cos(TAU * (i/divisions)),
                        0
                    ]),
                )
                dash_group.add(dash)
            return dash_group

        divs = 9
        hour = ValueTracker(0)
        minute = ValueTracker()
        hour_hand = Line(
            np.array([0,0,0]),
            np.array([
                (1.2)*np.sin(TAU * (hour.get_value()/divs)),
                (1.2)*np.cos(TAU * (hour.get_value()/divs)),
                0
            ]),
        ).set_opacity(0)
        minute_hand = Line(
            np.array([0,0,0]),
            np.array([
                (2)*np.sin(TAU * (minute.get_value()/divs)),
                (2)*np.cos(TAU * (minute.get_value()/divs)),
                0
            ]),
        ).set_opacity(0)
        numbers = vbm_numbers(1,9,1,2.4).set_color(WHITE)
        circle = Circle().scale(2).set_color(WHITE)
        dots = vbm_dots(1,9,1,2).set_color(WHITE)
        vbm_group = Group(numbers, circle, dots, hour_hand, minute_hand).shift(DOWN+2.5*LEFT)
        vbm_group.scale(0.9)
        self.play(
            FadeIn(circle),
            FadeIn(dots),
            FadeIn(numbers),
        )
        mod_example = Tex(r"145(\textup{mod}9)=1").shift(RIGHT*3+UP*0.7)
        frac_example = Tex(r"\frac{144}{9}=16\;r1").next_to(mod_example,DOWN,buff=0.5)
        digi_example = Tex(r"145\rightarrow 1+4+5 = 10").next_to(frac_example,DOWN,buff=0.5)
        digi_answer = Tex(r"10\rightarrow 1+0=1").next_to(digi_example,DOWN,buff=0.3)
        self.wait()
        self.play(
            FadeIn(mod_example)
        )
        self.wait()
        self.play(
            FadeIn(frac_example)
        )
        self.wait()
        self.play(
            FadeIn(digi_example)
        )
        self.wait()
        self.play(
            FadeIn(digi_answer)
        )
        self.wait()
        self.play(
            FadeOut(mod_example),
            FadeOut(frac_example),
            FadeOut(digi_example),
            FadeOut(digi_answer),
        )
        self.wait()
        big_example = Tex(r"7,492,374(\textup{mod}9)").shift(RIGHT*3+UP*0.7)
        big_answer1 = Tex(r"7"+r"+4"+r"+9"+r"+2"+r"+3"+r"+7"+r"+4"+r"=36").next_to(big_example,DOWN,buff=1)
        big_answer2 = Tex(r"3+6=9").next_to(big_answer1,DOWN,buff=0.5)
        self.play(
            FadeIn(big_example),
        )
        self.wait()
        self.play(
            FadeIn(big_answer1),
            vbm_group.animate.shift(LEFT*1)
        )
        self.wait()
        self.play(
            FadeIn(big_answer2),
        )
        self.wait()
        self.play(
            FadeOut(big_answer2),
        )


        curve_function_pos = lambda u: np.array([(2*0.9)*np.sin(u),(2*0.9)*np.cos(u),0])
        curve_function_neg = lambda u: np.array([-(2*0.9)*np.sin(u),(2*0.9)*np.cos(u),0])

        angle_start = ValueTracker(0)
        angle = ValueTracker(0)

        circle_dot = always_redraw(lambda: Dot().scale(1.5).set_color(YELLOW).move_to(
            np.array([(2*0.9)*np.sin(angle.get_value()), (2*0.9)*np.cos(angle.get_value()), 0])
        ).shift(DOWN+LEFT*3.5))
        arc_pos = always_redraw(lambda: ParametricCurve(
            curve_function_pos,
            color = YELLOW,
            t_range = np.array([angle_start.get_value(), angle.get_value(), 0.01])
        ).shift(DOWN+LEFT*3.5))

        big_answer_copy = Tex(r"7"+r"+4"+r"+9"+r"+2"+r"+3"+r"+7"+r"+4"+r"=36").next_to(big_answer1,DOWN,buff=0.5)
        
        self.wait()
        self.play(
            minute_hand.animate.set_opacity(1),
            FadeIn(circle_dot),
            FadeIn(arc_pos),
            FadeIn(big_answer_copy)
        )
        self.wait()
        minute_hand.add_updater(lambda m: m.become(
            Line(
                np.array([0,0,0]),
                np.array([
                    (2*0.9)*np.sin(TAU * (minute.get_value()/divs)),
                    (2*0.9)*np.cos(TAU * (minute.get_value()/divs)),
                    0
                ]),
            ).shift(DOWN+LEFT*3.5)
        ))
        arrow_big = Arrow([0,0,0],[0,-1,0]).next_to(big_answer1[0],UP).set_color(YELLOW)

        self.play(
            angle.animate.set_value(TAU*(7/9)),
            minute.animate.set_value(7),
            big_answer_copy[0].animate.set_color(YELLOW),
            FadeIn(arrow_big),
        )
        self.play(
            angle_start.animate.set_value(TAU*(7/9))
        )
        self.wait()
        

        big_answer3 = Tex(r"2"+r"+9"+r"+2"+r"+3"+r"+7"+r"+4"+r"=27").next_to(big_answer1,DOWN,buff=0.5)
        big_answer3[0].set_color(YELLOW)
        self.play(
            ReplacementTransform(big_answer_copy,big_answer3),
            angle.animate.set_value(TAU+TAU*(2/9)),
            minute.animate.set_value(9+2),
            arrow_big.animate.next_to(big_answer1[2],UP)
        )
        self.play(
            angle_start.animate.set_value(TAU+TAU*(2/9))
        )
        self.wait()

        big_answer4 = Tex(r"2"+r"+2"+r"+3"+r"+7"+r"+4"+r"=18").next_to(big_answer1,DOWN,buff=0.5)
        big_answer4[0].set_color(YELLOW)
        self.play(
            ReplacementTransform(big_answer3,big_answer4),
            arrow_big.animate.next_to(big_answer1[4],UP)
        )
        self.wait()

        big_answer5 = Tex(r"4"+r"+3"+r"+7"+r"+4"+r"=18").next_to(big_answer1,DOWN,buff=0.5)
        big_answer5[0].set_color(YELLOW)
        self.play(
            ReplacementTransform(big_answer4,big_answer5),
            angle.animate.set_value(TAU+TAU*(4/9)),
            minute.animate.set_value(9+4),
            arrow_big.animate.next_to(big_answer1[6],UP)
        )
        self.play(
            angle_start.animate.set_value(TAU+TAU*(4/9))
        )
        self.wait()

        big_answer6 = Tex(r"7"+r"+7"+r"+4"+r"=18").next_to(big_answer1,DOWN,buff=0.5)
        big_answer6[0].set_color(YELLOW)
        self.play(
            ReplacementTransform(big_answer5,big_answer6),
            angle.animate.set_value(TAU+TAU*(7/9)),
            minute.animate.set_value(9+7),
            arrow_big.animate.next_to(big_answer1[8],UP)
        )
        self.play(
            angle_start.animate.set_value(TAU+TAU*(7/9))
        )
        self.wait()

        big_answer7 = Tex(r"5"+r"+4"+r"=9").next_to(big_answer1,DOWN,buff=0.5)
        big_answer7[0].set_color(YELLOW)
        self.play(
            ReplacementTransform(big_answer6,big_answer7),
            angle.animate.set_value(TAU+TAU+TAU*(5/9)),
            minute.animate.set_value(18+5),
            arrow_big.animate.next_to(big_answer1[10],UP)
        )
        self.play(
            angle_start.animate.set_value(TAU+TAU+TAU*(5/9))
        )
        self.wait()

        big_answer8 = Tex(r"9"+r"=9").next_to(big_answer1,DOWN,buff=0.5)
        big_answer8[0].set_color(YELLOW)
        self.play(
            ReplacementTransform(big_answer7,big_answer8),
            angle.animate.set_value(TAU+TAU+TAU*(9/9)),
            minute.animate.set_value(18+9),
            arrow_big.animate.next_to(big_answer1[12],UP)
        )
        self.play(
            angle_start.animate.set_value(TAU+TAU+TAU*(9/9))
        )
        self.wait()

        minute_hand.clear_updaters()
        circle_dot.clear_updaters()
        arc_pos.clear_updaters()
        self.play(
            FadeOut(big_example),
            FadeOut(big_answer1),
            FadeOut(big_answer8),
            FadeOut(circle_dot),
            FadeOut(minute_hand),
            FadeOut(arc_pos),
            vbm_group.animate.shift(RIGHT*0.8),
            FadeOut(arrow_big)
        )
        self.wait()

        base_ten_title = Tex(r"\text{Base 10 Digital Roots}").move_to(big_example)
        self.play(
            FadeIn(base_ten_title)
        )
        self.wait()
        ones = ValueTracker(0)
        tens = ValueTracker(0)
        hundreds = ValueTracker(0)
        root_answer = ValueTracker(ones.get_value()+tens.get_value()+hundreds.get_value())

        ones_place = Tex(str(round(ones.get_value()))).scale(4)
        tens_place = Tex(str(round(tens.get_value()))).scale(4)
        hundreds_place = Tex(str(round(hundreds.get_value()))).scale(4)
        num_group = Group(ones_place, tens_place, hundreds_place).arrange(LEFT).next_to(base_ten_title,DOWN, buff=1)
        ones_title = Tex(r"1's").scale(0.8).next_to(ones_place,UP).set_color(BLUE)
        tens_title = Tex(r"10's").scale(0.8).next_to(tens_place,UP).set_color(RED)
        hundreds_title = Tex(r"100's").scale(0.8).next_to(hundreds_place,UP).set_color(PURPLE)
        title_group = Group(ones_title, tens_title, hundreds_title)
        self.play(
            FadeIn(num_group),
        )
        self.wait()
        self.play(
            FadeIn(ones_title),
            ones_place.animate.set_color(BLUE)
        )
        self.wait()
        self.play(
            FadeIn(tens_title),
            tens_place.animate.set_color(RED)
        )
        self.wait()
        self.play(
            FadeIn(hundreds_title),
            hundreds_place.animate.set_color(PURPLE)
        )
        self.wait()
        self.play(
            num_group.animate.shift(LEFT),
            title_group.animate.shift(LEFT),
        )
        ones_hand = Line(
                np.array([0,0,0]),
                np.array([0,(2*0.8),0]),
            ).shift(DOWN+LEFT*2.7).set_color(BLUE)
        tens_hand = Line(
                np.array([0,0,0]),
                np.array([0,(2*0.7),0]),
            ).shift(DOWN+LEFT*2.7).set_color(RED)
        hund_hand = Line(
                np.array([0,0,0]),
                np.array([0,(2*0.6),0]),
            ).shift(DOWN+LEFT*2.7).set_color(PURPLE)
        root_hand = Line(
                np.array([0,0,0]),
                np.array([0,(2*0.9),0]),
            ).shift(DOWN+LEFT*2.7).set_color(YELLOW)
        
        self.wait()
        self.play(
            FadeIn(root_hand),
            FadeIn(ones_hand),
            FadeIn(tens_hand),
            FadeIn(hund_hand),
        )

        ones_hand.add_updater(lambda m: m.become(
            Line(
                np.array([0,0,0]),
                np.array([
                    (2*0.8)*np.sin(TAU * (ones.get_value()/divs)),
                    (2*0.8)*np.cos(TAU * (ones.get_value()/divs)),
                    0
                ]),
            ).shift(DOWN+LEFT*2.7).set_color(BLUE)
        ))
        tens_hand.add_updater(lambda m: m.become(
            Line(
                np.array([0,0,0]),
                np.array([
                    (2*0.7)*np.sin(TAU * (tens.get_value()/divs)),
                    (2*0.7)*np.cos(TAU * (tens.get_value()/divs)),
                    0
                ]),
            ).shift(DOWN+LEFT*2.7).set_color(RED)
        ))
        hund_hand.add_updater(lambda m: m.become(
            Line(
                np.array([0,0,0]),
                np.array([
                    (2*0.6)*np.sin(TAU * (hundreds.get_value()/divs)),
                    (2*0.6)*np.cos(TAU * (hundreds.get_value()/divs)),
                    0
                ]),
            ).shift(DOWN+LEFT*2.7).set_color(PURPLE)
        ))

        root_hand.add_updater(lambda m: m.become(
            Line(
                np.array([0,0,0]),
                np.array([
                    (2*0.9)*np.sin(TAU * (root_answer.get_value()/divs)),
                    (2*0.9)*np.cos(TAU * (root_answer.get_value()/divs)),
                    0
                ]),
            ).shift(DOWN+LEFT*2.7).set_color(YELLOW)
        ))

        equals = Tex(r"=").next_to(num_group,RIGHT)
        root_place = Tex(str(round(root_answer.get_value()))).scale(4).set_color(YELLOW).next_to(equals,RIGHT)
        root_title = Tex(r"D.R.").scale(0.8).next_to(root_place,UP).set_color(YELLOW)
        self.play(
            FadeIn(equals),
            FadeIn(root_place),
            FadeIn(root_title),
        )

        ones_mod = ValueTracker(0)
        tens_mod = ValueTracker(0)
        hundreds_mod = ValueTracker(0)
        ones_place.add_updater(lambda m: m.become(Tex(str(round(ones_mod.get_value()+tens_mod.get_value())%10)).set_color(BLUE).scale(4).move_to(ones_place)))
        tens_place.add_updater(lambda m: m.become(Tex(str(round(tens_mod.get_value())%10)).set_color(RED).scale(4).move_to(tens_place)))
        hundreds_place.add_updater(lambda m: m.become(Tex(str(round(hundreds_mod.get_value())%10)).set_color(PURPLE).scale(4).move_to(hundreds_place)))
        root_mod = ValueTracker(0)
        root_place.add_updater(lambda m: m.become(Tex(str(round(root_mod.get_value()))).scale(4).set_color(YELLOW).next_to(equals,RIGHT)))

        self.wait()
        for i in range(1,10):
            if i%9 == 0:
                self.play(
                    ones.animate.set_value(i),
                    root_answer.animate.set_value(9),
                )
                ones_mod.set_value(i%10)
                root_mod.set_value(9)
                self.wait(0.5)
            else:
                self.play(
                    ones.animate.set_value(i),
                    root_answer.animate.set_value(i),
                )
                ones_mod.set_value(i%10)
                root_mod.set_value(i%9)
                self.wait(0.5)
        self.play(
            tens.animate.set_value(1),
            root_answer.animate.set_value(10),
        )
        tens_mod.set_value(1)
        root_mod.set_value(10%9)
        
        for i in range(10,19):
            if (i+1)%9 == 0:
                self.play(
                    ones.animate.set_value(i),
                    root_answer.animate.set_value(i+1),
                )
                ones_mod.set_value(i%10)
                root_mod.set_value(9)
                self.wait(0.5)
            else:
                self.play(
                    ones.animate.set_value(i),
                    root_answer.animate.set_value(i+1),
                )
                ones_mod.set_value(i%10)
                root_mod.set_value((i+1)%9)
                self.wait(0.5)

        self.play(
            tens.animate.set_value(2),
            root_answer.animate.set_value(20),
        )
        tens_mod.set_value(2)
        root_mod.set_value(20%9)


        for j in range(2,10):
            for i in range(j*10,(j*10)+9):
                if (i+1)%9 == 0:
                    self.play(
                        ones.animate.set_value(i-(j-1)),
                        root_answer.animate.set_value(i+1),
                        # run_time = 0.2
                    )
                    ones_mod.set_value((i-(j-1))%10)
                    root_mod.set_value(9)
                    # self.wait(0.1)
                else:
                    self.play(
                        ones.animate.set_value(i-(j-1)),
                        root_answer.animate.set_value(i+1),
                        # run_time = 0.2
                    )
                    ones_mod.set_value((i-(j-1))%10)
                    root_mod.set_value((i+1)%9)
                    # self.wait(0.1)
            if j == 9:
                self.play(
                    root_answer.animate.set_value((j+1)*10),
                    hundreds.animate.set_value(1),
                    # run_time = 0.2
                )
                hundreds_mod.set_value(1)
                root_mod.set_value(((j+1)*10)%9)
                tens_mod.set_value(j+1)
                # self.wait(0.1)
            else:
                self.play(
                    root_answer.animate.set_value((j+1)*10),
                    tens.animate.set_value(j+1),
                    # run_time = 0.2
                )
                tens_mod.set_value(j+1)
                root_mod.set_value(((j+1)*10)%9)
                # self.wait(0.1)
        self.wait()
        general_base_title = Tex(r"\text{Base }"+r"b"+r"\text{ Digital Roots}").move_to(base_ten_title)
        b0_title = Tex(r"b^{0}"+r"\text{'s}").scale(0.8).next_to(ones_place,UP).set_color(BLUE)
        b1_title = Tex(r"b^{1}"+r"\text{'s}").scale(0.8).next_to(tens_place,UP).set_color(RED)
        b2_title = Tex(r"b^{2}"+r"\text{'s}").scale(0.8).next_to(hundreds_place,UP).set_color(PURPLE)
        b_group = Group(b0_title, b1_title, b2_title)
        self.play(
            FadeOut(base_ten_title),
            FadeOut(title_group),
        )
        self.play(
            FadeIn(general_base_title),
            FadeIn(b_group),
        )
        self.wait()

class VBMEuler(Scene):
    def construct(self):
        frame = self.camera.frame
        scale = 2

        circle1 = ParametricCurve(
            lambda u: np.array([
                np.sin(u),
                np.cos(u),
                0
            ]),
            color = WHITE,
            t_range = np.array([-PI, PI, 0.01])
        ).scale(scale).set_stroke(width=4)
        numbers1 = vbm_numbers(1,9,1.0,2.6)
        positives = number_polarities_pos(numbers1, 0.5)
        dots1 = vbm_dots(1,9,1.4,2)

        group1 = Group(dots1, numbers1, positives)
        
        axes = NumberPlane().scale(2)
        euler_group = Group()
        
        r = 1.3
        left_shift = 3.1
        
        arrow_angle = ValueTracker(0)
        t2c = {
            "1":RED, "4":RED, "7":RED,
            "2":BLUE, "5":BLUE, "8":BLUE,
            "3":GREEN, "6":GREEN, "0":GREEN,
        }
        for i in range(0,9):
            if i == 0:
                euler_equation  = Tex(r"e^{i\frac{" + str(9) + "}{9}"+r"\tau}", tex_to_color_map = t2c)
            else:
                euler_equation  = Tex(r"e^{i\frac{" + str(i) + "}{9}"+r"\tau}", tex_to_color_map = t2c)

            euler_equation.shift(
                [
                    scale * r*np.sin(TAU * (i/9)),
                    scale * r*np.cos(TAU * (i/9)),
                    0
                ]            
            )
            euler_group.add(euler_equation)

        self.add(group1, circle1)
        self.wait(1)
        self.play(
            FadeOut(group1)
        )
        self.play(FadeIn(axes))
        self.wait()

        eisel = Rectangle(width=6.2,height=10,color=BLACK)
        eisel.move_to(4.05*LEFT).set_fill(BLACK).set_opacity(1.0)
        self.play(
            axes.animate.shift(RIGHT*left_shift),
            circle1.animate.shift(RIGHT*left_shift),
            FadeIn(eisel),
        )
        self.wait(1)

        roots_title = Tex(r"\textsc{Roots of Unity}").move_to(eisel).shift(UP*3.3).scale(1.3)

        self.play(
            FadeIn(roots_title),
            FadeOut(group1)
        )
        self.wait(1)

        real = Tex(r"Re").move_to([0,3.5,0]).shift(RIGHT*left_shift)
        imaginary = Tex(r"Im").move_to([3.5,0,0]).shift(RIGHT*left_shift)
        z_eq = Tex(r"z = x + iy").next_to(roots_title, DOWN, buff=0.7).scale(1.3)
        self.play(
            FadeIn(z_eq),
        )
        real_eq = Tex(r"Re\left ( z \right )=x" )
        imag_eq = Tex(r"Im\left ( z \right )=y" )
        real_imag = Group(real_eq, imag_eq).arrange(RIGHT).next_to(z_eq,DOWN, buff=0.5)
        self.wait(1)
        self.play(
            FadeIn(real),
            FadeIn(imaginary),
            FadeIn(real_imag)
        )

        pythag_eq = Tex(r"\sqrt{x^{2}+y^{2}}=1").next_to(real_imag,DOWN,buff=1)
        self.play(FadeIn(pythag_eq))
        self.wait()
        self.play(FadeIn(circle1))
        self.wait()

        mult_angle = ValueTracker(0)
        dot_mult = Dot(
            np.array([
                scale * np.sin(TAU * (mult_angle.get_value()/9)),
                scale * np.cos(TAU * (mult_angle.get_value()/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        dot_mult.add_updater(lambda m: m.become(Dot(
            np.array([
                scale * np.sin(TAU * (mult_angle.get_value()/9)),
                scale * np.cos(TAU * (mult_angle.get_value()/9)),
                0
            ])
        ).shift(RIGHT*left_shift)))
        z_tracker = Tex(r"z")
        z_tracker.add_updater(lambda m: m.move_to(
            np.array([
                1.2*scale * np.sin(TAU * (mult_angle.get_value()/9)),
                1.2*scale * np.cos(TAU * (mult_angle.get_value()/9)),
                0
            ])
        ).shift(RIGHT*left_shift))
        self.play(
            FadeIn(dot_mult),
            FadeIn(z_tracker),
        )
        self.play(
            mult_angle.animate.set_value(9)
        )
        pythag_eq2 = Tex(r"x^{2}+y^{2}=1").move_to(pythag_eq)
        self.wait()
        self.play(Transform(pythag_eq, pythag_eq2))
        self.wait()
        trig_eg = Tex(r"cos^{2}\theta + sin^{2}\theta = 1").next_to(pythag_eq2,DOWN,buff=0.5)
        self.play(
            FadeIn(trig_eg)
        )
        cos_eq = Tex(r"x = cos\theta").next_to(trig_eg,DOWN,buff=0.5)
        sin_eq = Tex(r"y = sin\theta").next_to(cos_eq,DOWN,buff=0.5)
        self.wait()
        self.play(
            FadeIn(cos_eq),
            FadeIn(sin_eq),
        )
        self.wait()
        self.play(
            FadeOut(cos_eq),
            FadeOut(sin_eq),
            FadeOut(trig_eg),
            FadeOut(pythag_eq)
        )
        self.wait()
        z_euler_eq = Tex(r"z=cos\theta+isin\theta").next_to(real_imag,DOWN,buff=1)
        self.play(
            FadeIn(z_euler_eq)
        )
        self.wait()
        cos_sin_color = {
            "cos":YELLOW,
            "sin":ORANGE,
        }
        euler = Tex(r"e^{i\theta}=cos\theta+isin \theta").next_to(z_euler_eq,DOWN,buff=0.5)
        self.play(
            FadeIn(euler)
        )
        true_complex = Tex(r"z = e^{i\theta}").next_to(euler,DOWN,buff=0.7).scale(1.3)
        self.wait()
        self.play(
            FadeIn(true_complex)
        )
        self.wait()

        tau_tracker = ValueTracker(0)
        line = always_redraw(lambda: Line(
            start=np.array([0,0,0]),
            end=np.array([
                scale * np.sin(tau_tracker.get_value()),
                scale * np.cos(tau_tracker.get_value()),
                0
            ]),buff=0
        ).shift(RIGHT*left_shift))
        disc = always_redraw(lambda: ParametricSurface(
            lambda u,v: np.array([
                    v*np.sin(u),
                    v*np.cos(u),
                    0
                ]),
                u_range=(0, tau_tracker.get_value()),
                v_range=(0, 2),
                color=BLUE,
        ).set_opacity(0.5).shift(RIGHT*left_shift))
        self.play(
            FadeIn(line),
            FadeIn(disc),
        )
        self.wait()
        mult_angle.set_value(0)
        self.play(
            tau_tracker.animate.set_value(TAU*(2/9)),
            mult_angle.animate.set_value(2),
        )
        self.wait()
        theta = Tex(r"\theta").next_to(np.array([left_shift,0,0]), UP + RIGHT)
        self.play(
            FadeIn(theta)
        )
        self.wait()
        self.play(
            FadeOut(theta),
        )
        self.play(
            tau_tracker.animate.set_value(0),
            mult_angle.animate.set_value(0),
        )
        self.wait()
        self.play(
            FadeOut(z_euler_eq),
            FadeOut(euler),
            FadeOut(z_eq),
            FadeOut(real_eq),
            FadeOut(imag_eq),
            true_complex.animate.next_to(roots_title, DOWN, 0.5)
        )
        multiplication = Tex(r"Multiplication").next_to(true_complex,DOWN, buff=1)
        mult_euler = Tex(r"z_{a}\cdot z_{b} = e^{i\theta_{a}}\cdot e^{i\theta_{b}}").next_to(multiplication,DOWN, buff=0.5)
        mult_euler2 = Tex(r"z_{c} = e^{i\left( \theta_{a}+\theta_{b}\right)}").next_to(mult_euler,DOWN, buff=0.5)
        z_sqrd_eq = Tex(r"z^{2}=\left(e^{i\theta}\right)^{2}")
        z_sqrd_answer = Tex(r"= e^{i2\theta}")
        z_sqrd_group = Group(z_sqrd_eq, z_sqrd_answer).arrange(RIGHT).next_to(mult_euler2,DOWN, buff=0.5)
        
        z_tracker.suspend_updating()
        dot_mult.suspend_updating()
        line.suspend_updating()
        disc.suspend_updating()

        self.play(
            FadeIn(multiplication)
        )
        self.wait()
        self.play(
            FadeIn(mult_euler),
        )
        self.wait()
        self.play(
            FadeIn(mult_euler2),
        )
        self.wait()

        z_a = Tex(r"z_{a}")
        z_b = Tex(r"z_{a}")
        z_c = Tex(r"z_{a}")
        za_angle = ValueTracker(0)
        zb_angle = ValueTracker(0)
        zc_angle = ValueTracker(TAU/3)

        za_tracker = Tex(r"z_{a}")
        za_tracker.add_updater(lambda m: m.move_to(
            np.array([
                1.2*scale * np.sin((za_angle.get_value())),
                1.2*scale * np.cos((za_angle.get_value())),
                0
            ])
        ).shift(RIGHT*left_shift))

        dot_za = always_redraw(lambda: Dot(
            np.array([
                scale * np.sin((za_angle.get_value())),
                scale * np.cos((za_angle.get_value())),
                0
            ])
        ).shift(RIGHT*left_shift))

        line_za = always_redraw(lambda: Line(
            start=np.array([0,0,0]),
            end=np.array([
                scale * np.sin(za_angle.get_value()),
                scale * np.cos(za_angle.get_value()),
                0
            ]),buff=0
        ).shift(RIGHT*left_shift))

        disc_za = always_redraw(lambda: ParametricSurface(
            lambda u,v: np.array([
                    v*np.sin(u),
                    v*np.cos(u),
                    0
                ]),
                u_range=(0, za_angle.get_value()),
                v_range=(0, 2),
                color=BLUE,
        ).set_opacity(0.5).shift(RIGHT*left_shift))


        self.play(
            FadeOut(z_tracker),
            FadeOut(dot_mult),
            FadeOut(disc),
            FadeIn(za_tracker),
            FadeIn(dot_za),
            FadeIn(line_za),
            FadeIn(disc_za),
        )
        self.wait()
        self.play(
            za_angle.animate.set_value(TAU*(1/8))
        )
        self.wait()

        zb_tracker = Tex(r"z_{b}")
        zb_tracker.add_updater(lambda m: m.move_to(
            np.array([
                1.2*scale * np.sin((zb_angle.get_value())),
                1.2*scale * np.cos((zb_angle.get_value())),
                0
            ])
        ).shift(RIGHT*left_shift))

        dot_zb = always_redraw(lambda: Dot(
            np.array([
                scale * np.sin((zb_angle.get_value())),
                scale * np.cos((zb_angle.get_value())),
                0
            ])
        ).shift(RIGHT*left_shift))

        line_zb = always_redraw(lambda: Line(
            start=np.array([0,0,0]),
            end=np.array([
                scale * np.sin(zb_angle.get_value()),
                scale * np.cos(zb_angle.get_value()),
                0
            ]),buff=0
        ).shift(RIGHT*left_shift))

        zc_start = ValueTracker(0)
        disc_zb = always_redraw(lambda: ParametricSurface(
            lambda u,v: np.array([
                    v*np.sin(u),
                    v*np.cos(u),
                    0
                ]),
                u_range=(zc_start.get_value(), zb_angle.get_value()),
                v_range=(0, 2),
                color=GREEN,
        ).set_opacity(0.5).shift(RIGHT*left_shift))

        self.play(
            FadeIn(zb_tracker),
            FadeIn(dot_zb),
            FadeIn(line_zb),
            FadeIn(disc_zb),
        )
        self.play(
            zb_angle.animate.set_value(TAU/3)
        )
        self.wait()

        disc_zb.clear_updaters()
        disc_zb.add_updater(lambda m: m.become(ParametricSurface(
            lambda u,v: np.array([
                    v*np.sin(u),
                    v*np.cos(u),
                    0
                ]),
                u_range=(zc_start.get_value(), zc_angle.get_value()),
                v_range=(0, 2),
                color=GREEN,
        ).set_opacity(0.5).shift(RIGHT*left_shift)))

        zc_tracker = Tex(r"z_{c}")
        zc_tracker.add_updater(lambda m: m.move_to(
            np.array([
                1.2*scale * np.sin((zc_angle.get_value())),
                1.2*scale * np.cos((zc_angle.get_value())),
                0
            ])
        ).shift(RIGHT*left_shift))

        dot_zc = always_redraw(lambda: Dot(
            np.array([
                scale * np.sin((zc_angle.get_value())),
                scale * np.cos((zc_angle.get_value())),
                0
            ])
        ).shift(RIGHT*left_shift))

        line_zc = always_redraw(lambda: Line(
            start=np.array([0,0,0]),
            end=np.array([
                scale * np.sin(zc_angle.get_value()),
                scale * np.cos(zc_angle.get_value()),
                0
            ]),buff=0
        ).shift(RIGHT*left_shift))
        
        line_origin = always_redraw(lambda: Line(
            start=np.array([0,0,0]),
            end=np.array([
                scale * np.sin(zc_start.get_value()),
                scale * np.cos(zc_start.get_value()),
                0
            ]),buff=0
        ).shift(RIGHT*left_shift))

        self.add(zc_tracker, dot_zc, line_zc, line_origin)
        self.play(
            zc_angle.animate.set_value((TAU/3)+(TAU/8)),
            zc_start.animate.set_value(TAU/8),
        )
        self.wait()
        self.play(
            za_angle.animate.set_value(0),
            zb_angle.animate.set_value(0),
            zc_angle.animate.set_value(0),
            zc_start.animate.set_value(0),
        )
        self.play(
            FadeOut(za_tracker),
            FadeOut(zb_tracker),
            FadeOut(zc_tracker),
            FadeOut(line_za),
            FadeOut(line_zb),
            FadeOut(line_zc),
            FadeOut(disc_za),
            FadeOut(disc_zb),
            FadeOut(dot_za),
            FadeOut(dot_zb),
            FadeOut(dot_zc),
            FadeIn(z_tracker),
            FadeIn(dot_mult),
            FadeIn(disc),
        )


        z_tracker.resume_updating()
        dot_mult.resume_updating()
        line.resume_updating()
        disc.resume_updating()

        self.wait()
        self.play(
            tau_tracker.animate.set_value((1/9)*TAU),
            mult_angle.animate.set_value(1),
        )

        tau_start = ValueTracker(tau_tracker.get_value())
        tau_sqrd = ValueTracker(TAU/9)
        new_disc = always_redraw(lambda: ParametricSurface(
            lambda u,v: np.array([
                    v*np.sin(u),
                    v*np.cos(u),
                    0
                ]),
                u_range=(tau_start.get_value(), tau_sqrd.get_value()),
                v_range=(0, 2),
                color=RED,
        ).set_opacity(0.5).shift(RIGHT*left_shift))
        dot_sqrd = always_redraw(lambda: Dot(
            np.array([
                scale * np.sin(tau_sqrd.get_value()),
                scale * np.cos(tau_sqrd.get_value()),
                0
            ])
        ).shift(RIGHT*left_shift))
        line_sqrd = always_redraw(lambda: Line(
            start=np.array([0,0,0]),
            end=np.array([
                scale * np.sin(tau_sqrd.get_value()),
                scale * np.cos(tau_sqrd.get_value()),
                0
            ]),buff=0
        ).shift(RIGHT*left_shift))
        z_sqrd_tracker = Tex(r"z^{2}")
        z_sqrd_tracker.add_updater(lambda m: m.move_to(
            np.array([
                1.2*scale * np.sin(tau_sqrd.get_value()),
                1.2*scale * np.cos(tau_sqrd.get_value()),
                0
            ])
        ).shift(RIGHT*left_shift))

        self.add(z_sqrd_tracker, new_disc, dot_sqrd, line_sqrd)
        self.wait()
        self.play(
            FadeIn(z_sqrd_group)
        )
        self.play(
            tau_sqrd.animate.set_value((2/9)*TAU),
        )
        self.wait()
        self.play(
            tau_tracker.animate.set_value((3/9)*TAU),
            tau_sqrd.animate.set_value((6/9)*TAU),
            mult_angle.animate.set_value(3),
        )
        self.wait()
        self.play(
            tau_tracker.animate.set_value((1/9)*TAU),
            tau_sqrd.animate.set_value((2/9)*TAU),
            mult_angle.animate.set_value(1),
        )
        self.wait()
        self.play(
            FadeOut(multiplication),
            FadeOut(mult_euler),
            FadeOut(mult_euler2),
            FadeOut(z_sqrd_group),
            tau_tracker.animate.set_value((0)*TAU),
            tau_sqrd.animate.set_value((0)*TAU),
            mult_angle.animate.set_value(0),
            tau_start.animate.set_value(0),
            FadeOut(z_sqrd_tracker),
        )

    ##############

        division = Tex(r"Division").next_to(true_complex,DOWN, buff=0.5)
        div_euler = Tex(r"z_{a}/ z_{b} = e^{i\theta_{a}}\cdot e^{-i\theta_{b}}").next_to(division,DOWN, buff=0.5)
        div_euler2 = Tex(r"z_{c} = e^{i\left( \theta_{a}-\theta_{b}\right)}").next_to(div_euler,DOWN, buff=0.5)
        z_sqrt_eq = Tex(r"\sqrt{z}=\left(e^{-i\theta}\right)^{\frac{1}{2}}")
        z_sqrt_answer = Tex(r"= e^{i\frac{1}{2}\theta}")
        z_sqrt_group = Group(z_sqrt_eq, z_sqrt_answer).arrange(RIGHT).next_to(div_euler2,DOWN, buff=0.5)

        self.play(
            FadeIn(division)
        )
        self.wait()
        self.play(
            FadeIn(div_euler),
        )
        self.wait()

        self.play(
            FadeOut(z_tracker),
            FadeOut(dot_mult),
            FadeOut(disc),
            FadeIn(za_tracker),
            FadeIn(dot_za),
            FadeIn(line_za),
            FadeIn(disc_za),
        )
        self.wait()
        self.play(
            za_angle.animate.set_value(TAU*(4/9))
        )
        self.wait()

        disc_za.clear_updaters()
        disc_za.add_updater(lambda m: m.become(ParametricSurface(
            lambda u,v: np.array([
                    v*np.sin(u),
                    v*np.cos(u),
                    0
                ]),
                u_range=(zb_angle.get_value(), za_angle.get_value()),
                v_range=(0, 2),
                color=BLUE,
        ).set_opacity(0.5).shift(RIGHT*left_shift)))

        self.play(
            FadeIn(zb_tracker),
            FadeIn(dot_zb),
            FadeIn(line_zb),
            FadeIn(disc_zb),
        )
        self.play(
            zb_angle.animate.set_value(TAU/9),
            zc_angle.animate.set_value(TAU/9),
        )
        self.wait()

        zc_tracker.clear_updaters()
        dot_zc.clear_updaters()
        line_zc.clear_updaters()
        zc_end = ValueTracker(zc_angle.get_value())

        zc_tracker.add_updater(lambda m: m.move_to(
            np.array([
                1.2*scale * np.sin((zc_end.get_value())),
                1.2*scale * np.cos((zc_end.get_value())),
                0
            ])
        ).shift(RIGHT*left_shift))

        dot_zc = always_redraw(lambda: Dot(
            np.array([
                scale * np.sin((zc_end.get_value())),
                scale * np.cos((zc_end.get_value())),
                0
            ])
        ).shift(RIGHT*left_shift))

        line_zc = always_redraw(lambda: Line(
            start=np.array([0,0,0]),
            end=np.array([
                scale * np.sin(zc_end.get_value()),
                scale * np.cos(zc_end.get_value()),
                0
            ]),buff=0
        ).shift(RIGHT*left_shift))

        disc_za.clear_updaters()
        disc_za.add_updater(lambda m: m.become(ParametricSurface(
            lambda u,v: np.array([
                    v*np.sin(u),
                    v*np.cos(u),
                    0
                ]),
                u_range=(zb_angle.get_value(), zc_end.get_value()),
                v_range=(0, 2),
                color=BLUE,
        ).set_opacity(0.5).shift(RIGHT*left_shift)))

        disc_zc = always_redraw(lambda: ParametricSurface(
            lambda u,v: np.array([
                    v*np.sin(u),
                    v*np.cos(u),
                    0
                ]),
                u_range=(za_angle.get_value(), zc_end.get_value()),
                v_range=(0, 2),
                color=GREEN,
        ).set_opacity(0.5).shift(RIGHT*left_shift))

        zc_end.set_value(za_angle.get_value())
        self.add(dot_zc, line_zc, disc_zc)
        self.play(
            zc_end.animate.set_value((TAU*(3/9))),
            FadeIn(zc_tracker),
            FadeIn(div_euler2)
        )
        self.wait()
        self.play(
            zc_end.animate.set_value(0),
            zc_angle.animate.set_value(0),
            zb_angle.animate.set_value(0),
            za_angle.animate.set_value(0),
        )
        self.play(
            FadeOut(za_tracker),
            FadeOut(zb_tracker),
            FadeOut(zc_tracker),
            FadeOut(dot_za),
            FadeOut(dot_zb),
            FadeOut(dot_zc),
            FadeOut(line_za),
            FadeOut(line_zb),
            FadeOut(line_zc),
            FadeOut(disc_za),
            FadeOut(disc_zb),
            FadeOut(disc_zc),
        )
        self.wait()




        dot_mult.resume_updating()
        line.resume_updating()
        disc.resume_updating()
        z_sqrd_tracker.resume_updating()
        dot_sqrd.resume_updating()
        line_sqrd.resume_updating()
        new_disc.clear_updaters()
        new_disc1 = always_redraw(lambda: ParametricSurface(
            lambda u,v: np.array([
                    v*np.sin(u),
                    v*np.cos(u),
                    0
                ]),
                u_range=(tau_start.get_value(), tau_sqrd.get_value()),
                v_range=(0, 2),
                color=RED,
        ).set_opacity(0.5).shift(RIGHT*left_shift))

        
        self.add(z_tracker,dot_mult,line,disc,z_sqrd_tracker,dot_sqrd,line_sqrd,new_disc1)
        self.play(
            mult_angle.animate.set_value(3),
            tau_tracker.animate.set_value(TAU*(3/9)),
            tau_sqrd.animate.set_value(TAU*(6/9)),
        )

        z_root_tracker = Tex(r"\sqrt{z}")
        z_root_tracker.add_updater(lambda m: m.move_to(
            np.array([
                1.2*scale * np.sin(TAU * (mult_angle.get_value()/9)),
                1.2*scale * np.cos(TAU * (mult_angle.get_value()/9)),
                0
            ])
        ).shift(RIGHT*left_shift))
        z_div_tracker = Tex(r"z")
        z_div_tracker.add_updater(lambda m: m.move_to(
            np.array([
                1.2*scale * np.sin(tau_sqrd.get_value()),
                1.2*scale * np.cos(tau_sqrd.get_value()),
                0
            ])
        ).shift(RIGHT*left_shift))
        disc.clear_updaters()
        new_disc1.clear_updaters()
        self.play(
            FadeOut(z_tracker),
            FadeOut(z_sqrd_tracker),
            FadeIn(z_sqrt_group),
            FadeIn(z_root_tracker),
            FadeIn(z_div_tracker),
            disc.animate.set_color(RED),
            new_disc1.animate.set_color(BLUE)
        )
        self.wait()
        disc.add_updater(lambda m: m.become(ParametricSurface(
            lambda u,v: np.array([
                    v*np.sin(u),
                    v*np.cos(u),
                    0
                ]),
                u_range=(0, tau_tracker.get_value()),
                v_range=(0, 2),
                color=RED,
        ).set_opacity(0.5).shift(RIGHT*left_shift)))
        new_disc1.add_updater(lambda m: m.become(ParametricSurface(
            lambda u,v: np.array([
                    v*np.sin(u),
                    v*np.cos(u),
                    0
                ]),
                u_range=(tau_start.get_value(), tau_sqrd.get_value()),
                v_range=(0, 2),
                color=BLUE,
        ).set_opacity(0.5).shift(RIGHT*left_shift)))

        self.play(
            mult_angle.animate.set_value(1),
            tau_tracker.animate.set_value(TAU*(1/9)),
            tau_sqrd.animate.set_value(TAU*(2/9)),
        )
        self.wait()
        self.play(
            mult_angle.animate.set_value(2.25),
            tau_tracker.animate.set_value(TAU*(2.25/9)),
            tau_sqrd.animate.set_value(TAU*(4.5/9)),
        )
        self.wait()
        self.play(
            mult_angle.animate.set_value(4.5),
            tau_tracker.animate.set_value(TAU*(4.5/9)),
            tau_sqrd.animate.set_value(TAU),
        )
        self.wait()
        z_unit = Tex(r"z=e^{i\tau}=cos(\tau)+isin(\tau)=1")
        z_sqrt_unit = Tex(r"\sqrt{z}=e^{i\frac{\tau}{2}}=cos(\frac{\tau}{2})+isin(\frac{\tau}{2})=-1")
        z_unit.scale(0.6).next_to(z_sqrt_group,DOWN)
        z_sqrt_unit.scale(0.6).next_to(z_unit,DOWN)
        self.play(
            FadeIn(z_unit)
        )
        self.wait()
        self.play(
            FadeIn(z_sqrt_unit)
        )
        self.wait()
        self.play(
            FadeOut(division),
            FadeOut(div_euler),
            FadeOut(div_euler2),
            FadeOut(z_sqrt_group),
            FadeOut(z_div_tracker),
            FadeOut(z_root_tracker),
            FadeOut(z_unit),
            FadeOut(z_sqrt_unit),
            mult_angle.animate.set_value(0),
            tau_tracker.animate.set_value(0),
            tau_sqrd.animate.set_value(0),
            
        )
        self.wait()
        tau_complex = Tex(r"z = e^{i\tau}=1").next_to(roots_title,DOWN,buff=0.5).scale(1.3)
        r = 1.25
        main_euler = Tex(r"e^{i\tau}").shift(
                [
                    left_shift+(scale * r*np.sin(0)),
                    scale * r*np.cos(0),
                    0
                ]            
            )


        self.play(
            ReplacementTransform(true_complex, tau_complex),
            FadeIn(main_euler),
        )
        self.wait()

        def make_roots(num_roots):
            dot_group = Group()
            line_group = Group()
            eq_group = Group()
            total = Group()
            for i in range(0,num_roots):
                dot = Dot(np.array([
                    scale * np.sin(TAU*(i/num_roots)),
                    scale * np.cos(TAU*(i/num_roots)),
                    0
                ]))
                line = Line(
                    np.array([0,0,0]),
                    np.array([
                        scale * np.sin(TAU*(i/num_roots)),
                        scale * np.cos(TAU*(i/num_roots)),
                        0
                    ])
                )
                eq = Tex(r"e^{i\frac{" + str(i) + r"}{" + str(num_roots) + r"}\tau}")
                eq.shift([
                    scale * r*np.sin(TAU * (i/num_roots)),
                    scale * r*np.cos(TAU * (i/num_roots)),
                    0
                ])
                dot_group.add(dot)
                line_group.add(line)
                eq_group.add(eq)
            total.add(dot_group, line_group, eq_group)
            return total

        two_root_1 = Tex(r"\sqrt{1}").next_to(tau_complex, DOWN, buff=0.5)
        pos1 = Tex(r"1")
        neg1 = Tex(r"-1")
        one_roots = Group(pos1, neg1).arrange(RIGHT, buff = 1.5).next_to(two_root_1, DOWN, buff=1)
        arrow1 = Arrow(
            two_root_1.get_bottom(),
            pos1.get_top()
        )
        arrow2 = Arrow(
            two_root_1.get_bottom(),
            neg1.get_top()
        )


        self.play(FadeIn(two_root_1))
        self.play(
            ShowCreation(arrow1),
            ShowCreation(arrow2),
            FadeIn(one_roots)
        )
        
        square_root = make_roots(2).shift(RIGHT*left_shift)
        self.play(
            FadeOut(main_euler),
            FadeIn(square_root)
        )
        self.wait()

        eq_scale = 0.7
        e0_eq = Tex(r"e^{i\frac{0}{2}\tau}=cos(\frac{0}{2}\tau)+isin(\frac{0}{2}\tau)=1").scale(eq_scale).next_to(one_roots, DOWN, buff=0.5)
        e1_eq = Tex(r"e^{i\frac{1}{2}\tau}=cos(\frac{1}{2}\tau)+isin(\frac{1}{2}\tau)=-1").scale(eq_scale).next_to(e0_eq, DOWN, buff=0.5)
        self.play(
            FadeIn(e0_eq),
        )
        self.wait()
        self.play(
            FadeIn(e1_eq),
        )
        self.wait()
        four_root_1 = Tex(r"\sqrt{\sqrt{1}}").scale(0.8).next_to(tau_complex, DOWN, buff=0.3)
        root_of_1 = Tex(r"\sqrt{1}")
        root_of_minus_1 = Tex(r"\sqrt{-1}")
        root_of_group = Group(root_of_1, root_of_minus_1).arrange(RIGHT, buff = 1.5).next_to(two_root_1, DOWN, buff=1)
        self.play(
            FadeOut(e0_eq),
            FadeOut(e1_eq),
        )
        self.wait()
        self.play(
            ReplacementTransform(two_root_1, four_root_1)
        )
        self.wait()
        self.play(
            ReplacementTransform(one_roots, root_of_group)
        )

        new_root_1 = Tex(r"1")
        new_root_2 = Tex(r"-1")
        new_root_3 = Tex(r"i")
        new_root_4 = Tex(r"-i")
        new_root_group_1 = Group(new_root_1, new_root_2).arrange(RIGHT, buff = 0.8).next_to(root_of_1, DOWN, buff=1)
        new_root_group_2 = Group(new_root_3, new_root_4).arrange(RIGHT, buff = 0.8).next_to(root_of_minus_1, DOWN, buff=1)
        
        arrow3 = Arrow(
            root_of_1.get_bottom(),
            new_root_1.get_top()
        )
        arrow4 = Arrow(
            root_of_1.get_bottom(),
            new_root_2.get_top()
        )
        arrow5 = Arrow(
            root_of_minus_1.get_bottom(),
            new_root_3.get_top()
        )
        arrow6 = Arrow(
            root_of_minus_1.get_bottom(),
            new_root_4.get_top()
        )

        self.play(
            FadeIn(new_root_group_1),
            FadeIn(arrow3),
            FadeIn(arrow4),
        )
        self.wait()
        self.play(
            FadeIn(new_root_group_2),
            FadeIn(arrow5),
            FadeIn(arrow6),
        )
        self.wait()
        four_root = Tex(r"\sqrt[4]{1}").next_to(tau_complex, DOWN, buff=0.5)
        self.play(
            ReplacementTransform(four_root_1, four_root)
        )
        self.wait()
        fourth_root = make_roots(4).shift(RIGHT*left_shift)
        self.play(
            FadeOut(square_root),
            FadeIn(fourth_root),
        )
        self.wait()
        eq_scale = 0.7

        r = 1.2
        circle_root_1 = Tex(r"1").move_to(
            np.array([
                scale * r* np.sin(0),
                scale * r* np.cos(0),
                0
            ])
        ).shift(RIGHT*left_shift)
        circle_root_2 = Tex(r"i").move_to(
            np.array([
                scale * r* np.sin(TAU*(1/4)),
                scale * r* np.cos(TAU*(1/4)),
                0
            ])
        ).shift(RIGHT*left_shift)
        circle_root_3 = Tex(r"-1").move_to(
            np.array([
                scale * r* np.sin(TAU*(2/4)),
                scale * r* np.cos(TAU*(2/4)),
                0
            ])
        ).shift(RIGHT*left_shift)
        circle_root_4 = Tex(r"-i").move_to(
            np.array([
                scale * r* np.sin(TAU*(3/4)),
                scale * r* np.cos(TAU*(3/4)),
                0
            ])
        ).shift(RIGHT*left_shift)
        operators = Group(circle_root_1,circle_root_2,circle_root_3,circle_root_4)

        root_start = ValueTracker(0)
        root_end = ValueTracker(0)
        disc_root = always_redraw(lambda: ParametricSurface(
            lambda u,v: np.array([
                    v*np.sin(u),
                    v*np.cos(u),
                    0
                ]),
                u_range=(root_start.get_value(), root_end.get_value()),
                v_range=(0, 2),
                color=RED,
        ).set_opacity(0.5).shift(RIGHT*left_shift))
        dot_root = always_redraw(lambda: Dot(
            np.array([
                scale * np.sin(root_end.get_value()),
                scale * np.cos(root_end.get_value()),
                0
            ])
        ).shift(RIGHT*left_shift))
        line_og = always_redraw(lambda: Line(
            start=np.array([0,0,0]),
            end=np.array([
                scale * np.sin(root_start.get_value()),
                scale * np.cos(root_start.get_value()),
                0
            ]),buff=0
        ).shift(RIGHT*left_shift))
        line_root = always_redraw(lambda: Line(
            start=np.array([0,0,0]),
            end=np.array([
                scale * np.sin(root_end.get_value()),
                scale * np.cos(root_end.get_value()),
                0
            ]),buff=0
        ).shift(RIGHT*left_shift))
        root_circle = Group(disc_root, dot_root, line_og, line_root)

        self.add(root_circle)
        self.wait()
        self.play(
            FadeOut(fourth_root[1]), 
            FadeOut(fourth_root[2]), 
            FadeIn(operators),
        )
        e0_eq = Tex(r"e^{i\frac{0}{4}\tau}=cos(\frac{0}{4}\tau)+isin(\frac{0}{4}\tau)=1").scale(eq_scale).next_to(tau_complex, DOWN, buff=4.5)
        e1_eq = Tex(r"e^{i\frac{1}{4}\tau}=cos(\frac{1}{4}\tau)+isin(\frac{1}{4}\tau)=i").scale(eq_scale).next_to(tau_complex, DOWN, buff=4.5)
        e2_eq = Tex(r"e^{i\frac{2}{4}\tau}=cos(\frac{2}{4}\tau)+isin(\frac{2}{4}\tau)=-1").scale(eq_scale).next_to(tau_complex, DOWN, buff=4.5)
        e3_eq = Tex(r"e^{i\frac{3}{4}\tau}=cos(\frac{3}{4}\tau)+isin(\frac{3}{4}\tau)=-i").scale(eq_scale).next_to(tau_complex, DOWN, buff=4.5)
        e4_eq = Tex(r"e^{i\frac{4}{4}\tau}=cos(\frac{4}{4}\tau)+isin(\frac{4}{4}\tau)=1").scale(eq_scale).next_to(tau_complex, DOWN, buff=4.5)
        self.wait()
        self.play(
            FadeIn(e0_eq),
        )
        self.play(
            FadeOut(e0_eq),
            FadeIn(e1_eq),
            root_end.animate.set_value(TAU*(1/4)),
        )
        self.play(
            root_start.animate.set_value(TAU*(1/4)),
        )
        self.wait()
        self.play(
            FadeOut(e1_eq), 
            FadeIn(e2_eq),
            root_end.animate.set_value(TAU*(2/4)),
        )
        self.play(
            root_start.animate.set_value(TAU*(2/4)),
        )
        self.wait()
        self.play(
            FadeOut(e2_eq), 
            FadeIn(e3_eq),
            root_end.animate.set_value(TAU*(3/4)),
        )
        self.play(
            root_start.animate.set_value(TAU*(3/4)),
        )
        self.wait()
        self.play(
            FadeOut(e3_eq), 
            FadeIn(e4_eq),
            root_end.animate.set_value(TAU*(4/4)),
        )
        self.play(
            root_start.animate.set_value(TAU*(4/4)),
        )
        self.wait()
        self.play(
            FadeOut(root_circle),
            FadeOut(e4_eq),
        )
        root_start.set_value(0)
        root_end.set_value(0)


        self.add(root_circle)
        self.wait()
        e0_eq = Tex(r"e^{i\frac{0}{4}\tau}=cos(\frac{0}{4}\tau)+isin(\frac{0}{4}\tau)=1").scale(eq_scale).next_to(tau_complex, DOWN, buff=4.5)
        e1_eq = Tex(r"e^{i\frac{2}{4}\tau}=cos(\frac{2}{4}\tau)+isin(\frac{2}{4}\tau)=-1").scale(eq_scale).next_to(tau_complex, DOWN, buff=4.5)
        e2_eq = Tex(r"e^{i\frac{4}{4}\tau}=cos(\frac{4}{4}\tau)+isin(\frac{4}{4}\tau)=1").scale(eq_scale).next_to(tau_complex, DOWN, buff=4.5)
        e3_eq = Tex(r"e^{i\frac{6}{4}\tau}=cos(\frac{6}{4}\tau)+isin(\frac{6}{4}\tau)=-1").scale(eq_scale).next_to(tau_complex, DOWN, buff=4.5)
        e4_eq = Tex(r"e^{i\frac{8}{4}\tau}=cos(\frac{8}{4}\tau)+isin(\frac{8}{4}\tau)=1").scale(eq_scale).next_to(tau_complex, DOWN, buff=4.5)

        self.play(
            FadeIn(e0_eq)
        )
        self.wait()
        self.play(
            FadeOut(e0_eq), 
            FadeIn(e1_eq),
            root_end.animate.set_value(TAU*(2/4)),
        )
        self.play(
            root_start.animate.set_value(TAU*(2/4)),
        )
        self.wait()
        self.play(
            FadeOut(e1_eq), 
            FadeIn(e2_eq),
            root_end.animate.set_value(TAU*(4/4)),
        )
        self.play(
            root_start.animate.set_value(TAU*(4/4)),
        )
        self.wait()
        self.play(
            FadeOut(e2_eq), 
            FadeIn(e3_eq),
            root_end.animate.set_value(TAU*(6/4)),
        )
        self.play(
            root_start.animate.set_value(TAU*(6/4)),
        )
        self.wait()
        self.play(
            FadeOut(e3_eq), 
            FadeIn(e4_eq),
            root_end.animate.set_value(TAU*(8/4)),
        )
        self.play(
            root_start.animate.set_value(TAU*(8/4)),
        )
        self.wait()
        self.play(
            FadeOut(root_circle),
            FadeOut(e4_eq),
        )
        root_start.set_value(0)
        root_end.set_value(0)
        self.add(root_circle)

        e0_eq = Tex(r"e^{i\frac{0}{4}\tau}=cos(\frac{0}{4}\tau)+isin(\frac{0}{4}\tau)=1").scale(eq_scale).next_to(tau_complex, DOWN, buff=4.5)
        e1_eq = Tex(r"e^{i\frac{3}{4}\tau}=cos(\frac{3}{4}\tau)+isin(\frac{3}{4}\tau)=-1").scale(eq_scale).next_to(tau_complex, DOWN, buff=4.5)
        e2_eq = Tex(r"e^{i\frac{6}{4}\tau}=cos(\frac{6}{4}\tau)+isin(\frac{6}{4}\tau)=1").scale(eq_scale).next_to(tau_complex, DOWN, buff=4.5)
        e3_eq = Tex(r"e^{i\frac{9}{4}\tau}=cos(\frac{9}{4}\tau)+isin(\frac{9}{4}\tau)=-1").scale(eq_scale).next_to(tau_complex, DOWN, buff=4.5)
        e4_eq = Tex(r"e^{i\frac{12}{4}\tau}=cos(\frac{12}{4}\tau)+isin(\frac{12}{4}\tau)=1").scale(eq_scale).next_to(tau_complex, DOWN, buff=4.5)

        self.wait()
        self.play(
            FadeIn(e0_eq)
        )
        self.play(
            FadeOut(e0_eq), 
            FadeIn(e1_eq),
            root_end.animate.set_value(TAU*(3/4)),
        )
        self.play(
            root_start.animate.set_value(TAU*(3/4)),
        )
        self.wait()
        self.play(
            FadeOut(e1_eq), 
            FadeIn(e2_eq),
            root_end.animate.set_value(TAU*(6/4)),
        )
        self.play(
            root_start.animate.set_value(TAU*(6/4)),
        )
        self.wait()
        self.play(
            FadeOut(e2_eq), 
            FadeIn(e3_eq),
            root_end.animate.set_value(TAU*(9/4)),
        )
        self.play(
            root_start.animate.set_value(TAU*(9/4)),
        )
        self.wait()
        self.play(
            FadeOut(e3_eq), 
            FadeIn(e4_eq),
            root_end.animate.set_value(TAU*(12/4)),
        )
        self.play(
            root_start.animate.set_value(TAU*(12/4)),
        )
        self.wait()
        self.play(
            FadeOut(root_circle),
            FadeOut(e4_eq),
        )
        root_start.set_value(0)
        root_end.set_value(0)
        self.add(root_circle)

        e0_eq = Tex(r"e^{-i\frac{0}{4}\tau}=cos(\frac{0}{4}\tau)-isin(\frac{0}{4}\tau)=1").scale(eq_scale).next_to(tau_complex, DOWN, buff=4.5)
        e1_eq = Tex(r"e^{-i\frac{1}{4}\tau}=cos(\frac{1}{4}\tau)-isin(\frac{1}{4}\tau)=-i").scale(eq_scale).next_to(tau_complex, DOWN, buff=4.5)
        e2_eq = Tex(r"e^{-i\frac{2}{4}\tau}=cos(\frac{2}{4}\tau)-isin(\frac{2}{4}\tau)=-1").scale(eq_scale).next_to(tau_complex, DOWN, buff=4.5)
        e3_eq = Tex(r"e^{-i\frac{3}{4}\tau}=cos(\frac{3}{4}\tau)-isin(\frac{3}{4}\tau)=i").scale(eq_scale).next_to(tau_complex, DOWN, buff=4.5)
        e4_eq = Tex(r"e^{-i\frac{4}{4}\tau}=cos(\frac{4}{4}\tau)-isin(\frac{4}{4}\tau)=1").scale(eq_scale).next_to(tau_complex, DOWN, buff=4.5)

        self.add(root_circle)
        self.wait()
        self.play(
            FadeIn(e0_eq)
        )
        self.play(
            FadeOut(e0_eq), 
            FadeIn(e1_eq),
            root_end.animate.set_value(TAU*(-1/4)),
        )
        self.play(
            root_start.animate.set_value(TAU*(-1/4)),
        )
        self.wait()
        self.play(
            FadeOut(e1_eq), 
            FadeIn(e2_eq),
            root_end.animate.set_value(TAU*(-2/4)),
        )
        self.play(
            root_start.animate.set_value(TAU*(-2/4)),
        )
        self.wait()
        self.play(
            FadeOut(e2_eq), 
            FadeIn(e3_eq),
            root_end.animate.set_value(TAU*(-3/4)),
        )
        self.play(
            root_start.animate.set_value(TAU*(-3/4)),
        )
        self.wait()
        self.play(
            FadeOut(e3_eq), 
            FadeIn(e4_eq),
            root_end.animate.set_value(TAU*(-4/4)),
        )
        self.play(
            root_start.animate.set_value(TAU*(-4/4)),
        )
        self.wait()
        self.play(
            FadeOut(root_circle),
            FadeOut(e4_eq),
        )
        root_start.set_value(0)
        root_end.set_value(0)
        self.add(root_circle)

        self.play(
            FadeOut(root_circle),
            FadeOut(root_of_minus_1),
            FadeOut(root_of_1),
            FadeOut(arrow3),
            FadeOut(arrow4),
            FadeOut(arrow5),
            FadeOut(arrow6),
            FadeOut(four_root),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(new_root_group_1),
            FadeOut(new_root_group_2),
            FadeOut(operators),
            FadeOut(fourth_root[0]),
        )

        self.wait()
        three_root = Tex(r"\sqrt[3]{1}").next_to(tau_complex, DOWN, buff=0.5)
        one_of_3 = Tex(r"1")
        two_of_3 = Tex(r"g")
        three_of_3 = Tex(r"h")
        mod3_group = Group(one_of_3, two_of_3, three_of_3).arrange(RIGHT, buff =0.8).next_to(three_root, DOWN, buff=1)
        arrow1 = Arrow(
            three_root.get_bottom(),
            one_of_3.get_top()
        )
        arrow2 = Arrow(
            three_root.get_bottom(),
            two_of_3.get_top()
        )
        arrow3 = Arrow(
            three_root.get_bottom(),
            three_of_3.get_top()
        )
        arrows_top = Group(arrow1, arrow2, arrow3)
        third_root = make_roots(3).shift(RIGHT*left_shift)

        self.play(
            FadeIn(third_root),
            FadeIn(three_root),
        )
        self.wait()
        r = 1.2
        circle_root_1 = Tex(r"1").move_to(
            np.array([
                scale * r* np.sin(0),
                scale * r* np.cos(0),
                0
            ])
        ).shift(RIGHT*left_shift)
        circle_root_2 = Tex(r"g").move_to(
            np.array([
                scale * r* np.sin(TAU*(1/3)),
                scale * r* np.cos(TAU*(1/3)),
                0
            ])
        ).shift(RIGHT*left_shift)
        circle_root_3 = Tex(r"h").move_to(
            np.array([
                scale * r* np.sin(TAU*(2/3)),
                scale * r* np.cos(TAU*(2/3)),
                0
            ])
        ).shift(RIGHT*left_shift)
        circle_three = Group(circle_root_1,circle_root_2,circle_root_3)
        self.play(
            FadeIn(mod3_group),
            FadeIn(arrows_top),
            FadeIn(circle_three),
            FadeOut(third_root[1]),
            FadeOut(third_root[2]),
        )

        e0_eq = Tex(r"e^{-i\frac{0}{3}\tau}=cos(\frac{0}{3}\tau)-isin(\frac{0}{3}\tau)=1").scale(eq_scale).next_to(mod3_group, DOWN, buff=1)
        e1_eq = Tex(r"e^{-i\frac{1}{3}\tau}=cos(\frac{1}{3}\tau)-isin(\frac{1}{3}\tau)=g").scale(eq_scale).next_to(mod3_group, DOWN, buff=1)
        e2_eq = Tex(r"e^{-i\frac{2}{3}\tau}=cos(\frac{2}{3}\tau)-isin(\frac{2}{3}\tau)=h").scale(eq_scale).next_to(mod3_group, DOWN, buff=1)
        e3_eq = Tex(r"e^{-i\frac{3}{3}\tau}=cos(\frac{3}{3}\tau)-isin(\frac{3}{3}\tau)=1").scale(eq_scale).next_to(mod3_group, DOWN, buff=1)

        self.add(root_circle)
        self.wait()
        self.play(
            FadeIn(e0_eq)
        )
        self.play(
            FadeOut(e0_eq), 
            FadeIn(e1_eq),
            root_end.animate.set_value(TAU*(1/3)),
        )
        self.play(
            root_start.animate.set_value(TAU*(1/3)),
        )
        self.wait()
        self.play(
            FadeOut(e1_eq), 
            FadeIn(e2_eq),
            root_end.animate.set_value(TAU*(2/3)),
        )
        self.play(
            root_start.animate.set_value(TAU*(2/3)),
        )
        self.wait()
        self.play(
            FadeOut(e2_eq), 
            FadeIn(e3_eq),
            root_end.animate.set_value(TAU*(3/3)),
        )
        self.play(
            root_start.animate.set_value(TAU*(3/3)),
        )
        self.wait()
        self.play(
            FadeOut(root_circle),
            FadeOut(e3_eq),
        )
        root_start.set_value(0)
        root_end.set_value(0)

        e0_eq = Tex(r"e^{-i\frac{0}{3}\tau}=cos(\frac{0}{3}\tau)-isin(\frac{0}{3}\tau)=1").scale(eq_scale).next_to(mod3_group, DOWN, buff=1)
        e1_eq = Tex(r"e^{-i\frac{2}{3}\tau}=cos(\frac{2}{3}\tau)-isin(\frac{2}{3}\tau)=h").scale(eq_scale).next_to(mod3_group, DOWN, buff=1)
        e2_eq = Tex(r"e^{-i\frac{4}{3}\tau}=cos(\frac{4}{3}\tau)-isin(\frac{4}{3}\tau)=g").scale(eq_scale).next_to(mod3_group, DOWN, buff=1)
        e3_eq = Tex(r"e^{-i\frac{6}{3}\tau}=cos(\frac{6}{3}\tau)-isin(\frac{6}{3}\tau)=1").scale(eq_scale).next_to(mod3_group, DOWN, buff=1)

        self.add(root_circle)
        self.wait()
        self.play(
            FadeIn(e0_eq)
        )
        self.play(
            FadeOut(e0_eq), 
            FadeIn(e1_eq),
            root_end.animate.set_value(TAU*(2/3)),
        )
        self.play(
            root_start.animate.set_value(TAU*(2/3)),
        )
        self.wait()
        self.play(
            FadeOut(e1_eq), 
            FadeIn(e2_eq),
            root_end.animate.set_value(TAU*(4/3)),
        )
        self.play(
            root_start.animate.set_value(TAU*(4/3)),
        )
        self.wait()
        self.play(
            FadeOut(e2_eq), 
            FadeIn(e3_eq),
            root_end.animate.set_value(TAU*(6/3)),
        )
        self.play(
            root_start.animate.set_value(TAU*(6/3)),
        )
        self.wait()
        self.play(
            FadeOut(root_circle),
            FadeOut(e3_eq),
        )
        root_start.set_value(0)
        root_end.set_value(0)

        self.wait()
        self.play(
            FadeIn(third_root[1]),
        )

        real_dashed1 = DashedLine(
            np.array([scale*np.sin(TAU/3),scale*np.cos(TAU/3),0]),
            np.array([scale*np.sin(TAU/3),0,0]),
        ).set_color(YELLOW).shift(RIGHT*left_shift)
        imag_dashed1 = DashedLine(
            np.array([0,0,0]),
            np.array([scale*np.sin(TAU/3),0,0]),
        ).set_color(ORANGE).shift(RIGHT*left_shift)
        real_dashed2 = DashedLine(
            np.array([-scale*np.sin(TAU/6),-scale*np.cos(TAU/6),0]),
            np.array([-scale*np.sin(TAU/6),0,0]),
        ).set_color(YELLOW).shift(RIGHT*left_shift)
        imag_dashed2 = DashedLine(
            np.array([0,0,0]),
            np.array([-scale*np.sin(TAU/6),0,0]),
        ).set_color(ORANGE).shift(RIGHT*left_shift)
        one_dashed = DashedLine(
            np.array([0,0,0]),
            np.array([0,2,0]),
        ).set_color(YELLOW).shift(RIGHT*left_shift)

        euler = Tex(r"z = e^{i\theta}=cos\theta+isin\theta", tex_to_color_map={r"cos\theta":YELLOW,r"sin\theta":ORANGE}).next_to(z_euler_eq,DOWN,buff=0.5)
        euler.set_color_by_tex(r"cos\theta", YELLOW)
        euler.set_color_by_tex(r"sin\theta", ORANGE)
        self.wait()
        self.play(
            ShowCreation(real_dashed1),
            ShowCreation(imag_dashed1),
            ShowCreation(real_dashed2),
            ShowCreation(imag_dashed2),
            ShowCreation(one_dashed),
            FadeIn(euler.scale(0.7).next_to(mod3_group, DOWN, buff=0.5))
        )
        self.wait()

        root_scale = 0.7

        r=1
        imag_root_1 = Tex(r"1+0i").scale(0.6).next_to(
            np.array([
                scale * r* np.sin(0),
                scale * r* np.cos(0),
                0
            ]), UP
        ).shift(RIGHT*left_shift)
        imag_root_2 = Tex(r"-\frac{1}{2}+\frac{\sqrt{3}}{2}").scale(0.6).next_to(
            np.array([
                scale * r* np.sin(TAU*(1/3)),
                scale * r* np.cos(TAU*(1/3)),
                0
            ]), DR
        ).shift(RIGHT*left_shift)
        imag_root_3 = Tex(r"-\frac{1}{2}+\frac{\sqrt{3}}{2}").scale(0.6).next_to(
            np.array([
                scale * r* np.sin(TAU*(2/3)),
                scale * r* np.cos(TAU*(2/3)),
                0
            ]), DL
        ).shift(RIGHT*left_shift)
        imag_three = Group(imag_root_1,imag_root_2,imag_root_3)
        one_equals = Tex(r"1 = e^{\frac{0}{3}\tau} = 1 + 0i").scale(root_scale)
        g_equals = Tex(r"g = e^{\frac{1}{3}\tau} = -\frac{1}{2} + \frac{\sqrt{3}}{2}i").scale(root_scale)
        h_equals = Tex(r"h = e^{\frac{2}{3}\tau} = -\frac{1}{2} - \frac{\sqrt{3}}{2}i").scale(root_scale)
        gh_group = Group(one_equals, g_equals, h_equals).arrange(DOWN).next_to(euler, DOWN, buff=0.3)
        self.play(
            FadeIn(gh_group),
            FadeOut(mod3_group),
            FadeIn(imag_three),
        )
        self.wait()
        self.play(FadeOut(gh_group))
        self.wait()
        gh_times_e = Tex(
            r"g \cdot h = e^{i\theta_{g}} \cdot e^{i\theta_{h}} = e^{\left( \theta_{g}+\theta_{h}\right)}"
        ).next_to(euler, DOWN, buff=0.5).scale(root_scale)
        gh_times_imag = Tex(
            r"g \cdot h =", r"\left(-\frac{1}{2}+\frac{\sqrt{3}}{2}i\right)\left(-\frac{1}{2}-\frac{\sqrt{3}}{2}i\right)"
        ).next_to(gh_times_e, DOWN, buff=0.3).scale(root_scale)
        self.play(
            FadeIn(gh_times_e)
        )
        self.wait()
        self.play(
            FadeIn(gh_times_imag)
        )
        self.wait()

        algebra1 = Tex(
            r"g \cdot h =", r"\frac{1}{4}+\frac{\sqrt{3}}{4}-\frac{\sqrt{3}}{4}+\frac{3}{4}"
        ).scale(root_scale).move_to(gh_times_imag.get_center())
        self.play(
            ReplacementTransform(gh_times_imag, algebra1)
        )
        self.wait()
        algebra2 = Tex(
            r"g \cdot h =", r"1"
        ).scale(root_scale).move_to(algebra1.get_center(), DOWN)

        self.play(
            ReplacementTransform(algebra1, algebra2)
        )
        self.wait()

        r=1.3
        exp_root_1 = Tex(r"e^{i\frac{0}{3}\theta}").move_to(
            np.array([
                scale * r* np.sin(0),
                scale * r* np.cos(0),
                0
            ])
        ).shift(RIGHT*left_shift)
        exp_root_2 = Tex(r"e^{i\frac{1}{3}\theta}").move_to(
            np.array([
                scale * r* np.sin(TAU*(1/3)),
                scale * r* np.cos(TAU*(1/3)),
                0
            ])
        ).shift(RIGHT*left_shift)
        exp_root_3 = Tex(r"e^{i\frac{2}{3}\theta}").move_to(
            np.array([
                scale * r* np.sin(TAU*(2/3)),
                scale * r* np.cos(TAU*(2/3)),
                0
            ])
        ).shift(RIGHT*left_shift)
        exp_three = Group(exp_root_1,exp_root_2,exp_root_3)

        self.play(
            FadeIn(exp_three),
            FadeOut(circle_three),
        )
        self.wait()

        self.play(
            FadeOut(gh_times_e),
            FadeOut(algebra2),
        )
        self.wait()

        r=1
        xy_root_1 = Tex(r"(1,0)").scale(0.6).next_to(
            np.array([
                scale * r* np.sin(0),
                scale * r* np.cos(0),
                0
            ]), UP
        ).shift(RIGHT*left_shift)
        xy_root_2 = Tex(r"\left(-\frac{1}{2},\frac{\sqrt{3}}{2}\right)").scale(0.6).next_to(
            np.array([
                scale * r* np.sin(TAU*(1/3)),
                scale * r* np.cos(TAU*(1/3)),
                0
            ]), DR
        ).shift(RIGHT*left_shift)
        xy_root_3 = Tex(r"\left(-\frac{1}{2},-\frac{\sqrt{3}}{2}\right)").scale(0.6).next_to(
            np.array([
                scale * r* np.sin(TAU*(2/3)),
                scale * r* np.cos(TAU*(2/3)),
                0
            ]), DL
        ).shift(RIGHT*left_shift)
        xy_three = Group(xy_root_1,xy_root_2,xy_root_3)
        
        xy_map = {"x":YELLOW, "y": ORANGE}
        x_circ = Tex(r"x = Re\left(z\right) = cos\theta", tex_to_color_map = xy_map).scale(0.7).next_to(euler,DOWN,buff=0.8)
        y_circ = Tex(r"y = Im\left(z\right) = sin\theta", tex_to_color_map=xy_map).scale(0.7).next_to(x_circ,DOWN,buff=0.5)
        x_title = Tex(r"x", tex_to_color_map=xy_map).next_to(real, DOWN)
        y_title = Tex(r"y", tex_to_color_map=xy_map).next_to(imaginary, LEFT)
        self.play(
            FadeOut(exp_three),
            FadeIn(xy_three),
            FadeIn(x_circ),
            FadeIn(y_circ),
            FadeIn(x_title),
            FadeIn(y_title),
        )
        self.wait(3)
        self.play(
            FadeOut(xy_three),
            FadeOut(x_circ),
            FadeOut(y_circ),
            FadeOut(x_title),
            FadeOut(y_title),
            FadeOut(real_dashed1),
            FadeOut(real_dashed2),
            FadeOut(imag_dashed1),
            FadeOut(imag_dashed2),
            FadeOut(one_dashed),
            FadeOut(euler),
            FadeOut(mod3_group),
            FadeOut(arrows_top),
            FadeOut(three_root),
            FadeOut(third_root[0]),
            FadeOut(third_root[1]),
        )
        self.wait()
        general_root = Tex(r"\sqrt[n]{1} = e^{i\frac{k}{n}\tau}").scale(1.5).next_to(tau_complex, DOWN, buff=1)
        n_def = Tex(r"n="+r"\text{modulus}").next_to(general_root,DOWN, buff=0.4)
        k_def = Tex(r"k="+r"\text{root}").next_to(n_def,DOWN, buff=0.4)
        self.play(
            FadeIn(general_root)
        )
        self.wait()
        r=1.3
        k_equals = Tex(r"k\in \mathbb{Z} \left( mod5 \right)").scale(0.7).next_to(k_def, DOWN, buff=0.7)
        z_equals = Tex(r"\mathbb{Z} = \left\{ ...,-2,-1,0,1,2,... \right\}").scale(0.7).next_to(k_equals, DOWN, buff=0.4)
        self.play(
            FadeIn(n_def)
        )
        self.wait()
        self.play(
            FadeIn(k_def)
        )
        self.wait()
        self.play(
            FadeIn(k_equals)
        )
        self.wait()
        self.play(
            FadeIn(z_equals)
        )
        self.wait(3)

class VBMEulerContinued(Scene):
    def construct(self):
        frame = self.camera.frame
        scale = 2

        circle1 = ParametricCurve(
            lambda u: np.array([
                np.sin(u),
                np.cos(u),
                0
            ]),
            color = WHITE,
            t_range = np.array([-PI, PI, 0.01])
        ).scale(scale).set_stroke(width=4)
        
        axes = NumberPlane().scale(2)
        euler_group = Group()
        
        r = 1.3
        left_shift = 3.1
        
        arrow_angle = ValueTracker(0)
        t2c = {
            "1":RED, "4":RED, "7":RED,
            "2":BLUE, "5":BLUE, "8":BLUE,
            "3":GREEN, "6":GREEN, "0":GREEN,
        }
        for i in range(0,9):
            if i == 0:
                euler_equation  = Tex(r"e^{i\frac{" + str(9) + "}{9}"+r"\tau}", tex_to_color_map = t2c)
                euler_equation[2].set_color(GREEN)
            else:
                euler_equation  = Tex(r"e^{i\frac{" + str(i) + "}{9}"+r"\tau}", tex_to_color_map = t2c)

            euler_equation.shift(
                [
                    scale * r*np.sin(TAU * (i/9)),
                    scale * r*np.cos(TAU * (i/9)),
                    0
                ]            
            )
            euler_group.add(euler_equation)
        euler_group.shift(RIGHT*left_shift)
        eisel = Rectangle(width=6.2,height=10,color=BLACK)
        eisel.move_to(4.05*LEFT).set_fill(BLACK).set_opacity(1.0)
        def make_roots(num_roots,scale):
            dot_group = Group()
            line_group = Group()
            eq_group = Group()
            total = Group()
            for i in range(0,num_roots):
                dot = Dot(np.array([
                    scale * np.sin(TAU*(i/num_roots)),
                    scale * np.cos(TAU*(i/num_roots)),
                    0
                ]))
                line = Line(
                    np.array([0,0,0]),
                    np.array([
                        scale * np.sin(TAU*(i/num_roots)),
                        scale * np.cos(TAU*(i/num_roots)),
                        0
                    ])
                )
                eq = Tex(r"e^{i\frac{" + str(i) + r"}{" + str(num_roots) + r"}\tau}")
                eq.shift([
                    scale * r*np.sin(TAU * (i/num_roots)),
                    scale * r*np.cos(TAU * (i/num_roots)),
                    0
                ])
                dot_group.add(dot)
                line_group.add(line)
                eq_group.add(eq)
            total.add(dot_group, line_group)
            return total
        real = Tex(r"Re").move_to([0,3.5,0]).shift(RIGHT*left_shift)
        imaginary = Tex(r"Im").move_to([3.5,0,0]).shift(RIGHT*left_shift)
        roots_title = Tex(r"\textsc{Roots of Unity}").move_to(eisel).shift(UP*3.3).scale(1.3)
        tau_complex = Tex(r"z = e^{i\tau}=1").next_to(roots_title,DOWN,buff=0.5).scale(1.3)
        axes.shift(RIGHT*left_shift),
        circle1.shift(RIGHT*left_shift),

        self.add(circle1, axes, eisel, real, imaginary, roots_title, tau_complex)

        self.wait(1)
        ninth_root = make_roots(9,2).shift(RIGHT*left_shift)
        ninth_root_copy = make_roots(9,2).shift(RIGHT*left_shift)
        euler_group_copy = euler_group.copy()
        triangle_ninth_root_numbers = Group(*euler_group_copy[0::3])
        triangle_ninth_root_lines = Group(*ninth_root_copy[1][0::3])
        triangle_ninth_root_dots = Group(*ninth_root_copy[0][0::3])
        triangle_ninth_root = Group(
            triangle_ninth_root_dots,
            triangle_ninth_root_lines,
            triangle_ninth_root_numbers,
        )
        nine_root_eq = Tex(r"\sqrt[9]{1}").next_to(tau_complex, DOWN, buff=0.8)
        third_root_eq = Tex(r"\sqrt[3]{1}").next_to(tau_complex, DOWN, buff=0.8)

        self.play(
            FadeIn(nine_root_eq),
        )
        self.wait()
        self.play(
            FadeIn(euler_group), 
            FadeIn(ninth_root),
            FadeIn(triangle_ninth_root),
        )
        self.wait()
        self.play(
            FadeOut(ninth_root),
            FadeOut(euler_group),
            ReplacementTransform(nine_root_eq, third_root_eq),
        )
        self.wait()


        r = 1.2
        circle_root_1 = Tex(r"1").move_to(
            np.array([
                scale * r* np.sin(0),
                scale * r* np.cos(0),
                0
            ])
        ).shift(RIGHT*left_shift)
        circle_root_2 = Tex(r"g").move_to(
            np.array([
                scale * r* np.sin(TAU*(1/3)),
                scale * r* np.cos(TAU*(1/3)),
                0
            ])
        ).shift(RIGHT*left_shift)
        circle_root_3 = Tex(r"h").move_to(
            np.array([
                scale * r* np.sin(TAU*(2/3)),
                scale * r* np.cos(TAU*(2/3)),
                0
            ])
        ).shift(RIGHT*left_shift)
        circle_three = Group(circle_root_1,circle_root_2,circle_root_3)


        one_of_3 = Tex(r"1")
        two_of_3 = Tex(r"g")
        three_of_3 = Tex(r"h")
        one_of_3_replace = Tex(r"\sqrt[3]{1}")
        two_of_3_replace = Tex(r"\sqrt[3]{g}")
        three_of_3_replace = Tex(r"\sqrt[3]{h}")
        mod3_group = Group(one_of_3, two_of_3, three_of_3).arrange(RIGHT, buff =1.6).next_to(third_root_eq, DOWN, buff=1)
        mod3_replace_group = Group(one_of_3_replace, two_of_3_replace, three_of_3_replace).arrange(RIGHT, buff =1.4).next_to(third_root_eq, DOWN, buff=1)

        arrow1 = Arrow(
            third_root_eq.get_bottom(),
            one_of_3.get_top()
        )
        arrow2 = Arrow(
            third_root_eq.get_bottom(),
            two_of_3.get_top()
        )
        arrow3 = Arrow(
            third_root_eq.get_bottom(),
            three_of_3.get_top()
        )
        arrows_top = Group(arrow1, arrow2, arrow3)
        self.wait()
        self.play(
            ReplacementTransform(triangle_ninth_root_numbers, circle_three),
            ShowCreation(arrows_top),
            ShowCreation(mod3_group)
        )
        third_of_third_root_eq = Tex(r"\sqrt[3]{\sqrt[3]{1}}").scale(0.8).next_to(tau_complex, DOWN, buff=0.5)
        self.wait()
        self.play(
            ReplacementTransform(third_root_eq, third_of_third_root_eq)
        )
        self.wait()
        self.play(
            ReplacementTransform(mod3_group, mod3_replace_group)
        )
        self.wait()
        nine_root_eq = Tex(r"\sqrt[9]{1}").next_to(tau_complex, DOWN, buff=0.7)

        self.play(
            ReplacementTransform(third_of_third_root_eq, nine_root_eq)
        )
        self.wait()
        one_of_3_copy = Tex(r"1")
        two_of_3_copy = Tex(r"g")
        three_of_3_copy = Tex(r"h")

        mod3_copy_group = Group(one_of_3_copy, two_of_3_copy, three_of_3_copy).arrange(RIGHT, buff =0.3).next_to(one_of_3, DOWN, buff=1)
        arrow4 = Arrow(
            one_of_3.get_bottom(),
            one_of_3_copy.get_top(),
            stroke_width = 0.1
        )
        arrow5 = Arrow(
            one_of_3.get_bottom(),
            two_of_3_copy.get_top()
        )
        arrow6 = Arrow(
            one_of_3.get_bottom(),
            three_of_3_copy.get_top()
        )
        arrows_top_2 = Group(arrow4, arrow5, arrow6)
        self.wait()
        self.play(
            FadeIn(arrows_top_2),
            FadeIn(mod3_copy_group),
        )
        first_family_numbers = Group(*euler_group_copy[1::3])
        first_family_lines = Group(*ninth_root_copy[1][1::3])
        first_family_dots = Group(*ninth_root_copy[0][1::3])
        first_family = Group(
            first_family_dots,
            first_family_lines,
            first_family_numbers,
        )
        self.wait()
        gamma1 = Tex(r"\gamma_{1}")
        gamma2 = Tex(r"\gamma_{2}")
        gamma3 = Tex(r"\gamma_{3}")
        gamma1[1].scale(0.6)
        gamma2[1].scale(0.6)
        gamma3[1].scale(0.6)
        gamma_group = Group(gamma1, gamma2, gamma3).arrange(RIGHT, buff =0.2).next_to(two_of_3, DOWN, buff=1)
        gamma1_copy = Tex(r"\gamma_{1}").move_to(
            np.array([
                scale * r* np.sin(TAU*(1/9)),
                scale * r* np.cos(TAU*(1/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        gamma2_copy = Tex(r"\gamma_{2}").move_to(
            np.array([
                scale * r* np.sin(TAU*(4/9)),
                scale * r* np.cos(TAU*(4/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        gamma3_copy = Tex(r"\gamma_{3}").move_to(
            np.array([
                scale * r* np.sin(TAU*(7/9)),
                scale * r* np.cos(TAU*(7/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        gamma1_copy[1].scale(0.6)
        gamma2_copy[1].scale(0.6)
        gamma3_copy[1].scale(0.6)
        gamma_copy_group = Group(gamma1_copy, gamma2_copy, gamma3_copy)
        arrow7 = Arrow(
            two_of_3.get_bottom(),
            gamma1.get_top(),
        )
        arrow8 = Arrow(
            two_of_3.get_bottom(),
            gamma2.get_top(),
        )
        arrow9 = Arrow(
            two_of_3.get_bottom(),
            gamma3.get_top(),
        )
        arrows_top_3 = Group(arrow7, arrow8, arrow9)
        self.wait()
        self.play(
            FadeIn(gamma_copy_group),
            FadeIn(first_family[1]),
            FadeIn(first_family[0]),
            FadeIn(arrows_top_3),
            FadeIn(gamma_group),
        )
        self.wait()
        self.play(
            FadeOut(gamma_copy_group), 
            FadeOut(first_family[1]),
            FadeOut(first_family[0]),
        )
        def parametric_wedge(start, end, scale):
            wedge = ParametricSurface(
                lambda u, v: np.array([
                    v * np.sin(u),
                    v * np.cos(u),
                    0
                ]),
                u_range = (start,end),
                v_range = (0,scale),
            ).set_opacity(0.8)
            return wedge

        start_tracker = ValueTracker(0)
        end_tracker = ValueTracker(0)
        gamma_wedge = always_redraw(lambda: parametric_wedge(
            start_tracker.get_value(),
            end_tracker.get_value(),
            2
        ).set_color(RED).shift(RIGHT*left_shift))

        gamma1_letter = Tex(r"\gamma_{1}^{1}").move_to(
            np.array([
                scale * r* np.sin(TAU*(1/9)),
                scale * r* np.cos(TAU*(1/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        gamma2_letter = Tex(r"\gamma_{1}^{2}").move_to(
            np.array([
                scale * r* np.sin(TAU*(2/9)),
                scale * r* np.cos(TAU*(2/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        gamma3_letter = Tex(r"\gamma_{1}^{3}").move_to(
            np.array([
                scale * (r+0.24) * np.sin(TAU*(3/9)),
                scale * (r+0.24) * np.cos(TAU*(3/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        gamma1_letter[1].scale(0.8)
        gamma2_letter[1].scale(0.8)
        gamma3_letter[1].scale(0.8)
        gamma1_letter[2].scale(0.6)
        gamma2_letter[2].scale(0.6)
        gamma3_letter[2].scale(0.6)

        self.wait()
        self.add(gamma_wedge)
        self.play(
            start_tracker.animate.set_value((1/9)*TAU)
        )
        self.play(
            FadeIn(gamma1_letter),
            FadeIn(ninth_root[0][1]),
        )
        self.wait()
        self.play(
            end_tracker.animate.set_value((1/9)*TAU)
        )
        self.play(
            start_tracker.animate.set_value((2/9)*TAU)
        )
        self.play(
            FadeIn(gamma2_letter),
            FadeIn(ninth_root[0][2]),
        )
        self.wait()
        self.play(
            end_tracker.animate.set_value((2/9)*TAU)
        )
        self.play(
            start_tracker.animate.set_value((3/9)*TAU)
        )
        self.play(
            FadeIn(gamma3_letter),
            FadeIn(ninth_root[0][3]),
        )
        self.wait()
        self.play(
            end_tracker.animate.set_value((3/9)*TAU)
        )
        self.remove(gamma_wedge)
        start_tracker.set_value(0)
        end_tracker.set_value(0)
        self.wait()
        
        self.play(
            FadeOut(gamma1_letter),
            FadeOut(gamma2_letter),
            FadeOut(gamma3_letter),
            FadeOut(ninth_root[0][1]),
            FadeOut(ninth_root[0][2]),
            FadeOut(ninth_root[0][3]),
        )
        self.wait()


        gamma4_letter = Tex(r"\gamma_{2}^{1}").move_to(
            np.array([
                scale * r* np.sin(TAU*(4/9)),
                scale * r* np.cos(TAU*(4/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        gamma5_letter = Tex(r"\gamma_{2}^{2}").move_to(
            np.array([
                scale * r* np.sin(TAU*(8/9)),
                scale * r* np.cos(TAU*(8/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        gamma6_letter = Tex(r"\gamma_{2}^{3}").move_to(
            np.array([
                scale * (r+0.24) * np.sin(TAU*(3/9)),
                scale * (r+0.24) * np.cos(TAU*(3/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        gamma4_letter[1].scale(0.8)
        gamma5_letter[1].scale(0.8)
        gamma6_letter[1].scale(0.8)
        gamma4_letter[2].scale(0.6)
        gamma5_letter[2].scale(0.6)
        gamma6_letter[2].scale(0.6)

        self.add(gamma_wedge)
        self.play(
            start_tracker.animate.set_value((4/9)*TAU)
        )
        self.play(
            FadeIn(gamma4_letter),
            FadeIn(ninth_root[0][4]),
        )
        self.wait()
        self.play(
            end_tracker.animate.set_value((4/9)*TAU)
        )
        self.play(
            start_tracker.animate.set_value((8/9)*TAU)
        )
        self.play(
            FadeIn(gamma5_letter),
            FadeIn(ninth_root[0][8]),
        )
        self.wait()
        self.play(
            end_tracker.animate.set_value((8/9)*TAU)
        )
        self.play(
            start_tracker.animate.set_value((12/9)*TAU)
        )
        self.play(
            FadeIn(gamma6_letter),
            FadeIn(ninth_root[0][3]),
        )
        self.wait()
        self.play(
            end_tracker.animate.set_value((12/9)*TAU)
        )
        self.remove(gamma_wedge)
        start_tracker.set_value(0)
        end_tracker.set_value(0)
        self.wait()
        
        self.play(
            FadeOut(gamma4_letter),
            FadeOut(gamma5_letter),
            FadeOut(gamma6_letter),
            FadeOut(ninth_root[0][4]),
            FadeOut(ninth_root[0][8]),
            FadeOut(ninth_root[0][3]),
        )
        self.wait()

        gamma7_letter = Tex(r"\gamma_{3}^{1}").move_to(
            np.array([
                scale * r* np.sin(TAU*(7/9)),
                scale * r* np.cos(TAU*(7/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        gamma8_letter = Tex(r"\gamma_{3}^{2}").move_to(
            np.array([
                scale * r* np.sin(TAU*(5/9)),
                scale * r* np.cos(TAU*(5/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        gamma9_letter = Tex(r"\gamma_{3}^{3}").move_to(
            np.array([
                scale * (r+0.24) * np.sin(TAU*(3/9)),
                scale * (r+0.24) * np.cos(TAU*(3/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        gamma7_letter[1].scale(0.8)
        gamma8_letter[1].scale(0.8)
        gamma9_letter[1].scale(0.8)
        gamma7_letter[2].scale(0.6)
        gamma8_letter[2].scale(0.6)
        gamma9_letter[2].scale(0.6)

        self.add(gamma_wedge)
        self.play(
            start_tracker.animate.set_value((7/9)*TAU)
        )
        self.play(
            FadeIn(gamma7_letter),
            FadeIn(ninth_root[0][7]),
        )
        self.wait()
        self.play(
            end_tracker.animate.set_value((7/9)*TAU)
        )
        self.play(
            start_tracker.animate.set_value((14/9)*TAU)
        )
        self.play(
            FadeIn(gamma8_letter),
            FadeIn(ninth_root[0][5]),
        )
        self.wait()
        self.play(
            end_tracker.animate.set_value((14/9)*TAU)
        )
        self.play(
            start_tracker.animate.set_value((21/9)*TAU)
        )
        self.play(
            FadeIn(gamma9_letter),
            FadeIn(ninth_root[0][3]),
        )
        self.wait()
        self.play(
            end_tracker.animate.set_value((21/9)*TAU)
        )
        self.remove(gamma_wedge)
        start_tracker.set_value(0)
        end_tracker.set_value(0)
        self.wait()
        
        self.play(
            FadeOut(gamma7_letter),
            FadeOut(gamma8_letter),
            FadeOut(gamma9_letter),
            FadeOut(ninth_root[0][7]),
            FadeOut(ninth_root[0][5]),
            FadeOut(ninth_root[0][3]),
        )
        self.wait()

    #############
        second_family_numbers = Group(*euler_group_copy[2::3])
        second_family_lines = Group(*ninth_root_copy[1][2::3])
        second_family_dots = Group(*ninth_root_copy[0][2::3])
        second_family = Group(
            second_family_dots,
            second_family_lines,
            second_family_numbers,
        )
        eta1 = Tex(r"\eta_{1}")
        eta2 = Tex(r"\eta_{2}")
        eta3 = Tex(r"\eta_{3}")
        eta1[1].scale(0.6)
        eta2[1].scale(0.6)
        eta3[1].scale(0.6)
        eta_group = Group(eta1, eta2, eta3).arrange(RIGHT, buff =0.2).next_to(three_of_3, DOWN, buff=1)
        eta1_copy = Tex(r"\eta_{1}").move_to(
            np.array([
                scale * r* np.sin(TAU*(8/9)),
                scale * r* np.cos(TAU*(8/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        eta2_copy = Tex(r"\eta_{2}").move_to(
            np.array([
                scale * r* np.sin(TAU*(5/9)),
                scale * r* np.cos(TAU*(5/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        eta3_copy = Tex(r"\eta_{3}").move_to(
            np.array([
                scale * r* np.sin(TAU*(2/9)),
                scale * r* np.cos(TAU*(2/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        eta1_copy[1].scale(0.6)
        eta2_copy[1].scale(0.6)
        eta3_copy[1].scale(0.6)
        eta_copy_group = Group(eta1_copy, eta2_copy, eta3_copy)
        arrow7 = Arrow(
            three_of_3.get_bottom(),
            eta1.get_top(),
        )
        arrow8 = Arrow(
            three_of_3.get_bottom(),
            eta2.get_top(),
        )
        arrow9 = Arrow(
            three_of_3.get_bottom(),
            eta3.get_top(),
        )
        arrows_top_3 = Group(arrow7, arrow8, arrow9)

        eta1_letter = Tex(r"\eta_{1}^{1}").move_to(
            np.array([
                scale * r* np.sin(TAU*(8/9)),
                scale * r* np.cos(TAU*(8/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        eta2_letter = Tex(r"\eta_{1}^{2}").move_to(
            np.array([
                scale * r* np.sin(TAU*(7/9)),
                scale * r* np.cos(TAU*(7/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        eta3_letter = Tex(r"\eta_{1}^{3}").move_to(
            np.array([
                scale * (r+0.24) * np.sin(TAU*(6/9)),
                scale * (r+0.24) * np.cos(TAU*(6/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        eta1_letter[1].scale(0.8)
        eta2_letter[1].scale(0.8)
        eta3_letter[1].scale(0.8)
        eta1_letter[2].scale(0.6)
        eta2_letter[2].scale(0.6)
        eta3_letter[2].scale(0.6)

        self.wait()
        self.play(
            FadeIn(eta_copy_group),
            FadeIn(second_family[1]),
            FadeIn(second_family[0]),
            FadeIn(arrows_top_3),
            FadeIn(eta_group),
        )
        self.wait()
        self.play(
            FadeOut(eta_copy_group), 
            FadeOut(second_family[1]),
            FadeOut(second_family[0]),
        )
        def parametric_wedge(start, end, scale):
            wedge = ParametricSurface(
                lambda u, v: np.array([
                    v * np.sin(u),
                    v * np.cos(u),
                    0
                ]),
                u_range = (start,end),
                v_range = (0,scale),
            ).set_opacity(0.8)
            return wedge

        start_tracker = ValueTracker(0)
        end_tracker = ValueTracker(0)
        eta_wedge = always_redraw(lambda: parametric_wedge(
            start_tracker.get_value(),
            end_tracker.get_value(),
            2
        ).set_color(BLUE).shift(RIGHT*left_shift))

        self.wait()
        self.add(eta_wedge)
        self.play(
            start_tracker.animate.set_value((8/9)*TAU)
        )
        self.play(
            FadeIn(eta1_letter),
            FadeIn(ninth_root[0][8]),
        )
        self.wait()
        self.play(
            end_tracker.animate.set_value((8/9)*TAU)
        )
        self.play(
            start_tracker.animate.set_value((16/9)*TAU)
        )
        self.play(
            FadeIn(eta2_letter),
            FadeIn(ninth_root[0][7]),
        )
        self.wait()
        self.play(
            end_tracker.animate.set_value((16/9)*TAU)
        )
        self.play(
            start_tracker.animate.set_value((24/9)*TAU)
        )
        self.play(
            FadeIn(eta3_letter),
            FadeIn(ninth_root[0][6]),
        )
        self.wait()
        self.play(
            end_tracker.animate.set_value((24/9)*TAU)
        )
        self.remove(eta_wedge)
        start_tracker.set_value(0)
        end_tracker.set_value(0)
        self.wait()
        
        self.play(
            FadeOut(eta1_letter),
            FadeOut(eta2_letter),
            FadeOut(eta3_letter),
            FadeOut(ninth_root[0][8]),
            FadeOut(ninth_root[0][7]),
            FadeOut(ninth_root[0][6]),
        )
        self.wait()


        eta4_letter = Tex(r"\eta_{2}^{1}").move_to(
            np.array([
                scale * r* np.sin(TAU*(5/9)),
                scale * r* np.cos(TAU*(5/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        eta5_letter = Tex(r"\eta_{2}^{2}").move_to(
            np.array([
                scale * r* np.sin(TAU*(1/9)),
                scale * r* np.cos(TAU*(1/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        eta6_letter = Tex(r"\eta_{2}^{3}").move_to(
            np.array([
                scale * (r+0.24) * np.sin(TAU*(6/9)),
                scale * (r+0.24) * np.cos(TAU*(6/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        eta4_letter[1].scale(0.8)
        eta5_letter[1].scale(0.8)
        eta6_letter[1].scale(0.8)
        eta4_letter[2].scale(0.6)
        eta5_letter[2].scale(0.6)
        eta6_letter[2].scale(0.6)
        self.add(eta_wedge)
        self.play(
            start_tracker.animate.set_value((5/9)*TAU)
        )
        self.play(
            FadeIn(eta4_letter),
            FadeIn(ninth_root[0][5]),
        )
        self.wait()
        self.play(
            end_tracker.animate.set_value((5/9)*TAU)
        )
        self.play(
            start_tracker.animate.set_value((10/9)*TAU)
        )
        self.play(
            FadeIn(eta5_letter),
            FadeIn(ninth_root[0][1]),
        )
        self.wait()
        self.play(
            end_tracker.animate.set_value((10/9)*TAU)
        )
        self.play(
            start_tracker.animate.set_value((15/9)*TAU)
        )
        self.play(
            FadeIn(eta6_letter),
            FadeIn(ninth_root[0][6]),
        )
        self.wait()
        self.play(
            end_tracker.animate.set_value((15/9)*TAU)
        )
        self.remove(eta_wedge)
        start_tracker.set_value(0)
        end_tracker.set_value(0)
        self.wait()
        
        self.play(
            FadeOut(eta4_letter),
            FadeOut(eta5_letter),
            FadeOut(eta6_letter),
            FadeOut(ninth_root[0][5]),
            FadeOut(ninth_root[0][1]),
            FadeOut(ninth_root[0][6]),
        )
        self.wait()


        eta7_letter = Tex(r"\eta_{3}^{1}").move_to(
            np.array([
                scale * r* np.sin(TAU*(2/9)),
                scale * r* np.cos(TAU*(2/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        eta8_letter = Tex(r"\eta_{3}^{2}").move_to(
            np.array([
                scale * r* np.sin(TAU*(4/9)),
                scale * r* np.cos(TAU*(4/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        eta9_letter = Tex(r"\eta_{3}^{3}").move_to(
            np.array([
                scale * (r+0.24) * np.sin(TAU*(6/9)),
                scale * (r+0.24) * np.cos(TAU*(6/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        eta7_letter[1].scale(0.8)
        eta8_letter[1].scale(0.8)
        eta9_letter[1].scale(0.8)
        eta7_letter[2].scale(0.6)
        eta8_letter[2].scale(0.6)
        eta9_letter[2].scale(0.6)
        self.add(eta_wedge)
        self.play(
            start_tracker.animate.set_value((2/9)*TAU)
        )
        self.play(
            FadeIn(eta7_letter),
            FadeIn(ninth_root[0][2]),
        )
        self.wait()
        self.play(
            end_tracker.animate.set_value((2/9)*TAU)
        )
        self.play(
            start_tracker.animate.set_value((4/9)*TAU)
        )
        self.play(
            FadeIn(eta8_letter),
            FadeIn(ninth_root[0][4]),
        )
        self.wait()
        self.play(
            end_tracker.animate.set_value((4/9)*TAU)
        )
        self.play(
            start_tracker.animate.set_value((6/9)*TAU)
        )
        self.play(
            FadeIn(eta9_letter),
            FadeIn(ninth_root[0][6]),
        )
        self.wait()
        self.play(
            end_tracker.animate.set_value((6/9)*TAU)
        )
        self.remove(eta_wedge)
        start_tracker.set_value(0)
        end_tracker.set_value(0)
        self.wait()
        
        self.play(
            FadeOut(eta7_letter),
            FadeOut(eta8_letter),
            FadeOut(eta9_letter),
            FadeOut(ninth_root[0][2]),
            FadeOut(ninth_root[0][4]),
            FadeOut(ninth_root[0][6]),
        )
        self.wait()
        self.play(
            FadeIn(first_family[1]),
            FadeIn(first_family[0]),
            FadeIn(second_family[1]),
            FadeIn(second_family[0]),
            FadeIn(gamma_copy_group),
            FadeIn(eta_copy_group),
        )
        self.wait(2)

class ComplexConjugate(Scene):
    def construct(self):
        frame = self.camera.frame
        scale = 2
        r = 1.3
        left_shift = 3.1
        def make_roots(num_roots,scale):
            dot_group = Group()
            line_group = Group()
            eq_group = Group()
            total = Group()
            for i in range(0,num_roots):
                dot = Dot(np.array([
                    scale * np.sin(TAU*(i/num_roots)),
                    scale * np.cos(TAU*(i/num_roots)),
                    0
                ]))
                line = Line(
                    np.array([0,0,0]),
                    np.array([
                        scale * np.sin(TAU*(i/num_roots)),
                        scale * np.cos(TAU*(i/num_roots)),
                        0
                    ])
                )
                eq = Tex(r"e^{i\frac{" + str(i) + r"}{" + str(num_roots) + r"}\tau}")
                eq.shift([
                    scale * r*np.sin(TAU * (i/num_roots)),
                    scale * r*np.cos(TAU * (i/num_roots)),
                    0
                ])
                dot_group.add(dot)
                line_group.add(line)
                eq_group.add(eq)
            total.add(dot_group, line_group)
            return total
        circle1 = ParametricCurve(
            lambda u: np.array([
                np.sin(u),
                np.cos(u),
                0
            ]),
            color = WHITE,
            t_range = np.array([-PI, PI, 0.01])
        ).scale(scale).set_stroke(width=4).shift(RIGHT*left_shift)
        
        axes = NumberPlane().scale(2).shift(RIGHT*left_shift)
        euler_group = Group()
        
        arrow_angle = ValueTracker(0)
        t2c = {
            "1":RED, "4":RED, "7":RED,
            "2":BLUE, "5":BLUE, "8":BLUE,
            "3":GREEN, "6":GREEN, "0":GREEN,
        }
        ninth_root = make_roots(9,2).shift(RIGHT*left_shift)
        eisel = Rectangle(width=6.2,height=10,color=BLACK)
        eisel.move_to(4.05*LEFT).set_fill(BLACK).set_opacity(1.0)

        eta1_copy = Tex(r"\eta_{1}").move_to(
            np.array([
                scale * r* np.sin(TAU*(8/9)),
                scale * r* np.cos(TAU*(8/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        eta2_copy = Tex(r"\eta_{2}").move_to(
            np.array([
                scale * r* np.sin(TAU*(5/9)),
                scale * r* np.cos(TAU*(5/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        eta3_copy = Tex(r"\eta_{3}").move_to(
            np.array([
                scale * r* np.sin(TAU*(2/9)),
                scale * r* np.cos(TAU*(2/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        eta1_copy[1].scale(0.6)
        eta2_copy[1].scale(0.6)
        eta3_copy[1].scale(0.6)
        gamma1_copy = Tex(r"\gamma_{1}").move_to(
            np.array([
                scale * r* np.sin(TAU*(1/9)),
                scale * r* np.cos(TAU*(1/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        gamma2_copy = Tex(r"\gamma_{2}").move_to(
            np.array([
                scale * r* np.sin(TAU*(4/9)),
                scale * r* np.cos(TAU*(4/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        gamma3_copy = Tex(r"\gamma_{3}").move_to(
            np.array([
                scale * r* np.sin(TAU*(7/9)),
                scale * r* np.cos(TAU*(7/9)),
                0
            ])
        ).shift(RIGHT*left_shift)
        gamma1_copy[1].scale(0.6)
        gamma2_copy[1].scale(0.6)
        gamma3_copy[1].scale(0.6)
        gamma_copy_group = Group(gamma1_copy, gamma2_copy, gamma3_copy)
        eta_copy_group = Group(eta1_copy, eta2_copy, eta3_copy)
        circle_root_1 = Tex(r"1").move_to(
            np.array([
                scale * r* np.sin(0),
                scale * r* np.cos(0),
                0
            ])
        ).shift(RIGHT*left_shift)
        circle_root_2 = Tex(r"g").move_to(
            np.array([
                scale * r* np.sin(TAU*(1/3)),
                scale * r* np.cos(TAU*(1/3)),
                0
            ])
        ).shift(RIGHT*left_shift)
        circle_root_3 = Tex(r"h").move_to(
            np.array([
                scale * r* np.sin(TAU*(2/3)),
                scale * r* np.cos(TAU*(2/3)),
                0
            ])
        ).shift(RIGHT*left_shift)
        circle_three = Group(circle_root_1,circle_root_2,circle_root_3)
        real = Tex(r"Re").move_to([0,3.5,0]).shift(RIGHT*left_shift)
        imaginary = Tex(r"Im").move_to([3.5,0,0]).shift(RIGHT*left_shift)

        self.add(
            axes,
            eisel,
            real,
            imaginary,
            circle1,
            eta_copy_group,
            gamma_copy_group,
            ninth_root[0],
            ninth_root[1],
            circle_three,
        )
        self.wait()
        conjugate_title = Tex(r"\textsc{Complex Conjugate}").move_to(eisel).shift(UP*3.3)
        self.play(
            FadeIn(conjugate_title)
        )
        conj_eq1 = Tex(r"z = x + iy").next_to(conjugate_title, DOWN, buff=0.7)
        conj_eq2 = Tex(r"\bar{z}= x - iy").next_to(conj_eq1, DOWN, buff=0.4)
        self.play(
            FadeIn(conj_eq1)
        )
        self.wait()
        self.play(
            FadeIn(conj_eq2)
        )
        conj_add_eq = Tex(r"z+\bar{z}=2x").scale(0.7)
        conj_minus_eq = Tex(r"z-\bar{z}=2y").scale(0.7)
        conj_group_1 = Group(conj_add_eq, conj_minus_eq).arrange(RIGHT, buff=0.8).next_to(conj_eq2, DOWN, buff=0.5)
        self.wait()
        self.play(
            FadeIn(conj_group_1)
        )
        real_eq1 = Tex(r"\frac{z+\bar{z}}{2}=Re(z)").scale(0.6).next_to(conj_add_eq, DOWN, buff = 0.5)
        real_eq2 = Tex(r"\frac{z-\bar{z}}{2}=Im(z)").scale(0.6).next_to(conj_minus_eq, DOWN, buff = 0.5)
        real_eq_group = Group(real_eq1, real_eq2)
        self.wait()
        self.play(
            FadeIn(real_eq1)
        )
        self.wait()
        self.play(
            FadeIn(real_eq2)
        )
        mult_eq = Tex(r"z\bar{z}=x^2+y^2=\left|z\right|^{2}").scale(0.7).next_to(real_eq_group, DOWN, buff = 0.7)
        self.wait()
        self.play(Write(mult_eq))
        conj_euler1 = Tex(r"z = cos\theta + isin\theta").scale(0.6)
        conj_euler2 = Tex(r"z = cos\theta - isin\theta").scale(0.6)
        conj_euler_group = Group(conj_euler1, conj_euler2).arrange(DOWN).next_to(mult_eq, DOWN, buff=0.5)
        self.wait()
        self.play(
            FadeIn(conj_euler_group)
        )
        self.wait()
        mult_replace = Tex(r"z\bar{z}=x^2+y^2=1").scale(0.7).next_to(real_eq_group, DOWN, buff = 0.7)
        self.play(TransformMatchingTex(mult_eq, mult_replace))

        vertical = DashedLine(circle1.get_top(), circle1.get_bottom())
        vertical.set_color(PURPLE)
        mid_18 = np.array([left_shift,ninth_root[0][1].get_center()[1],0])
        mid_72 = np.array([left_shift,ninth_root[0][7].get_center()[1],0])
        mid_45 = np.array([left_shift,ninth_root[0][4].get_center()[1],0])
        mid_36 = np.array([left_shift,ninth_root[0][3].get_center()[1],0])
        horizontal_1 = DashedLine(ninth_root[0][1],mid_18).set_color(RED)
        horizontal_8 = DashedLine(ninth_root[0][8],mid_18).set_color(BLUE)
        horizontal_7 = DashedLine(ninth_root[0][7], mid_72).set_color(RED)
        horizontal_2 = DashedLine(ninth_root[0][2], mid_72).set_color(BLUE)
        horizontal_4 = DashedLine(ninth_root[0][4], mid_45).set_color(RED)
        horizontal_5 = DashedLine(ninth_root[0][5], mid_45).set_color(BLUE)
        horizontal_3 = DashedLine(ninth_root[0][3], mid_36).set_color(GREEN)
        horizontal_6 = DashedLine(ninth_root[0][6], mid_36).set_color(GREEN)
        lines = Group(
            horizontal_1, 
            horizontal_2, 
            horizontal_3,
            horizontal_4, 
            horizontal_5, 
            horizontal_6,
            horizontal_7, 
            horizontal_8, 
            vertical,
        )
        self.play(
            FadeOut(conj_euler_group),
            FadeOut(real_eq2),
            FadeOut(real_eq1),
            FadeOut(conj_group_1),
            FadeOut(mult_replace),
        )
        self.wait()
        self.play(
            ShowCreation(vertical)
        )

        gamma_eu1 = Tex(r"\gamma_{1} = e^{i\frac{1}{9}}")
        gamma_eu2 = Tex(r"\eta_{1} = e^{i\frac{8}{9}}")
        gamma_eu_group = Group(gamma_eu1, gamma_eu2).arrange(RIGHT, buff = 0.5).next_to(conj_eq2, DOWN, buff=0.5)
        gamma_eu1[1].scale(0.6)
        gamma_eu1[0].set_color(RED)
        gamma_eu1[5].set_color(RED)
        gamma_eu2[1].scale(0.6)
        gamma_eu2[0].set_color(BLUE)
        gamma_eu2[5].set_color(BLUE)
        self.wait()
        self.play(
            gamma_copy_group[0][0].animate.set_color(RED),
            gamma_copy_group[1][0].animate.set_color(RED),
            gamma_copy_group[2][0].animate.set_color(RED),
            eta_copy_group[0][0].animate.set_color(BLUE),
            eta_copy_group[1][0].animate.set_color(BLUE),
            eta_copy_group[2][0].animate.set_color(BLUE),
            circle_three.animate.set_color(GREEN)
        )
        self.wait()
        self.play(
            Write(gamma_eu1), 
            Write(gamma_eu2),
            ShowCreation(horizontal_1),
            ShowCreation(horizontal_8),
        )
        gamma_mult = Tex(r"\gamma_{1}\eta_{1} = e^{i\frac{1}{9}}\cdot e^{i\frac{8}{9}} = 1")
        gamma_mult[1].scale(0.6)
        gamma_mult[0].set_color(RED)
        gamma_mult[3].scale(0.6)
        gamma_mult[2].set_color(BLUE)
        gamma_mult[7].set_color(RED)
        gamma_mult[13].set_color(BLUE)
        gamma_mult[17].set_color(GREEN)
        gamma_mult.next_to(gamma_eu_group, DOWN, buff=0.5)
        self.wait()
        self.play(FadeIn(gamma_mult))
        self.wait()
        self.play(
            FadeOut(gamma_eu1),
            FadeOut(gamma_eu2),
            gamma_mult.animate.shift(UP*0.8)
        )
        gamma_mult_2 = Tex(r"\gamma_{2}\eta_{2} = e^{i\frac{4}{9}}\cdot e^{i\frac{5}{9}} = 1")
        gamma_mult_2[1].scale(0.6)
        gamma_mult_2[0].set_color(RED)
        gamma_mult_2[3].scale(0.6)
        gamma_mult_2[2].set_color(BLUE)
        gamma_mult_2[7].set_color(RED)
        gamma_mult_2[13].set_color(BLUE)
        gamma_mult_2[17].set_color(GREEN)
        gamma_mult_2.next_to(gamma_mult, DOWN, buff=0.3)

        gamma_mult_3 = Tex(r"\gamma_{3}\eta_{3} = e^{i\frac{7}{9}}\cdot e^{i\frac{2}{9}} = 1")
        gamma_mult_3[1].scale(0.6)
        gamma_mult_3[0].set_color(RED)
        gamma_mult_3[3].scale(0.6)
        gamma_mult_3[2].set_color(BLUE)
        gamma_mult_3[7].set_color(RED)
        gamma_mult_3[13].set_color(BLUE)
        gamma_mult_3[17].set_color(GREEN)
        gamma_mult_3.next_to(gamma_mult_2, DOWN, buff=0.3)

        gamma_mult_4 = Tex(r"gh = e^{i\frac{3}{9}}\cdot e^{i\frac{6}{9}} = 1")
        gamma_mult_4[0].set_color(GREEN)
        gamma_mult_4[1].set_color(GREEN)
        gamma_mult_4[5].set_color(GREEN)
        gamma_mult_4[11].set_color(GREEN)
        gamma_mult_4[15].set_color(GREEN)
        gamma_mult_4.next_to(gamma_mult_3, DOWN, buff=0.3)

        self.play(
            ShowCreation(gamma_mult_2),
            ShowCreation(horizontal_4),
            ShowCreation(horizontal_5),
        )
        self.wait()
        self.play(
            ShowCreation(gamma_mult_3),
            ShowCreation(horizontal_7),
            ShowCreation(horizontal_2),
        )
        self.wait()
        self.play(
            ShowCreation(gamma_mult_4),
            ShowCreation(horizontal_3),
            ShowCreation(horizontal_6),
        )
        self.wait(3)
        # TO DO LIST
        # - put x and y on axes
        # - Show general example for z before putting our greek letters around the circle
        # - Put hat over z in sin cos formula

class Equivalence(Scene):
    def construct(self):
        frame = self.camera.frame
        scale = 2

        circle1 = ParametricCurve(
            lambda u: np.array([
                np.sin(u),
                np.cos(u),
                0
            ]),
            color = WHITE,
            t_range = np.array([-PI, PI, 0.01])
        ).scale(scale).set_stroke(width=4)
        circle2 = ParametricCurve(
            lambda u: np.array([
                np.sin(u),
                np.cos(u),
                0
            ]),
            color = WHITE,
            t_range = np.array([-PI, PI, 0.01])
        ).scale(scale).set_stroke(width=4)
        numbers1 = vbm_numbers(1,9,1.0,2.6)
        positives = number_polarities_pos(numbers1, 0.5)
        dots1 = vbm_dots(1,9,1.4,2)
        dots2 = vbm_dots(1,9,1.4,2).set_color(WHITE)

        group1 = Group(dots1, numbers1, circle1).scale(0.8)
        
        vbm_circle_title = Tex(r"\textsc{VBM Circle}")
        complex_circle_title = Tex(r"\textsc{Complex Circle}")
        axes = NumberPlane().scale(2)
        euler_group = Group()
        r = 1.3
        t2c = {
            "1":RED, "4":RED, "7":RED,
            "2":BLUE, "5":BLUE, "8":BLUE,
            "3":GREEN, "6":GREEN, "9":GREEN,
        }
        for i in range(0,9):
            if i == 0:
                euler_equation  = Tex(r"e^{i\frac{" + str(9) + "}{9}"+r"\tau}")
            else:
                euler_equation  = Tex(r"e^{i\frac{" + str(i) + "}{9}"+r"\tau}")

            euler_equation.shift(
                [
                    scale * r*np.sin(TAU * (i/9)),
                    scale * r*np.cos(TAU * (i/9)),
                    0
                ]            
            )
            euler_group.add(euler_equation)

        left_shift = 3.5
        self.play(
            FadeIn(group1),
        )
        self.wait()
        self.play(
            group1.animate.shift(LEFT*left_shift)
        )

        group2 = Group(circle2,euler_group,dots2).scale(0.8).shift(RIGHT*left_shift)
        vbm_circle_title.next_to(circle1, UP, buff=1.5)
        complex_circle_title.next_to(circle2, UP, buff=1.5)
        self.wait()
        self.play(
            FadeIn(group2),
            FadeIn(vbm_circle_title),
            FadeIn(complex_circle_title),
        )
        self.wait()
        vbm_number_title = Tex(r"\text{Which Circle}")
        direction_title = Tex(r"\text{Direction}")
        space_title = Tex(r"\text{Dual Space}")
        title_group1 = Group(vbm_number_title, direction_title, space_title).arrange(DOWN).scale(0.8).next_to(circle1,DOWN, buff=0.7)

        complex_title = Tex(r"\text{Which Angle}")
        theta_title = Tex(r"\text{Angle Polarity}")
        conjugate_title = Tex(r"\text{Complex Conjugate}")
        title_group2 = Group(complex_title, theta_title, conjugate_title).arrange(DOWN).scale(0.8).next_to(circle2,DOWN, buff=0.7)

        arrow = Tex(r"\to").scale(2).shift(DOWN*3)
        arrow_copy = Tex(r"\to").scale(2).shift(UP*0.3)

        self.play(
            group1.animate.shift(UP*0.3),
            group2.animate.shift(UP*0.3),
        )
        self.play(
            FadeIn(vbm_number_title),
        )
        self.wait()
        self.play(
            FadeIn(direction_title),
        )
        self.wait()
        self.play(
            FadeIn(space_title),
        )
        self.wait()
        self.play(
            FadeIn(title_group2),
            ShowCreation(arrow),
            ShowCreation(arrow_copy),
        )
        self.wait()
        self.play(
            FadeOut(title_group1),
            FadeOut(title_group2),
            Uncreate(arrow),
            Uncreate(arrow_copy),
        )
        self.wait()

        k_title = Tex(r"k_{dp}").scale(1.3).shift(DOWN*1.6)
        d_title = Tex(r"d = (\hat{1},\hat{4},\hat{7}) or (\hat{8},\hat{5},\hat{2})",tex_to_color_map=t2c).scale(0.6).next_to(k_title,DOWN,buff=0.3)
        p_title = Tex(r"p = \bullet / \circ",tex_to_color_map=t2c).scale(0.6).next_to(d_title,DOWN,buff=0.3)
        p_title[2].scale(0.7)
        self.play(
            FadeIn(k_title)
        )
        self.wait()
        self.play(
            FadeIn(d_title)
        )
        self.wait()
        self.play(
            FadeIn(p_title)
        )
        self.wait()

        vbm_num = Tex(r"V= (k\cdot d)_{p}", tex_to_color_map = t2c).scale(1.5).next_to(group1, DOWN,buff=0.8)

        self.play(
            FadeIn(vbm_num),
        )
        self.wait()
        comp_num2 = Tex(r"Z=e^{i(\frac{k}{9}\tau)_{d}}_{p}").scale(1.5).next_to(group2, DOWN,buff=0.6)
        self.play(
            FadeIn(comp_num2)
        )

        self.wait()

        euler_group3 = Group()
        colors = [GREEN,RED,BLUE]
        for i in range(0,9):
            if i == 0:
                euler_equation3  = Tex(r"e^{i\frac{" + str(9) + r"}{9}"+r"\tau}")
            else:
                euler_equation3  = Tex(r"e^{i\frac{" + str(i) + r"}{9}"+r"\tau}")

            euler_equation3[2].set_color(colors[i%3])
            euler_equation3.shift(
                [
                    scale * r*np.sin(TAU * (i/9)),
                    scale * r*np.cos(TAU * (i/9)),
                    0
                ]            
            )
            euler_group3.add(euler_equation3)
        euler_group3.scale(0.8).shift(RIGHT*left_shift+UP*0.3)

        self.play(
            FadeOut(euler_group),
            FadeIn(euler_group3)
        )
        numbers2 = vbm_numbers(4,9,1.0,2.6).scale(0.8).shift(LEFT*left_shift+UP*0.3)
        numbers3 = vbm_numbers(7,9,1.0,2.6).scale(0.8).shift(LEFT*left_shift+UP*0.3)

        self.wait()
        self.play(
            FadeOut(numbers1),
            FadeIn(numbers2),
        )
        self.wait()
        self.play(
            FadeOut(numbers2),
            FadeIn(numbers3),
        )
        self.wait()

        self.play(
            k_title.animate.shift(LEFT*0.8)
        )
        k_answer = Tex(r"=5_{\hat{4}\bullet}").scale(1.3).next_to(k_title,RIGHT)
        k_answer[len(k_answer)-1].scale(0.7)
        self.play(
            FadeIn(k_answer)
        )
        self.wait()
        self.play(
            FadeOut(numbers3),
            FadeIn(numbers2),
        )
        self.wait()

        curve_function_pos = lambda u: np.array([(2*0.8)*np.sin(u),(2*0.8)*np.cos(u),0])
        curve_function_neg = lambda u: np.array([-(2*0.8)*np.sin(u),(2*0.8)*np.cos(u),0])

        angle_start = ValueTracker(0)
        angle = ValueTracker(0)

        circle_dot = always_redraw(lambda: Dot().scale(1.5).set_color(YELLOW).move_to(
            np.array([(2*0.8)*np.sin(angle.get_value()), (2*0.8)*np.cos(angle.get_value()), 0])
        ).shift(LEFT*left_shift+UP*0.3))
        arc_pos = always_redraw(lambda: ParametricCurve(
            curve_function_pos,
            color = YELLOW,
            t_range = np.array([angle_start.get_value(), angle.get_value(), 0.01])
        ).shift(LEFT*left_shift+UP*0.3))
        self.play(
            FadeIn(circle_dot),
            FadeIn(arc_pos),
        )
        self.wait()
        for i in range(1,6):
            self.play(
                angle.animate.set_value((i/9)*TAU)
            )
        self.wait()
        
        vbm_num2 = Tex(r"V = (5\cdot 4)_{\bullet}").scale(1.5).next_to(group1, DOWN,buff=0.8)
        vbm_num2[len(vbm_num2)-1].scale(0.7)
        self.wait()
        self.play(
            ReplacementTransform(vbm_num, vbm_num2)
        )
        vbm_num3 = Tex(r"V = 2_{\bullet}").scale(1.5).next_to(group1, DOWN,buff=0.8)
        vbm_num3[len(vbm_num3)-1].scale(0.7)
        vbm_num3[2].set_color(BLUE)
        self.wait()
        self.play(
            ReplacementTransform(vbm_num2, vbm_num3)
        )
        self.wait()
        vbm_num4 = Tex(r"V = (4\cdot 5)_{\bullet}").scale(1.5).next_to(group1, DOWN,buff=0.8)
        vbm_num4[len(vbm_num4)-1].scale(0.7)

        k_answer2 = Tex(r"=4_{5\bullet}").scale(1.3).next_to(k_title,RIGHT)
        k_answer2[len(k_answer2)-1].scale(0.7)
        self.play(
            ReplacementTransform(k_answer, k_answer2)
        )
        self.wait()
        self.play(
            ReplacementTransform(vbm_num3, vbm_num4)
        )
        self.wait()
        self.play(
            angle.animate.set_value((0)*TAU)
        )
        self.play(
            angle.animate.set_value((-4/9)*TAU)
        )
        vbm_num5 = Tex(r"V = 2_{\bullet}").scale(1.5).next_to(group1, DOWN,buff=0.8)
        vbm_num5[len(vbm_num5)-1].scale(0.7)
        vbm_num5[2].set_color(BLUE)
        self.wait()
        self.play(
            ReplacementTransform(vbm_num4, vbm_num5)
        )
        angle_start2 = ValueTracker(0)
        angle2 = ValueTracker(0)

        circle_dot2 = always_redraw(lambda: Dot().scale(1.5).set_color(YELLOW).move_to(
            np.array([(2*0.8)*np.sin(angle2.get_value()), (2*0.8)*np.cos(angle2.get_value()), 0])
        ).shift(RIGHT*left_shift+UP*0.3))
        arc_pos2 = always_redraw(lambda: ParametricCurve(
            curve_function_pos,
            color = YELLOW,
            t_range = np.array([angle_start2.get_value(), angle2.get_value(), 0.01])
        ).shift(RIGHT*left_shift+UP*0.3))

        self.wait()
        self.play(
            FadeIn(circle_dot2),
            FadeIn(arc_pos2),
        )
        comp_num3 = Tex(r"Z=e^{i(\frac{4}{9}\tau)_{d}}_{\bullet}").scale(1.5).next_to(group2, DOWN,buff=0.6)
        comp_num3[len(comp_num3)-1].scale(0.7)
        self.wait()
        self.play(
            ReplacementTransform(comp_num2,comp_num3)
        )
        self.wait()
        self.play(
            d_title.animate.shift(DOWN*0.3),
            p_title.animate.shift(DOWN*0.3),
        )
        pos_ang_title = Tex(r"+ang",tex_to_color_map=t2c).scale(0.5).next_to(d_title,UP,buff=0.1).shift(LEFT*0.35)
        neg_ang_title = Tex(r"-ang",tex_to_color_map=t2c).scale(0.5).next_to(d_title,UP,buff=0.1).shift(RIGHT*0.85)
        self.wait()
        self.play(
            FadeIn(pos_ang_title),
            FadeIn(neg_ang_title),
        )
        self.wait()
        comp_num4 = Tex(r"Z=e^{-i\frac{4}{9}\tau}_{\bullet}").scale(1.5).next_to(group2, DOWN,buff=0.6)
        comp_num4[len(comp_num4)-1].scale(0.7)
        self.play(
            ReplacementTransform(comp_num3,comp_num4)
        )
        self.wait()
        self.play(angle2.animate.set_value((-4/9)*TAU))
        comp_num5 = Tex(r"Z=e^{-i\theta_{d}}_{\bullet}").scale(1.5).next_to(group2, DOWN,buff=0.6)
        comp_num5[len(comp_num5)-1].scale(0.7)
        self.wait()
        self.play(
            ReplacementTransform(comp_num4, comp_num5)
        )
        theta_d = Tex(r",\theta_{d}=\frac{4}{9}\tau").scale(0.8).next_to(comp_num5,RIGHT).shift(DOWN*0.1)
        self.wait()
        self.play(
            FadeIn(theta_d)
        )
        self.wait()
        self.play(
            FadeOut(theta_d),
            FadeOut(k_answer2),
            FadeOut(pos_ang_title),
            FadeOut(neg_ang_title),
            FadeOut(d_title),
            FadeOut(p_title),
            FadeOut(k_title),
        )
        self.wait()
        vbm_num6 = Tex(r"V = (k\cdot d)_{\bullet}", tex_to_color_map = t2c).scale(1.5).next_to(group1, DOWN,buff=0.8)
        vbm_num6[len(vbm_num6)-1].scale(0.7)

        comp_num6 = Tex(r"Z=e^{i(\frac{k}{9}\tau)_{d}}_{\bullet}").scale(1.5).next_to(group2, DOWN,buff=0.6)
        comp_num6[len(comp_num6)-1].scale(0.7)

        self.play(
            FadeOut(numbers2),
            FadeIn(numbers1),
            ReplacementTransform(vbm_num5, vbm_num6),
            ReplacementTransform(comp_num5, comp_num6),
            angle.animate.set_value(0),
            angle2.animate.set_value(0),
        )
        self.wait()
        operator_title = Tex(r"k_{dp}").scale(1.5).shift(DOWN*1.6)
        self.play(
            FadeIn(operator_title)
        )
        self.wait()
        # d_to_angle = Tex(r"d:ang").scale(0.7).next_to(operator_title,DOWN,buff=0.3)
        equals_theta_plus = Tex(r"1:\theta",tex_to_color_map = t2c)
        equals_theta_minus = Tex(r"8:-\theta",tex_to_color_map = t2c)
        theta_group = Group(equals_theta_plus, equals_theta_minus).arrange(RIGHT, buff=0.3)
        equals_phi_plus = Tex(r"4:\varphi",tex_to_color_map = t2c)
        equals_phi_minus = Tex(r"5:-\varphi",tex_to_color_map = t2c)
        phi_group = Group(equals_phi_plus, equals_phi_minus).arrange(RIGHT, buff=0.3)
        equals_psi_plus = Tex(r"7:\psi",tex_to_color_map = t2c)
        equals_psi_minus = Tex(r"2:-\psi",tex_to_color_map = t2c)
        psi_group = Group(equals_psi_plus, equals_psi_minus).arrange(RIGHT, buff=0.3)
        angle_group = Group(theta_group, phi_group, psi_group).arrange(DOWN).scale(0.7)
        angle_group.next_to(operator_title,DOWN,buff=0.5)
        # self.play(
        #     FadeIn(d_to_angle)
        # )
        # self.wait()
        self.play(
            FadeIn(theta_group)
        )
        self.wait()
        self.play(
            FadeIn(phi_group)
        )
        self.wait()
        self.play(
            FadeIn(psi_group)
        )
        self.wait()
        text_scale=0.8
        which_18_pos = Tex(r"(1,8)_{\bullet}").scale(text_scale).next_to(circle1,UR)
        which_18_neg = Tex(r"(1,8)_{\circ}").scale(text_scale).next_to(circle1,UR)
        which_45_pos = Tex(r"(4,5)_{\bullet}").scale(text_scale).next_to(circle1,UR)
        which_45_neg = Tex(r"(4,5)_{\circ}").scale(text_scale).next_to(circle1,UR)
        which_72_pos = Tex(r"(7,2)_{\bullet}").scale(text_scale).next_to(circle1,UR)
        which_72_neg = Tex(r"(7,2)_{\circ}").scale(text_scale).next_to(circle1,UR)

        which_theta_pos = Tex(r"(\theta)_{\bullet}").scale(text_scale).next_to(circle2,UR)
        which_theta_neg = Tex(r"(\theta)_{\circ}").scale(text_scale).next_to(circle2,UR)
        which_phi_pos = Tex(r"(\varphi)_{\bullet}").scale(text_scale).next_to(circle2,UR)
        which_phi_neg = Tex(r"(\varphi)_{\circ}").scale(text_scale).next_to(circle2,UR)
        which_psi_pos = Tex(r"(\psi)_{\bullet}").scale(text_scale).next_to(circle2,UR)
        which_psi_neg = Tex(r"(\psi)_{\circ}").scale(text_scale).next_to(circle2,UR)
        self.play(
            FadeIn(which_18_pos),
            FadeIn(which_theta_pos),
        )
        self.wait()
        example_op1 = Tex(r"7_{1\bullet}").scale(1.5).shift(DOWN*1.6)
        example_op1[len(example_op1)-1].scale(0.7)
        self.play(
            ReplacementTransform(operator_title, example_op1)
        )
        self.wait()

        vbm_71 = Tex(r"V = (7\cdot 1)_{\bullet}").scale(1.5).next_to(group1, DOWN,buff=0.8)
        vbm_71[len(vbm_71)-1].scale(0.7)

        reduced_71 = Tex(r"V = 7_{\bullet}", tex_to_color_map = t2c).scale(1.5).next_to(group1, DOWN,buff=0.8)
        reduced_71[len(reduced_71)-1].scale(0.7)

        comp_71 = Tex(r"Z=e^{i(\frac{7}{9}\tau)_{d}}_{\bullet}").scale(1.5).next_to(group2, DOWN,buff=0.6)
        comp_71[5].set_color(RED)
        comp_71[len(comp_71)-1].scale(0.7)
        self.play(
            ReplacementTransform(vbm_num6,vbm_71)
        )
        self.wait()
        self.play(
            ReplacementTransform(vbm_71, reduced_71),
            angle.animate.set_value((7/9)*TAU),
        )
        self.wait()
        self.play(
            ReplacementTransform(comp_num6, comp_71),
            angle2.animate.set_value((7/9)*TAU),
        )
        self.wait()
        vbm_num6 = Tex(r"V = (k\cdot d)_{\bullet}", tex_to_color_map = t2c).scale(1.5).next_to(group1, DOWN,buff=0.8)
        vbm_num6[len(vbm_num6)-1].scale(0.7)

        comp_num6 = Tex(r"Z=e^{i(\frac{k}{9}\tau)_{d}}_{\bullet}").scale(1.5).next_to(group2, DOWN,buff=0.6)
        comp_num6[len(comp_num6)-1].scale(0.7)
        self.play(
            angle.animate.set_value(0),
            angle2.animate.set_value(0),
            ReplacementTransform(reduced_71, vbm_num6),
            ReplacementTransform(comp_71, comp_num6)
        )
        self.wait()
        example_op2 = Tex(r"3_{2\bullet}").scale(1.5).shift(DOWN*1.6)
        example_op2[len(example_op2)-1].scale(0.7)
        reduced_32 = Tex(r"V = 6_{\bullet}", tex_to_color_map = t2c).scale(1.5).next_to(group1, DOWN,buff=0.8)
        reduced_32[len(reduced_32)-1].scale(0.7)
        comp_32 = Tex(r"Z=e^{i(\frac{-3}{9}\tau)_{d}}_{\bullet}").scale(1.5).next_to(group2, DOWN,buff=0.6)
        comp_32[6].set_color(GREEN)
        comp_32[len(comp_32)-1].scale(0.7)
        self.play(
            ReplacementTransform(example_op1, example_op2)
        )
        self.wait()
        self.play(
            ReplacementTransform(which_18_pos, which_72_pos),
            ReplacementTransform(numbers1, numbers3),
        )
        self.wait()
        self.play(
            ReplacementTransform(vbm_num6, reduced_32),
            angle.animate.set_value((-3/9)*TAU),
        )
        self.wait()
        self.play(
            ReplacementTransform(which_theta_pos, which_psi_pos),
        )
        self.wait()
        self.play(
            ReplacementTransform(comp_num6, comp_32),
            angle2.animate.set_value((-3/9)*TAU),
        )
        self.wait()
        vbm_num6 = Tex(r"V = (k\cdot d)_{\bullet}", tex_to_color_map = t2c).scale(1.5).next_to(group1, DOWN,buff=0.8)
        vbm_num6[len(vbm_num6)-1].scale(0.7)

        comp_num6 = Tex(r"Z=e^{i(\frac{k}{9}\tau)_{d}}_{\bullet}").scale(1.5).next_to(group2, DOWN,buff=0.6)
        comp_num6[len(comp_num6)-1].scale(0.7)
        self.play(
            angle.animate.set_value(0),
            angle2.animate.set_value(0),
            ReplacementTransform(reduced_32, vbm_num6),
            ReplacementTransform(comp_32, comp_num6)
        )
        self.wait()

        example_op3 = Tex(r"5_{4\circ}").scale(1.5).shift(DOWN*1.6)
        example_op3[len(example_op3)-1].scale(0.7)
        reduced_54 = Tex(r"V = 2_{\circ}", tex_to_color_map = t2c).scale(1.5).next_to(group1, DOWN,buff=0.8)
        reduced_54[len(reduced_54)-1].scale(0.7)
        comp_54 = Tex(r"Z=e^{i(\frac{5}{9}\tau)_{d}}_{\circ}").scale(1.5).next_to(group2, DOWN,buff=0.6)
        comp_54[5].set_color(BLUE)
        comp_54[len(comp_54)-1].scale(0.7)
        self.play(
            ReplacementTransform(example_op2, example_op3)
        )
        self.wait()
        numbers2.set_color(WHITE)
        self.play(
            ReplacementTransform(which_72_pos, which_45_neg),
            ReplacementTransform(numbers3, numbers2),
            dots1.animate.set_color(WHITE)
        )
        self.wait()
        self.play(
            ReplacementTransform(vbm_num6, reduced_54),
            angle.animate.set_value((5/9)*TAU),
        )
        self.wait()
        self.play(
            ReplacementTransform(which_psi_pos, which_phi_pos),
            euler_group.animate.set_color(WHITE)
        )
        self.wait()
        self.play(
            ReplacementTransform(comp_num6, comp_54),
            angle2.animate.set_value((5/9)*TAU),
        )
        self.wait()
        vbm_num6 = Tex(r"V = (k\cdot d)_{\bullet}", tex_to_color_map = t2c).scale(1.5).next_to(group1, DOWN,buff=0.8)
        vbm_num6[len(vbm_num6)-1].scale(0.7)

        comp_num6 = Tex(r"Z=e^{i(\frac{k}{9}\tau)_{d}}_{\bullet}").scale(1.5).next_to(group2, DOWN,buff=0.6)
        comp_num6[len(comp_num6)-1].scale(0.7)



        plus_min = Tex(r"(+/-)").scale(0.5)
    # ###########
    #     z_eq = Tex(r"z^{n}=1")
    #     z_sqrt_eg = Tex(r"z=\sqrt[n]{1}")
    #     z_roots_eq = Tex(r"roots:z_{0}, z_{1}, ... \, , z_{n}")
    #     self.wait(1)
    #     self.play(FadeIn(z_eq.next_to(roots_title,DOWN, buff=1)))
    #     self.wait(1)
    #     self.play(FadeIn(z_sqrt_eg.next_to(z_eq, DOWN, buff=1)))
    #     self.wait(1)
    #     self.play(FadeIn(z_roots_eq.next_to(z_sqrt_eg, DOWN, buff=1)))
    #     self.wait(1)

    #     z_group = Group()
    #     r=1.2
    #     for i in range(0,9):
    #         z_equation  = Tex(r"z_{" + str(i) + r"}")
    #         z_equation.shift(
    #             [
    #                 scale * r*np.sin(TAU * (i/9)),
    #                 scale * r*np.cos(TAU * (i/9)),
    #                 0
    #             ]            
    #         )
    #         z_group.add(z_equation)
    #     z_group.shift(LEFT*left_shift)
    #     ninth_root_eq = Tex(r"z = \sqrt[9]{1}").next_to(z_roots_eq, DOWN, buff=1)

    #     self.play(
    #         FadeOut(numbers1),
    #         FadeOut(positives),
    #         FadeIn(z_group),
    #         FadeIn(ninth_root_eq),
    #         FadeIn(real),
    #         FadeIn(imaginary), 
    #     )
    #     self.wait(1)

    #     z_eu_eq = Tex(r"z = e^{i\theta}")
    #     euler = Tex(r"e^{i\theta}=cos\theta+isin \theta")
    #     z_eu_eq.next_to(roots_title, DOWN, buff=1)
    #     euler.next_to(z_eu_eq, DOWN, buff=1)

    #     k_roots = Tex(r"e^{-i\frac{k_{" + str(round(arrow_angle.get_value())) + 
    #         "}}{n}"+r"\tau}=cos\frac{k_{" + 
    #         str(round(arrow_angle.get_value())) + 
    #         "}}{n}"+r"\tau+isin \frac{k_{" + 
    #         str(round(arrow_angle.get_value())) + 
    #         "}}{n}"+r"\tau", tex_to_color_map = t2c).next_to(euler,DOWN,buff=1)
    #     roots_eq = Tex(
    #         r"e^{i\frac{" + str(round(arrow_angle.get_value())) + 
    #         "}{9}"+r"\tau}=cos\frac{" + 
    #         str(round(arrow_angle.get_value())) + 
    #         "}{9}"+r"\tau+isin \frac{" + 
    #         str(round(arrow_angle.get_value())) + 
    #         "}{9}"+r"\tau", tex_to_color_map = t2c).next_to(k_roots,DOWN,buff=1)
        
    #     self.play(
    #         FadeOut(ninth_root_eq),
    #         FadeOut(z_eq),
    #         FadeOut(z_sqrt_eg),
    #         FadeOut(z_roots_eq),
    #     )
    #     self.wait(1)

    #     self.play(FadeIn(z_eu_eq))
    #     self.wait(1)
    #     self.play(FadeIn(euler))
    #     self.wait(1)




    #     example_root_eq = Tex(r"z_{1}=e^{i\frac{1}{9}\tau}")
    #     self.play(FadeIn(example_root_eq.next_to(euler, DOWN, buff=1)))
    #     for i in range(0,8):
    #         mult_eq1 = Tex(r"e^{i\frac{"+str(i+1)+r"}{9}\tau}")
    #         mult_eq2 = Tex(r"\cdot\, e^{i\frac{1}{9}\tau}=")
    #         answer = Tex(r"e^{i\frac{"+str(i+2)+r"}{9}\tau}")
    #         mult_eq2.next_to(mult_eq1,RIGHT)
    #         answer.next_to(mult_eq2,RIGHT)
    #         mult_group = Group(mult_eq1,mult_eq2,answer).next_to(example_root_eq,DOWN,buff=1)
    #         self.add(mult_group)
    #         self.wait(1)
    #         mult_trans = Tex(r"e^{i\frac{"+str(i+2)+r"}{9}\tau}").move_to(mult_eq1)
    #         if i+2 == 9:
    #             break
    #         self.play(
    #             FadeOut(mult_eq1),
    #             Transform(answer, mult_trans),
    #         )
    #         self.remove(answer, mult_trans, mult_eq2)
        
    #     self.wait(1)
    #     self.play(
    #         FadeOut(mult_group),
    #         FadeOut(example_root_eq),
    #     )
    #     self.wait(1)
    #     form_eq = Tex(r"e^{i\frac{k}{n}\tau}").scale(2.5)
    #     self.play(FadeIn(form_eq.next_to(euler, DOWN, buff=1.5)))
            





    # # # #Euler Angles
    #     euler_group.shift(LEFT*left_shift)
    #     self.play(
    #         FadeOut(z_group),
    #         FadeIn(euler_group),
    #     )
    #     self.wait(1)


    #     arrow = Arrow(
    #         start=np.array([0,0,0]),
    #         end=np.array([
    #             scale * np.sin(TAU * (arrow_angle.get_value()/9)),
    #             scale * np.cos(TAU * (arrow_angle.get_value()/9)),
    #             0
    #         ]),buff=0
    #     ).set_color(YELLOW).shift(LEFT*left_shift)
    #     dot = Dot(
    #         np.array([
    #             scale * np.sin(TAU * (arrow_angle.get_value()/9)),
    #             scale * np.cos(TAU * (arrow_angle.get_value()/9)),
    #             0
    #         ])
    #     ).set_color(YELLOW).shift(LEFT*left_shift)
    #     self.play(FadeIn(arrow))
    #     self.play(FadeIn(dot))
    #     arrow.add_updater(lambda m: m.become(Arrow(
    #         start=np.array([0,0,0]),
    #         end=np.array([
    #             scale * np.sin(TAU * (arrow_angle.get_value()/9)),
    #             scale * np.cos(TAU * (arrow_angle.get_value()/9)),
    #             0
    #         ]),buff=0
    #     ).set_color(YELLOW).shift(LEFT*left_shift)))
    #     dot.add_updater(lambda m: m.become(Dot(
    #         np.array([
    #             scale * np.sin(TAU * (arrow_angle.get_value()/9)),
    #             scale * np.cos(TAU * (arrow_angle.get_value()/9)),
    #             0
    #         ])
    #     ).set_color(YELLOW).shift(LEFT*left_shift)))

    #     self.play(FadeIn(k_roots))
    #     self.wait(0.1)
    #     self.play(FadeIn(roots_eq))
    #     roots_eq.add_updater(lambda m: m.become(Tex(
    #         r"e^{i\frac{" + str(round(arrow_angle.get_value())) + 
    #         "}{9}"+r"\tau}=cos\frac{" + 
    #         str(round(arrow_angle.get_value())) + 
    #         "}{9}"+r"\tau+isin \frac{" + 
    #         str(round(arrow_angle.get_value())) + 
    #         "}{9}"+r"\tau").next_to(k_roots,DOWN,buff=1)))
    #     k_roots.add_updater(lambda m: m.become(Tex(r"e^{-i\frac{k_{" + str(round(arrow_angle.get_value())) + 
    #         "}}{n}"+r"\tau}=cos\frac{k_{" + 
    #         str(round(arrow_angle.get_value())) + 
    #         "}}{n}"+r"\tau+isin \frac{k_{" + 
    #         str(round(arrow_angle.get_value())) + 
    #         "}}{n}"+r"\tau").next_to(euler,DOWN,buff=1)))
    #     self.wait(0.1)
    #     for i in range(0,10):
    #         self.wait(0.5)
    #         arrow_angle.set_value(i)

    #     neg_roots_eq = Tex(
    #         r"e^{-i\frac{" + str(round(arrow_angle.get_value())) + 
    #         "}{9}"+r"\tau}=cos\frac{" + 
    #         str(round(arrow_angle.get_value())) + 
    #         "}{9}"+r"\tau-isin \frac{" + 
    #         str(round(arrow_angle.get_value())) + 
    #         "}{9}"+r"\tau").next_to(roots_eq,DOWN,buff=1)
    #     neg_arrow = Arrow(
    #         start=np.array([0,0,0]),
    #         end=np.array([
    #             scale * np.sin(TAU * (-arrow_angle.get_value()/9)),
    #             scale * np.cos(TAU * (-arrow_angle.get_value()/9)),
    #             0
    #         ]),buff=0
    #     ).set_color(BLUE).shift(LEFT*left_shift)
    #     neg_dot = Dot(
    #         np.array([
    #             scale * np.sin(TAU * (-arrow_angle.get_value()/9)),
    #             scale * np.cos(TAU * (-arrow_angle.get_value()/9)),
    #             0
    #         ])
    #     ).set_color(BLUE).shift(LEFT*left_shift)
    #     self.play(
    #         FadeIn(neg_roots_eq),
    #         FadeIn(neg_arrow),
    #         FadeIn(neg_dot)
    #     )
    #     neg_roots_eq.add_updater(lambda m: m.become(Tex(
    #         r"e^{-i\frac{" + str(round(arrow_angle.get_value())) + 
    #         "}{9}"+r"\tau}=cos\frac{" + 
    #         str(round(arrow_angle.get_value())) + 
    #         "}{9}"+r"\tau-isin \frac{" + 
    #         str(round(arrow_angle.get_value())) + 
    #         "}{9}"+r"\tau").next_to(roots_eq,DOWN,buff=1)))
    #     neg_arrow.add_updater(lambda m: m.become(Arrow(
    #         start=np.array([0,0,0]),
    #         end=np.array([
    #             scale * np.sin(TAU * (-arrow_angle.get_value()/9)),
    #             scale * np.cos(TAU * (-arrow_angle.get_value()/9)),
    #             0
    #         ]),buff=0
    #     ).set_color(BLUE).shift(LEFT*left_shift)))
    #     neg_dot.add_updater(lambda m: m.become(Dot(
    #         np.array([
    #             scale * np.sin(TAU * (-arrow_angle.get_value()/9)),
    #             scale * np.cos(TAU * (-arrow_angle.get_value()/9)),
    #             0
    #         ])
    #     ).set_color(BLUE).shift(LEFT*left_shift)))
    #     for i in range(0,10):
    #         self.wait(0.5)
    #         arrow_angle.set_value(i)

class SymbolFinal(Scene):
    def construct(self):
        numbers = vbm_numbers(1,9,1.2,2.5)
        circle = Circle().scale(2).set_color(WHITE)
        dots = vbm_dots(1,9,1,2)
        symbol = vbm_symbol().scale(2)
        neg_circle = Circle().scale(2).set_color(WHITE)
        neg_dots = vbm_dots(1,9,1,2).set_color(WHITE)
        pos_space_label = Tex(r"\bullet").next_to(circle, UR)
        neg_space_label = Tex(r"\circ").next_to(neg_circle, UR)
        rad = 2.4
        stroke = 1
        circle_emination = Circle().set_stroke(width=5)
        arrow1 = Arrow(
            start = np.array([np.sin((10/12)*TAU), np.cos((10/12)*TAU), 0]),
            end = np.array([rad * np.sin((10/12)*TAU), rad * np.cos((10/12)*TAU), 0]),
        ).set_stroke(width=stroke)
        arrow2 = Arrow(
            start = np.array([np.sin((9/12)*TAU), np.cos((9/12)*TAU), 0]),
            end = np.array([rad * np.sin((9/12)*TAU), rad * np.cos((9/12)*TAU), 0]),
        ).set_stroke(width=stroke)
        arrow3 = Arrow(
            start = np.array([np.sin((8/12)*TAU), np.cos((8/12)*TAU), 0]),
            end = np.array([rad * np.sin((8/12)*TAU), rad * np.cos((8/12)*TAU), 0]),
        ).set_stroke(width=stroke)

        arrow4 = Arrow(
            start = np.array([np.sin((2/12)*TAU), np.cos((2/12)*TAU), 0]),
            end = np.array([rad * np.sin((2/12)*TAU), rad * np.cos((2/12)*TAU), 0]),
        ).set_stroke(width=stroke)
        arrow5 = Arrow(
            start = np.array([np.sin((3/12)*TAU), np.cos((3/12)*TAU), 0]),
            end = np.array([rad * np.sin((3/12)*TAU), rad * np.cos((3/12)*TAU), 0]),
        ).set_stroke(width=stroke)
        arrow6 = Arrow(
            start = np.array([np.sin((4/12)*TAU), np.cos((4/12)*TAU), 0]),
            end = np.array([rad * np.sin((4/12)*TAU), rad * np.cos((4/12)*TAU), 0]),
        ).set_stroke(width=stroke)
        center_emination = Group(
            circle_emination, 
            arrow1, arrow2, arrow3, arrow4, arrow5, arrow6
        ).set_color(YELLOW).scale(0.25).shift(DOWN*0.7)

        hexagon = RegularPolygon(n=6).scale(0.42).set_color(GREEN)
        triangle_up = RegularPolygon(n=3).scale(0.5).set_color(GREEN)
        triangle_down = RegularPolygon(n=3).scale(0.5).set_color(GREEN)
        rhombus = Polygon(
            [0,1,0],
            [0.7,0,0],
            [0,-1,0],
            [-0.7,0,0],
        ).scale(0.45).set_color(PURPLE)
        hexagon.move_to(numbers[6])
        triangle_up.move_to(numbers[3]).shift(UP*0.1)
        rhombus.move_to(numbers[0])
        shapes = Group(hexagon, triangle_up, rhombus)
    ###########
        self.play(
            FadeIn(numbers),
            FadeIn(symbol),
            FadeIn(shapes),
            FadeIn(center_emination),
        )
        one = Tex(r"1").set_color(RED)
        two = Tex(r"2").set_color(BLUE)
        four = Tex(r"4").set_color(RED)
        eight = Tex(r"8").set_color(BLUE)
        seven = Tex(r"7").set_color(RED)
        five = Tex(r"5").set_color(BLUE)
        three = Tex(r"3").set_color(GREEN)
        six = Tex(r"6").set_color(GREEN)
        nine = Tex(r"9").set_color(GREEN)

        title_add_1s = Group(
            two.copy(),three.copy(),
            four.copy(),five.copy(),six.copy(),
            seven.copy(),eight.copy(),nine.copy(),
        ).arrange(buff=0.2).scale(0.7).next_to(numbers[1], buff=0.1)

        title_add_2s = Group(
            four.copy(),six.copy(),
            eight.copy(),one.copy(),three.copy(),
            five.copy(),seven.copy(),nine.copy(),
        ).arrange(buff=0.2).scale(0.7).next_to(numbers[2], buff=0.1)
        
        title_add_3s = Group(
            three.copy(),six.copy(),nine.copy(),
            three.copy(),six.copy(),nine.copy(),
            three.copy(),six.copy(),nine.copy(),
        ).arrange(buff=0.4)

        title_add_4s = Group(
            eight.copy(),three.copy(),
            seven.copy(),two.copy(),six.copy(),
            one.copy(),five.copy(),nine.copy(),
        ).arrange(buff=0.2).scale(0.7).next_to(numbers[4], buff=0.1)
        
        title_add_5s = Group(
            one.copy(),six.copy(),
            two.copy(),seven.copy(),three.copy(),
            eight.copy(),four.copy(),nine.copy(),
        ).arrange(LEFT, buff=0.2).scale(0.7).next_to(numbers[5], LEFT, buff=0.1)

        title_add_6s = Group(
            six.copy(),three.copy(),nine.copy(),
            six.copy(),three.copy(),nine.copy(),
            six.copy(),three.copy(),nine.copy(),
        ).arrange(buff=0.4)

        title_add_7s = Group(
            five.copy(),three.copy(),
            one.copy(),eight.copy(),six.copy(),
            four.copy(),two.copy(),nine.copy(),
        ).arrange(LEFT,buff=0.2).scale(0.7).next_to(numbers[7], LEFT, buff=0.1)

        title_add_8s = Group(
            seven.copy(),six.copy(),
            five.copy(),four.copy(),three.copy(),
            two.copy(),one.copy(),nine.copy(),
        ).arrange(LEFT,buff=0.2).scale(0.7).next_to(numbers[8], LEFT, buff=0.1)

        title_add_9s = Group(
            nine.copy(),nine.copy(),nine.copy(),
            nine.copy(),nine.copy(),nine.copy(),
            nine.copy(),nine.copy(),nine.copy(),
        ).arrange(buff=0.4)

        self.play(
            ShowCreation(title_add_1s),
            ShowCreation(title_add_2s),
            ShowCreation(title_add_4s),
            ShowCreation(title_add_5s),
            ShowCreation(title_add_7s),
            ShowCreation(title_add_8s),
        )
        self.wait()
        self.play(
            FadeIn(pos_space_label.copy().next_to(rhombus, LEFT)),
            FadeIn(neg_space_label.copy().next_to(rhombus, RIGHT)),
        )
        self.wait(3)
        self.play(self.frame.animate.scale(1000), run_time = 15)

class TwoDPlane(Scene):

    def construct(self):
        frame = self.camera.frame
        pos_diamonds_x_axis = diamond_plane_pos(1,5,0,"xy").set_opacity(0)
        pos_diamonds_y_axis = diamond_plane_pos(5,1,0,"xy").set_opacity(0)
        pos_numbers_x_axis = generate_number_grid_pos(1,5,0,"xy",9).set_opacity(0)
        pos_numbers_y_axis = generate_number_grid_pos(5,1,0,"xy",9).set_opacity(0)
        
        axes = ThreeDAxes(
            x_range = (-5,5,1),
            y_range = (-5,5,1),
            z_range = (-5,5,1),
        ).apply_depth_test()
        axes_neg = ThreeDAxes(
            x_range = (-5,5,1),
            y_range = (-5,5,1),
            z_range = (-5,5,1),
        ).apply_depth_test().move_to([0.5,0.5,-0.1]).set_color(GREY)
        self.add(
            axes,
        )
        line = ParametricCurve(
            lambda u: np.array([
                u,
                0,
                0
            ]),
            color = WHITE,
            t_range = np.array([-4.5, 4.5, 0.01])
        )
        circle = ParametricCurve(
            lambda u: np.array([
                np.sin(u),
                np.cos(u),
                0
            ]),
            color = WHITE,
            t_range = np.array([-PI, PI, 0.01])
        )
        dots = vbm_dots(1,9,1,1)
        nums = vbm_numbers(1,9,1,1.4)
        self.add(circle)
        self.wait(2)
        self.play(
            FadeIn(dots),
            FadeIn(nums),
        )

        new_dots = Group()
        for i in range(0,5):
            n_d = dots[i].copy().move_to(np.array([i,0,0]))
            new_dots.add(n_d)
        for i in range(5,9):
            n_d = dots[i].copy().move_to(np.array([i-9,0,0]))
            new_dots.add(n_d)

        new_nums = Group()
        for i in range(0,5):
            n_n = nums[i].copy().next_to(np.array([i,0,0]), UP)
            new_nums.add(n_n)
        for i in range(5,9):
            n_n = nums[i].copy().next_to(np.array([i-9,0,0]), UP)
            new_nums.add(n_n)

        self.wait(2)
        self.play(
            frame.animate.scale(1.6).shift(RIGHT*4),
        )
        self.wait(2)

        numbers1 = vbm_numbers(1,9,1.0,2.6)
        circle1 = circle.copy().set_color(WHITE).scale(2).set_stroke(width=4)
        positives = number_polarities_pos(numbers1, 0.5)
        dots1 = vbm_dots(1,9,1.4,2)
        group1 = Group(dots1, numbers1, circle1, positives).shift(RIGHT*10)
        self.play(
            FadeIn(group1),
        )
        self.add(dots1)
        self.wait(2)
        self.play(
            Transform(circle,line),
            Transform(dots,new_dots),
            Transform(nums,new_nums),
        )
        self.wait(2)
        points = Group(
            Dot(np.array([-4.5,0,0.1])),
            Dot(np.array([4.5,0,0.1])),
        )
        vbm_point = Group(
            Dot().move_to(circle1, DOWN).shift(DOWN*0.1),
        )
        group1.add(vbm_point)
        self.play(
            Indicate(points[0]), 
            Indicate(points[1]),
            Indicate(vbm_point)
        )


        self.wait(2)
        self.play(
            FadeOut(new_nums),
            FadeOut(new_dots),
            FadeOut(nums),
            FadeOut(dots),
        )

        self.add(
            pos_diamonds_x_axis,
            pos_numbers_x_axis,
        )
        self.play(
            pos_diamonds_x_axis.animate.set_opacity(1.0),
            pos_numbers_x_axis.animate.set_opacity(1.0),
        )
        self.wait(2)
        x_coord = ValueTracker(0)
        y_coord = ValueTracker(0)
        gold_dot = always_redraw(lambda: Circle(radius=0.3).move_to(np.array([x_coord.get_value(),y_coord.get_value(),0])).set_color(YELLOW))
        
        x_label_pos_top = Tex("(1+)").scale(0.7).next_to([5,0,0],RIGHT)
        # ARROW TIP CURVE
        angle = ValueTracker(0)
        radius = 3.2
        curve_function_pos = lambda u: np.array([radius*np.sin(u),radius*np.cos(u),0])
        curve_function_neg = lambda u: np.array([-radius*np.sin(u),radius*np.cos(u),0])
        arc_pos = ParametricCurve(
            curve_function_pos,
            color = YELLOW,
            t_range = np.array([0, angle.get_value(), 0.01])
        )
        arrow_tip = ArrowTip().scale(0.5).set_color(YELLOW)
        arc_neg = ParametricCurve(
            curve_function_pos,
            color = YELLOW,
            t_range = np.array([0, angle.get_value(), 0.01])
        )
        arrow_tip_pos = ArrowTip().scale(0.5).set_color(YELLOW)
        arrow_tip_neg = ArrowTip().scale(0.5).set_color(YELLOW)
        def get_tangent(curve_func, t, dt=1e-5):
            p1 = curve_func(t)
            p2 = curve_func(t + dt)
            return normalize(p2 - p1)

        def update_arrow_pos(mob):
            end_point = arc_pos.get_end()
            tangent_vector = get_tangent(curve_function_pos, angle.get_value())
            ang = angle_of_vector(tangent_vector)
            mob.move_to(end_point)
            mob.rotate(ang - mob.get_angle())
        def update_arrow_neg(mob):
            end_point = arc_neg.get_end()
            tangent_vector = get_tangent(curve_function_neg, angle.get_value())
            ang = angle_of_vector(tangent_vector)
            mob.move_to(end_point)
            mob.rotate(ang - mob.get_angle())

        arrow_tip_pos.add_updater(update_arrow_pos)
        arc_pos.add_updater(lambda m: m.become(
                ParametricCurve(
                curve_function_pos,
                color = YELLOW,
                t_range = np.array([0, angle.get_value(), 0.01])
            ).shift(RIGHT*10)

        ))
        arrow_tip_neg.add_updater(update_arrow_neg)
        arc_neg.add_updater(lambda m: m.become(
                ParametricCurve(
                curve_function_neg,
                color = YELLOW,
                t_range = np.array([0, angle.get_value(), 0.01])
            ).shift(RIGHT*10)

        ))
        def make_arrow(start, end, col):
            arrow = Arrow(start, end, stroke_width = 3).set_color(col)
            return arrow
        a1_length = ValueTracker(0.3)
        arrow1 = always_redraw(lambda:
            make_arrow(
                np.array([0.3,0.8,0]), 
                np.array([a1_length.get_value(),0.8,0]),
                YELLOW,
            )
        )

        self.add(arc_pos, arrow1)
        self.play(FadeIn(arrow_tip_pos, run_time=0.2))
        self.play(
            FadeIn(x_label_pos_top),
            angle.animate.set_value((2/9)*TAU),
            a1_length.animate.set_value(4.5),
        )
        self.wait(2)

        self.remove(arrow_tip_pos, arc_pos, arrow1)
        angle.set_value(0)
        self.wait()
        x_label_pos_bot = Tex("(8+)").scale(0.7).next_to([-5,0,0],LEFT)

        a1_length.set_value(0.3)
        arrow2 = always_redraw(lambda:
            make_arrow(
                np.array([-0.3,0.8,0]), 
                np.array([-a1_length.get_value(),0.8,0]),
                YELLOW,
            )
        )
        self.add(arc_neg, arrow2)
        self.play(FadeIn(arrow_tip_neg, run_time=0.2))
        self.play(
            FadeIn(x_label_pos_bot),
            angle.animate.set_value((2/9)*TAU),
            a1_length.animate.set_value(4.5),
        )
        self.wait(2)
        self.remove(arrow_tip_neg, arc_neg, arrow2)
        angle.set_value(0)
        
        arc_pos1 = ParametricCurve(
            curve_function_pos,
            color = YELLOW,
            t_range = np.array([0, angle.get_value(), 0.01])
        )

        curve_function_pos1 = lambda u: np.array([2*np.sin(u),2*np.cos(u),0])
        arc_pos1.add_updater(lambda m: m.become(
                ParametricCurve(
                curve_function_pos1,
                color = YELLOW,
                t_range = np.array([angle_start.get_value(), angle.get_value(), 0.01])
            ).shift(RIGHT*10)

        ))
        circle_dot = always_redraw(lambda: Dot().scale(2).set_color(YELLOW).move_to(
            np.array([2*np.sin(angle.get_value())+10, 2*np.cos(angle.get_value()), 0])
        ))
        angle_start = ValueTracker(0)

        self.wait()
        self.add(arc_pos1)
        self.play(
            FadeIn(gold_dot),
            FadeIn(circle_dot)
        )
        self.wait(2)
        
        number = Tex("1").scale(2).move_to(circle1.get_center())
        plus = Tex("+").next_to(number, LEFT)
        sub_number = Tex("1+").next_to(number, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1).set_color(RED)

        self.play(
            x_coord.animate.set_value(1),
            angle.animate.set_value((1/9)*TAU),
            FadeIn(number),
            FadeIn(sub_number),
            FadeIn(plus)
        )
        self.wait(2)
        self.play(
            FadeOut(number),
            FadeOut(sub_number),
            FadeOut(plus)
        )
        
        self.wait()
        self.remove(arc_pos1)
        angle_start.set_value((1/9)*TAU)
        self.add(arc_pos1)

        self.play(
            x_coord.animate.set_value(2),
            angle.animate.set_value((2/9)*TAU),
            FadeIn(number),
            FadeIn(sub_number),
            FadeIn(plus)
        )
        self.wait(2)

        self.play(
            FadeOut(number),
            FadeOut(sub_number),
            FadeOut(plus)
        )
        
        self.wait()
        self.remove(arc_pos1)
        angle_start.set_value((2/9)*TAU)
        self.add(arc_pos1)
        number = Tex("1").scale(2).move_to(circle1.get_center())
        plus = Tex("+").next_to(number, LEFT)
        sub_number = Tex("8+").next_to(number, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1).set_color(BLUE)

        self.play(
            x_coord.animate.set_value(1),
            angle.animate.set_value((1/9)*TAU),
            FadeIn(number),
            FadeIn(sub_number),
            FadeIn(plus)
        )
        self.wait(2)

        self.play(
            FadeOut(number),
            FadeOut(sub_number),
            FadeOut(plus)
        )
        
        self.wait()
        self.remove(arc_pos1)
        angle_start.set_value((1/9)*TAU)
        self.add(arc_pos1)
        number = Tex("2").scale(2).move_to(circle1.get_center())
        plus = Tex("+").next_to(number, LEFT)
        sub_number = Tex("8+").next_to(number, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1).set_color(BLUE)

        self.play(
            x_coord.animate.set_value(-1),
            angle.animate.set_value(-(1/9)*TAU),
            FadeIn(number),
            FadeIn(sub_number),
            FadeIn(plus)
        )
        self.wait(2)

        self.play(
            FadeOut(number),
            FadeOut(sub_number),
            FadeOut(plus)
        )

        self.wait()
        self.remove(arc_pos1)
        angle_start.set_value(-(1/9)*TAU)
        self.add(arc_pos1)
        number = Tex("3").scale(2).move_to(circle1.get_center())
        plus = Tex("+").next_to(number, LEFT)
        sub_number = Tex("8+").next_to(number, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1).set_color(BLUE)

        self.play(
            x_coord.animate.set_value(-4),
            angle.animate.set_value(-(4/9)*TAU),
            FadeIn(number),
            FadeIn(sub_number),
            FadeIn(plus)
        )
        self.wait(2)

        self.play(
            FadeOut(number),
            FadeOut(sub_number),
            FadeOut(plus)
        )

        
        self.wait()
        self.remove(arc_pos1)
        angle_start.set_value(-(4/9)*TAU)
        self.add(arc_pos1)
        x_coord.set_value(4)
        number = Tex("5").scale(2).move_to(circle1.get_center())
        plus = Tex("+").next_to(number, LEFT)
        sub_number = Tex("8+").next_to(number, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1).set_color(BLUE)

        self.play(
            x_coord.animate.set_value(0),
            angle.animate.set_value(-TAU),
            FadeIn(number),
            FadeIn(sub_number),
            FadeIn(plus)
        )
        self.wait(2)

        self.play(
            FadeOut(number),
            FadeOut(sub_number),
            FadeOut(plus)
        )

        self.remove(gold_dot,circle_dot,arc_pos1)
        
        self.wait(2)

        group1_shift = 3
        self.play(
            group1.animate.shift(UP*group1_shift),
        )

        gold_dot.shift(UP*group1_shift)
        circle_dot.shift(UP*group1_shift)
        arc_pos1.shift(UP*group1_shift)
        angle_start.set_value(0)
        angle.set_value(0)
        circle_copy = ParametricCurve(
            lambda u: np.array([
                np.sin(u),
                np.cos(u),
                0
            ]),
            color = WHITE,
            t_range = np.array([-PI, PI, 0.01])
        )
        numbers2 = vbm_numbers(4,9,1.0,2.6)
        circle2 = circle_copy.copy().set_color(WHITE).scale(2).set_stroke(width=4)
        positives2 = number_polarities_pos(numbers2, 0.5)
        dots2 = vbm_dots(4,9,1.4,2)
        group2 = Group(dots2, numbers2, circle2, positives2).shift(RIGHT*10)
        group2.shift(DOWN*group1_shift)


        angle2 = ValueTracker(0)
        angle2_start = ValueTracker(0)
        curve_function_pos2 = lambda u: np.array([2*np.sin(u),2*np.cos(u),0])
        arc_pos2 = ParametricCurve(
            curve_function_pos2,
            color = YELLOW,
            t_range = np.array([0, angle2.get_value(), 0.01])
        )
        arc_pos2.add_updater(lambda m: m.become(
                ParametricCurve(
                curve_function_pos2,
                color = YELLOW,
                t_range = np.array([angle2_start.get_value(), angle2.get_value(), 0.01])
            ).shift(RIGHT*10).shift(DOWN*group1_shift)

        ))
        arc_pos1.clear_updaters()
        arc_pos1.add_updater(lambda m: m.become(
                ParametricCurve(
                curve_function_pos1,
                color = YELLOW,
                t_range = np.array([angle_start.get_value(), angle.get_value(), 0.01])
            ).shift(RIGHT*10).shift(UP*group1_shift)

        ))
        circle_dot.clear_updaters()
        circle_dot = always_redraw(lambda: Dot().scale(2).set_color(YELLOW).move_to(
            np.array([2*np.sin(angle.get_value())+10, 2*np.cos(angle.get_value())+group1_shift, 0])
        ))
        circle_dot2 = always_redraw(lambda: Dot().scale(2).set_color(YELLOW).move_to(
            np.array([2*np.sin(angle2.get_value())+10, 2*np.cos(angle2.get_value())-group1_shift, 0])
        ))
        arc2_group = Group(arc_pos2, circle_dot2)


        self.add(
            pos_diamonds_y_axis,
            pos_numbers_y_axis,
        )
        vbm_point2 = Group(
            Dot().move_to(circle2, DOWN).shift(DOWN*0.1),
        )
        group2.add(vbm_point2)
        self.play(
            FadeIn(group2)
        )
        self.wait(2)
        circle_dot.shift(UP*group1_shift)
        self.play(
            pos_diamonds_y_axis.animate.set_opacity(1.0),
            pos_numbers_y_axis.animate.set_opacity(1.0),
        )
        self.add(arc_pos1, arc_pos2)

        arc_pos.clear_updaters()
        new_arc_angle = ValueTracker(0)
        arc_pos.add_updater(lambda m: m.become(
                ParametricCurve(
                curve_function_pos,
                color = YELLOW,
                t_range = np.array([0, new_arc_angle.get_value(), 0.01])
            ).shift(RIGHT*10+DOWN*group1_shift)

        ))
        y_label_pos_top = Tex("(4+)").scale(0.7).next_to([0,5,0],UP)

        angle.set_value(0)
        arrow_tip_pos = ArrowTip().scale(0.5).set_color(YELLOW)
        arrow_tip_neg = ArrowTip().scale(0.5).set_color(YELLOW)
        new_arc_angle = ValueTracker(0)
        def get_tangent(curve_func, t, dt=1e-5):
            p1 = curve_func(t)
            p2 = curve_func(t + dt)
            return normalize(p2 - p1)

        def update_arrow_pos(mob):
            end_point = arc_pos.get_end()
            tangent_vector = get_tangent(curve_function_pos, new_arc_angle.get_value())
            ang = angle_of_vector(tangent_vector)
            mob.move_to(end_point)
            mob.rotate(ang - mob.get_angle())
        def update_arrow_neg(mob):
            end_point = arc_neg.get_end()
            tangent_vector = get_tangent(curve_function_neg, new_arc_angle.get_value())
            ang = angle_of_vector(tangent_vector)
            mob.move_to(end_point)
            mob.rotate(ang - mob.get_angle())

        arrow_tip_pos.add_updater(update_arrow_pos)
        arc_pos.add_updater(lambda m: m.become(
                ParametricCurve(
                curve_function_pos,
                color = YELLOW,
                t_range = np.array([0, new_arc_angle.get_value(), 0.01])
            ).shift(RIGHT*10+DOWN*group1_shift)

        ))
        arrow_tip_neg.add_updater(update_arrow_neg)
        arc_neg.add_updater(lambda m: m.become(
                ParametricCurve(
                curve_function_neg,
                color = YELLOW,
                t_range = np.array([0, new_arc_angle.get_value(), 0.01])
            ).shift(RIGHT*10+DOWN*group1_shift)

        ))
        arrow3 = always_redraw(lambda:
            make_arrow(
                np.array([0.8,0.8,0]), 
                np.array([0.8,a1_length.get_value(),0]),
                YELLOW,
            )
        )
        arrow4 = always_redraw(lambda:
            make_arrow(
                np.array([0.8,-0.8,0]), 
                np.array([0.8,a1_length.get_value(),0]),
                YELLOW,
            )
        )
        a1_length.set_value(0.8)
        self.add(arc_pos, arrow_tip_pos, arrow3)
        self.play(
            FadeIn(y_label_pos_top),
            new_arc_angle.animate.set_value((2/9)*TAU),
            a1_length.animate.set_value(4.8)
        )
        y_label_pos_bot = Tex("(5+)").scale(0.7).next_to([0,-5,0],DOWN)
        self.wait(2)
        self.remove(arc_pos, arrow_tip_pos, arrow3)
        self.wait()
        new_arc_angle.set_value(0)
        a1_length.set_value(-0.8)
        self.add(arc_neg, arrow_tip_neg, arrow4)

        self.play(
            FadeIn(y_label_pos_bot),
            new_arc_angle.animate.set_value((2/9)*TAU),
            a1_length.animate.set_value(-4.8)
        )
        points_y = Group(
            Dot(np.array([0,-4.5,0.1])),
            Dot(np.array([0,4.5,0.1])),
        )
        self.wait(2)
        self.remove(arc_neg, arrow_tip_neg, arrow4)
        self.wait(2)
        self.play(
            FadeIn(points_y)
        )
        self.wait(2)
        self.play(
            FadeIn(gold_dot),
            FadeIn(circle_dot),
            FadeIn(circle_dot2),
        )
        self.wait(2)

        number2 = Tex("1").scale(2).move_to(circle2.get_center())
        plus2 = Tex("+").next_to(number2, LEFT)
        sub_number2 = Tex("4+").next_to(number2, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1).set_color(BLUE)

        self.play(
            y_coord.animate.set_value(1),
            angle2.animate.set_value((1/9)*TAU),
            FadeIn(number2),
            FadeIn(plus2),
            FadeIn(sub_number2),
        )
        self.wait(2)

        self.play(
            FadeOut(number2),
            FadeOut(plus2),
            FadeOut(sub_number2),
        )

        self.remove(arc_pos2)
        self.wait()
        angle2_start.set_value((1/9)*TAU)
        self.add(arc_pos2)
        number2 = Tex("2").scale(2).move_to(circle2.get_center())
        plus2 = Tex("+").next_to(number2, LEFT)
        sub_number2 = Tex("4+").next_to(number2, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1).set_color(BLUE)

        self.play(
            y_coord.animate.set_value(3),
            angle2.animate.set_value((3/9)*TAU),
            FadeIn(number2),
            FadeIn(plus2),
            FadeIn(sub_number2),
        )
        self.wait(2)

        self.play(
            FadeOut(number2),
            FadeOut(plus2),
            FadeOut(sub_number2),
        )

        self.remove(arc_pos2)
        self.wait()
        angle2_start.set_value((3/9)*TAU)
        self.add(arc_pos2)
        number2 = Tex("4").scale(2).move_to(circle2.get_center())
        plus2 = Tex("+").next_to(number2, LEFT)
        sub_number2 = Tex("5+").next_to(number2, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1).set_color(BLUE)

        self.play(
            y_coord.animate.set_value(-1),
            angle2.animate.set_value(-(1/9)*TAU),
            FadeIn(number2),
            FadeIn(plus2),
            FadeIn(sub_number2),
        )
        self.wait(2)

        self.play(
            FadeOut(number2),
            FadeOut(plus2),
            FadeOut(sub_number2),
        )

        self.remove(arc_pos2)
        self.wait()
        angle2_start.set_value(-(1/9)*TAU)
        self.add(arc_pos2)
        number2 = Tex("3").scale(2).move_to(circle2.get_center())
        plus2 = Tex("+").next_to(number2, LEFT)
        sub_number2 = Tex("5+").next_to(number2, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1).set_color(BLUE)

        self.play(
            y_coord.animate.set_value(-4),
            angle2.animate.set_value(-(4/9)*TAU),
            FadeIn(number2),
            FadeIn(plus2),
            FadeIn(sub_number2),
        )
        self.wait(2)

        self.play(
            FadeOut(number2),
            FadeOut(plus2),
            FadeOut(sub_number2),
        )

        self.remove(arc_pos2)
        self.wait()
        angle2_start.set_value(-(4/9)*TAU)
        y_coord.set_value(4)
        self.add(arc_pos2)
        number2 = Tex("5").scale(2).move_to(circle2.get_center())
        plus2 = Tex("+").next_to(number2, LEFT)
        sub_number2 = Tex("5+").next_to(number2, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1).set_color(BLUE)

        self.play(
            y_coord.animate.set_value(0),
            angle2.animate.set_value(-TAU),
            FadeIn(number2),
            FadeIn(plus2),
            FadeIn(sub_number2),
        )
        self.wait(2)
        self.play(
            FadeOut(number2),
            FadeOut(plus2),
            FadeOut(sub_number2),
            FadeOut(gold_dot),
            FadeOut(circle_dot),
            FadeOut(circle_dot2),
        )

        angle.set_value(0)
        angle_start.set_value(0)
        angle2.set_value(0)
        angle2_start.set_value(0)

        self.wait(2)
        pos_diamonds_xy = diamond_plane_pos(5,5,0,"xy").set_opacity(0)
        neg_diamonds_xy = diamond_plane_neg(5,5,0,"xy").set_opacity(0)
        pos_numbers_xy = generate_number_grid_pos(5,5,0,"xy",9).set_opacity(0)
        neg_numbers_xy = generate_number_grid_neg(5,5,0,"xy",2).set_opacity(0)

        self.wait(2)
        self.play(
            pos_diamonds_xy.animate.set_opacity(1.0),
            pos_numbers_xy.animate.set_opacity(1.0),
        )

        vertical_group = Group(
            Line(np.array([-4.5,4.5,0]),np.array([-4.5,-4.5,0])),
            Line(np.array([4.5,4.5,0]),np.array([4.5,-4.5,0])),
        )
        horizontal_group = Group(
            Line(np.array([-4.5,4.5,0]),np.array([4.5,4.5,0])),
            Line(np.array([-4.5,-4.5,0]),np.array([4.5,-4.5,0])),
        )

        self.wait(2)
        self.play(FadeIn(vertical_group))
        self.wait(2)
        self.play(FadeOut(vertical_group))
        self.play(FadeIn(horizontal_group))
        self.wait(2)
        self.play(FadeOut(horizontal_group))
        self.wait(2)

        self.play(
            FadeIn(gold_dot),
            FadeIn(circle_dot),
            FadeIn(circle_dot2),
        )
        self.wait(2)
        self.add(arc_pos2)

        number = Tex("2").scale(2).move_to(circle1.get_center())
        sub_number = Tex("1+").next_to(number, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1).set_color(RED)

        number2 = Tex("2").scale(2).move_to(circle2.get_center())
        sub_number2 = Tex("4+").next_to(number2, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1).set_color(RED)

        self.play(
            x_coord.animate.set_value(2),
            angle.animate.set_value((2/9)*TAU),
            FadeIn(number),
            FadeIn(sub_number),
        )
        self.wait(2)

        self.play(
            y_coord.animate.set_value(2),
            angle2.animate.set_value((2/9)*TAU),
            FadeIn(number2),
            FadeIn(sub_number2),
        )
        self.wait(2)

        self.play(
            FadeOut(number),
            FadeOut(sub_number),
        )
        number = Tex("3").scale(2).move_to(circle1.get_center())
        sub_number = Tex("8+").next_to(number, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1).set_color(BLUE)

        self.play(
            x_coord.animate.set_value(-3),
            angle.animate.set_value(-(3/9)*TAU),
            FadeIn(number),
            FadeIn(sub_number),
        )
        self.wait(2)

        self.play(
            FadeOut(number2),
            FadeOut(sub_number2),
        )
        number2 = Tex("1").scale(2).move_to(circle2.get_center())
        sub_number2 = Tex("4+").next_to(number2, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1).set_color(RED)

        self.play(
            y_coord.animate.set_value(1),
            angle2.animate.set_value((1/9)*TAU),
            FadeIn(number2),
            FadeIn(sub_number2),
        )
        self.wait(2)

        self.play(
            FadeOut(number),
            FadeOut(sub_number),
        )
        number = Tex("1").scale(2).move_to(circle1.get_center())
        sub_number = Tex("8+").next_to(number, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1).set_color(BLUE)

        self.play(
            x_coord.animate.set_value(-1),
            angle.animate.set_value(-(1/9)*TAU),
            FadeIn(number),
            FadeIn(sub_number),
        )
        self.wait(2)

        self.play(
            FadeOut(number2),
            FadeOut(sub_number2),
        )
        number2 = Tex("2").scale(2).move_to(circle2.get_center())
        sub_number2 = Tex("5+").next_to(number2, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1).set_color(BLUE)

        self.play(
            y_coord.animate.set_value(-2),
            angle2.animate.set_value(-(2/9)*TAU),
            FadeIn(number2),
            FadeIn(sub_number2),
        )
        self.wait(2)

        self.play(
            FadeOut(number),
            FadeOut(sub_number),
        )
        number = Tex("1").scale(2).move_to(circle1.get_center())
        sub_number = Tex("1+").next_to(number, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1).set_color(RED)

        self.play(
            x_coord.animate.set_value(1),
            angle.animate.set_value((1/9)*TAU),
            FadeIn(number),
            FadeIn(sub_number),
        )
        self.wait(2)

        self.play(
            FadeOut(number2),
            FadeOut(sub_number2),
            y_coord.animate.set_value(-4),
        )
        number2 = Tex("7").scale(2).move_to(circle2.get_center())
        sub_number2 = Tex("4+").next_to(number2, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1).set_color(RED)

        y_coord.set_value(4)
        self.play(
            y_coord.animate.set_value(-2),
            angle2.animate.set_value((7/9)*TAU),
            FadeIn(number2),
            FadeIn(sub_number2),
        )
        self.wait(2)

        self.play(
            FadeOut(number),
            FadeOut(sub_number),
            x_coord.animate.set_value(-4),
        )
        number = Tex("8").scale(2).move_to(circle1.get_center())
        sub_number = Tex("8+").next_to(number, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1).set_color(BLUE)

        x_coord.set_value(4)
        self.play(
            x_coord.animate.set_value(1),
            angle.animate.set_value(-(8/9)*TAU),
            FadeIn(number),
            FadeIn(sub_number),
        )
        self.wait(2)
        arc_pos1.clear_updaters()
        arc_pos2.clear_updaters()
        gold_dot.clear_updaters()
        circle_dot.clear_updaters()
        circle_dot2.clear_updaters()
        self.play(
            FadeOut(gold_dot),
            FadeOut(circle_dot),
            FadeOut(circle_dot2),
            FadeOut(arc_pos1),
            FadeOut(arc_pos2),
            FadeOut(number),
            FadeOut(sub_number),
            FadeOut(number2),
            FadeOut(sub_number2),
            FadeOut(vbm_point),
            FadeOut(vbm_point2),
            FadeOut(dots1),
            FadeOut(numbers1),
            FadeOut(dots2),
            FadeOut(numbers2),
            FadeOut(positives),
            FadeOut(positives2),
        )
        self.wait(2)

        negatives = number_polarities_neg(numbers1, 0.5)
        negatives2 = number_polarities_neg(numbers2, 0.5)

        dots1.set_color(WHITE),
        numbers1.set_color(WHITE),
        dots2.set_color(WHITE),
        numbers2.set_color(WHITE),


        self.play(
            neg_diamonds_xy[36].animate.set_opacity(1.0),
            neg_numbers_xy[36].animate.set_opacity(1.0),
        )
        self.wait(2)
        self.play(
            neg_diamonds_xy[29].animate.set_opacity(1.0),
            neg_numbers_xy[29].animate.set_opacity(1.0),
        )
        self.wait(2)
        self.play(
            neg_diamonds_xy[22].animate.set_opacity(1.0),
            neg_numbers_xy[22].animate.set_opacity(1.0),
        )
        self.wait(2)
        self.play(
            neg_diamonds_xy[15].animate.set_opacity(1.0),
            neg_numbers_xy[15].animate.set_opacity(1.0),
            neg_diamonds_xy[43].animate.set_opacity(1.0),
            neg_numbers_xy[43].animate.set_opacity(1.0),
            neg_diamonds_xy[50].animate.set_opacity(1.0),
            neg_numbers_xy[50].animate.set_opacity(1.0),
            neg_diamonds_xy[57].animate.set_opacity(1.0),
            neg_numbers_xy[57].animate.set_opacity(1.0),
        )

        self.wait(2)
        self.play(
            neg_diamonds_xy[27].animate.set_opacity(1.0),
            neg_numbers_xy[27].animate.set_opacity(1.0),
        )
        self.wait(2)
        self.play(
            neg_diamonds_xy[20].animate.set_opacity(1.0),
            neg_numbers_xy[20].animate.set_opacity(1.0),
        )
        self.wait(2)
        self.play(
            neg_diamonds_xy[13].animate.set_opacity(1.0),
            neg_numbers_xy[13].animate.set_opacity(1.0),
        )
        self.wait(2)
        self.play(
            neg_diamonds_xy[6].animate.set_opacity(1.0),
            neg_numbers_xy[6].animate.set_opacity(1.0),
            neg_diamonds_xy[34].animate.set_opacity(1.0),
            neg_numbers_xy[34].animate.set_opacity(1.0),
            neg_diamonds_xy[41].animate.set_opacity(1.0),
            neg_numbers_xy[41].animate.set_opacity(1.0),
            neg_diamonds_xy[48].animate.set_opacity(1.0),
            neg_numbers_xy[48].animate.set_opacity(1.0),
        )

        self.wait(2)
        def select_diags(array, pattern, offset):
            result = Group()
            i = offset
            pattern_index = 0
            while i < len(array):
                result.add(array[i])
                i += pattern[pattern_index]
                pattern_index = (pattern_index + 1) % len(pattern)
            return result

        blue_diags = select_diags(neg_diamonds_xy,[3,3,4,3,4,3,3,1],0)
        red_diags = select_diags(neg_diamonds_xy,[3,4,3,3,1,3,3,4],2)
        blue_nums = select_diags(neg_numbers_xy,[3,3,4,3,4,3,3,1],0)
        red_nums = select_diags(neg_numbers_xy,[3,4,3,3,1,3,3,4],2)

        self.play(
            blue_diags.animate.set_opacity(1.0),
            red_diags.animate.set_opacity(1.0),
            blue_nums.animate.set_opacity(1.0),
            red_nums.animate.set_opacity(1.0),
        )
        self.wait(2)

        self.play(
            neg_diamonds_xy[28].animate.set_opacity(1.0),
            neg_numbers_xy[28].animate.set_opacity(1.0),
        )
        self.wait(2)

        self.play(
            neg_diamonds_xy[4].animate.set_opacity(1.0),
            neg_numbers_xy[4].animate.set_opacity(1.0),
            neg_diamonds_xy[52].animate.set_opacity(1.0),
            neg_numbers_xy[52].animate.set_opacity(1.0),
        )
        self.wait(2)
        x_label_neg_right = Tex("(8-)").scale(0.7).next_to([5.5,0.5,0],RIGHT).set_opacity(0)
        x_label_neg_left = Tex("(1-)").scale(0.7).next_to([-4.5,0.5,0],LEFT).set_opacity(0)
        self.wait(2)
        self.add(x_label_neg_right, x_label_neg_left)

        self.play(
            FadeIn(axes_neg.x_axis),
            x_label_neg_left.animate.set_opacity(1.0),
            x_label_neg_right.animate.set_opacity(1.0),
            FadeIn(dots1),
            FadeIn(numbers1),
            FadeIn(negatives),
        )
        self.wait(2)

        self.play(
            neg_diamonds_xy[32].animate.set_opacity(1.0),
            neg_numbers_xy[32].animate.set_opacity(1.0),
            neg_diamonds_xy[35].animate.set_opacity(1.0),
            neg_numbers_xy[35].animate.set_opacity(1.0),
            neg_diamonds_xy[38].animate.set_opacity(1.0),
            neg_numbers_xy[38].animate.set_opacity(1.0),
        )
        y_label_neg_right = Tex("(5-)").scale(0.7).next_to([0.5,5.5,0],UP).set_opacity(0)
        y_label_neg_left = Tex("(4-)").scale(0.7).next_to([0.5,-4.5,0],DOWN).set_opacity(0)
        self.wait(2)
        self.add(y_label_neg_right, y_label_neg_left)
        self.play(
            FadeIn(axes_neg.y_axis),
            y_label_neg_left.animate.set_opacity(1.0),
            y_label_neg_right.animate.set_opacity(1.0),
            FadeIn(dots2),
            FadeIn(numbers2),
            FadeIn(negatives2),
        )
        self.wait(2)

        neg_diamonds_new = diamond_plane_neg(6,6,0,"xy").set_opacity(0)
        neg_numbers_new = generate_number_grid_neg(6,6,0,"xy",2).set_opacity(0)

        def skip_and_filter(array, start_index, skip_nth):
            filtered_part = array[start_index:]
            trimmed = [x for i, x in enumerate(filtered_part) if(i+1) % skip_nth!=0]
            result = Group(*trimmed)
            return result
        
        neg_diamonds_offset = skip_and_filter(neg_diamonds_new, 11, 10)
        neg_numbers_offset = skip_and_filter(neg_numbers_new, 11, 10)

        self.play(
            neg_diamonds_offset.animate.set_opacity(1.0),
            neg_numbers_offset.animate.set_opacity(1.0)
        )

        self.wait(2)

        circle_dot.set_color(TEAL)
        circle_dot2.set_color(TEAL)
        arc_pos1.set_color(TEAL)
        arc_pos2.set_color(TEAL)
        angle.set_value(0)
        angle2.set_value(0)
        angle_start.set_value(0)
        angle2_start.set_value(0)
        x_coord.set_value(2.5)
        y_coord.set_value(0.5)

        blue_dot=always_redraw(lambda: 
            Circle(radius=0.3).move_to(
                np.array([x_coord.get_value(),y_coord.get_value(),0])
            ).set_color(TEAL))

        arc_pos1.add_updater(lambda m: m.become(
                ParametricCurve(
                curve_function_pos1,
                color = TEAL,
                t_range = np.array([angle_start.get_value(), angle.get_value(), 0.01])
            ).shift(RIGHT*10).shift(UP*group1_shift)

        ))
        circle_dot = always_redraw(lambda: Dot().scale(2).set_color(TEAL).move_to(
            np.array([2*np.sin(angle.get_value())+10, 2*np.cos(angle.get_value())+group1_shift, 0])
        ))
        arc_pos2.add_updater(lambda m: m.become(
                ParametricCurve(
                curve_function_pos2,
                color = TEAL,
                t_range = np.array([angle2_start.get_value(), angle2.get_value(), 0.01])
            ).shift(RIGHT*10).shift(DOWN*group1_shift)

        ))
        circle_dot2 = always_redraw(lambda: Dot().scale(2).set_color(TEAL).move_to(
            np.array([2*np.sin(angle2.get_value())+10, 2*np.cos(angle2.get_value())-group1_shift, 0])
        ))
        
        self.play(
            FadeIn(blue_dot),
            FadeIn(circle_dot),
            FadeIn(circle_dot2),
            FadeIn(arc_pos1),
            FadeIn(arc_pos2),
        )
        

    #############

        self.wait(2)
        self.add(arc_pos2)

        number = Tex("4").scale(2).move_to(circle1.get_center())
        sub_number = Tex("1-").next_to(number, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1)

        number2 = Tex("2").scale(2).move_to(circle2.get_center())
        sub_number2 = Tex("4-").next_to(number2, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1)

        self.play(
            x_coord.animate.set_value(-1.5),
            angle.animate.set_value((4/9)*TAU),
            FadeIn(number),
            FadeIn(sub_number),
        )
        self.wait(2)

        self.play(
            y_coord.animate.set_value(-1.5),
            angle2.animate.set_value((2/9)*TAU),
            FadeIn(number2),
            FadeIn(sub_number2),
        )
        self.wait(2)

        self.play(
            FadeOut(number),
            FadeOut(sub_number),
        )
        number = Tex("2").scale(2).move_to(circle1.get_center())
        sub_number = Tex("8-").next_to(number, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1)

        self.play(
            x_coord.animate.set_value(4.5),
            angle.animate.set_value(-(2/9)*TAU),
            FadeIn(number),
            FadeIn(sub_number),
        )
        self.wait(2)

        self.play(
            FadeOut(number2),
            FadeOut(sub_number2),
        )
        number2 = Tex("2").scale(2).move_to(circle2.get_center())
        sub_number2 = Tex("5-").next_to(number2, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1)

        self.play(
            y_coord.animate.set_value(2.5),
            angle.animate.set_value((2/9)*TAU),
            FadeIn(number2),
            FadeIn(sub_number2),
        )
        self.wait(2)

        self.play(
            FadeOut(number),
            FadeOut(sub_number),
        )
        x_coord.set_value(-3.5)
        number = Tex("5").scale(2).move_to(circle1.get_center())
        sub_number = Tex("8-").next_to(number, DOWN+RIGHT).shift(UP*0.4+LEFT*0.1)
        self.play(
            x_coord.animate.set_value(-0.5),
            angle.animate.set_value(-(5/9)*TAU),
            FadeIn(number),
            FadeIn(sub_number),
        )
        self.wait(2)

        blue_dot.clear_updaters()
        arc_pos1.clear_updaters()
        arc_pos2.clear_updaters()
        gold_dot.clear_updaters()
        circle_dot.clear_updaters()
        circle_dot2.clear_updaters()
        self.play(
            FadeOut(blue_dot),
            FadeOut(circle_dot),
            FadeOut(circle_dot2),
            FadeOut(arc_pos1),
            FadeOut(arc_pos2),
            FadeOut(number),
            FadeOut(sub_number),
            FadeOut(number2),
            FadeOut(sub_number2),
            FadeOut(vbm_point),
            FadeOut(vbm_point2),
            FadeOut(dots1),
            FadeOut(numbers1),
            FadeOut(dots2),
            FadeOut(numbers2),
            FadeOut(negatives),
            FadeOut(negatives2),
        )
        self.wait(2)

        def triangle_maker(offset, u_d):
            line_group = Group()
            r = 2
            for i in range(0,3):
                new_line = Line(
                    [
                        10 + (r * np.sin(offset+(TAU * (((i*3)%9) / 9)))),
                        (u_d * group1_shift) + (r * np.cos(offset+(TAU * (((i*3)%9) / 9)))),
                        0
                    ],
                    [
                        10 + (r * np.sin(offset+(TAU * (((i*3+3)%9) / 9)))),
                        (u_d * group1_shift) + (r * np.cos(offset+(TAU * (((i*3+3)%9) / 9)))),
                        0
                    ],
                ).set_stroke(width=5)
                line_group.add(new_line)
            return line_group

        offset_angle = ValueTracker(0)
        triangle_pos = always_redraw(lambda: triangle_maker(offset_angle.get_value(), 1))
        triangle_neg = always_redraw(lambda: triangle_maker(-offset_angle.get_value(), -1))

        numbers1_new = vbm_numbers(1,9,1.0,2.6)
        positives_new = number_polarities_pos(numbers1_new, 0.5)
        dots1_new = vbm_dots(1,9,1.4,2)
        group1_new = Group(dots1_new, numbers1_new, positives_new, triangle_pos).shift(RIGHT*10)
        group1_new.shift(UP*group1_shift)

        numbers2_new = vbm_numbers(1,9,1.0,2.6).set_color(WHITE)
        negatives_new = number_polarities_neg(numbers2_new, 0.5)
        dots2_new = vbm_dots(1,9,1.4,2).set_color(WHITE)
        group2_new = Group(dots2_new, numbers2_new, negatives_new, triangle_neg).shift(RIGHT*10)
        group2_new.shift(DOWN*group1_shift)

        triangle_pos.suspend_updating()
        triangle_neg.suspend_updating()
        self.play(
            FadeIn(group1_new),
            FadeIn(group2_new),
        )
        triangle_pos.resume_updating()
        triangle_neg.resume_updating()


        neg_diamonds_xy_new = diamond_plane_neg(5,5,0,"xy")
        neg_numbers_xy_new = generate_number_grid_neg(5,5,0,"xy",2)
        pos_diamonds_xy_new = diamond_plane_pos(5,5,0,"xy")
        pos_numbers_xy_new = generate_number_grid_pos(5,5,0,"xy",9)

        green_diags_neg = select_diags(neg_diamonds_xy_new,[3,3,1,3,3,4,3,4],1)
        green_nums_neg = select_diags(neg_numbers_xy_new,[3,3,1,3,3,4,3,4],1)
        green_diags_pos = select_diags(pos_diamonds_xy_new,[3,3,2,3,3,2,3,3,5],2)
        green_nums_pos = select_diags(pos_numbers_xy_new,[3,3,2,3,3,2,3,3,5],2)
        green_diags = Group(
            green_diags_neg,
            green_diags_pos,
            green_nums_neg,
            green_nums_pos,
        ).set_opacity(0)
        self.add(green_diags)

        self.play(
            FadeOut(neg_diamonds_offset),
            FadeOut(neg_numbers_offset),
            FadeOut(pos_diamonds_xy),
            FadeOut(pos_numbers_xy),
            FadeOut(pos_diamonds_x_axis),
            FadeOut(pos_numbers_x_axis),
            FadeOut(pos_diamonds_y_axis),
            FadeOut(pos_numbers_y_axis),
            FadeOut(neg_diamonds_xy),
            FadeOut(neg_numbers_xy),
            green_diags.animate.set_opacity(1),
        )
        self.wait(2)
        red_diags_neg = select_diags(neg_diamonds_xy_new,[3,4,3,3,1,3,3,4],2).set_opacity(0)
        red_nums_neg = select_diags(neg_numbers_xy_new,[3,4,3,3,1,3,3,4],2).set_opacity(0)
        red_diags_pos = select_diags(pos_diamonds_xy_new,[3,3,5,3,3,2,3,3,2],0).set_opacity(0)
        red_nums_pos = select_diags(pos_numbers_xy_new,[3,3,5,3,3,2,3,3,2],0).set_opacity(0)
        red_diags = Group(
            red_diags_neg,
            red_diags_pos,
            red_nums_neg,
            red_nums_pos,
        ).set_opacity(0)

        self.add(red_diags)

        self.play(
            green_diags.animate.set_opacity(0),
            red_diags.animate.set_opacity(1),
            offset_angle.animate.set_value(TAU/9)
        )
        self.wait(2)
        blue_diags_neg = select_diags(neg_diamonds_xy_new,[3,3,4,3,4,3,3,1],0).set_opacity(0)
        blue_nums_neg = select_diags(neg_numbers_xy_new,[3,3,4,3,4,3,3,1],0).set_opacity(0)
        blue_diags_pos = select_diags(pos_diamonds_xy_new,[3,3,2,3,3,5,3,3,2],1).set_opacity(0)
        blue_nums_pos = select_diags(pos_numbers_xy_new,[3,3,2,3,3,5,3,3,2],1).set_opacity(0)
        blue_diags = Group(
            blue_diags_neg,
            blue_diags_pos,
            blue_nums_neg,
            blue_nums_pos,
        ).set_opacity(0)

        self.add(blue_diags)

        self.play(
            red_diags.animate.set_opacity(0),
            blue_diags.animate.set_opacity(1),
            offset_angle.animate.set_value(2*TAU/9)
        )
        self.wait(2)
        self.remove(red_diags, green_diags)
        red_diags.set_opacity(1)
        green_diags.set_opacity(1)
        for i in range(0,54):
            diags = [blue_diags, green_diags, red_diags]
            self.remove(diags[i%3])
            self.add(diags[(i+1)%3])
            offset_angle.set_value((3+i)*TAU/9)
            self.wait(0.3)

        for i in range(0,108):
            diags = [blue_diags, green_diags, red_diags]
            self.remove(diags[i%3])
            self.add(diags[(i+1)%3])
            offset_angle.set_value((3+i)*TAU/9)
            self.wait(0.1)
    
        self.wait(2)

class PlaneProperties(Scene):
    def construct(self):
        frame = self.camera.frame
        frame.scale(1.5)
        pos_diamonds = diamond_plane_pos(5,5,0,"xy")
        pos_diamonds_copy = diamond_plane_pos(5,5,0,"xy")
        for pd in pos_diamonds:
            pd.set_stroke(width = 3)
        neg_diamonds = diamond_plane_neg(5,5,0,"xy")
        neg_diamonds_copy = diamond_plane_neg(5,5,0,"xy")
        for nd in neg_diamonds:
            nd.set_stroke(width = 3)
        pos_numbers = generate_number_grid_pos(5,5,0,"xy",9)
        pos_numbers_copy = generate_number_grid_pos(5,5,0,"xy",9)
        neg_numbers = generate_number_grid_neg(5,5,0,"xy",2)
        neg_numbers_copy = generate_number_grid_neg(5,5,0,"xy",2)

        def select_diags(array, pattern, offset):
            result = Group()
            i = offset
            pattern_index = 0
            while i < len(array):
                result.add(array[i])
                i += pattern[pattern_index]
                pattern_index = (pattern_index + 1) % len(pattern)
            return result

        green_diags_neg = select_diags(select_diags(neg_diamonds_copy,[3,3,1,3,3,4,3,4],1),[4,3,3,1,3,3,4],0)
        for gd in green_diags_neg:
            gd.set_stroke(width = 8.0)
        green_nums_neg = select_diags(select_diags(neg_numbers_copy,[3,3,1,3,3,4,3,4],1),[4,3,3,1,3,3,4],0)
        green_diags_pos = select_diags(select_diags(pos_diamonds_copy,[3,3,2,3,3,2,3,3,5],2),[4,1,3,4,4,3,1,4],1)
        for gd in green_diags_pos:
            gd.set_stroke(width = 8.0)
        green_nums_pos = select_diags(select_diags(pos_numbers_copy,[3,3,2,3,3,2,3,3,5],2),[4,1,3,4,4,3,1,4],1)
        green_diags = Group(
            green_diags_neg,
            green_diags_pos,
            green_nums_neg,
            green_nums_pos,
        )

        base_grid = Group(
            pos_diamonds,
            neg_diamonds,
            pos_numbers,
            neg_numbers,
        )
        self.add(
            base_grid
        )

        square = Group(
            Line([0,1.5,0],[1.5,0,0]).set_color(BLACK).set_stroke(width=8.0),
            Line([1.5,0,0],[0,-1.5,0]).set_color(BLACK).set_stroke(width=8.0),
            Line([0,-1.5,0],[-1.5,0,0]).set_color(BLACK).set_stroke(width=8.0),
            Line([-1.5,0,0],[0,1.5,0]).set_color(BLACK).set_stroke(width=8.0),
        )
        square2 = square.copy().shift(LEFT*1.5 + UP*1.5)
        square3 = square.copy().shift(LEFT*3 + UP*3)
        square4 = square.copy().shift(RIGHT*1.5 + DOWN*1.5)
        square5 = square.copy().shift(RIGHT*3 + DOWN*3)
        big_square_group = Group(
            square,
            square2,
            square3,
            square4,
            square5,
        )
        square6 = square3.copy().shift(RIGHT*2.5 + UP*0.5)
        square7 = square2.copy().shift(RIGHT*2.5 + UP*0.5)
        square8 = square.copy().shift(RIGHT*2.5 + UP*0.5)
        square9 = square4.copy().shift(RIGHT*2.5 + UP*0.5)
        big_square_group.add(square6,square7,square8,square9)
        square10 = square2.copy().shift(LEFT*2.5 + DOWN*0.5)
        square11 = square.copy().shift(LEFT*2.5 + DOWN*0.5)
        square12 = square4.copy().shift(LEFT*2.5 + DOWN*0.5)
        square13 = square5.copy().shift(LEFT*2.5 + DOWN*0.5)
        big_square_group.add(square10,square11,square12,square13)

        square14 = square12.copy().shift(LEFT*2.5 + DOWN*0.5)
        square15 = square13.copy().shift(LEFT*2.5 + DOWN*0.5)
        square16 = square6.copy().shift(RIGHT*2.5 + UP*0.5)
        square17 = square7.copy().shift(RIGHT*2.5 + UP*0.5)
        big_square_group.add(square14,square15,square16,square17)

        self.wait()
        sqr_blocker_right = Rectangle(width=3,height=12).set_stroke(width=0).set_fill(color="#0A1433").set_opacity(1)
        sqr_blocker_right.shift(RIGHT*6)
        sqr_blocker_left = Rectangle(width=3,height=12).set_stroke(width=0).set_fill(color="#0A1433").set_opacity(1)
        sqr_blocker_left.shift(LEFT*6)
        sqr_blocker_top = Rectangle(width=12,height=3).set_stroke(width=0).set_fill(color="#0A1433").set_opacity(1)
        sqr_blocker_top.shift(UP*6)
        sqr_blocker_bottom = Rectangle(width=12,height=3).set_stroke(width=0).set_fill(color="#0A1433").set_opacity(1)
        sqr_blocker_bottom.shift(DOWN*6)
        sqr_blocker = Group(
            sqr_blocker_right,
            sqr_blocker_left,
            sqr_blocker_top,
            sqr_blocker_bottom,
        ).set_z_index(0.3)
        self.add(sqr_blocker)
        self.play(
            FadeIn(big_square_group),
            FadeIn(green_diags),
        )
        self.wait()
        self.play(
            big_square_group.animate.shift(LEFT*3.8),
            green_diags.animate.shift(LEFT*3.8),
            base_grid.animate.shift(LEFT*3.8),
            sqr_blocker.animate.shift(LEFT*3.8),
        )

        sample_pos = Group(
            square.copy().set_color(PURPLE),
            green_diags_pos[4].copy(),
            base_grid[0][40].copy(),
            base_grid[2][40].copy(),
            base_grid[0][41].copy(),
            base_grid[2][41].copy(),
            base_grid[0][39].copy(),
            base_grid[2][39].copy(),
            base_grid[0][31].copy(),
            base_grid[2][31].copy(),
            base_grid[0][49].copy(),
            base_grid[2][49].copy(),
            base_grid[1][27].copy(),
            base_grid[3][27].copy(),
            base_grid[1][28].copy(),
            base_grid[3][28].copy(),
            base_grid[1][35].copy(),
            base_grid[3][35].copy(),
            base_grid[1][36].copy(),
            base_grid[3][36].copy(),
        ).set_z_index(0.4)
        sample_neg = Group(
            square2.copy().set_color(YELLOW),
            green_diags_neg[2].copy(),
            base_grid[0][23].copy(),
            base_grid[2][23].copy(),
            base_grid[0][24].copy(),
            base_grid[2][24].copy(),
            base_grid[0][32].copy(),
            base_grid[2][32].copy(),
            base_grid[0][33].copy(),
            base_grid[2][33].copy(),
            base_grid[1][21].copy(),
            base_grid[3][21].copy(),
            base_grid[1][13].copy(),
            base_grid[3][13].copy(),
            base_grid[1][29].copy(),
            base_grid[3][29].copy(),
            base_grid[1][20].copy(),
            base_grid[3][20].copy(),
            base_grid[1][22].copy(),
            base_grid[3][22].copy(),
        ).set_z_index(0.4)
        self.play(
            sample_pos.animate.shift(RIGHT*9.3+UP*2.2)
        )
        pos_nest_title = Tex(r"\text{Positive Nested Vortices}").next_to(sample_pos, UP,buff=0.4).set_z_index(0.6)
        self.play(FadeIn(pos_nest_title))
        self.play(
            sample_neg.animate.shift(RIGHT*10.8+DOWN*4)
        )
        neg_nest_title = Tex(r"\text{Negative Nested Vortices}").next_to(sample_neg, UP,buff=0.4).set_z_index(0.6)
        self.play(FadeIn(neg_nest_title))
        self.wait()

        example_sqr_pos = Square(1.5*np.sqrt(2),color = PURPLE_A).rotate(PI/4).set_opacity(0.8).set_stroke(color=BLACK)
        example_sqr_neg = Square(1.5*np.sqrt(2),color = YELLOW_A).rotate(PI/4).set_opacity(0.8).set_stroke(color=BLACK)

        pos_squares = Group(
            example_sqr_pos.copy().move_to(sample_pos),
            example_sqr_pos.copy().move_to(square),
            example_sqr_pos.copy().move_to(square3),
            example_sqr_pos.copy().move_to(square5),
            example_sqr_pos.copy().move_to(square7),
            example_sqr_pos.copy().move_to(square9),
            example_sqr_pos.copy().move_to(square10),
            example_sqr_pos.copy().move_to(square12),
            example_sqr_pos.copy().move_to(square15),
            example_sqr_pos.copy().move_to(square16),

            example_sqr_pos.copy().move_to(square).shift(LEFT*5+DOWN),
            example_sqr_pos.copy().move_to(square).shift(LEFT*2+UP*5),
            example_sqr_pos.copy().move_to(square).shift(RIGHT*5+UP),
            example_sqr_pos.copy().move_to(square).shift(RIGHT*2+DOWN*5),
        ).set_z_index(0.4)
        neg_squares = Group(
            example_sqr_neg.copy().move_to(square2),
            example_sqr_neg.copy().move_to(square4),
            example_sqr_neg.copy().move_to(square6),
            example_sqr_neg.copy().move_to(square8),
            example_sqr_neg.copy().move_to(square11),
            example_sqr_neg.copy().move_to(square13),
            example_sqr_neg.copy().move_to(square14),
            example_sqr_neg.copy().move_to(square17),
            example_sqr_neg.copy().move_to(sample_neg),

            example_sqr_neg.copy().move_to(square).shift(LEFT*4.5+DOWN*4.5),
            example_sqr_neg.copy().move_to(square).shift(LEFT*4.5+UP*4.5),
            example_sqr_neg.copy().move_to(square).shift(RIGHT*4.5+DOWN*4.5),
            example_sqr_neg.copy().move_to(square).shift(RIGHT*4.5+UP*4.5),
            example_sqr_neg.copy().move_to(square).shift(LEFT*0.5+DOWN*5.5),
            example_sqr_neg.copy().move_to(square).shift(LEFT*5.5+UP*2.5),
            example_sqr_neg.copy().move_to(square).shift(RIGHT*5.5+DOWN*2.5),
            example_sqr_neg.copy().move_to(square).shift(RIGHT*0.5+UP*5.5),
        ).set_z_index(0.4)
        sqr_blocker.set_z_index(0.5)
        self.play(
            FadeIn(pos_squares),
        )
        self.wait()
        self.play(
            FadeIn(neg_squares),
        )
        self.wait()

        s1 = 2.8
        arrow1 = Arrow(
            np.array([-1*s1,-2*s1,0]),
            np.array([1*s1,2*s1,0]),
        ).set_z_index(0.7).shift(LEFT*3.8).set_color(PURPLE).set_stroke(width = 5)
        arrow2 = Arrow(
            np.array([1*s1,2*s1,0]),
            np.array([-1*s1,-2*s1,0]),
        ).set_z_index(0.7).shift(LEFT*6.05).set_color(YELLOW_B).set_stroke(width = 5)
        arrow3 = Arrow(
            np.array([1*s1,2*s1,0]),
            np.array([-1*s1,-2*s1,0]),
        ).set_z_index(0.7).shift(LEFT*1.55).set_color(YELLOW_B).set_stroke(width = 5)

        arrow4 = Arrow(
            green_diags_pos[0],
            green_diags_pos[1],
        ).set_z_index(0.7).set_color(PURPLE).set_stroke(width = 5).scale(12.2)
        
        arrow5 = Arrow(
            green_diags_pos[7],
            green_diags_pos[8],
        ).set_z_index(0.7).set_color(PURPLE).set_stroke(width = 5).scale(12.2)
        
        diag_pos_copy = green_diags_pos.copy().set_z_index(0.6)
        diag_neg_copy = green_diags_neg.copy().set_z_index(0.6)
        self.play(
            ShowCreation(arrow1),
            ShowCreation(arrow4),
            ShowCreation(arrow5),
            FadeIn(diag_pos_copy)
        )
        self.wait()
        self.play(
            ShowCreation(arrow2),
            ShowCreation(arrow3),
            FadeIn(diag_neg_copy)
        )
        self.wait()

        self.play(
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(arrow3),
            FadeOut(arrow4),
            FadeOut(arrow5),
            FadeOut(diag_pos_copy),
            FadeOut(diag_neg_copy),
            FadeOut(pos_squares),
            FadeOut(neg_squares),
        )
        self.wait()
        self.play(
            FadeOut(big_square_group),
            FadeOut(green_diags),
            FadeOut(pos_nest_title),
            FadeOut(neg_nest_title),
            FadeOut(sample_pos),
            FadeOut(sample_neg),
        )
        waves_title = Tex(r"\text{``Waves of 9''}").shift(RIGHT*5.5+UP*4).scale(2).set_z_index(1)
        self.wait()
        self.play(ShowCreation(waves_title))
        self.wait()
        zeroth_wave_title = Tex(r"\text{zeroth wave:}").scale(1.2).set_z_index(1)
        first_wave_title = Tex(r"\text{first wave:}").scale(1.2).set_z_index(1)
        second_wave_title = Tex(r"\text{second wave:}").scale(1.2).set_z_index(1)
        third_wave_title = Tex(r"\text{third wave:}").scale(1.2).set_z_index(1)
        fourth_wave_title = Tex(r"\text{fourth wave:}").scale(1.2).set_z_index(1)

        zeroth_wave_title.set_z_index(1).next_to(waves_title, DOWN).shift(DOWN*0.7+LEFT*2.5)
        first_wave_title.set_z_index(1).next_to(zeroth_wave_title, DOWN).shift(DOWN+RIGHT*0.24)

        self.play(ShowCreation(zeroth_wave_title))
        self.wait()
        self.play(
            FadeIn(green_diags[1][4].set_z_index(1).set_color(YELLOW).set_stroke(color=BLACK)),
            FadeIn(green_diags[3][4].set_z_index(1)),
        )

        self.wait()
        nine_example = Tex(r"9").set_color(GREEN).next_to(zeroth_wave_title, RIGHT, buff=0.7).scale(1.5)
        self.play(FadeIn(nine_example))
        self.wait()
        self.play(nine_example.animate.set_color(YELLOW))
        self.wait()
        first_wave_square = Square(1.5*np.sqrt(2),color = YELLOW_A).rotate(PI/4).set_opacity(0.8).set_stroke(width=8, color=BLACK)
        first_wave_square.move_to(green_diags[1][4]).set_z_index(0.3)
        self.play(
            FadeIn(first_wave_square),
            ShowCreation(first_wave_title),
        )
        self.wait()
        numbers = Group(
            Tex(r"+"),
            Tex(r"1").scale(1.5), Tex(r"2").scale(1.5), Tex(r"3").scale(1.5),
            Tex(r"4").scale(1.5), Tex(r"5").scale(1.5), Tex(r"6").scale(1.5),
            Tex(r"7").scale(1.5), Tex(r"8").scale(1.5), Tex(r"9").scale(1.5),
        )
        wave_order_pos = [41,31,39,49]
        wave_order_neg = [28,27,35,36]
        n0 = numbers[4].copy().set_color(RED).next_to(first_wave_title, RIGHT, buff=0.7)
        self.play(
            FadeIn(pos_numbers[wave_order_pos[0]].copy().set_z_index(1)),
            FadeIn(n0)
        )
        self.wait()
        p1 = numbers[0].copy().next_to(n0, RIGHT)
        n1 = numbers[3].copy().set_color(WHITE).next_to(p1, RIGHT)
        self.play(
            FadeIn(neg_numbers[wave_order_neg[0]].copy().set_z_index(1)),
            FadeIn(p1),
            FadeIn(n1),
        )
        self.wait()
        equal_sign = Tex(r"=").next_to(n0, DOWN, buff=0.7)
        sum1 = numbers[7].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)
        self.play(
            FadeIn(equal_sign),
            FadeIn(sum1),
        )
        self.wait()
        p2 = numbers[0].copy().next_to(n1, RIGHT)
        n2 = numbers[8].copy().set_color(BLUE).next_to(p2, RIGHT)
        sum2 = numbers[6].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)

        self.play(
            FadeIn(pos_numbers[wave_order_pos[1]].copy().set_z_index(1)),
            FadeIn(p2),
            FadeIn(n2),
            ReplacementTransform(sum1, sum2)
        )
        self.wait()

        p3 = numbers[0].copy().next_to(n2, RIGHT)
        n3 = numbers[7].copy().set_color(WHITE).next_to(p3, RIGHT)
        sum3 = numbers[4].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)

        self.play(
            FadeIn(neg_numbers[wave_order_neg[1]].copy().set_z_index(1)),
            FadeIn(p3),
            FadeIn(n3),
            ReplacementTransform(sum2, sum3)
        )
        self.wait()
        self.play(
            equal_sign.animate.shift(DOWN),
            sum3.animate.shift(DOWN),
        )
        p4 = numbers[0].copy().next_to(n3, RIGHT)
        n4 = numbers[5].copy().set_color(BLUE).next_to(n0, DOWN, buff=0.5)
        sum4 = numbers[9].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)

        self.play(
            FadeIn(pos_numbers[wave_order_pos[2]].copy().set_z_index(1)),
            FadeIn(p4),
            FadeIn(n4),
            ReplacementTransform(sum3, sum4)
        )
        self.wait()

        p5 = numbers[0].copy().next_to(n4, RIGHT)
        n5 = numbers[6].copy().set_color(WHITE).next_to(p5, RIGHT)
        sum5 = numbers[6].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)

        self.play(
            FadeIn(neg_numbers[wave_order_neg[2]].copy().set_z_index(1)),
            FadeIn(p5),
            FadeIn(n5),
            ReplacementTransform(sum4, sum5)
        )
        self.wait()

        p6 = numbers[0].copy().next_to(n5, RIGHT)
        n6 = numbers[1].copy().set_color(RED).next_to(p6, RIGHT)
        sum6 = numbers[7].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)

        self.play(
            FadeIn(pos_numbers[wave_order_pos[3]].copy().set_z_index(1)),
            FadeIn(p6),
            FadeIn(n6),
            ReplacementTransform(sum5, sum6)
        )
        self.wait()

        p7 = numbers[0].copy().next_to(n6, RIGHT)
        n7 = numbers[2].copy().set_color(WHITE).next_to(p7, RIGHT)
        sum7 = numbers[9].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)

        self.play(
            FadeIn(neg_numbers[wave_order_neg[3]].copy().set_z_index(1)),
            FadeIn(p7),
            FadeIn(n7),
            ReplacementTransform(sum6, sum7)
        )
        self.wait()

        self.play(
            FadeOut(n0), FadeOut(n1), FadeOut(n2), FadeOut(n3),
            FadeOut(n4), FadeOut(n5), FadeOut(n6), FadeOut(n7),
            FadeOut(p1), FadeOut(p2), FadeOut(p3),
            FadeOut(p4), FadeOut(p5), FadeOut(p6), FadeOut(p7),
            FadeOut(equal_sign),
            sum7.animate.move_to(n0)
        )
        second_wave_title.set_z_index(1).next_to(first_wave_title, DOWN).shift(DOWN+LEFT*0.36)
        self.wait()

        second_wave_square = Square(2.5*np.sqrt(2),color = YELLOW_A).rotate(PI/4).set_opacity(0.8).set_stroke(width=8, color=BLACK)
        second_wave_square.move_to(green_diags[1][4]).set_z_index(0.2)
        self.play(
            FadeIn(second_wave_square),
            ShowCreation(second_wave_title),
        )
        self.wait()
        wave_order_pos = [42,32,22,30,38,48,58,50]
        wave_order_neg = [29,20,19,26,34,43,44,37]
        n0 = numbers[8].copy().set_color(BLUE).next_to(second_wave_title, RIGHT, buff=0.7)
        self.play(
            FadeIn(pos_numbers[wave_order_pos[0]].copy().set_z_index(1)),
            FadeIn(n0)
        )
        self.wait()

        p1 = numbers[0].copy().next_to(n0, RIGHT)
        n1 = numbers[8].copy().set_color(WHITE).next_to(p1, RIGHT)
        self.play(
            FadeIn(neg_numbers[wave_order_neg[0]].copy().set_z_index(1)),
            FadeIn(p1),
            FadeIn(n1),
        )
        self.wait()

        equal_sign = Tex(r"=").next_to(n0, DOWN, buff=0.7)
        sum1 = numbers[7].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)
        self.play(
            FadeIn(equal_sign),
            FadeIn(sum1),
        )
        self.wait()

        p2 = numbers[0].copy().next_to(n1, RIGHT)
        n2 = numbers[3].copy().set_color(GREEN).next_to(p2, RIGHT)
        sum2 = numbers[1].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)
        self.play(
            FadeIn(pos_numbers[wave_order_pos[1]].copy().set_z_index(1)),
            FadeIn(p2),
            FadeIn(n2),
            ReplacementTransform(sum1, sum2)
        )
        self.wait()

        p3 = numbers[0].copy().next_to(n2, RIGHT)
        n3 = numbers[4].copy().set_color(WHITE).next_to(p3, RIGHT)
        sum3 = numbers[5].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)
        self.play(
            FadeIn(neg_numbers[wave_order_neg[1]].copy().set_z_index(1)),
            FadeIn(p3),
            FadeIn(n3),
            ReplacementTransform(sum2, sum3)
        )
        self.wait()
        self.play(
            sum3.animate.shift(DOWN),
            equal_sign.animate.shift(DOWN),
        )
        self.wait()

        p4 = numbers[0].copy().next_to(n3, RIGHT)
        n4 = numbers[7].copy().set_color(RED).next_to(n0, DOWN, buff=0.5)
        sum4 = numbers[3].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)
        self.play(
            FadeIn(pos_numbers[wave_order_pos[2]].copy().set_z_index(1)),
            FadeIn(p4),
            FadeIn(n4),
            ReplacementTransform(sum3, sum4)
        )
        self.wait()

        p5 = numbers[0].copy().next_to(n4, RIGHT)
        n5 = numbers[8].copy().set_color(WHITE).next_to(p5, RIGHT)
        sum5 = numbers[2].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)
        self.play(
            FadeIn(neg_numbers[wave_order_neg[2]].copy().set_z_index(1)),
            FadeIn(p5),
            FadeIn(n5),
            ReplacementTransform(sum4, sum5)
        )
        self.wait()

        p6 = numbers[0].copy().next_to(n5, RIGHT)
        n6 = numbers[4].copy().set_color(RED).next_to(p6, RIGHT)
        sum6 = numbers[6].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)
        self.play(
            FadeIn(pos_numbers[wave_order_pos[3]].copy().set_z_index(1)),
            FadeIn(p6),
            FadeIn(n6),
            ReplacementTransform(sum5, sum6)
        )
        self.wait()

        p7 = numbers[0].copy().next_to(n6, RIGHT)
        n7 = numbers[2].copy().set_color(WHITE).next_to(p7, RIGHT)
        sum7 = numbers[8].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)
        self.play(
            FadeIn(neg_numbers[wave_order_neg[3]].copy().set_z_index(1)),
            FadeIn(p7),
            FadeIn(n7),
            ReplacementTransform(sum6, sum7)
        )
        self.wait()

        self.play(
            sum7.animate.shift(DOWN),
            equal_sign.animate.shift(DOWN),
        )
        self.wait()

        p8 = numbers[0].copy().next_to(n7, RIGHT)
        n8 = numbers[1].copy().set_color(RED).next_to(n4, DOWN, buff=0.5)
        sum8 = numbers[9].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)
        self.play(
            FadeIn(pos_numbers[wave_order_pos[4]].copy().set_z_index(1)),
            FadeIn(p8),
            FadeIn(n8),
            ReplacementTransform(sum7, sum8)
        )
        self.wait()

        p9 = numbers[0].copy().next_to(n8, RIGHT)
        n9 = numbers[1].copy().set_color(WHITE).next_to(p9, RIGHT)
        sum9 = numbers[1].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)
        self.play(
            FadeIn(neg_numbers[wave_order_neg[4]].copy().set_z_index(1)),
            FadeIn(p9),
            FadeIn(n9),
            ReplacementTransform(sum8, sum9)
        )
        self.wait()

        p10 = numbers[0].copy().next_to(n9, RIGHT)
        n10 = numbers[6].copy().set_color(GREEN).next_to(p10, RIGHT)
        sum10 = numbers[7].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)
        self.play(
            FadeIn(pos_numbers[wave_order_pos[5]].copy().set_z_index(1)),
            FadeIn(p10),
            FadeIn(n10),
            ReplacementTransform(sum9, sum10)
        )
        self.wait()

        p11 = numbers[0].copy().next_to(n10, RIGHT)
        n11 = numbers[5].copy().set_color(WHITE).next_to(p11, RIGHT)
        sum11 = numbers[3].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)
        self.play(
            FadeIn(neg_numbers[wave_order_neg[5]].copy().set_z_index(1)),
            FadeIn(p11),
            FadeIn(n11),
            ReplacementTransform(sum10, sum11)
        )
        self.wait()

        self.play(
            sum11.animate.shift(DOWN),
            equal_sign.animate.shift(DOWN),
        )
        self.wait()

        p12 = numbers[0].copy().next_to(n11, RIGHT)
        n12 = numbers[2].copy().set_color(BLUE).next_to(n8, DOWN, buff=0.5)
        sum12 = numbers[5].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)
        self.play(
            FadeIn(pos_numbers[wave_order_pos[6]].copy().set_z_index(1)),
            FadeIn(p12),
            FadeIn(n12),
            ReplacementTransform(sum11, sum12)
        )
        self.wait()

        p13 = numbers[0].copy().next_to(n12, RIGHT)
        n13 = numbers[1].copy().set_color(WHITE).next_to(p13, RIGHT)
        sum13 = numbers[6].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)
        self.play(
            FadeIn(neg_numbers[wave_order_neg[6]].copy().set_z_index(1)),
            FadeIn(p13),
            FadeIn(n13),
            ReplacementTransform(sum12, sum13)
        )
        self.wait()

        p14 = numbers[0].copy().next_to(n13, RIGHT)
        n14 = numbers[5].copy().set_color(BLUE).next_to(p14, RIGHT)
        sum14 = numbers[2].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)
        self.play(
            FadeIn(pos_numbers[wave_order_pos[7]].copy().set_z_index(1)),
            FadeIn(p14),
            FadeIn(n14),
            ReplacementTransform(sum13, sum14)
        )
        self.wait()

        p15 = numbers[0].copy().next_to(n14, RIGHT)
        n15 = numbers[7].copy().set_color(WHITE).next_to(p15, RIGHT)
        sum15 = numbers[9].copy().set_color(YELLOW).next_to(equal_sign, RIGHT)
        self.play(
            FadeIn(neg_numbers[wave_order_neg[7]].copy().set_z_index(1)),
            FadeIn(p15),
            FadeIn(n15),
            ReplacementTransform(sum14, sum15)
        )
        self.wait()

        self.play(
            FadeOut(n0), FadeOut(n1), FadeOut(n2), FadeOut(n3),
            FadeOut(n4), FadeOut(n5), FadeOut(n6), FadeOut(n7),
            FadeOut(n8), FadeOut(n9), FadeOut(n10), FadeOut(n11),
            FadeOut(n12), FadeOut(n13), FadeOut(n14), FadeOut(n15),
            FadeOut(p1), FadeOut(p2), FadeOut(p3),
            FadeOut(p4), FadeOut(p5), FadeOut(p6), FadeOut(p7),
            FadeOut(p8), FadeOut(p9), FadeOut(p10), FadeOut(p11),
            FadeOut(p12), FadeOut(p13), FadeOut(p14), FadeOut(p15),
            FadeOut(equal_sign),
            sum15.animate.move_to(n0)
        )
        third_wave_title.set_z_index(1).next_to(second_wave_title, DOWN).shift(DOWN + RIGHT*0.18)
        self.wait()
        self.play(ShowCreation(third_wave_title))

        wave_order_pos = [43,33,23,13,21,29,37,47,57,67,59,51]
        wave_order_neg = [30,21,12,11,18,25,33,42,51,52,45,38]
        pos_group = Group()
        neg_group = Group()
        for i in range(0,12):
            pos_group.add(pos_numbers[wave_order_pos[i]].copy())
        for i in range(0,12):
            neg_group.add(neg_numbers[wave_order_neg[i]].copy())
        self.wait()
        third_wave_square = Square(3.5*np.sqrt(2),color = YELLOW_A).rotate(PI/4).set_opacity(0.8).set_stroke(width=8, color=BLACK)
        third_wave_square.move_to(green_diags[1][4]).set_z_index(0.2)

        first_line = Tex(r"3+4+7+9+2+5+")
        counter = 0
        for i in first_line:
            color_order = [GREEN,WHITE,WHITE,WHITE,RED,WHITE,WHITE,WHITE,BLUE,WHITE,WHITE,WHITE]
            i.set_color(color_order[counter])
            counter+=1

        second_line = Tex(r"6+9+3+3+9+6+")
        counter = 0
        for i in second_line:
            color_order = [GREEN,WHITE,WHITE,WHITE,GREEN,WHITE,WHITE,WHITE,GREEN,WHITE,WHITE,WHITE]
            i.set_color(color_order[counter])
            counter+=1

        third_line = Tex(r"6+5+2+9+7+4+")
        counter = 0
        for i in third_line:
            color_order = [GREEN,WHITE,WHITE,WHITE,BLUE,WHITE,WHITE,WHITE,RED,WHITE,WHITE,WHITE]
            i.set_color(color_order[counter])
            counter+=1

        fourth_line = Tex(r"3+9+6+6+9+3")
        counter = 0
        for i in fourth_line:
            color_order = [GREEN,WHITE,WHITE,WHITE,GREEN,WHITE,WHITE,WHITE,GREEN,WHITE,WHITE]
            i.set_color(color_order[counter])
            counter+=1
        
        third_wave_eq = Group(
            first_line,
            second_line,
            third_line,
            fourth_line,
        ).arrange(DOWN)
        third_wave_eq.next_to(third_wave_title, RIGHT, buff=0.7).shift(DOWN)

        self.play(
            FadeIn(third_wave_square),
            FadeIn(pos_group.set_z_index(1)),
            FadeIn(neg_group.set_z_index(1)),
            FadeIn(third_wave_eq)
        )
        self.wait()
        third_nine = numbers[9].copy().set_color(YELLOW).next_to(third_wave_title, RIGHT, buff=0.7)

        self.play(
            FadeOut(third_wave_eq),
            FadeIn(third_nine)
        )


        fourth_wave_title.set_z_index(1).next_to(third_wave_title, DOWN).shift(DOWN + LEFT*0.18)
        wave_order_pos = [44,34,24,14,4,12,20,28,36,46,56,66,76,68,60,52]
        wave_order_neg = [31,22,13,4,3,10,17,24,32,41,50,59,60,53,46,39]
        pos_group = Group()
        neg_group = Group()
        for i in range(0,16):
            pos_group.add(pos_numbers[wave_order_pos[i]].copy())
        for i in range(0,16):
            neg_group.add(neg_numbers[wave_order_neg[i]].copy())
        self.wait()
        fourth_wave_square = Square(4.5*np.sqrt(2),color = YELLOW_A).rotate(PI/4).set_opacity(0.8).set_stroke(width=8, color=BLACK)
        fourth_wave_square.move_to(green_diags[1][4]).set_z_index(0.2)

        self.play(ShowCreation(fourth_wave_title))
        self.wait()

        first_line = Tex(r"7+9+2+5+6+1+1+6+")
        counter = 0
        for i in first_line:
            color_order = [RED,WHITE,WHITE,WHITE,BLUE,WHITE,WHITE,WHITE,GREEN,WHITE,WHITE,WHITE,RED,WHITE,WHITE,WHITE]
            i.set_color(color_order[counter])
            counter+=1

        second_line = Tex(r"5+1+2+4+8+7+5+1+")
        counter = 0
        for i in second_line:
            color_order = [BLUE,WHITE,WHITE,WHITE,BLUE,WHITE,WHITE,WHITE,BLUE,WHITE,WHITE,WHITE,BLUE,WHITE,WHITE,WHITE]
            i.set_color(color_order[counter])
            counter+=1

        third_line = Tex(r"2+9+7+4+3+8+8+3+")
        counter = 0
        for i in third_line:
            color_order = [BLUE,WHITE,WHITE,WHITE,RED,WHITE,WHITE,WHITE,GREEN,WHITE,WHITE,WHITE,BLUE,WHITE,WHITE,WHITE]
            i.set_color(color_order[counter])
            counter+=1

        fourth_line = Tex(r"4+8+7+5+1+2+4+8")
        counter = 0
        for i in fourth_line:
            color_order = [RED,WHITE,WHITE,WHITE,RED,WHITE,WHITE,WHITE,RED,WHITE,WHITE,WHITE,RED,WHITE,WHITE]
            i.set_color(color_order[counter])
            counter+=1
        
        fourth_wave_eq = Group(
            first_line,
            second_line,
            third_line,
            fourth_line,
        ).arrange(DOWN).scale(0.7)
        fourth_wave_eq.next_to(fourth_wave_title, RIGHT, buff=0.7).shift(DOWN*0.5)

        self.play(
            FadeIn(fourth_wave_square),
            FadeIn(pos_group.set_z_index(1)),
            FadeIn(neg_group.set_z_index(1)),
            FadeIn(fourth_wave_eq)
        )
        self.wait()

        fourth_nine = numbers[9].copy().set_color(YELLOW).next_to(fourth_wave_title, RIGHT, buff=0.7)

        self.play(
            FadeOut(fourth_wave_eq),
            FadeIn(fourth_nine)
        )
        self.wait()

### CURRENTLY WORKING ON

class GroupStructure(Scene):
    def construct(self):
        frame = self.camera.frame
        scale = 2

        circle1 = ParametricCurve(
            lambda u: np.array([
                np.sin(u),
                np.cos(u),
                0
            ]),
            color = WHITE,
            t_range = np.array([-PI, PI, 0.01])
        ).scale(scale).set_stroke(width=4)
        numbers1 = vbm_numbers(1,9,1.0,2.6)
        dots1 = vbm_dots(1,9,1.4,2)

        group1 = Group(dots1, numbers1)
        
        euler_group = Group()
        
        r = 1.3
        left_shift = 3.1
        
        arrow_angle = ValueTracker(0)
        t2c = {
            "1":RED, "4":RED, "7":RED,
            "2":BLUE, "5":BLUE, "8":BLUE,
            "3":GREEN, "6":GREEN, "9":GREEN,
        }
        t2c2 = {
            "1":RED, "4":RED, "7":RED,
            "2":BLUE, "5":BLUE, "8":BLUE,
            "3":GREEN, "6":GREEN, "0":GREEN,
        }
        for i in range(0,9):
            if i == 0:
                euler_equation  = Tex(r"e^{i\frac{" + str(9) + "}{9}"+r"\tau}", tex_to_color_map = t2c)
            else:
                euler_equation  = Tex(r"e^{i\frac{" + str(i) + "}{9}"+r"\tau}", tex_to_color_map = t2c)

            euler_equation.shift(
                [
                    scale * r*np.sin(TAU * (i/9)),
                    scale * r*np.cos(TAU * (i/9)),
                    0
                ]            
            )
            euler_group.add(euler_equation)

        self.add(group1, circle1)
        self.wait(1)

        eisel = Rectangle(width=6.2,height=10,color=BLACK)
        eisel.move_to(4.05*RIGHT).set_fill(BLACK).set_opacity(1.0)
        self.play(
            circle1.animate.shift(LEFT*left_shift),
            group1.animate.shift(LEFT*left_shift),
            FadeIn(eisel),
        )
        self.wait(1)

        group_title = Tex(r"\textsc{Group Structure}").move_to(eisel).shift(UP*3.3).scale(1.3)

        self.play(
            FadeIn(group_title),
        )
        self.wait(1)

        integers_title = Tex(r"\text{Integers mod}9").next_to(group_title, DOWN, buff=0.5)
        mod9_group_title = Tex(r"\mathbb{Z}/9\mathbb{Z}").next_to(integers_title, DOWN, buff=0.6)
        self.play(FadeIn(integers_title))
        self.wait()
        self.play(Write(mod9_group_title))
        group_set1 = Tex(r"\left\{ 0,1,2,3,4,5,6,7,8\right\}")
        group_set2 = Tex(r"\left\{ 0,1,2,3,4,5,6,7,8\right\}", tex_to_color_map = t2c2)
        group_set1.next_to(mod9_group_title, DOWN, buff=0.3)
        group_set2.next_to(mod9_group_title, DOWN, buff=0.3)
        self.wait()
        self.play(ShowCreation(group_set1))
        self.wait()
        zero = Tex(r"0").set_color(GREEN).move_to(numbers1[0])
        self.play(Transform(numbers1[0], zero))
        self.wait()
        self.play(Transform(group_set1, group_set2))
        self.wait()

        closure_eq1 = Tex(r"a,b\in\mathbb{Z}/9\mathbb{Z} \text{ },")
        closure_eq2 = Tex(r"a+b \text{ } (\text{mod}9)\in\mathbb{Z}/9\mathbb{Z}")
        closure_eq1.next_to(group_set2,DOWN,buff=0.7).scale(0.8)
        closure_eq2.next_to(closure_eq1,DOWN).scale(0.8)

        self.play(Write(closure_eq1)),
        self.wait()
        self.play(Write(closure_eq2))
        self.wait()

        ex_map1 = {
            "4":RED,
            "8":BLUE,
            "3":GREEN
        }
        add_example1 = Tex(r"4+8=12", tex_to_color_map = ex_map1)
        add_example2 = Tex(r"4+8=3", tex_to_color_map = ex_map1)
        add_example1.next_to(closure_eq2,DOWN, buff=0.5).scale(0.8)
        add_example2.next_to(closure_eq2,DOWN, buff=0.5).scale(0.8)
        self.play(Write(add_example1))
        self.wait()
        self.play(ReplacementTransform(add_example1,add_example2))
        self.wait()

        closure_title = Tex(r"\text{CLOSURE}")
        closure_title.next_to(add_example2, DOWN, buff=0.6)

        self.play(FadeIn(closure_title))
        self.wait()
        self.play(
            FadeOut(closure_eq1),
            FadeOut(closure_eq2),
            FadeOut(add_example2),
            FadeOut(closure_title)
        )
        self.wait()
        identity_title = Tex(r"\text{IDENTITY}")
        identity_title.next_to(group_set2,DOWN,buff=0.5).scale(0.8)
        self.play(FadeIn(identity_title))
        self.wait()
        zero1 = zero.copy().scale(0.8).next_to(identity_title,DOWN,buff=0.4)
        self.play(Write(zero1))
        self.wait()
        inverses_title = Tex(r"\text{INVERSES}")
        inverses_title.next_to(zero1,DOWN,buff=0.6).scale(0.8)
        self.play(FadeIn(inverses_title))
        self.wait()
        inv18 = Tex(r"1+8=0",tex_to_color_map = t2c2).scale(0.8)
        inv27 = Tex(r"2+7=0",tex_to_color_map = t2c2).scale(0.8)
        inv36 = Tex(r"3+6=0",tex_to_color_map = t2c2).scale(0.8)
        inv45 = Tex(r"4+5=0",tex_to_color_map = t2c2).scale(0.8)
        inv00 = Tex(r"0+0=0",tex_to_color_map = t2c2).scale(0.8)
        inverses_group1 = Group(inv18,inv27,inv45).arrange(RIGHT,buff=0.5)
        inverses_group1.next_to(inverses_title,DOWN,buff=0.5)
        inverses_group2 = Group(inv36,inv00).arrange(RIGHT,buff=0.5)
        inverses_group2.next_to(inverses_group1,DOWN,buff=0.4)
        self.play(Write(inv18))
        self.wait()
        self.play(Write(inv27))
        self.wait()
        self.play(Write(inv45))
        self.wait()
        self.play(Write(inv36))
        self.wait()
        self.play(Write(inv00))
        self.wait()
        self.play(
            FadeOut(inverses_group1),
            FadeOut(inverses_group2),
            FadeOut(zero1),
            identity_title.animate.shift(DOWN*0.9)
        )
        clos_title = closure_title.copy().scale(0.8)
        clos_title.next_to(identity_title,UP, buff=0.4)
        self.play(FadeIn(clos_title))
        self.wait()
        com_title = Tex(r"\text{ASSOCIATITY}")
        com_title.scale(0.8).next_to(inverses_title,DOWN,buff=0.4)
        self.play(FadeIn(com_title))
        com_eq = Tex(r"(a+b)+c=a+(b+c)")
        com_eq.scale(0.6).next_to(com_title,DOWN,buff=0.4)
        self.wait()
        self.play(ShowCreation(com_eq))
        self.wait()
        self.play(FadeOut(com_eq))
        self.wait()
        self.play(
            FadeOut(clos_title),
            FadeOut(identity_title),
            FadeOut(inverses_title),
            FadeOut(com_title),
        )

        sub_title = Tex(r"\text{Subgroups}")
        sub_title.next_to(group_set2,DOWN,buff=0.5)
        self.wait()
        self.play(FadeIn(sub_title))
        self.wait()

        identity_eq = Tex(r"\left\{0\right\}").scale(0.8)
        total_eq = Tex(r"\mathbb{Z}/9\mathbb{Z}").scale(0.8)
        trivial = Group(identity_eq, total_eq).arrange(RIGHT,buff=0.5)
        trivial.next_to(sub_title,DOWN,buff=0.5)

        self.play(ShowCreation(trivial))
        self.wait()
        self.play(Uncreate(trivial))
        self.wait()
        natural_eq = Tex(r"N=\left\{0,3,6\right\}", tex_to_color_map=t2c2)
        natural_eq.next_to(sub_title,DOWN,buff=0.5).scale(0.8)

        self.play(Write(natural_eq))
        self.wait()

        tri036 = Group(
            Line(dots1[0].get_center(),dots1[3].get_center()).set_color(GREEN),
            Line(dots1[3].get_center(),dots1[6].get_center()).set_color(GREEN),
            Line(dots1[6].get_center(),dots1[0].get_center()).set_color(GREEN),
        )
        self.play(FadeIn(tri036))
        self.wait()

        coset1_eq = Tex(r"g_{1}N=\left\{1,4,7\right\}", tex_to_color_map=t2c2)
        coset1_eq.next_to(natural_eq,DOWN,buff=0.3).scale(0.8)

        tri147 = Group(
            Line(dots1[1].get_center(),dots1[4].get_center()).set_color(RED),
            Line(dots1[4].get_center(),dots1[7].get_center()).set_color(RED),
            Line(dots1[7].get_center(),dots1[1].get_center()).set_color(RED),
        )
        self.play(
            FadeIn(tri147),
            Write(coset1_eq)
        )
        self.wait()

        coset2_eq = Tex(r"g_{2}N=\left\{2,5,8\right\}", tex_to_color_map=t2c2)
        coset2_eq.next_to(coset1_eq,DOWN,buff=0.3).scale(0.8)

        tri258 = Group(
            Line(dots1[2].get_center(),dots1[5].get_center()).set_color(BLUE),
            Line(dots1[5].get_center(),dots1[8].get_center()).set_color(BLUE),
            Line(dots1[8].get_center(),dots1[2].get_center()).set_color(BLUE),
        )
        self.play(
            FadeIn(tri258),
            Write(coset2_eq)
        )
        self.wait()

class Isomorphisms(Scene):
    def construct(self):
        frame = self.camera.frame
        scale = 2

        circle1 = ParametricCurve(
            lambda u: np.array([
                np.sin(u),
                np.cos(u),
                0
            ]),
            color = WHITE,
            t_range = np.array([-PI, PI, 0.01])
        ).scale(scale).set_stroke(width=4)
        numbers1 = vbm_numbers(1,9,1.0,2.6)
        dots1 = vbm_dots(1,9,1.4,2)

        group1 = Group(dots1, numbers1)
        
        euler_group = Group()
        
        r = 1.3
        left_shift = 3.1
        
        arrow_angle = ValueTracker(0)
        t2c = {
            "1":RED, "4":RED, "7":RED,
            "2":BLUE, "5":BLUE, "8":BLUE,
            "3":GREEN, "6":GREEN, "9":GREEN,
        }
        t2c2 = {
            "1":RED, "4":RED, "7":RED,
            "2":BLUE, "5":BLUE, "8":BLUE,
            "3":GREEN, "6":GREEN, "0":GREEN,
        }
        for i in range(0,9):

            euler_equation  = Tex(r"e^{i\frac{" + str(9) + "}{9}"+r"\tau}")
            euler_equation.shift(
                [
                    scale * r*np.sin(TAU * (i/9)),
                    scale * r*np.cos(TAU * (i/9)),
                    0
                ]            
            )
            euler_group.add(euler_equation)

        eisel = Rectangle(width=6.2,height=10,color=BLACK)
        eisel.move_to(4.05*RIGHT).set_fill(BLACK).set_opacity(1.0)

        group_title = Tex(r"\textsc{Group Structure}").move_to(eisel).shift(UP*3.3).scale(1.3)
        
        self.add(group1.shift(LEFT*left_shift), circle1.shift(LEFT*left_shift), eisel, group_title)
        iso_title = Tex(r"\text{Isomorphisms}")
        iso_title.next_to(group_title,DOWN,buff=0.5)
        self.play(FadeIn(iso_title))
        self.wait()
        vbm_group = Group(group1,circle1)
        self.play(vbm_group.animate.scale(0.6).shift(UP*1.8))
        self.wait()
        group_set = Tex(r"\left\{ 0,1,2,3,4,5,6,7,8\right\}", tex_to_color_map = t2c2)
        group_set.scale(0.9).next_to(iso_title,DOWN,buff=0.5)


        circle2 = ParametricCurve(
            lambda u: np.array([
                np.sin(u),
                np.cos(u),
                0
            ]),
            color = WHITE,
            t_range = np.array([-PI, PI, 0.01])
        ).scale(scale).set_stroke(width=4)
        dots2 = vbm_dots(1,9,1.4,2).set_color(WHITE)

        eul_group = Group(euler_group, circle2, dots2).shift(LEFT*left_shift)
        eul_group.scale(0.6).shift(DOWN*1.8)
        self.play(FadeIn(eul_group))
        self.wait()

        z_title = Tex(r"\mathbb{Z}/9\mathbb{Z}")
        z_title.next_to(vbm_group,LEFT,buff=0.7)
        addition = Tex(r"(+)").next_to(vbm_group,RIGHT,buff=1)
        self.play(
            FadeIn(z_title),
            FadeIn(addition)
        )
        self.wait()
        self.play(Write(group_set))
        self.wait()

        c_title = Tex(r"C_{9}").next_to(eul_group,LEFT,buff=0.9)
        multiplication = Tex(r"(\times)").next_to(eul_group,RIGHT,buff=0.7)
        self.play(
            FadeIn(c_title),
            FadeIn(multiplication)
        )
        self.wait()
        self.play(Uncreate(euler_group))
        
        omega_group = Group()
        for i in range(0,9):

            omega_eq  = Tex(r"\omega^{" + str(i) + "}")
            omega_eq.shift(
                [
                    scale * r*np.sin(TAU * (i/9)),
                    scale * r*np.cos(TAU * (i/9)),
                    0
                ]            
            )
            omega_group.add(omega_eq)

        omega_group.move_to(circle2.get_center()).scale(0.6)
        group_omega = Tex(
            r"\left\{\omega^{0},\omega^{1},\omega^{2},\omega^{3},\omega^{4},\omega^{5},\omega^{6},\omega^{7},\omega^{8}\right\}"
        )
        group_omega.scale(0.7).next_to(group_set,DOWN,buff=0.5)
        self.play(
            ShowCreation(omega_group),
        )
        self.wait()
        self.play(Write(group_omega))
        self.wait()
        ex_eq1 = Tex(r"4+6=1", tex_to_color_map=t2c2)
        ex_eq2 = Tex(r"\omega^{4}\times\omega^{6}=\omega^{1}")
        ex_eq1.next_to(group_omega,DOWN,buff=0.7).scale(0.9)
        ex_eq2.next_to(ex_eq1,DOWN,buff=0.4).scale(0.8)
        self.play(
            Write(ex_eq1)
        )
        self.wait()
        self.play(
            Write(ex_eq2)
        )
        self.wait()
        iso_final = Tex(r"\mathbb{Z}/9\mathbb{Z}\cong C_{9}")
        iso_final.next_to(ex_eq2,DOWN,buff=1)
        self.play(FadeIn(iso_final))

class Automorphisms(Scene):
    def construct(self):

        t2c2 = {
            "1":RED, "4":RED, "7":RED,
            "2":BLUE, "5":BLUE, "8":BLUE,
            "3":GREEN, "6":GREEN, "0":GREEN,
        }
        auto_title = Tex(r"\text{Automorphisms}").scale(1.5)
        auto_title.next_to(TOP,DOWN,buff=0.7)
        self.play(FadeIn(auto_title))
        definition = Tex(r"\textit{An isomorphism of a group to itself, that preserves the group structure}")
        definition.next_to(auto_title,DOWN,buff=0.5).scale(0.8)
        self.wait()
        self.play(Write(definition))
        self.wait()

        auto1 = Tex(r"\left<1\right>=\left\{0,1,2,3,4,5,6,7,8\right\}",tex_to_color_map=t2c2)
        auto2 = Tex(r"\left<2\right>=\left\{0,2,4,6,8,1,3,5,7\right\}",tex_to_color_map=t2c2).scale(0.8)
        auto3 = Tex(r"\left<3\right>=\left\{0,3,6\right\}",tex_to_color_map=t2c2).scale(0.8)
        auto4 = Tex(r"\left<4\right>=\left\{0,4,8,3,7,2,6,1,5\right\}",tex_to_color_map=t2c2).scale(0.8)
        auto5 = Tex(r"\left<5\right>=\left\{0,5,1,6,2,7,3,8,4\right\}",tex_to_color_map=t2c2).scale(0.8)
        auto6 = Tex(r"\left<6\right>=\left\{0,6,3\right\}",tex_to_color_map=t2c2).scale(0.8)
        auto7 = Tex(r"\left<7\right>=\left\{0,7,5,3,1,8,6,4,2\right\}",tex_to_color_map=t2c2).scale(0.8)
        auto8 = Tex(r"\left<8\right>=\left\{0,8,7,6,5,4,3,2,1\right\}",tex_to_color_map=t2c2).scale(0.8)
        auto9 = Tex(r"\left<0\right>=\left\{0\right\}",tex_to_color_map=t2c2).scale(0.8)

        self.play(ShowCreation(auto1))
        self.wait()
        self.play(
            auto1.animate.scale(0.8).shift(UP*1.2)
        )

        auto2.next_to(auto1,DOWN,buff=0.2),
        auto3.next_to(auto2,DOWN,buff=0.2),
        auto4.next_to(auto3,DOWN,buff=0.2),
        auto5.next_to(auto4,DOWN,buff=0.2),
        auto6.next_to(auto5,DOWN,buff=0.2),
        auto7.next_to(auto6,DOWN,buff=0.2),
        auto8.next_to(auto7,DOWN,buff=0.2),
        auto9.next_to(auto8,DOWN,buff=0.2),

        auto3.shift(LEFT*(auto3.get_left()[0]-auto1.get_left()[0]))
        auto6.shift(LEFT*(auto6.get_left()[0]-auto1.get_left()[0]))
        auto9.shift(LEFT*(auto9.get_left()[0]-auto1.get_left()[0]))
        
        autos = Group(
            auto2, auto3, auto4, auto5, auto6, auto7, auto8, auto9
        )
        self.wait()
        for i in range(len(autos)):
            self.add(autos[i])
            self.wait(0.2)
        
        cross3 = Group(
            Line([1,1],[-1,-1]).set_color(RED).set_stroke(width=8),
            Line([1,-1],[-1,1]).set_color(RED).set_stroke(width=8),
        ).scale(0.15).next_to(auto3,LEFT,buff=0.2)
        cross6 = cross3.copy().next_to(auto6,LEFT,buff=0.2)
        cross9 = cross3.copy().next_to(auto9,LEFT,buff=0.2)
        self.add(cross3, cross6, cross9)
        self.wait()
        self.play(
            FadeOut(cross3),
            FadeOut(cross6),
            FadeOut(cross9),
            FadeOut(auto3),
            FadeOut(auto6),
            FadeOut(auto9),
        )
        autos = Group(
            auto1, auto2, auto4, auto5, auto7, auto8
        )
        self.wait()
        self.play(autos.animate.arrange(DOWN).shift(DOWN*1.6))
        self.wait()
        aut_z = Tex(r"\text{Aut}(\mathbb{Z}/9\mathbb{Z})").next_to(auto1,UP,buff=0.5)
        self.play(Write(aut_z))
        

### NOT FINISHED

class AllMods(Scene):
    def construct(self):
        self.add(vbm_families(0))
        self.add(vbm_families(1))
        self.add(vbm_families(2))

        previous_circle = mod_circle(0,1,1)
        previous_double = doubling_sequence(0,2,0,1)
        previous_half = halving_sequence(0)
        i=0
        while i < 26:
            self.remove(previous_circle)
            self.remove(previous_double)
            self.remove(previous_half)
            circle = mod_circle(i,1,1)
            double = doubling_sequence(i,2,0,1)
            half = halving_sequence(i)
            self.add(circle)
            self.add(double)
            self.add(half)
            previous_circle = circle
            previous_double = double
            previous_half = half
            self.wait(0.5)
            i+=1

class CircleToAxis(Scene):
    def construct(self):

        axes = Axes()
        nums = vbm_numbers(1,36,0.4,1).scale(2)
        nums_proj = vbm_projection(1,36,0.5)
        dots = vbm_dots(1,36,1,2)
        dots_proj = dot_projection(1,36,1)
        theta = ValueTracker(0)
        lines_proj = projection_lines(36)
        circle_proj = always_redraw(lambda: ParametricCurve(
            lambda u: np.array([
                2*(1/np.cos(theta.get_value()))*np.sin(u),
                2*(np.tan(theta.get_value())+((1/np.cos(theta.get_value()))*np.cos(u))),
                0
            ]),
            color = WHITE,
            t_range = np.array([-PI, PI, 0.01])
        )).scale(2)

        self.add(nums,circle_proj,axes)
        self.add(lines_proj)
        self.wait(0.1)
        self.play(
            FadeOut(nums),
            FadeIn(dots)
        )
        self.wait(0.1)
        dots[0].set_opacity(0),
        dots_proj[0].set_opacity(0),
        self.play(Transform(dots,dots_proj), run_time = 3, rate_func = linear)
        self.wait(0.1)
        self.play(
            FadeOut(dots),
            FadeIn(nums_proj)
        )
        self.wait(0.1)
        self.play(theta.animate.set_value(PI/2-non_zero), run_time = 3, rate_func = linear)

class VBMDualMapFrequency(Scene):
    def construct(self):

        symbol = vbm_symbol().scale(2)
        numbers1 = vbm_numbers(1,9,1.0,2.6)
        circle1 = Circle().set_color(WHITE).scale(2.06).set_stroke(width=10)
        positives = number_polarities_pos(numbers1, 1.0)
        group1 = Group(numbers1, circle1, positives, symbol)
        self.add(circle1)
        self.add(symbol)
        self.add(numbers1)
        self.wait(0.1)
        self.play(FadeIn(positives))
        self.wait(0.1)
        self.play(FadeOut(symbol))
        group1.remove(symbol)
        self.wait(0.1)
        tri1 = vbm_families(0).set_opacity(0)
        tri2 = vbm_families(1).set_opacity(0)
        tri3 = vbm_families(2).set_opacity(0)

        triangle_group1 = Group(tri1,tri2,tri3)
        triangle_group1.scale(2)
        self.play(tri1.animate.set_opacity(1.0))
        self.play(
            group1.animate.shift(LEFT*3),
            triangle_group1.animate.shift(LEFT*3)
        )

        numbers2 = vbm_numbers(1,9,1.0,2.6)
        circle2 = Circle().set_color(WHITE).scale(2.06).set_stroke(width=10)
        positives = number_polarities_pos(numbers2, 1.0)
        group2 = Group(numbers2, circle2, positives)
        group2.shift(RIGHT*3)
        tri4 = vbm_families(0).set_opacity(0)
        tri5 = vbm_families(1).set_opacity(0)
        tri6 = vbm_families(2).set_opacity(0)

        triangle_group2 = Group(tri4,tri5,tri6)
        triangle_group2.scale(2)
        triangle_group2.shift(RIGHT*3)
        self.play(
            FadeIn(group2),
            tri4.animate.set_opacity(1.0)
        )

        for i in range(0,120):
            self.wait(0.2)
            self.play(
                triangle_group1[i%3].animate.set_opacity(0),
                triangle_group1[(i+1)%3].animate.set_opacity(1.0),
                triangle_group2[-i%3].animate.set_opacity(0),
                triangle_group2[(-i-1)%3].animate.set_opacity(1.0), run_time=0.3
            )
