from manimlib import *
import sys
sys.path.append("C:/Users/thund/Downloads/manim-master/manimprojects")
from vbm_funcs import *
from dots_example import *

class NewDotGridCompanion(Scene):
    def construct(self):
        def diamond_plane_pos(num_rows, num_cols, offset_value, plane, stroke_size):
            sqr_group = Group()
            sqr = Square(np.sqrt(2)/2).rotate(45*DEGREES).set_stroke(width = stroke_size)
            col = [GREEN, RED, BLUE]
            if plane == "xy":
                for i in range (-num_cols+1, num_cols):
                    for j in range(-num_rows+1, num_rows):
                        diamond = sqr.copy()
                        diamond.move_to([i, j, 0])
                        diamond.set_color(col[(offset_value+i+j)%3]).set_opacity(1.0).set_stroke(BLACK)
                        sqr_group.add(diamond)
            if plane == "xz":
                for i in range (-num_cols+1, num_cols):
                    for j in range(-num_rows+1, num_rows):
                        diamond = sqr.copy()
                        diamond.move_to([i, j, 0])
                        diamond.set_color(col[(offset_value+i+j)%3]).set_opacity(1.0).set_stroke(BLACK)
                        sqr_group.add(diamond)
            if plane == "yz":
                for i in range (-num_cols+1, num_cols):
                    for j in range(-num_rows+1, num_rows):
                        diamond = sqr.copy()

                        diamond.move_to([i, j, 0])
                        diamond.set_color(col[(offset_value+i+j)%3]).set_opacity(1.0).set_stroke(BLACK)
                        sqr_group.add(diamond)
            return sqr_group

        def diamond_plane_neg(num_rows, num_cols, offset_value, plane, stroke_size):
            sqr_group = Group()
            sqr = Square(np.sqrt(2)/2).rotate(45*DEGREES).set_stroke(width = stroke_size)
            col = [GREEN, RED, BLUE]
            if plane == "xy":
                for i in range (-num_cols+1, num_cols-1):
                    for j in range(-num_rows+1, num_rows-1):
                        diamond = sqr.copy()
                        diamond.move_to([i+1/2, j+1/2, 0])
                        diamond.set_color(WHITE).set_opacity(1.0).set_stroke(BLACK)
                        sqr_group.add(diamond)
            if plane == "xz":
                for i in range (-num_cols+1, num_cols-1):
                    for j in range(-num_rows+1, num_rows-1):
                        diamond = sqr.copy()
                        diamond.move_to([i+1/2, j+1/2, 0])
                        diamond.set_color(WHITE).set_opacity(1.0).set_stroke(BLACK)
                        sqr_group.add(diamond)
            if plane == "yz":
                for i in range (-num_cols+1, num_cols-1):
                    for j in range(-num_rows+1, num_rows-1):
                        diamond = sqr.copy()
                        diamond.move_to([i+1/2, j+1/2, 0])
                        diamond.set_color(WHITE).set_opacity(1.0).set_stroke(BLACK)
                        sqr_group.add(diamond)
            return sqr_group

        def generate_number_grid_pos(num_rows, num_cols, offset_value, plane, start_num):
            number_group = Group()
            if plane == "xy":
                for i in range (-num_cols+1, num_cols):
                    for j in range(-num_rows+1, num_rows):
                        if (start_num+(j*4)+i)%9 == 0:
                            number = Text(str(9))
                            number.move_to([i, j, 0]).set_color(BLACK)
                            number_group.add(number)
                        else:
                            number = Text(str((start_num+(j*4)+i)%9))
                            number.move_to([i, j, 0]).set_color(BLACK)
                            number_group.add(number)
            if plane == "xz":
                for i in range (-num_cols+1, num_cols):
                    for j in range(-num_rows+1, num_rows):
                        if (start_num+(j*7)+i)%9 == 0:
                            number = Text(str(9))
                            number.move_to([i, j, 0]).set_color(BLACK)
                            number_group.add(number)
                        else:
                            number = Text(str((start_num+(j*7)+i)%9))
                            number.move_to([i, j, 0]).set_color(BLACK)
                            number_group.add(number)
            if plane == "yz":
                for i in range (-num_cols+1, num_cols):
                    for j in range(-num_rows+1, num_rows):
                        if (start_num+(j*7)+(i*4))%9 == 0:
                            number = Text(str(9))
                            number.move_to([i, j, 0]).set_color(BLACK)
                            number_group.add(number)
                        else:
                            number = Text(str((start_num+(j*7)+(i*4))%9))
                            number.move_to([i, j, 0]).set_color(BLACK)
                            number_group.add(number)
            return number_group

        def generate_number_grid_neg(num_rows, num_cols, offset_value, plane, start_num):
            number_group = Group()
            if plane == "xy":
                for i in range (-num_cols+1, num_cols-1):
                    for j in range(-num_rows+1, num_rows-1):
                        if (start_num-(j*4)-i)%9 == 0:
                            number = Text(str(9))
                            number.move_to([i+1/2, j+1/2, 0]).set_color(BLACK)
                            number_group.add(number)
                        else:
                            number = Text(str((start_num-(j*4)-i)%9))
                            number.move_to([i+1/2, j+1/2, 0]).set_color(BLACK)
                            number_group.add(number)
            if plane == "xz":
                for i in range (-num_cols+1, num_cols-1):
                    for j in range(-num_rows+1, num_rows-1):
                        if (start_num-(j*7)-i)%9 == 0:
                            number = Text(str(9))
                            number.move_to([i+1/2, j+1/2, 0]).set_color(BLACK)
                            number_group.add(number)
                        else:
                            number = Text(str((start_num-(j*7)-i)%9))
                            number.move_to([i+1/2, j+1/2, 0]).set_color(BLACK)
                            number_group.add(number)
            if plane == "yz":
                for i in range (-num_cols+1, num_cols-1):
                    for j in range(-num_rows+1, num_rows-1):
                        if (start_num-(j*7)-(i*4))%9 == 0:
                            number = Text(str(9))
                            number.move_to([i+1/2, j+1/2, 0]).set_color(BLACK)
                            number_group.add(number)
                        else:
                            number = Text(str((start_num-(j*7)-(i*4))%9))
                            number.move_to([i+1/2, j+1/2, 0]).set_color(BLACK)
                            number_group.add(number)
            return number_group

        def counter_space_grid(num_rows, num_cols, offset_value, plane, stroke_size):
            sqr_group = Group()
            sqr = Square(np.sqrt(2)/2).rotate(45*DEGREES).set_stroke(width = stroke_size)
            col = [GREEN, RED, BLUE]
            if plane == "xy":
                for i in range (-num_cols+1, num_cols):
                    for j in range(-num_rows+1, num_rows):
                        diamond = sqr.copy()
                        diamond.move_to([i-0.5, j, 0])
                        diamond.set_color(WHITE).set_opacity(1.0).set_stroke(BLACK)
                        sqr_group.add(diamond)
                for i in range (-num_cols+1, num_cols):
                    for j in range(-num_rows+1, num_rows):
                        diamond = sqr.copy()
                        diamond.move_to([i, j-0.5, 0])
                        diamond.set_color(WHITE).set_opacity(1.0).set_stroke(BLACK)
                        sqr_group.add(diamond)
                sqr_group.add(sqr_group[0:9].copy().shift(RIGHT*9))
                for i in range(-num_rows+1, num_rows):
                    diamond = sqr.copy()
                    diamond.move_to([i, num_rows-0.5, 0])
                    diamond.set_color(WHITE).set_opacity(1.0).set_stroke(BLACK)
                    sqr_group.add(diamond)
            return sqr_group

        def counter_number_grid(num_rows, num_cols, offset_value, plane, start_num):
            number_group = Group()
            if plane == "xy":
                for i in range (-num_cols+1, num_cols):
                    for j in range(-num_rows+1, num_rows):
                        if (start_num+(j*4)+i+offset_value)%9 == 0:
                            number = Text(str(9))
                            number.move_to([i-0.5, j, 0]).set_color(BLACK)
                            number_group.add(number)
                        else:
                            number = Text(str(-(start_num+(j*4)+i+offset_value)%9))
                            number.move_to([i-0.5, j, 0]).set_color(BLACK)
                            number_group.add(number)
                new_start1 = start_num + 3
                for i in range (-num_cols+1, num_cols):
                    for j in range(-num_rows+1, num_rows):
                        if (new_start1+(j*4)+i+offset_value)%9 == 0:
                            number = Text(str(9))
                            number.move_to([i, j-0.5, 0]).set_color(BLACK)
                            number_group.add(number)
                        else:
                            number = Text(str(-(new_start1+(j*4)+i+offset_value)%9))
                            number.move_to([i, j-0.5, 0]).set_color(BLACK)
                            number_group.add(number)
                new_start2 = start_num + 5
                for i in range (-num_cols+1, num_cols):
                    if (new_start2+(i*4)+offset_value)%9 == 0:
                        number = Text(str(9))
                        number.move_to([num_cols-0.5, i, 0]).set_color(BLACK)
                        number_group.add(number)
                    else:
                        number = Text(str(-(new_start2+(i*4)+offset_value)%9))
                        number.move_to([num_cols-0.5, i, 0]).set_color(BLACK)
                        number_group.add(number)
                new_start3 = start_num + 5
                for i in range (-num_cols+1, num_cols):
                    if (new_start3+(i)+offset_value)%9 == 0:
                        number = Text(str(9))
                        number.move_to([i, num_cols-0.5, 0]).set_color(BLACK)
                        number_group.add(number)
                    else:
                        number = Text(str(-(new_start3+(i)+offset_value)%9))
                        number.move_to([i, num_cols-0.5, 0]).set_color(BLACK)
                        number_group.add(number)
            return(number_group)

        frame = self.camera.frame
        frame.scale(1.3)

        for i in range(0,9):
            dia_plane_pos_xy = diamond_plane_pos(5,5,(i*7)%9,"xy",1)
            dia_plane_neg_xy = diamond_plane_neg(5,5,(i*7)%9,"xy",1)
            num_grid_pos_xy = generate_number_grid_pos(5,5,(i*7)%9,"xy",((i)*7)%9)
            num_grid_neg_xy = generate_number_grid_neg(5,5,(i*7)%9,"xy",((i*7)-7)%9)
            self.add(
                dia_plane_pos_xy,
                dia_plane_neg_xy,
                num_grid_pos_xy,
                num_grid_neg_xy
            )
            self.wait(5)
            self.remove(
                dia_plane_pos_xy,
                dia_plane_neg_xy,
                num_grid_pos_xy,
                num_grid_neg_xy
            )
            counter_plane_xy = counter_space_grid(5,5,(i*7)%9,"xy",1)
            counter_nums_pos = counter_number_grid(5,5,(i*7)%9,"xy",3)
            self.add(
                counter_plane_xy,
                counter_nums_pos,
            )
            self.wait(5)
            self.remove(
                counter_plane_xy,
                counter_nums_pos,
            )
        dia_plane_pos_xy = diamond_plane_pos(5,5,0,"xy",1)
        dia_plane_neg_xy = diamond_plane_neg(5,5,0,"xy",1)
        num_grid_pos_xy = generate_number_grid_pos(5,5,0,"xy",1)
        num_grid_neg_xy = generate_number_grid_neg(5,5,0,"xy",1)
        self.add(
            dia_plane_pos_xy,
            dia_plane_neg_xy,
            num_grid_pos_xy,
            num_grid_neg_xy
        )

        self.wait(5)
        
        for i in range(0,9):
            dia_plane_pos_xy = diamond_plane_pos(5,5,(i*7)%9,"xy",1)
            dia_plane_neg_xy = diamond_plane_neg(5,5,(i*7)%9,"xy",1)
            num_grid_pos_xy = generate_number_grid_pos(5,5,(i*7)%9,"xy",((i)*7)%9)
            num_grid_neg_xy = generate_number_grid_neg(5,5,(i*7)%9,"xy",((i*7)+2)%9)
            self.add(
                dia_plane_pos_xy,
                dia_plane_neg_xy,
                num_grid_pos_xy,
                num_grid_neg_xy
            )
            self.wait(5)
            self.remove(
                dia_plane_pos_xy,
                dia_plane_neg_xy,
                num_grid_pos_xy,
                num_grid_neg_xy
            )

        self.wait(5)

        for i in range(0,9):
            dia_plane_pos_xy = diamond_plane_pos(5,5,(i*7)%9,"xz",1)
            dia_plane_neg_xy = diamond_plane_neg(5,5,(i*7)%9,"xz",1)
            num_grid_pos_xy = generate_number_grid_pos(5,5,(i*7)%9,"xz",((i)*7)%9)
            num_grid_neg_xy = generate_number_grid_neg(5,5,(i*7)%9,"xz",((i*7)-7)%9)
            self.add(
                dia_plane_pos_xy,
                dia_plane_neg_xy,
                num_grid_pos_xy,
                num_grid_neg_xy
            )
            self.wait(5)
            self.remove(
                dia_plane_pos_xy,
                dia_plane_neg_xy,
                num_grid_pos_xy,
                num_grid_neg_xy
            )

        self.wait(5)

        for i in range(0,9):
            dia_plane_pos_xy = diamond_plane_pos(5,5,(i*7)%9,"yz",1)
            dia_plane_neg_xy = diamond_plane_neg(5,5,(i*7)%9,"yz",1)
            num_grid_pos_xy = generate_number_grid_pos(5,5,(i*7)%9,"yz",((i)*7)%9)
            num_grid_neg_xy = generate_number_grid_neg(5,5,(i*7)%9,"yz",((i*7)-7)%9)
            self.add(
                dia_plane_pos_xy,
                dia_plane_neg_xy,
                num_grid_pos_xy,
                num_grid_neg_xy
            )
            self.wait(5)
            self.remove(
                dia_plane_pos_xy,
                dia_plane_neg_xy,
                num_grid_pos_xy,
                num_grid_neg_xy
            )

class DotGridBreakdownCompanion(Scene):
    def construct(self):


        def triangular_patch(size, spacing=1.0):
            """
            Generate a centered, 180° inverted triangular patch of an equilateral lattice.
            
            - size: number of rows (triangle height)
            - spacing: distance between nearest neighbors
            
            Returns: list of (x, y) coordinates
            """
            h = spacing * math.sqrt(3) / 2.0  # vertical step between rows
            pts = []

            for row in range(size):
                y = row * h  # point goes downward (inverted)
                row_width = row + 1
                x_start = - (row_width - 1) * spacing / 2.0
                for col in range(row_width):
                    x = x_start + col * spacing
                    pts.append((x, y))

            # --- recentre to origin ---
            xs, ys = zip(*pts)
            cx = (min(xs) + max(xs)) / 2.0
            cy = (min(ys) + max(ys)) / 2.0
            pts = [(x - cx, y - cy) for (x, y) in pts]

            return pts

        # Triangle 1
        pts = triangular_patch(size=1, spacing=0.6)
        circle1 = VGroup(*[
            Circle(radius=0.2, stroke_width=3).set_opacity(1.0).set_color(GREEN).set_stroke(color=BLACK).move_to(np.array([x, y, 0]))
            for (x, y) in pts
        ])
        self.add(circle1)
        self.wait()
        self.remove(circle1)
        
        pts = triangular_patch(size=3, spacing=0.6)

        # Triangle 2
        circle2 = VGroup(*[
            Circle(radius=0.2, stroke_width=3).set_opacity(1.0).set_color(WHITE).set_stroke(color=BLACK).move_to(np.array([x, y, 0]))
            for (x, y) in pts
        ])
        circle2[0].set_color(BLUE).set_stroke(color=BLACK, width=3)
        circle2[3::2].set_color(BLUE).set_stroke(color=BLACK, width=3)
        
        self.add(circle2)

        # Triangle 3
        pts = triangular_patch(size=5, spacing=0.6)
        circle3 = VGroup(*[
            Circle(radius=0.2, stroke_width=3).set_opacity(1.0).set_color(WHITE).set_stroke(color=BLACK).move_to(np.array([x, y, 0]))
            for (x, y) in pts
        ])
        circle3[0].set_color(RED).set_stroke(color=BLACK, width=3)
        circle3[3:6:2].set_color(RED).set_stroke(color=BLACK, width=3)
        circle3[10::2].set_color(RED).set_stroke(color=BLACK, width=3)
        
        self.wait()
        self.remove(circle2)
        self.add(circle3)

        # Triangle 4
        pts = triangular_patch(size=7, spacing=0.6)
        circle4 = VGroup(*[
            Circle(radius=0.2, stroke_width=3).set_opacity(1.0).set_color(WHITE).set_stroke(color=BLACK).move_to(np.array([x, y, 0]))
            for (x, y) in pts
        ])
        circle4[0].set_color(GREEN).set_stroke(color=BLACK, width=3)
        circle4[3:6:2].set_color(GREEN).set_stroke(color=BLACK, width=3)
        circle4[10:15:2].set_color(GREEN).set_stroke(color=BLACK, width=3)
        circle4[21::2].set_color(GREEN).set_stroke(color=BLACK, width=3)
        
        self.wait()
        self.remove(circle3)
        self.add(circle4)

        # Triangle 5
        pts = triangular_patch(size=9, spacing=0.6)
        circle5 = VGroup(*[
            Circle(radius=0.2, stroke_width=3).set_opacity(1.0).set_color(WHITE).set_stroke(color=BLACK).move_to(np.array([x, y, 0]))
            for (x, y) in pts
        ])
        circle5[0].set_color(BLUE).set_stroke(color=BLACK, width=3)
        circle5[3:6:2].set_color(BLUE).set_stroke(color=BLACK, width=3)
        circle5[10:15:2].set_color(BLUE).set_stroke(color=BLACK, width=3)
        circle5[21:28:2].set_color(BLUE).set_stroke(color=BLACK, width=3)
        circle5[36::2].set_color(BLUE).set_stroke(color=BLACK, width=3)
        
        self.wait()
        self.remove(circle4)
        self.add(circle5)

        # Triangle 6
        pts = triangular_patch(size=11, spacing=0.6)
        circle6 = VGroup(*[
            Circle(radius=0.2, stroke_width=3).set_opacity(1.0).set_color(WHITE).set_stroke(color=BLACK).move_to(np.array([x, y, 0]))
            for (x, y) in pts
        ])
        circle6[0].set_color(RED).set_stroke(color=BLACK, width=3)
        circle6[3:6:2].set_color(RED).set_stroke(color=BLACK, width=3)
        circle6[10:15:2].set_color(RED).set_stroke(color=BLACK, width=3)
        circle6[21:28:2].set_color(RED).set_stroke(color=BLACK, width=3)
        circle6[36:45:2].set_color(RED).set_stroke(color=BLACK, width=3)
        circle6[55::2].set_color(RED).set_stroke(color=BLACK, width=3)
        
        self.wait()
        self.remove(circle5)
        self.add(circle6)

        # Triangle 7
        pts = triangular_patch(size=13, spacing=0.6)
        circle7 = VGroup(*[
            Circle(radius=0.2, stroke_width=3).set_opacity(1.0).set_color(WHITE).set_stroke(color=BLACK).move_to(np.array([x, y, 0]))
            for (x, y) in pts
        ])
        circle7[0].set_color(GREEN).set_stroke(color=BLACK, width=3)
        circle7[3:6:2].set_color(GREEN).set_stroke(color=BLACK, width=3)
        circle7[10:15:2].set_color(GREEN).set_stroke(color=BLACK, width=3)
        circle7[21:28:2].set_color(GREEN).set_stroke(color=BLACK, width=3)
        circle7[36:45:2].set_color(GREEN).set_stroke(color=BLACK, width=3)
        circle7[55:66:2].set_color(GREEN).set_stroke(color=BLACK, width=3)
        circle7[78::2].set_color(GREEN).set_stroke(color=BLACK, width=3)
        
        self.wait()
        self.remove(circle6)
        self.add(circle7)

        # Triangle 8
        pts = triangular_patch(size=15, spacing=0.6)
        circle8 = VGroup(*[
            Circle(radius=0.2, stroke_width=3).set_opacity(1.0).set_color(WHITE).set_stroke(color=BLACK).move_to(np.array([x, y, 0]))
            for (x, y) in pts
        ])
        circle8[0].set_color(BLUE).set_stroke(color=BLACK, width=3)
        circle8[3:6:2].set_color(BLUE).set_stroke(color=BLACK, width=3)
        circle8[10:15:2].set_color(BLUE).set_stroke(color=BLACK, width=3)
        circle8[21:28:2].set_color(BLUE).set_stroke(color=BLACK, width=3)
        circle8[36:45:2].set_color(BLUE).set_stroke(color=BLACK, width=3)
        circle8[55:66:2].set_color(BLUE).set_stroke(color=BLACK, width=3)
        circle8[78:91:2].set_color(BLUE).set_stroke(color=BLACK, width=3)
        circle8[105::2].set_color(BLUE).set_stroke(color=BLACK, width=3)
        
        self.wait()
        self.remove(circle7)
        self.add(circle8)

        # Triangle 9
        pts = triangular_patch(size=17, spacing=0.6)
        circle9 = VGroup(*[
            Circle(radius=0.2, stroke_width=3).set_opacity(1.0).set_color(WHITE).set_stroke(color=BLACK).move_to(np.array([x, y, 0]))
            for (x, y) in pts
        ])
        circle9[0].set_color(GREEN).set_stroke(color=BLACK, width=3)
        circle9[3:6:2].set_color(GREEN).set_stroke(color=BLACK, width=3)
        circle9[10:15:2].set_color(GREEN).set_stroke(color=BLACK, width=3)
        circle9[21:28:2].set_color(GREEN).set_stroke(color=BLACK, width=3)
        circle9[36:45:2].set_color(GREEN).set_stroke(color=BLACK, width=3)
        circle9[55:66:2].set_color(GREEN).set_stroke(color=BLACK, width=3)
        circle9[78:91:2].set_color(GREEN).set_stroke(color=BLACK, width=3)
        circle9[105:120:2].set_color(GREEN).set_stroke(color=BLACK, width=3)
        circle9[136::2].set_color(GREEN).set_stroke(color=BLACK, width=3)
        
        self.wait()
        self.remove(circle8)
        self.add(circle9)


'cool animation'
LaggedStartMap(FadeIn, circles, lag_ratio=0.02, run_time=2)




