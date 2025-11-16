from manimlib import *
import sys
sys.path.append("C:/Users/thund/Downloads/manim-master/manimprojects")
from diamond_funcs import *
from vbm_funcs import *
from dots_example import *
from funcs_dots import *

### FINISHED DRAFTS

class ProjectAxes(Scene):
    def construct(self):
        sphere_size = 0.1
        frame = self.camera.frame
        frame.reorient(30,60)

        axes = ThreeDAxes(
            x_range = (-10,10,1),
            y_range = (-10,10,1),
            z_range = (-10,10,1),
        ).apply_depth_test()

        theta1 = ValueTracker(0)
        theta2 = ValueTracker(0)
        theta3 = ValueTracker(0)
        opacity_tracker1 = ValueTracker(0)
        opacity_tracker2 = ValueTracker(0)
        opacity_tracker3 = ValueTracker(0)

        circle_proj_xy = always_redraw(lambda: ParametricCurve(
            lambda u: np.array([
                (1/np.cos(theta1.get_value()))*np.sin(u),
                (np.tan(theta1.get_value())+((1/np.cos(theta1.get_value()))*np.cos(u))),
                0
            ]),
            color = WHITE,
            t_range = np.array([-PI, PI, 0.01])
        ).apply_depth_test().set_stroke(opacity=opacity_tracker1.get_value()))
        circle_proj_xz = always_redraw(lambda: ParametricCurve(
            lambda u: np.array([
                (np.tan(theta2.get_value())+((1/np.cos(theta2.get_value()))*np.cos(u))),
                0,
                (1/np.cos(theta2.get_value()))*np.sin(u),

            ]),
            color = WHITE,
            t_range = np.array([-PI, PI, 0.01])
        ).apply_depth_test().set_stroke(opacity=opacity_tracker2.get_value()))
        circle_proj_yz = always_redraw(lambda: ParametricCurve(
            lambda u: np.array([
                0,
                (1/np.cos(theta3.get_value()))*np.sin(u),
                (np.tan(theta3.get_value())+((1/np.cos(theta3.get_value()))*np.cos(u))),
            ]),
            color = WHITE,
            t_range = np.array([-PI, PI, 0.01])
        ).apply_depth_test().set_stroke(opacity=opacity_tracker3.get_value()))

        x_line = Group(
            diamond_plane_pos(1,10,0,"xy"),
            diamond_plane_neg(1,10,0,"xy"),
            generate_number_grid_pos(1,10,0,"xy",9),
            generate_number_grid_neg(1,10,0,"xy",2),
        )
        y_line = Group(
            diamond_plane_pos(10,1,0,"xz"),
            diamond_plane_neg(10,1,0,"xz"),
            generate_number_grid_pos(10,1,0,"xz",9),
            generate_number_grid_neg(10,1,0,"xz",2),
        )
        z_line = Group(
            diamond_plane_pos(1,10,0,"yz"),
            diamond_plane_neg(1,10,0,"yz"),
            generate_number_grid_pos(1,10,0,"yz",9),
            generate_number_grid_neg(1,10,0,"yz",2),
        )
        line_segment_z = Line([0,0,0],[0,0,5]).set_z_index(1)
        line_segment_y = Line([0,0,0],[0,5,0]).set_z_index(1)
        line_segment_x = Line([0,0,0],[5,0,0]).set_z_index(1)
        dia_plane_pos_xy = diamond_plane_pos(10,10,0,"xy")
        dia_plane_neg_xy = diamond_plane_neg(10,10,0,"xy")
        num_grid_pos_xy = generate_number_grid_pos(10,10,0,"xy",9)
        num_grid_neg_xy = generate_number_grid_neg(10,10,0,"xy",2)

        dia_plane_pos_xz = diamond_plane_pos(10,10,0,"xz")
        dia_plane_neg_xz = diamond_plane_neg(10,10,0,"xz")
        num_grid_pos_xz = generate_number_grid_pos(10,10,0,"xz",9)
        num_grid_neg_xz = generate_number_grid_neg(10,10,0,"xz",2)

        dia_plane_pos_yz = diamond_plane_pos(10,10,0,"yz")
        dia_plane_neg_yz = diamond_plane_neg(10,10,0,"yz")
        num_grid_pos_yz = generate_number_grid_pos(10,10,0,"yz",9)
        num_grid_neg_yz = generate_number_grid_neg(10,10,0,"yz",2)

        dia_x_axis = diamond_plane_pos(1,10,0,"xy")
        num_x_axis = generate_number_grid_pos(1,10,0,"xy",9)
        dia_y_axis = diamond_plane_pos(10,1,0,"xy")
        num_y_axis = generate_number_grid_pos(10,1,0,"xy",9)
        dia_z_axis = diamond_plane_pos(10,1,0,"xz")
        num_z_axis = generate_number_grid_pos(10,1,0,"xz",9)

        circle_proj_xy.set_z_index(1)
        circle_proj_yz.set_z_index(1)
        circle_proj_xz.set_z_index(1)

        
        self.wait()
        self.play(FadeIn(axes.apply_depth_test()))
        self.wait()

        self.add(circle_proj_xy,circle_proj_xz,circle_proj_yz)
        self.play(opacity_tracker1.animate.set_value(1.0))
        self.wait(0.1)
        self.play(opacity_tracker2.animate.set_value(1.0))
        self.wait(0.1)
        self.play(opacity_tracker3.animate.set_value(1.0))
        self.wait(0.1)
        self.play(theta1.animate.set_value(PI/2-non_zero), run_time = 3, rate_func = linear)
        self.wait(0.1)
        self.play(theta3.animate.set_value(PI/2-non_zero), run_time = 3, rate_func = linear)
        self.wait(0.1)
        self.play(theta2.animate.set_value(PI/2-non_zero), run_time = 3, rate_func = linear)
        self.play(FadeOut(axes))

        self.play(
            FadeIn(dia_plane_pos_xy.set_opacity(0.5)),
            FadeIn(dia_plane_neg_xy.set_opacity(0.5)),
            FadeIn(num_grid_pos_xy.set_opacity(0.5)),
            FadeIn(num_grid_neg_xy.set_opacity(0.5)),
        ),
        self.wait()


        self.play(
            Indicate(dia_x_axis),
            Indicate(num_x_axis),
        )
        self.wait()
        self.play(
            Indicate(dia_y_axis),
            Indicate(num_y_axis),
        )
        self.wait()

        self.play(
            FadeOut(dia_plane_pos_xy),
            FadeOut(dia_plane_neg_xy),
            FadeOut(num_grid_pos_xy),
            FadeOut(num_grid_neg_xy),
        )

        self.play(
            FadeIn(dia_plane_pos_xz.set_opacity(0.5)),
            FadeIn(dia_plane_neg_xz.set_opacity(0.5)),
            FadeIn(num_grid_pos_xz.set_opacity(0.5)),
            FadeIn(num_grid_neg_xz.set_opacity(0.5)),
        ),
        self.wait()


        self.play(
            Indicate(dia_z_axis),
            Indicate(num_z_axis),
        )
        self.wait()

        self.play(
            Indicate(dia_x_axis),
            Indicate(num_x_axis),
        )
        self.wait()

        self.play(
            FadeOut(dia_plane_pos_xz),
            FadeOut(dia_plane_neg_xz),
            FadeOut(num_grid_pos_xz),
            FadeOut(num_grid_neg_xz),
        )

        self.wait()
        
        self.play(
            FadeIn(dia_plane_pos_yz.set_opacity(0.5)),
            FadeIn(dia_plane_neg_yz.set_opacity(0.5)),
            FadeIn(num_grid_pos_yz.set_opacity(0.5)),
            FadeIn(num_grid_neg_yz.set_opacity(0.5)),
        ),
        self.wait()

        self.play(
            Indicate(dia_z_axis),
            Indicate(num_z_axis),
        )
        self.wait()

        self.play(
            Indicate(dia_y_axis),
            Indicate(num_y_axis),
        )
        self.wait()

        self.play(
            FadeOut(dia_plane_pos_yz),
            FadeOut(dia_plane_neg_yz),
            FadeOut(num_grid_pos_yz),
            FadeOut(num_grid_neg_yz),
        )

        self.wait()

        self.play(
            
            FadeOut(dia_z_axis),
            FadeOut(num_z_axis),
            opacity_tracker2.animate.set_value(0)
        )
        self.play(
            FadeOut(dia_x_axis),
            FadeOut(num_x_axis),
            FadeOut(dia_y_axis),
            FadeOut(num_y_axis),
            FadeIn(dia_plane_pos_xy.set_opacity(1.0)),
            FadeIn(dia_plane_neg_xy.set_opacity(1.0)),
            FadeIn(num_grid_pos_xy.set_opacity(1.0)),
            FadeIn(num_grid_neg_xy.set_opacity(1.0)),
        )
        self.wait()

        dots_xy_pos = dot_plane_pos(9,9,0,"xy")
        dots_xy_neg = dot_plane_neg(9,9,0,"xy")
        self.play(
            FadeIn(dots_xy_pos),
            FadeIn(dots_xy_neg),
        )
        self.play(
            FadeOut(dia_plane_pos_xy),
            FadeOut(dia_plane_neg_xy),
            FadeOut(num_grid_pos_xy),
            FadeOut(num_grid_neg_xy),
        )
        self.wait()
        self.play(
            FadeOut(dots_xy_pos),
            FadeOut(dots_xy_neg)
        )

class DotGrid(Scene):
    def construct(self):
        sphere_size = 0.1
        frame = self.camera.frame
        frame.scale(1.8)

        axes = ThreeDAxes(
            x_range = (-5,5,1),
            y_range = (-5,5,1),
            z_range = (-5,5,1),
        ).apply_depth_test()
        axes_neg = ThreeDAxes(
            x_range = (-5,5,1),
            y_range = (-5,5,1),
            z_range = (-5,5,1),
        ).apply_depth_test().move_to([0.5,-0.5,0]).set_color(GREY)

        axes.z_axis.set_opacity(0)
        axes_neg.z_axis.set_opacity(0)

        x_label_pos = Tex("(+1,-8)").scale(0.7).next_to([5,0,0],RIGHT)
        y_label_pos = Tex("(+4,-5)").scale(0.7).next_to([0,5,0],LEFT)
        x_label_neg = Tex("(+8,-1)").scale(0.7).next_to([-4.5,-0.5,0],LEFT)
        y_label_neg = Tex("(+5,-4)").scale(0.7).next_to([0.5,-5.5,0],RIGHT)

        pos_xy_plane = dot_plane_pos(5,5,0,"xy").apply_depth_test()
        neg_xy_plane = dot_plane_neg(5,5,0,"xy").apply_depth_test()

        dia_plane_pos_xy = diamond_plane_pos(5,5,0,"xy")
        dia_plane_neg_xy = diamond_plane_neg(5,5,0,"xy")
        num_grid_pos_xy = generate_number_grid_pos(5,5,0,"xy",9)
        num_grid_neg_xy = generate_number_grid_neg(5,5,0,"xy",2)

        self.play(
            FadeIn(dia_plane_pos_xy),
            FadeIn(dia_plane_neg_xy),
            FadeIn(num_grid_pos_xy),
            FadeIn(num_grid_neg_xy),
        )
        self.wait()
        self.play(
            FadeIn(axes),
            FadeIn(x_label_pos),
            FadeIn(y_label_pos),
        )
        self.wait()
        self.play(
            FadeOut(axes),
            FadeOut(x_label_pos),
            FadeOut(y_label_pos),
        )
        self.wait()
        self.play(
            FadeIn(axes_neg),
            FadeIn(x_label_neg),
            FadeIn(y_label_neg),
        )
        self.wait()
        self.play(
            FadeIn(axes),
            FadeIn(x_label_pos),
            FadeIn(y_label_pos),
        )
        self.wait()
        self.play(
            FadeOut(dia_plane_pos_xy),
            FadeOut(dia_plane_neg_xy),
            FadeOut(num_grid_pos_xy),
            FadeOut(num_grid_neg_xy),
            FadeOut(axes_neg),
            FadeOut(x_label_neg),
            FadeOut(y_label_neg),
            FadeIn(pos_xy_plane),
            FadeIn(neg_xy_plane)
        )

        self.wait()
        self.play(frame.animate.reorient(30,60))
        self.wait()
        self.play(axes.z_axis.animate.set_opacity(1))
        self.wait()

        z_label_pos = Tex("(+2,-7)").scale(0.7).next_to([0,0,5],RIGHT).rotate(PI/2,RIGHT)

        self.play(
            FadeIn(z_label_pos),
        )


        # DOT PLANES
        dots_pos_xy = Group()
        for i in range(-2,3):
            dots_pos = dot_plane_pos(3,3,i,"xy").apply_depth_test()
            dots_pos_xy.add(dots_pos)

        dots_neg_xy = Group()
        for i in range(-2,3):
            dots_neg = dot_plane_neg(3,3,i,"xy").apply_depth_test()
            dots_neg_xy.add(dots_neg)
        
        dots_neg_xz = Group()
        for i in range(-2,3):
            dots_neg = dot_plane_neg(3,3,i,"xz").apply_depth_test()
            dots_neg_xy.add(dots_neg)
        
        dots_neg_yz = Group()
        for i in range(-2,3):
            dots_neg = dot_plane_neg(3,3,i,"yz").apply_depth_test()
            dots_neg_xy.add(dots_neg)

        planes_pos_xy = Group()
        for i in range(-2,3):
            planes_pos = plane_pos_xyz(2,i,"xy").set_opacity(0.7).apply_depth_test()
            planes_pos_xy.add(planes_pos)

        vert_grid_pos_xy = Group()
        for i in range(-2,3):
            vert_grid_pos = grid_pos_xyz(2,i,"xy",2)[0].apply_depth_test()
            vert_grid_pos_xy.add(vert_grid_pos)

        horiz_grid_pos_xy = Group()
        for i in range(-2,3):
            horiz_grid = grid_pos_xyz(2,i,"xy",2)[1].apply_depth_test()
            horiz_grid_pos_xy.add(horiz_grid)

        dots_counter_xy = Group()
        for i in range(-2,2):
            dots_counter = dot_plane_counter(3,3,i,"xy").apply_depth_test()
            dots_counter_xy.add(dots_counter)

        planes_neg_xy = Group()
        for i in range(-2,2):
            planes_neg = plane_neg_xyz(2,i,"xy").set_opacity(0.7).apply_depth_test()
            planes_neg_xy.add(planes_neg)

        vert_grid_neg_xy = Group()
        for i in range(-2,2):
            vert_grid_neg = grid_neg_xyz(2,i,"xy",2)[0].apply_depth_test()
            vert_grid_neg_xy.add(vert_grid_neg)

        horiz_grid_neg_xy = Group()
        for i in range(-2,2):
            horiz_grid_neg = grid_neg_xyz(2,i,"xy",2)[1].apply_depth_test()
            horiz_grid_neg_xy.add(horiz_grid_neg)

        self.wait()
        self.add(dots_pos_xy[2], dots_neg_xy[2])
        self.play(FadeOut(pos_xy_plane), FadeOut(neg_xy_plane))
        self.wait()

        self.play(frame.animate.scale(0.7))
        self.wait()
        self.play(
            FadeIn(planes_pos_xy[2]),
            FadeIn(vert_grid_pos_xy[2]),
            FadeIn(horiz_grid_pos_xy[2]),
        )
        self.wait(3)
        self.play(
            FadeIn(dots_counter_xy[2]),
            FadeIn(planes_neg_xy[2]),
            FadeIn(vert_grid_neg_xy[2]),
            FadeIn(horiz_grid_neg_xy[2]),
            FadeIn(dots_counter_xy[1]),
            FadeIn(planes_neg_xy[1]),
            FadeIn(vert_grid_neg_xy[1]),
            FadeIn(horiz_grid_neg_xy[1]),
        )
        self.wait(3)

        self.play(
            FadeIn(dots_pos_xy[3]),
            FadeIn(dots_neg_xy[3]),
            FadeIn(planes_pos_xy[3]),
            FadeIn(vert_grid_pos_xy[3]),
            FadeIn(horiz_grid_pos_xy[3]),
            FadeIn(dots_pos_xy[1]),
            FadeIn(dots_neg_xy[1]),
            FadeIn(planes_pos_xy[1]),
            FadeIn(vert_grid_pos_xy[1]),
            FadeIn(horiz_grid_pos_xy[1]),
        )
        self.wait(3)
        self.play(
            FadeIn(dots_counter_xy[3]),
            FadeIn(planes_neg_xy[3]),
            FadeIn(vert_grid_neg_xy[3]),
            FadeIn(horiz_grid_neg_xy[3]),
            FadeIn(dots_counter_xy[0]),
            FadeIn(planes_neg_xy[0]),
            FadeIn(vert_grid_neg_xy[0]),
            FadeIn(horiz_grid_neg_xy[0]),
        )
        self.wait(3)

        self.play(
            FadeIn(dots_pos_xy[4]),
            FadeIn(dots_neg_xy[4]),
            FadeIn(planes_pos_xy[4]),
            FadeIn(vert_grid_pos_xy[4]),
            FadeIn(horiz_grid_pos_xy[4]),
            FadeIn(dots_pos_xy[0]),
            FadeIn(dots_neg_xy[0]),
            FadeIn(planes_pos_xy[0]),
            FadeIn(vert_grid_pos_xy[0]),
            FadeIn(horiz_grid_pos_xy[0]),
        )
        self.wait(3)
        dot_grid = make_box_grid(4, 1.5).scale(0.5)
        
        self.play(
            FadeOut(planes_pos_xy),
            FadeOut(vert_grid_pos_xy),
            FadeOut(horiz_grid_pos_xy),
            FadeOut(planes_neg_xy),
            FadeOut(vert_grid_neg_xy),
            FadeOut(horiz_grid_neg_xy),
        )
        self.wait()
        frame.add_updater(lambda m, dt: m.increment_theta(-0.1*dt))
        self.wait(3)

        planes_array_xy = Group()
        for i in range(-2,2):
            planes_xy = plane_neg_xyz(3,i,"xy").set_opacity(0.7).apply_depth_test()
            planes_array_xy.add(planes_xy)

        planes_array_xz = Group()
        for i in range(-2,2):
            planes_xz = plane_neg_xyz(3,i,"xz").set_opacity(0.7).apply_depth_test()
            planes_array_xz.add(planes_xz)

        planes_array_yz = Group()
        for i in range(-2,2):
            planes_yz = plane_neg_xyz(3,i,"yz").set_opacity(0.7).apply_depth_test()
            planes_array_yz.add(planes_yz)
        
        self.wait(3)
        self.play(
            FadeIn(planes_array_yz)
        )
        self.wait(10)
        self.play(
            FadeIn(planes_array_xy)
        )
        self.wait(10)
        self.play(
            FadeIn(planes_array_xz)
        )
        self.wait(20)

class DotGrid2(Scene):
    def construct(self):
        sphere_size = 0.1
        frame = self.camera.frame
        frame.scale(1.8)
        frame.reorient(30,60)
        axes = ThreeDAxes(
            x_range = (-5,5,1),
            y_range = (-5,5,1),
            z_range = (-5,5,1),
        ).apply_depth_test()
        self.add(axes)
        for i in range(0,5):
            if i == 0:
                dots_pos = dot_plane_pos(5,5,-i,"xz").set_opacity(0.0).apply_depth_test()
                dots_neg = dot_plane_neg(5,5,-i,"xz").set_opacity(0.0).apply_depth_test()
                plane_pos = plane_pos_xyz(4,-i,"xz").set_opacity(0.0).apply_depth_test()
                grid_pos = Group(grid_pos_xyz(4,-i,"xz",2)[0], grid_pos_xyz(4,-i,"xz",2)[1]).set_opacity(0.0)
                self.play(
                    dots_pos.animate.set_opacity(1.0), 
                    dots_neg.animate.set_opacity(1.0),
                    plane_pos.animate.set_opacity(1.0), 
                    grid_pos.animate.set_opacity(1.0),
                )

                dots_counter = dot_plane_counter(5,5,-i,"xz").set_opacity(0.0).apply_depth_test()
                plane_neg = plane_neg_xyz(4,-i,"xz").set_opacity(0.0).apply_depth_test()
                grid_neg = Group(grid_neg_xyz(4,-i,"xz",2)[0], grid_neg_xyz(4,-i,"xz",2)[1]).set_opacity(0.0)

                self.play(
                    dots_pos.animate.set_opacity(0.0), 
                    dots_neg.animate.set_opacity(0.0),
                    plane_pos.animate.set_opacity(0.0), 
                    grid_pos.animate.set_opacity(0.0),
                    dots_counter.animate.set_opacity(1.0),
                    plane_neg.animate.set_opacity(1.0),
                    grid_neg.animate.set_opacity(1.0),
                )

            else:
                dots_pos = dot_plane_pos(5,5,-i,"xz").set_opacity(0.0).apply_depth_test()
                dots_neg = dot_plane_neg(5,5,-i,"xz").set_opacity(0.0).apply_depth_test()
                plane_pos = plane_pos_xyz(4,-i,"xz").set_opacity(0.0).apply_depth_test()
                grid_pos = Group(grid_pos_xyz(4,-i,"xz",2)[0], grid_pos_xyz(4,-i,"xz",2)[1]).set_opacity(0.0)
                self.play(
                    dots_pos.animate.set_opacity(1.0), 
                    dots_neg.animate.set_opacity(1.0),
                    plane_pos.animate.set_opacity(1.0), 
                    grid_pos.animate.set_opacity(1.0),
                    dots_counter.animate.set_opacity(0.0),
                    plane_neg.animate.set_opacity(0.0),
                    grid_neg.animate.set_opacity(0.0),
                )

                dots_counter = dot_plane_counter(5,5,-i,"xz").set_opacity(0.0).apply_depth_test()
                plane_neg = plane_neg_xyz(4,-i,"xz").set_opacity(0.0).apply_depth_test()
                grid_neg = Group(grid_neg_xyz(4,-i,"xz",2)[0], grid_neg_xyz(4,-i,"xz",2)[1]).set_opacity(0.0)

                self.play(
                    dots_pos.animate.set_opacity(0.0), 
                    dots_neg.animate.set_opacity(0.0),
                    plane_pos.animate.set_opacity(0.0), 
                    grid_pos.animate.set_opacity(0.0),
                    dots_counter.animate.set_opacity(1.0),
                    plane_neg.animate.set_opacity(1.0),
                    grid_neg.animate.set_opacity(1.0),
                )

        self.play(
            dots_counter.animate.set_opacity(0.0),
            plane_neg.animate.set_opacity(0.0),
            grid_neg.animate.set_opacity(0.0),
        )
        self.wait()
        self.remove(dots_pos, dots_neg, dots_counter)
        self.remove(plane_pos, plane_neg, grid_pos, grid_neg)

class DotGrid3(Scene):
    def construct(self):
        sphere_size = 0.1
        frame = self.camera.frame
        frame.scale(1.8)

        axes = ThreeDAxes(
            x_range = (-5,5,1),
            y_range = (-5,5,1),
            z_range = (-5,5,1),
        ).apply_depth_test()
        for i in range(0,5):
            if i == 0:
                dots_pos = dot_plane_pos(5,5,i,"yz").set_opacity(0.0).apply_depth_test()
                dots_neg = dot_plane_neg(5,5,i,"yz").set_opacity(0.0).apply_depth_test()
                plane_pos = plane_pos_xyz(4,i,"yz").set_opacity(0.7).set_opacity(0.0).apply_depth_test()
                grid_pos = Group(grid_pos_xyz(4,i,"yz",2)[0], grid_pos_xyz(4,i,"yz",2)[1]).set_opacity(0.0)
                self.play(
                    dots_pos.animate.set_opacity(1.0), 
                    dots_neg.animate.set_opacity(1.0),
                    plane_pos.animate.set_opacity(1.0), 
                    grid_pos.animate.set_opacity(1.0),
                )

                dots_counter = dot_plane_counter(5,5,i,"yz").set_opacity(0.0).apply_depth_test()
                plane_neg = plane_neg_xyz(4,i,"yz").set_opacity(0.7).set_opacity(0.0).apply_depth_test()
                grid_neg = Group(grid_neg_xyz(4,i,"yz",2)[0], grid_neg_xyz(4,i,"yz",2)[1]).set_opacity(0.0)

                self.play(
                    dots_pos.animate.set_opacity(0.0), 
                    dots_neg.animate.set_opacity(0.0),
                    plane_pos.animate.set_opacity(0.0), 
                    grid_pos.animate.set_opacity(0.0),
                    dots_counter.animate.set_opacity(1.0),
                    plane_neg.animate.set_opacity(1.0),
                    grid_neg.animate.set_opacity(1.0),
                )

            else:
                dots_pos = dot_plane_pos(5,5,i,"yz").set_opacity(0.0).apply_depth_test()
                dots_neg = dot_plane_neg(5,5,i,"yz").set_opacity(0.0).apply_depth_test()
                plane_pos = plane_pos_xyz(4,i,"yz").set_opacity(0.7).set_opacity(0.0).apply_depth_test()
                grid_pos = Group(grid_pos_xyz(4,i,"yz",2)[0], grid_pos_xyz(4,i,"yz",2)[1]).set_opacity(0.0)
                self.play(
                    dots_pos.animate.set_opacity(1.0), 
                    dots_neg.animate.set_opacity(1.0),
                    plane_pos.animate.set_opacity(1.0), 
                    grid_pos.animate.set_opacity(1.0),
                    dots_counter.animate.set_opacity(0.0),
                    plane_neg.animate.set_opacity(0.0),
                    grid_neg.animate.set_opacity(0.0),
                )

                dots_counter = dot_plane_counter(5,5,i,"yz").set_opacity(0.0).apply_depth_test()
                plane_neg = plane_neg_xyz(4,i,"yz").set_opacity(0.7).set_opacity(0.0).apply_depth_test()
                grid_neg = Group(grid_neg_xyz(4,i,"yz",2)[0], grid_neg_xyz(4,i,"yz",2)[1]).set_opacity(0.0)

                self.play(
                    dots_pos.animate.set_opacity(0.0), 
                    dots_neg.animate.set_opacity(0.0),
                    plane_pos.animate.set_opacity(0.0), 
                    grid_pos.animate.set_opacity(0.0),
                    dots_counter.animate.set_opacity(1.0),
                    plane_neg.animate.set_opacity(1.0),
                    grid_neg.animate.set_opacity(1.0),
                )

        self.play(
            dots_counter.animate.set_opacity(0.0),
            plane_neg.animate.set_opacity(0.0),
            grid_neg.animate.set_opacity(0.0),
        )
        self.wait()
        self.remove(dots_pos, dots_neg, dots_counter)
        self.remove(plane_pos, plane_neg, grid_pos, grid_neg)
        # grid_pos = Group()
        # grid_neg_xy = Group()
        # grid_neg_xz = Group()
        # grid_neg_yz = Group()

        # for i in range(-2,3):
            
        #     box_grid_pos = dot_plane_pos(3,3,i,"xy").apply_depth_test()
        #     grid_pos.add(box_grid_pos)

        # self.wait()
        # self.play(FadeIn(grid_pos))

        # box_grid_neg = dot_plane_neg(3,3,i,"xy").apply_depth_test()

        # self.wait()

        # frame.set_euler_angles(
        #     theta=30*DEGREES,
        #     phi=60*DEGREES,
        # )
        # frame.add_updater(lambda m, dt: m.increment_theta(-0.1*dt))
        # self.play(frame.animate.scale(1/1.8).scale(1.5))
        # for i in range(-2,3):
        #     box_grid_neg_xy = dot_plane_neg(3,3,i,"xy").apply_depth_test()
        #     grid_neg_xy.add(box_grid_neg_xy)

        # self.play(FadeIn(grid_neg_xy))
        # self.wait(3)

        # for i in range(-2,3):
        #     box_grid_neg_xz = dot_plane_neg(3,3,i,"xz").apply_depth_test()
        #     grid_neg_xz.add(box_grid_neg_xz)

        # self.play(FadeIn(grid_neg_xz))
        # self.wait(3)  

        # for i in range(-2,3):
        #     box_grid_neg_yz = dot_plane_neg(3,3,i,"yz").apply_depth_test()
        #     grid_neg_yz.add(box_grid_neg_yz)

        # self.play(FadeIn(grid_neg_yz))
        # self.wait(3)


        # self.play(frame.animate.reorient(0,90))

        # planes_pos_xy = Group()
        # planes_neg_xy = Group()
        # for i in range(-2,3):
        #     box_plane_pos_xy = plane_pos_xyz(3,i,"xy").apply_depth_test()
        #     box_plane_neg_xy = plane_neg_xyz(3,i,"xy").apply_depth_test()
        #     planes_pos_xy.add(box_plane_pos_xy)
        #     planes_neg_xy.add(box_plane_neg_xy)
        
        # self.play(FadeIn(planes_pos_xy))
        # self.wait()
        # self.play(FadeIn(planes_neg_xy))
        # self.wait(3)
        # self.play(
        #     FadeOut(planes_pos_xy),
        #     FadeOut(planes_neg_xy),
        # )
        # self.wait()

        # self.play(frame.animate.reorient(30,60))
        
        # planes_pos_xz = Group()
        # planes_neg_xz = Group()
        # for i in range(-2,3):
        #     box_plane_pos_xz = plane_pos_xyz(3,i,"xz").apply_depth_test()
        #     box_plane_neg_xz = plane_neg_xyz(3,i,"xz").apply_depth_test()
        #     planes_pos_xz.add(box_plane_pos_xz)
        #     planes_neg_xz.add(box_plane_neg_xz)

        # self.play(FadeIn(planes_pos_xz))
        # self.wait()
        # self.play(FadeIn(planes_neg_xz))
        # self.wait(3)
        # self.play(
        #     FadeOut(planes_pos_xz),
        #     FadeOut(planes_neg_xz)
        # )
        # self.wait()

        # planes_pos_yz = Group()
        # planes_neg_yz = Group()
        # for i in range(-2,3):
        #     box_plane_pos_yz = plane_pos_xyz(3,i,"yz").apply_depth_test()
        #     box_plane_neg_yz = plane_neg_xyz(3,i,"yz").apply_depth_test()
        #     planes_pos_yz.add(box_plane_pos_yz)
        #     planes_neg_yz.add(box_plane_neg_yz)

        # self.play(FadeIn(planes_pos_yz))
        # self.wait()
        # self.play(FadeIn(planes_neg_yz))
        # self.wait(3)
        # self.play(
        #     FadeOut(planes_pos_yz),
        #     FadeOut(planes_neg_yz)
        # )
        # self.wait()

class GeoBreakdown(Scene):
    def construct(self):

        frame = self.camera.frame
        frame.scale(1.5)
        frame.set_euler_angles(
            theta=30*DEGREES,
            phi=60*DEGREES,
        )

        grid_pos2 = Group()
        grid_neg_xy2 = Group()
        grid_neg_xz2 = Group()
        grid_neg_yz2 = Group()
        for i in range(-1,2):
            
            box_grid_pos2 = dot_plane_pos(2,2,i,"xy").apply_depth_test()
            grid_pos2.add(box_grid_pos2)

        for i in range(-1,2):
            box_grid_neg_xy2 = dot_plane_neg(2,2,i,"xy").apply_depth_test()
            grid_neg_xy2.add(box_grid_neg_xy2)

        for i in range(-1,2):
            box_grid_neg_xz2 = dot_plane_neg(2,2,i,"xz").apply_depth_test()
            grid_neg_xz2.add(box_grid_neg_xz2)

        for i in range(-1,2):
            box_grid_neg_yz2 = dot_plane_neg(2,2,i,"yz").apply_depth_test()
            grid_neg_yz2.add(box_grid_neg_yz2)

        self.wait()
        self.add(grid_pos2, grid_neg_xy2, grid_neg_xz2, grid_neg_yz2)
        self.wait()

        axes = ThreeDAxes(
            x_range = (-5,5,1),
            y_range = (-5,5,1),
            z_range = (-5,5,1),
        ).apply_depth_test()
        axes_neg = ThreeDAxes(
            x_range = (-5,5,1),
            y_range = (-5,5,1),
            z_range = (-5,5,1),
        ).apply_depth_test().move_to([0.5,-0.5,0]).set_color(GREY)

        self.play(
            frame.animate.scale(1/1.5).scale(0.7),
        )
        self.wait()
        self.play(FadeIn(axes))

        frame.add_updater(lambda m, dt: m.increment_theta(-0.1*dt))

        grid_pos3 = Group()
        for i in range(0,1):
            box_grid_pos3 = dot_plane_pos(1,1,i,"xy").apply_depth_test()
            grid_pos3.add(box_grid_pos3)

        self.wait()

        sphere_size=0.12
        dot1 = Sphere(radius=sphere_size).move_to([0.5,0.5,0]).set_color(YELLOW).apply_depth_test()
        dot2 = Sphere(radius=sphere_size).move_to([-0.5,0.5,0]).set_color(YELLOW).apply_depth_test()
        dot3 = Sphere(radius=sphere_size).move_to([0.5,-0.5,0]).set_color(YELLOW).apply_depth_test()
        dot4 = Sphere(radius=sphere_size).move_to([-0.5,-0.5,0]).set_color(YELLOW).apply_depth_test()

        dot5 = Sphere(radius=sphere_size).move_to([0.5,0,0.5]).set_color(YELLOW).apply_depth_test()
        dot6 = Sphere(radius=sphere_size).move_to([-0.5,0,0.5]).set_color(YELLOW).apply_depth_test()
        dot7 = Sphere(radius=sphere_size).move_to([0.5,0,-0.5]).set_color(YELLOW).apply_depth_test()
        dot8 = Sphere(radius=sphere_size).move_to([-0.5,0,-0.5]).set_color(YELLOW).apply_depth_test()

        dot9 = Sphere(radius=sphere_size).move_to([0,0.5,0.5]).set_color(YELLOW).apply_depth_test()
        dot10 = Sphere(radius=sphere_size).move_to([0,-0.5,0.5]).set_color(YELLOW).apply_depth_test()
        dot11 = Sphere(radius=sphere_size).move_to([0,0.5,-0.5]).set_color(YELLOW).apply_depth_test()
        dot12 = Sphere(radius=sphere_size).move_to([0,-0.5,-0.5]).set_color(YELLOW).apply_depth_test()

        vector_dots = Group(dot1,dot2,dot3,dot4,dot5,dot6,dot7,dot8,dot9,dot10,dot11,dot12)
        
        self.add(Sphere(radius=0.1).set_color(GREEN).apply_depth_test())
        self.play(FadeIn(vector_dots))
        self.wait()
        self.play(
            vector_dots.animate.scale(0.9),
            vector_dots.animate.set_color(WHITE),
            FadeOut(grid_pos2), 
            FadeOut(grid_neg_xy2), 
            FadeOut(grid_neg_xz2), 
            FadeOut(grid_neg_yz2),
        )
        self.wait(3)

        self.play(
            frame.animate.scale(1/0.7).scale(0.4),
        )

        vector_lines = Group()
        for dot in vector_dots:
            new_line = Line(dot.get_center(),[0,0,0]).apply_depth_test()
            vector_lines.add(new_line)
        
        self.play(ShowCreation(vector_lines))
        self.wait(3.2)
        frame.suspend_updating()

        num1 = Tex("2").scale(0.5).move_to(vector_dots[0]).rotate(PI/2,RIGHT).set_color(BLACK)
        num2 = Tex("3").scale(0.5).move_to(vector_dots[1]).rotate(PI/2,RIGHT).set_color(BLACK)
        num3 = Tex("6").scale(0.5).move_to(vector_dots[2]).rotate(PI/2,RIGHT).set_color(BLACK)
        num4 = Tex("7").scale(0.5).move_to(vector_dots[3]).rotate(PI/2,RIGHT).set_color(BLACK)
        num5 = Tex("5").scale(0.5).move_to(vector_dots[4]).rotate(PI/2,RIGHT).set_color(BLACK)
        num6 = Tex("6").scale(0.5).move_to(vector_dots[5]).rotate(PI/2,RIGHT).set_color(BLACK)
        num7 = Tex("3").scale(0.5).move_to(vector_dots[6]).rotate(PI/2,RIGHT).set_color(BLACK)
        num8 = Tex("4").scale(0.5).move_to(vector_dots[7]).rotate(PI/2,RIGHT).set_color(BLACK)
        num9 = Tex("8").scale(0.5).move_to(vector_dots[8]).rotate(PI/2,RIGHT).set_color(BLACK)
        num10 = Tex("3").scale(0.5).move_to(vector_dots[9]).rotate(PI/2,RIGHT).set_color(BLACK)
        num11 = Tex("6").scale(0.5).move_to(vector_dots[10]).rotate(PI/2,RIGHT).set_color(BLACK)
        num12 = Tex("1").scale(0.5).move_to(vector_dots[11]).rotate(PI/2,RIGHT).set_color(BLACK)
        num_center = Tex("9").scale(0.5).rotate(PI/2,RIGHT).set_color(BLACK)

        numbers = Group(
            num1,num2,num3,num4,
            num5,num6,num7,num8,
            num9,num10,num11,num12,
            num_center
        )
        self.play(FadeIn(numbers))
        self.wait()


        triangle_369 = Group(
            parametric_triangle(np.array([0,-0.5,0.5]),np.array([0.5,-0.5,0]),np.array([0,0,0])),
            parametric_triangle(np.array([0.5,0,-0.5]),np.array([0.5,-0.5,0]),np.array([0,0,0])),
            parametric_triangle(np.array([0.5,0,-0.5]),np.array([0,0.5,-0.5]),np.array([0,0,0])),
            parametric_triangle(np.array([-0.5,0.5,0]),np.array([0,0.5,-0.5]),np.array([0,0,0])),
            parametric_triangle(np.array([-0.5,0.5,0]),np.array([-0.5,0,0.5]),np.array([0,0,0])),
            parametric_triangle(np.array([0,-0.5,0.5]),np.array([-0.5,0,0.5]),np.array([0,0,0])),
        )

        octa_ve = half_octa_grid(GREEN,0.5).set_opacity(0)
        self.play(ShowCreation(octa_ve.set_opacity(0.7)))
        self.wait()

        self.play(
            octa_ve.animate.set_opacity(0),
        )
        self.remove(octa_ve)
        self.wait()
        tetra_ve = vector_equilibrium(0.5,BLUE,RED).set_opacity(0)
        tetra_top = tetra_ve[0].copy().set_opacity(0)
        tetra_bottom = tetra_ve[1].copy().set_opacity(0)
        self.play(ShowCreation(tetra_ve.set_opacity(0.7)))
        self.wait()
        self.add(tetra_top,tetra_bottom)
        self.play(
            tetra_ve.animate.set_opacity(0),
            tetra_top.animate.set_opacity(0.7),
            tetra_bottom.animate.set_opacity(0.7),
        )
        self.remove(tetra_ve)
        self.wait()

        self.add(triangle_369.set_color(GREEN).set_opacity(0))
        self.play(triangle_369.animate.set_opacity(0.7))
        self.wait()
        self.play(FadeOut(numbers))
        
        

        self.wait(3)

        frame.resume_updating()
        self.wait()
        self.play(
            triangle_369.animate.set_opacity(0),
            tetra_top.animate.set_opacity(0),
            tetra_bottom.animate.set_opacity(0),
        )
        self.remove(
            triangle_369,
            tetra_top,
            tetra_bottom
        )
        self.play(
            octa_ve.animate.set_opacity(0.7),
            tetra_ve.animate.set_opacity(0.7),
        )

        

        self.wait(13)
        frame.suspend_updating()
        
        self.play(frame.animate.scale(1/0.4).scale(0.7))
        self.wait()
        self.play(
            octa_ve.animate.set_opacity(0),
            tetra_ve.animate.set_opacity(0),
        )
        self.wait()
        self.remove(octa_ve,tetra_ve,triangle_369,tetra_top,tetra_bottom)

        plane_size = 2
        square_xy = parametric_square(
            np.array([0,0,0]),
            np.array([plane_size,0,0]),
            np.array([0,plane_size,0]),
            1,
        ).apply_depth_test().set_color(WHITE).set_opacity(0.7)

        square_xz = parametric_square(
            np.array([0,0,0]),
            np.array([plane_size,0,0]),
            np.array([0,0,plane_size]),
            1,
        ).apply_depth_test().set_color(WHITE).set_opacity(0.7)
        
        square_yz = parametric_square(
            np.array([0,0,0]),
            np.array([0,plane_size,0]),
            np.array([0,0,plane_size]),
            1,
        ).apply_depth_test().set_color(WHITE).set_opacity(0.7)
        
        self.play(
            FadeIn(square_xy),
            Indicate(vector_dots[0]),
            Indicate(vector_dots[1]),
            Indicate(vector_dots[2]),
            Indicate(vector_dots[3]),
        )
        self.wait()
        self.play(
            FadeIn(square_xz),
            Indicate(vector_dots[4]),
            Indicate(vector_dots[5]),
            Indicate(vector_dots[6]),
            Indicate(vector_dots[7]),
        )
        self.wait()
        self.play(
            FadeIn(square_yz),
            Indicate(vector_dots[8]),
            Indicate(vector_dots[9]),
            Indicate(vector_dots[10]),
            Indicate(vector_dots[11]),
        )
        self.wait()
    
        frame.resume_updating()

        square_xy_neg1 = parametric_square(
            np.array([0,0,0.5]),
            np.array([plane_size,0,0]),
            np.array([0,plane_size,0]),
            1,
        ).apply_depth_test().set_color(GREY).set_opacity(0)
        square_xy_neg2 = parametric_square(
            np.array([0,0,-0.5]),
            np.array([plane_size,0,0]),
            np.array([0,plane_size,0]),
            1,
        ).apply_depth_test().set_color(GREY).set_opacity(0)

        self.wait()
        self.add(square_xy_neg1,square_xy_neg2)
        self.play(
            square_xy_neg1.animate.set_opacity(0.7),
            square_xy_neg2.animate.set_opacity(0.7),
        )
        self.wait(5)
        self.play(
            square_xy_neg1.animate.set_opacity(0),
            square_xy_neg2.animate.set_opacity(0),
        )
        self.remove(square_xy_neg1,square_xy_neg2)

        square_yz_neg1 = parametric_square(
            np.array([0.5,0,0]),
            np.array([0,plane_size,0]),
            np.array([0,0,plane_size]),
            1,
        ).apply_depth_test().set_color(GREY).set_opacity(0)
        square_yz_neg2 = parametric_square(
            np.array([-0.5,0,0]),
            np.array([0,plane_size,0]),
            np.array([0,0,plane_size]),
            1,
        ).apply_depth_test().set_color(GREY).set_opacity(0)

        self.wait()
        self.add(square_yz_neg1,square_yz_neg2)
        self.play(
            square_yz_neg1.animate.set_opacity(0.7),
            square_yz_neg2.animate.set_opacity(0.7),
        )
        self.wait(5)
        self.play(
            square_yz_neg1.animate.set_opacity(0),
            square_yz_neg2.animate.set_opacity(0),
        )
        self.remove(square_yz_neg1,square_yz_neg2)

        self.wait(5)

        square_xz_neg1 = parametric_square(
            np.array([0,0.5,0]),
            np.array([plane_size,0,0]),
            np.array([0,0,plane_size]),
            1,
        ).apply_depth_test().set_color(GREY).set_opacity(0)
        square_xz_neg2 = parametric_square(
            np.array([0,-0.5,0]),
            np.array([plane_size,0,0]),
            np.array([0,0,plane_size]),
            1,
        ).apply_depth_test().set_color(GREY).set_opacity(0)

        self.add(square_xz_neg1,square_xz_neg2)
        self.play(
            square_xz_neg1.animate.set_opacity(0.7),
            square_xz_neg2.animate.set_opacity(0.7),
        )
        self.wait(5)
        self.play(
            square_xz_neg1.animate.set_opacity(0),
            square_xz_neg2.animate.set_opacity(0),
        )
        self.remove(square_xz_neg1,square_xz_neg2)

        self.wait()

        frame.suspend_updating()
        self.add(square_xz_neg1,square_yz_neg1)
        self.play(
            square_xz_neg2.animate.set_opacity(0.7),
            square_yz_neg1.animate.set_opacity(0.7),
        )
        self.wait()
        self.play(FadeIn(axes_neg))

class SpaceGrid(Scene):
    def construct(self):
        frame = self.camera.frame
        frame.scale(1.5)
        frame.set_euler_angles(
            theta=30*DEGREES,
            phi=60*DEGREES,
        )
        axes = ThreeDAxes(
            x_range = (-5,5,1),
            y_range = (-5,5,1),
            z_range = (-5,5,1),
        ).apply_depth_test()
        axes_neg = ThreeDAxes(
            x_range = (-5,5,1),
            y_range = (-5,5,1),
            z_range = (-5,5,1),
        )
        sphere_size = 0.1
        red_center_x = make_ve_dots(RED, sphere_size)
        red_center_y = make_ve_dots(RED, sphere_size)
        red_center_z = make_ve_dots(RED, sphere_size)
        blue_center_x = make_ve_dots(BLUE, sphere_size)
        blue_center_y = make_ve_dots(BLUE, sphere_size)
        blue_center_z = make_ve_dots(BLUE, sphere_size)
        green_center = make_ve_dots(GREEN, sphere_size)

        frame.scale(0.5)
        frame.add_updater(lambda m, dt: m.increment_theta(-0.1*dt))
        self.add(axes,green_center)
        self.wait()
        self.add(red_center_x.set_opacity(0))
        self.play(red_center_x.animate.move_to([1,0,0]).set_opacity(1))
        self.wait()
        self.add(blue_center_x.set_opacity(0))
        self.play(blue_center_x.animate.move_to([-1,0,0]).set_opacity(1))

        self.wait()
        self.add(red_center_y.set_opacity(0))
        self.play(red_center_y.animate.move_to([0,1,0]).set_opacity(1))
        self.wait()
        self.add(blue_center_y.set_opacity(0))
        self.play(blue_center_y.animate.move_to([0,-1,0]).set_opacity(1))

        self.wait()
        self.add(red_center_z.set_opacity(0))
        self.play(red_center_z.animate.move_to([0,0,1]).set_opacity(1))
        self.wait()
        self.add(blue_center_z.set_opacity(0))
        self.play(blue_center_z.animate.move_to([0,0,-1]).set_opacity(1))

        grid_pos2 = Group()
        grid_neg_xy2 = Group()
        grid_neg_xz2 = Group()
        grid_neg_yz2 = Group()
        for i in range(-1,2):
            
            box_grid_pos2 = dot_plane_pos(2,2,i,"xy").apply_depth_test()
            grid_pos2.add(box_grid_pos2)

        for i in range(-1,2):
            box_grid_neg_xy2 = dot_plane_neg(2,2,i,"xy").apply_depth_test()
            grid_neg_xy2.add(box_grid_neg_xy2)

        for i in range(-1,2):
            box_grid_neg_xz2 = dot_plane_neg(2,2,i,"xz").apply_depth_test()
            grid_neg_xz2.add(box_grid_neg_xz2)

        for i in range(-1,2):
            box_grid_neg_yz2 = dot_plane_neg(2,2,i,"yz").apply_depth_test()
            grid_neg_yz2.add(box_grid_neg_yz2)

        self.wait()
        self.play(
            FadeIn(grid_pos2), 
            FadeIn(grid_neg_xy2), 
            FadeIn(grid_neg_xz2), 
            FadeIn(grid_neg_yz2),
        )
        self.wait()

        self.remove(red_center_x,red_center_y,red_center_z,blue_center_x,blue_center_y,blue_center_z,green_center)

        self.play(
            red_center_x.animate.set_opacity(0),
            red_center_y.animate.set_opacity(0),
            red_center_z.animate.set_opacity(0),
            blue_center_x.animate.set_opacity(0),
            blue_center_y.animate.set_opacity(0),
            blue_center_z.animate.set_opacity(0),
            green_center.animate.set_opacity(0),
        )
        self.wait()

        frame.suspend_updating()
        self.wait()

        self.play(
            FadeOut(grid_neg_xy2), 
            FadeOut(grid_neg_xz2), 
            FadeOut(grid_neg_yz2),
        )
        self.wait()

class PolyGrid(Scene):
    def construct(self):

        frame = self.camera.frame
        frame.scale(1)
        frame.set_euler_angles(
            theta=30*DEGREES,
            phi=60*DEGREES,
        )
        frame.scale(0.7)
        axes = ThreeDAxes(
            x_range = (-5,5,1),
            y_range = (-5,5,1),
            z_range = (-5,5,1),
        ).apply_depth_test()

        def vec_grid_pos(num_rows, num_cols, offset, col1, col2):
            ve_grid = Group()
            for i in range(-num_rows+1,num_rows):
                for j in range(-num_cols+1,num_cols):
                    new_vec = vector_equilibrium(0.5,col1,col2)[0].shift([(i),(j),offset])
                    ve_grid.add(new_vec)
            return ve_grid
        def vec_grid_neg(num_rows, num_cols, offset, col1, col2):
            ve_grid = Group()
            for i in range(-num_rows+1,num_rows):
                for j in range(-num_cols+1,num_cols):
                    new_vec = vector_equilibrium(0.5,col1,col2)[1].shift([(i),(j),offset])
                    ve_grid.add(new_vec)
            return ve_grid
        def octa_grid(num_rows, num_cols, offset, col):
            ve_grid = Group()
            for i in range(-num_rows+1,num_rows):
                for j in range(-num_cols+1,num_cols):
                    new_vec = half_octa_grid(col,0.5).shift([(i),(j),offset])
                    ve_grid.add(new_vec)
            return ve_grid

        def diff_octa_grid(num_rows, num_cols, offset, col):
            ve_grid = Group()
            for i in range(-num_rows+1,num_rows-1):
                for j in range(-num_cols+1,num_cols-1):
                    new_vec = octahedron(0.5).shift([(i+0.5),(j+0.5),offset+0.5]).set_color(col)
                    ve_grid.add(new_vec)
            return ve_grid
        
        vec_top_pos = vec_grid_pos(2,2,1,BLUE,RED)
        vec_mid_pos = vec_grid_pos(2,2,0,BLUE,RED)
        vec_bot_pos = vec_grid_pos(2,2,-1,BLUE,RED)
        tetras_pos = Group(vec_top_pos, vec_mid_pos, vec_bot_pos).set_opacity(0)

        vec_top_neg = vec_grid_neg(2,2,1,BLUE,RED).set_opacity(0)
        vec_mid_neg = vec_grid_neg(2,2,0,BLUE,RED).set_opacity(0)
        vec_bot_neg = vec_grid_neg(2,2,-1,BLUE,RED).set_opacity(0)
        tetras_neg = Group(vec_top_neg, vec_mid_neg, vec_bot_neg).set_opacity(0)

        octa_top = octa_grid(2,2,1,GREEN).set_opacity(0)
        octa_mid = octa_grid(2,2,0,GREEN).set_opacity(0)
        octa_bot = octa_grid(2,2,-1,GREEN).set_opacity(0)
        octas = Group(octa_top, octa_mid, octa_bot).set_opacity(0)

        diff_octa_mid1 = diff_octa_grid(3,3,0,PURPLE)
        diff_octa_mid2 = diff_octa_grid(3,3,-1,PURPLE)
        diff_octa_top = diff_octa_grid(3,3,1,PURPLE)
        diff_octa_bot = diff_octa_grid(3,3,-2,PURPLE)
        diff_octas = Group(diff_octa_mid1,diff_octa_mid2,diff_octa_top,diff_octa_bot).set_opacity(0)
        

        self.wait()
        frame.add_updater(lambda m, dt: m.increment_theta(-0.1*dt))
        self.add(axes)

        self.add(make_box_grid(1, 2).scale(0.5))
        self.add(make_ve_dots(GREEN,0.1))
        self.wait(7)
        self.play(frame.animate.scale(1.5))
        
        pos_dots = dot_box_pos(2)
        neg_dots = dot_box_neg(3)
        self.play(
            FadeIn(make_box_grid(3, 2).scale(0.5)),
            FadeIn(pos_dots),
            FadeIn(neg_dots),
        )
        self.wait(5)


        
        self.add(vec_mid_pos, vec_mid_neg, octa_mid)
        self.play(
            tetras_pos.animate.set_opacity(1),
            tetras_neg.animate.set_opacity(1),
            octas.animate.set_opacity(1),
        )
        self.wait(5)

        self.add(diff_octas)
        self.play(
            diff_octas.animate.set_opacity(1)
        )
        self.wait(5)
        self.remove(diff_octas,tetras_neg, octas)
        self.play(
            diff_octas.animate.set_opacity(0),
            tetras_neg.animate.set_opacity(0),
            octas.animate.set_opacity(0),
        )
        self.wait(5)
        self.remove(diff_octas,tetras_neg, octas)

        self.play(
            tetras_pos.animate.set_opacity(0),
        )
        self.remove(tetras_pos)
       
        self.add(tetras_neg) 
        self.play(
            tetras_neg.animate.set_opacity(1),
        )
        self.wait(5)
        self.play(
            tetras_neg.animate.set_opacity(0),
        )
        self.remove(tetras_neg)
        self.add(octas)
        self.play(
            octas.animate.set_opacity(1),
        )
        self.wait(5)
        self.remove(octas)
        self.play(
            octas.animate.set_opacity(0),
        )
        self.remove(octas)

        self.add(diff_octas)
        self.play(
            diff_octas.animate.set_opacity(1)
        )
        self.wait(5)

        self.add(vec_mid_pos, vec_mid_neg, octa_mid)
        self.play(
            tetras_pos.animate.set_opacity(1),
            tetras_neg.animate.set_opacity(1),
            octas.animate.set_opacity(1),
        )
        self.wait(20)
        

        # self.add(octa_top, octa_bot, vec_top_pos, vec_bot_pos, vec_top_neg, vec_bot_neg)
        # self.play(
        #     octa_top.animate.set_opacity(1),
        #     octa_bot.animate.set_opacity(1),
        #     vec_top_pos.animate.set_opacity(1),
        #     vec_bot_pos.animate.set_opacity(1),
        #     vec_top_neg.animate.set_opacity(1),
        #     vec_bot_neg.animate.set_opacity(1),
        # )

        # self.wait(3)
        # self.remove(octa_top, octa_mid, octa_bot, vec_top_neg, vec_mid_neg, vec_bot_neg)
        # self.play(
        #     octa_top.animate.set_opacity(0),
        #     octa_mid.animate.set_opacity(0),
        #     octa_bot.animate.set_opacity(0),
        #     vec_top_neg.animate.set_opacity(0),
        #     vec_mid_neg.animate.set_opacity(0),
        #     vec_bot_neg.animate.set_opacity(0),
        # )
        # self.wait(3)
        # self.remove(vec_top_neg, vec_mid_neg, vec_bot_neg)
        # self.play(
        #     vec_top_neg.animate.set_opacity(0),
        #     vec_mid_neg.animate.set_opacity(0),
        #     vec_bot_neg.animate.set_opacity(0),
        # )
        # self.add(vec_top_pos, vec_mid_pos, vec_bot_pos)
        # self.play(
        #     vec_top_pos.animate.set_opacity(1),
        #     vec_mid_pos.animate.set_opacity(1),
        #     vec_bot_pos.animate.set_opacity(1),
        # )
        # self.wait(3)
        # self.remove(vec_top_pos, vec_mid_pos, vec_bot_pos)
        # self.play(
        #     vec_top_pos.animate.set_opacity(0),
        #     vec_mid_pos.animate.set_opacity(0),
        #     vec_bot_pos.animate.set_opacity(0),
        # )
        # self.add(octa_top, octa_mid, octa_bot)
        # self.play(
        #     octa_top.animate.set_opacity(1),
        #     octa_mid.animate.set_opacity(1),
        #     octa_bot.animate.set_opacity(1),
        # )


### CURRENTLY WORKING ON

class NewDotGrid(Scene):
    def construct(self):
        def _ensure_drawable(m):
        # Only for vectorized objects
            from manimlib.mobject.types.vectorized_mobject import VMobject
            if isinstance(m, VMobject):
                pts = m.get_points()
                if pts is None or len(pts) == 0 or np.isnan(pts).any():
                    # Place a single degenerate point; prevents ModernGL from choking
                    m.set_points(np.zeros((1, 3)))
            return m
        sphere_size = 0.1
        frame = self.camera.frame
        frame.scale(1.8)

        axes = ThreeDAxes(
            x_range = (-5,5,1),
            y_range = (-5,5,1),
            z_range = (-5,5,1),
        ).apply_depth_test()
        axes_neg = ThreeDAxes(
            x_range = (-5,5,1),
            y_range = (-5,5,1),
            z_range = (-5,5,1),
        ).apply_depth_test().move_to([0.5,-0.5,0]).set_color(GREY)

        
        x_label_pos = Tex("(+1,-8)").scale(0.7).next_to([5,0,0],RIGHT).apply_depth_test()
        y_label_pos = Tex("(+4,-5)").scale(0.7).next_to([0,5,0],LEFT).apply_depth_test()
        x_label_neg = Tex("(+8,-1)").scale(0.7).next_to([-4.5,-0.5,0],LEFT).apply_depth_test()
        y_label_neg = Tex("(+5,-4)").scale(0.7).next_to([0.5,-5.5,0],RIGHT).apply_depth_test()

        pos_xy_plane = _ensure_drawable(dot_plane_pos(5,5,0,"xy").apply_depth_test())
        neg_xy_plane = _ensure_drawable(dot_plane_neg(5,5,0,"xy").apply_depth_test())

        dia_plane_pos_xy = diamond_plane_pos(5,5,0,"xy")
        dia_plane_neg_xy = diamond_plane_neg(5,5,0,"xy")
        num_grid_pos_xy = generate_number_grid_pos(5,5,0,"xy",9)
        num_grid_neg_xy = generate_number_grid_neg(5,5,0,"xy",2)

        self.play(
            FadeIn(dia_plane_pos_xy),
            FadeIn(dia_plane_neg_xy),
            FadeIn(num_grid_pos_xy),
            FadeIn(num_grid_neg_xy),
        )
        self.wait()
        self.play(
            FadeIn(axes.x_axis),
            FadeIn(axes.y_axis),
            FadeIn(x_label_pos),
            FadeIn(y_label_pos),
        )
        self.wait()
        self.play(
            FadeOut(axes.x_axis),
            FadeOut(axes.y_axis),
            FadeOut(x_label_pos),
            FadeOut(y_label_pos),
        )
        self.wait()
        self.play(
            FadeIn(axes_neg.x_axis),
            FadeIn(axes_neg.y_axis),
            FadeIn(x_label_neg),
            FadeIn(y_label_neg),
        )
        self.wait()
        self.play(
            FadeIn(axes.x_axis),
            FadeIn(axes.y_axis),
            FadeIn(x_label_pos),
            FadeIn(y_label_pos),
        )
        self.wait()

        plane_xy = ParametricSurface(
            lambda u,v: np.array([v,u,0]),
            u_range=(-4.5,4.5),
            v_range=(-4.5,4.5),
            resolution=(12, 12),   
        ).set_color(GREY).set_opacity(0.9).apply_depth_test()
        plane_xz = ParametricSurface(
            lambda u,v: np.array([u,0,v]),
            u_range=(-4.5,4.5),
            v_range=(-4.5,4.5),
            resolution=(12, 12),   
        ).set_color(GREY).set_opacity(0.9).apply_depth_test()
        plane_yz = ParametricSurface(
            lambda u,v: np.array([0,u,v]),
            u_range=(-4.5,4.5),
            v_range=(-4.5,4.5),
            resolution=(12, 12),   
        ).set_color(GREY).set_opacity(0.9).apply_depth_test()

        self.play(
            FadeOut(dia_plane_pos_xy),
            FadeOut(dia_plane_neg_xy),
            FadeOut(num_grid_pos_xy),
            FadeOut(num_grid_neg_xy),
            FadeOut(axes_neg.x_axis),
            FadeOut(axes_neg.y_axis),
            FadeOut(x_label_neg),
            FadeOut(y_label_neg),
            FadeIn(pos_xy_plane),
            FadeIn(neg_xy_plane),
            FadeIn(plane_xy),
        )

        self.wait()
        self.play(frame.animate.reorient(30,60))
        self.wait()

        z_label_pos = Tex("(+2,-7)").scale(0.7).next_to([0,0,5],RIGHT).rotate(PI/2,RIGHT).apply_depth_test()

        self.play(
            FadeIn(z_label_pos),
            FadeIn(axes.z_axis)
        )
        self.wait()

        pos_xz_plane = _ensure_drawable(dot_plane_pos(5,5,0,"xz")).apply_depth_test()
        neg_xz_plane = _ensure_drawable(dot_plane_neg(5,5,0,"xz")).apply_depth_test()

        self.play(
            FadeIn(pos_xz_plane),
            FadeIn(neg_xz_plane),
            FadeIn(plane_xz),
        )
        self.wait()

        pos_yz_plane = _ensure_drawable(dot_plane_pos(5,5,0,"yz").apply_depth_test())
        neg_yz_plane = _ensure_drawable(dot_plane_neg(5,5,0,"yz").apply_depth_test())

        self.play(
            FadeIn(pos_yz_plane),
            FadeIn(neg_yz_plane),
            FadeIn(plane_yz),
        )
        self.wait()
        
        def make_planes(offset, color, plane):
            if plane == "xy":
                back = ParametricSurface(
                    lambda u,v: np.array([v,u,offset]),
                    u_range=(-4.5,4.5),
                    v_range=(-4.5,4.5),
                    resolution=(12, 12),   
                ).set_color(color).set_opacity(0.9).apply_depth_test()
            if plane == "xz":
                back = ParametricSurface(
                    lambda u,v: np.array([v,offset,u]),
                    u_range=(-4.5,4.5),
                    v_range=(-4.5,4.5),
                    resolution=(12, 12),   
                ).set_color(color).set_opacity(0.9).apply_depth_test()
            if plane == "yz":
                back = ParametricSurface(
                    lambda u,v: np.array([offset,v,u]),
                    u_range=(-4.5,4.5),
                    v_range=(-4.5,4.5),
                    resolution=(12, 12),   
                ).set_color(color).set_opacity(0.9).apply_depth_test()
            return back

        frame.add_updater(lambda m, dt: m.increment_theta(-0.1*dt)) 

        self.remove(pos_xy_plane,neg_xy_plane,plane_xy)
        for i in range(1,5):
            plane = dot_plane_pos(5,5,i,"xy").apply_depth_test()
            negs = dot_plane_neg(5,5,i,"xy").apply_depth_test()
            back = make_planes(i, GREY,"xy")
            self.add(plane,back,negs)
            self.wait()
            self.remove(plane,back,negs)
        for i in range(-4,0):
            plane = dot_plane_pos(5,5,i,"xy")
            negs = dot_plane_neg(5,5,i,"xy").apply_depth_test()
            back = make_planes(i, GREY,"xy")
            self.add(plane,back,negs)
            self.wait()
            self.remove(plane,back,negs)
        self.add(pos_xy_plane,neg_xy_plane,plane_xy)

        self.wait()
        self.remove(pos_yz_plane,neg_yz_plane,plane_yz)
        for i in range(1,5):
            plane = dot_plane_pos(5,5,i,"yz").apply_depth_test()
            negs = dot_plane_neg(5,5,i,"yz").apply_depth_test()
            back = make_planes(i, GREY, "yz")
            self.add(plane,back,negs)
            self.wait()
            self.remove(plane,back,negs)
        for i in range(-4,0):
            plane = dot_plane_pos(5,5,i,"yz")
            negs = dot_plane_neg(5,5,i,"yz").apply_depth_test()
            back = make_planes(i, GREY,"yz")
            self.add(plane,back,negs)
            self.wait()
            self.remove(plane,back,negs)
        self.add(pos_yz_plane,neg_yz_plane,plane_yz)
                
        self.wait()
        self.remove(pos_xz_plane,neg_xz_plane,plane_xz)
        for i in range(1,5):
            plane = dot_plane_pos(5,5,i,"xz").apply_depth_test()
            negs = dot_plane_neg(5,5,i,"xz").apply_depth_test()
            back = make_planes(i, GREY, "xz")
            self.add(plane,back,negs)
            self.wait()
            self.remove(plane,back,negs)
        for i in range(-4,0):
            plane = dot_plane_pos(5,5,i,"xz")
            negs = dot_plane_neg(5,5,i,"xz").apply_depth_test()
            back = make_planes(i, GREY,"xz")
            self.add(plane,back,negs)
            self.wait()
            self.remove(plane,back,negs)
        self.add(pos_xz_plane,neg_xz_plane,plane_xz)

        pos_dot_planes_xy = Group()
        pos_dot_planes_xz = Group()
        pos_dot_planes_yz = Group()
        neg_dot_planes_xy = Group()
        neg_dot_planes_xz = Group()
        neg_dot_planes_yz = Group()
        the_planes_xy = Group()
        the_planes_xz = Group()
        the_planes_yz = Group()
        for i in range(-4,5):
            pos_dot_planes_xy.add(_ensure_drawable(dot_plane_pos(5,5,i,"xy").apply_depth_test()))
            pos_dot_planes_xz.add(_ensure_drawable(dot_plane_pos(5,5,i,"xz").apply_depth_test()))
            pos_dot_planes_yz.add(_ensure_drawable(dot_plane_pos(5,5,i,"yz").apply_depth_test()))

            neg_dot_planes_xy.add(_ensure_drawable(dot_plane_neg(5,5,i,"xy").apply_depth_test()))
            neg_dot_planes_xz.add(_ensure_drawable(dot_plane_neg(5,5,i,"xz").apply_depth_test()))
            neg_dot_planes_yz.add(_ensure_drawable(dot_plane_neg(5,5,i,"yz").apply_depth_test()))
        
            the_planes_xy.add(make_planes(i,GREY,"xy"))
            the_planes_xz.add(make_planes(i,GREY,"xz"))
            the_planes_yz.add(make_planes(i,GREY,"yz"))
        self.wait()
        self.play(
            # FadeOut(plane_xy),
            # FadeOut(plane_xz),
            # FadeOut(plane_yz),
            FadeOut(pos_xy_plane),
            FadeOut(pos_xz_plane),
            FadeOut(neg_xy_plane),
            FadeOut(neg_xz_plane),

        )
        self.wait()

        frame.suspend_updating()

        self.play(

            FadeIn(pos_dot_planes_yz[3]),
            FadeIn(pos_dot_planes_yz[5]),
            FadeIn(neg_dot_planes_yz[3]),
            FadeIn(neg_dot_planes_yz[5]),
        )
        self.wait()

        self.play(
            FadeIn(pos_dot_planes_yz[2]),
            FadeIn(pos_dot_planes_yz[6]),
            FadeIn(neg_dot_planes_yz[2]),
            FadeIn(neg_dot_planes_yz[6]),
        )
        self.wait()
        
        self.play(
            FadeIn(pos_dot_planes_yz[1]),
            FadeIn(pos_dot_planes_yz[7]),
            FadeIn(neg_dot_planes_yz[1]),
            FadeIn(neg_dot_planes_yz[7]),
        )
        self.wait()

        self.play(
            FadeIn(pos_dot_planes_yz[0]),
            FadeIn(pos_dot_planes_yz[8]),
            FadeIn(neg_dot_planes_yz[0]),
            FadeIn(neg_dot_planes_yz[8]),
        )
        self.wait()

        frame.resume_updating()
        self.wait(7)
        frame.suspend_updating()

        self.wait()
        ex_plane_xy = make_planes(4,GREY,"xy")
        ex_plane_xz = make_planes(4,GREY,"xz")
        self.play(FadeIn(ex_plane_xy))
        self.wait()
        self.play(FadeIn(ex_plane_xz))
        self.wait()
        self.play(
            FadeOut(ex_plane_xy),
            FadeOut(ex_plane_xz),
        )
        self.wait()
        self.play(frame.animate.reorient(90,90))
        self.wait()
        self.play(FadeIn(the_planes_yz[8]))
        self.remove(plane_yz,plane_xy,plane_xz)
        self.wait(0.4)
        for i in range(0,8):
            self.remove(the_planes_yz[8-i])
            self.add(the_planes_yz[(8-i)-1])
            self.wait(0.4)
        self.remove(the_planes_yz[0])
        self.wait()
        self.play(
            FadeIn(the_planes_xz)
        )

        the_neg_planes_xy = Group()
        the_neg_planes_xz = Group()
        the_neg_planes_yz = Group()
        for i in range(-4,4):
            the_neg_planes_xy.add(make_planes(i+0.5,BLACK,"xy"))
            the_neg_planes_xz.add(make_planes(i+0.5,BLACK,"xz"))
            the_neg_planes_yz.add(make_planes(i+0.5,BLACK,"yz"))
        self.wait()
        self.play(
            FadeIn(the_neg_planes_xz)
        )
        self.wait()
        frame.resume_updating()
        self.wait(20)
        self.play(
            FadeOut(the_planes_xz),
            FadeOut(the_neg_planes_xz),
            FadeIn(the_planes_yz),
            FadeIn(the_neg_planes_yz),
        )
        self.wait(10)
        frame.suspend_updating()
        self.wait()
        self.play(frame.animate.reorient(30,60))
        self.wait()
        self.add(plane_yz)
        self.play(
            FadeOut(the_planes_yz),
            FadeOut(the_neg_planes_yz),
            FadeIn(plane_xy),
            FadeIn(plane_xz),
        )
        self.wait()
        for i in range(-4,5):
            self.add(neg_dot_planes_xz[i+4])
            if i < 4:
                self.add(the_neg_planes_xz[i+4])
            self.wait(0.4)
            if i < 4:
                self.remove(the_neg_planes_xz[i+4])
        self.wait()
        for i in range(-4,5):
            self.add(neg_dot_planes_xy[i+4])
            if i < 4:
                self.add(the_neg_planes_xy[i+4])
            self.wait(0.4)
            if i < 4:
                self.remove(the_neg_planes_xy[i+4])
        self.wait()
        

        self.remove(neg_yz_plane)
        self.play(
            FadeOut(neg_dot_planes_xy),
            FadeOut(neg_dot_planes_xz),
            FadeOut(neg_dot_planes_yz),
        )
        self.wait(5)

        pos_grid = Group()
        for j in range(-4,5):
            for i in range(-4,5):
                pos_grid.add(
                    Line([i,-4,j],[i,4,j], stroke_width = 2),
                )
            for i in range(-4,5):
                pos_grid.add(
                    Line([-4,i,j],[4,i,j], stroke_width = 2),
                )
            for i in range(-4,4):
                pos_grid.add(
                    Line([i,j,-4],[i,j,4], stroke_width = 2),
                )
        self.play(
            FadeIn(pos_grid),
            FadeOut(plane_xy),
            FadeOut(plane_xz),
            FadeOut(plane_yz),
        )
        self.wait()



        neg_grid_1 = Group()
        for j in range(-4,5):
            for i in range(-4,4):
                neg_grid_1.add(
                    Line([-3.5,i+0.5,j],[3.5,i+0.5,j], stroke_width = 2).set_color(TEAL),
                )
            for i in range(-4,4):
                neg_grid_1.add(
                    Line([i+0.5,-3.5,j],[i+0.5,3.5,j], stroke_width = 2).set_color(TEAL),
                )
            for i in range(-4,4):
                if j < 4:
                    neg_grid_1.add(
                        Line([i+0.5,j+0.5,-4],[i+0.5,j+0.5,4], stroke_width = 2).set_color(TEAL),
                    )
        frame.resume_updating()
        self.play(
            FadeOut(pos_dot_planes_yz),
            FadeOut(pos_grid),
            FadeOut(pos_yz_plane),
            FadeIn(neg_dot_planes_xy),
            FadeIn(neg_grid_1),
        )
        self.wait(5)

        neg_grid_2 = Group()
        for j in range(-4,5):
            for i in range(-4,4):
                if j < 4:
                    neg_grid_2.add(
                        Line([i+0.5,4,j+0.5],[i+0.5,-4,j+0.5], stroke_width = 2).set_color(YELLOW),
                    )
            for i in range(-4,4):
                neg_grid_2.add(
                    Line([-3.5,j,i+0.5],[3.5,j,i+0.5], stroke_width = 2).set_color(YELLOW),
                )
            for i in range(-4,5):
                if j < 4:
                    neg_grid_2.add(
                        Line([j+0.5,i,-3.5],[j+0.5,i,3.5], stroke_width = 2).set_color(YELLOW),
                    )
        self.play(
            FadeOut(neg_grid_1),
            FadeOut(neg_dot_planes_xy),
            FadeIn(neg_dot_planes_xz),
            FadeIn(neg_grid_2),
        )
        self.wait(5)

        neg_grid_3 = Group()
        for j in range(-4,4):
            for i in range(-4,4):
                neg_grid_3.add(
                    Line([-4,i+0.5,j+0.5],[4,i+0.5,j+0.5], stroke_width = 2).set_color(PINK),
                )
            for i in range(-4,5):
                neg_grid_3.add(
                    Line([i,-3.5,j+0.5],[i,3.5,j+0.5], stroke_width = 2).set_color(PINK),
                )
            for i in range(-4,5):
                neg_grid_3.add(
                    Line([i,j+0.5,-3.5],[i,j+0.5,3.5], stroke_width = 2).set_color(PINK),
                )
        self.play(
            FadeOut(neg_grid_2),
            FadeOut(neg_dot_planes_xz),
            FadeIn(neg_dot_planes_yz),
            FadeIn(neg_grid_3),
        )
        self.wait()
        self.play(
            FadeIn(pos_grid),
            FadeOut(neg_grid_3),

            FadeIn(pos_dot_planes_yz),
            FadeIn(neg_dot_planes_xy),
            FadeIn(neg_dot_planes_xz),
            FadeIn(neg_dot_planes_yz),
        )
        self.wait(3)
        self.play(
            FadeOut(pos_grid),
            FadeIn(neg_grid_1),
        )
        self.wait(3)
        self.play(
            FadeOut(neg_grid_1),
            FadeIn(neg_grid_2),
        )
        self.wait(3)
        self.play(
            FadeOut(neg_grid_2),
            FadeIn(neg_grid_3),
        )
        self.wait(3)
        self.play(FadeOut(neg_grid_3))
        frame.suspend_updating()
        self.wait()
        self.play(frame.animate.reorient(30,60))
        self.wait(2)
        
        for i in range(-4,5):
            self.add(pos_dot_planes_xy[i+4])
            if i < 4:
                self.add(the_planes_xy[i+4])
            self.wait(0.4)
            if i < 4:
                self.remove(the_planes_xy[i+4])

            self.add(neg_dot_planes_xy[i+4])
            if i < 4:
                self.add(the_neg_planes_xy[i+4])
            self.wait(0.4)
            if i < 4:
                self.remove(the_neg_planes_xy[i+4])
        self.wait()









                




            # FadeIn(neg_dot_planes_xy),
            # FadeIn(neg_dot_planes_xz),
            # FadeIn(neg_dot_planes_yz),




        xy_planes = Group()
        xz_planes = Group()
        yz_planes = Group()
        
        # for i in range(-4,5):
        #     xy_guy = _ensure_drawable(make_planes(i, GREY, "xy"))
        #     xy_planes.add(xy_guy)
        # for i in range(-4,5):
        #     xz_guy = _ensure_drawable(make_planes(i, GREY, "xz"))
        #     xz_planes.add(make_planes(i, GREY, "xz"))
        # for i in range(-4,5):
        #     yz_guy = _ensure_drawable(make_planes(i, GREY, "yz"))
        #     yz_planes.add(make_planes(i, GREY, "yz"))  
        
        # self.wait()
        # self.play(FadeIn(xy_planes))

        


        # dub_xy = doubling_curve_xyz(5,0,"xy").apply_depth_test()
        # dub_xz = doubling_curve_xyz(5,0,"xz").apply_depth_test()
        # dub_yz = doubling_curve_xyz(5,0,"yz").apply_depth_test()
        # self.add(dub_xy)
        # self.add(dub_xz)
        # self.add(dub_yz)

class CubeDot(Scene):
  
    def construct(self):
        sphere_size = 0.1
        frame = self.camera.frame
        frame.scale(1.8)
        frame.reorient(120,60)

        axes = ThreeDAxes().apply_depth_test()
        def make_planes(offset, color, plane):
            if plane == "xy":
                back = ParametricSurface(
                    lambda u,v: np.array([v,u,offset]),
                    u_range=(-4.5,4.5),
                    v_range=(-4.5,4.5),
                    resolution=(12, 12),   
                ).set_color(color).set_opacity(1).apply_depth_test()
            if plane == "xz":
                back = ParametricSurface(
                    lambda u,v: np.array([v,offset,u]),
                    u_range=(-4.5,4.5),
                    v_range=(-4.5,4.5),
                    resolution=(12, 12),   
                ).set_color(color).set_opacity(1).apply_depth_test()
            if plane == "yz":
                back = ParametricSurface(
                    lambda u,v: np.array([offset,v,u]),
                    u_range=(-4.5,4.5),
                    v_range=(-4.5,4.5),
                    resolution=(12, 12),   
                ).set_color(color).set_opacity(1).apply_depth_test()
            return back
    # --- helpers ---
        A, B = -4.5, 4.5
        SPAN = B - A  # 9.0

        def wrap_scalar(t):
            # wrap into [-4.5, 4.5)
            return ((t - A) % SPAN) + A

        def seg(p0, p1, color=YELLOW, w=10):
            return Line(p0, p1).set_stroke(width=w).set_color(color).apply_depth_test()

        # Build a toroidal trace along a given axis for an unwrapped tracker "t".
        # axis_dir is a unit vector (e.g., RIGHT, UP, OUT) telling us which axis.
        # origin is where "0" lives for that axis.
        def make_axis_trace(t, axis_dir, origin=np.array([0,0,0]), color=YELLOW):
            wrapped = wrap_scalar(t)

            # points on that axis: origin + s * axis_dir
            def P(s): return origin + s * axis_dir

            if -4.5 <= t <= 4.5:
                # single segment from 0 to t (direction handled automatically)
                return seg(P(0), P(t), color)
            elif t > 4.5:
                # crossed the +cut: keep [0, 4.5] + extra [-4.5, wrapped]
                return VGroup(
                    seg(P(0),   P(4.5), color),
                    seg(P(-4.5), P(wrapped), color),
                )
            else:  # t < -4.5
                # crossed the -cut: keep [-4.5, 0] + extra [wrapped, 4.5]
                return VGroup(
                    seg(P(-4.5), P(0), color),
                    seg(P(wrapped), P(4.5), color),
                )

        # --- your builders keeping your variable names/style for x ---
        def make_x_line():
            t = x_tracker.get_value()
            return make_axis_trace(t, RIGHT, origin=np.array([0,0,0]), color=YELLOW)

        def make_y_line():
            t = y_tracker.get_value()
            # y-axis goes "up"; origin at (0,0,0)
            return make_axis_trace(t, UP, origin=np.array([wrap_scalar(x_tracker.get_value()),0,0]), color=YELLOW)

        def make_z_line():
            t = z_tracker.get_value()
            # z-axis goes "out of screen"; origin at (0,0,0)
            return make_axis_trace(t, OUT, origin=np.array([wrap_scalar(x_tracker.get_value()),wrap_scalar(y_tracker.get_value()),0]), color=YELLOW)

        pos_dot_planes_xy = Group()
        pos_dot_planes_xz = Group()
        pos_dot_planes_yz = Group()
        neg_dot_planes_xy = Group()
        neg_dot_planes_xz = Group()
        neg_dot_planes_yz = Group()
        the_planes_xy = Group()
        the_planes_xz = Group()
        the_planes_yz = Group()
        for i in range(-4,5):
            pos_dot_planes_xy.add(dot_plane_pos(5,5,i,"xy").apply_depth_test())
            pos_dot_planes_xz.add(dot_plane_pos(5,5,i,"xz").apply_depth_test())
            pos_dot_planes_yz.add(dot_plane_pos(5,5,i,"yz").apply_depth_test())

            neg_dot_planes_xy.add(dot_plane_neg(5,5,i,"xy").apply_depth_test())
            neg_dot_planes_xz.add(dot_plane_neg(5,5,i,"xz").apply_depth_test())
            neg_dot_planes_yz.add(dot_plane_neg(5,5,i,"yz").apply_depth_test())
        
            the_planes_xy.add(make_planes(i,GREY,"xy"))
            the_planes_xz.add(make_planes(i,GREY,"xz"))
            the_planes_yz.add(make_planes(i,GREY,"yz"))

        self.add(
            axes,
            pos_dot_planes_xy[4],
            neg_dot_planes_xy[4],
            the_planes_xy[4],
        )

        corner_group = Group()
        for plane in pos_dot_planes_xy:
            for dot in plane:
                if dot.get_center()[0] > 0 and dot.get_center()[1] > 0 and dot.get_center()[2] > 0:
                    corner_group.add(dot)
        for plane in neg_dot_planes_xy:
            for dot in plane:
                if dot.get_center()[0] > 0 and dot.get_center()[1] > 0 and dot.get_center()[2] > 0:
                    corner_group.add(dot)
        for plane in neg_dot_planes_xz:
            for dot in plane:
                if dot.get_center()[0] > 0 and dot.get_center()[1] > 0 and dot.get_center()[2] > 0:
                    corner_group.add(dot)
        for plane in neg_dot_planes_yz:
            for dot in plane:
                if dot.get_center()[0] > 0 and dot.get_center()[1] > 0 and dot.get_center()[2] > 0:
                    corner_group.add(dot)
        
        self.wait()

        x_tracker = ValueTracker(0)
        y_tracker = ValueTracker(0)
        z_tracker = ValueTracker(0)


        yellow_dot = always_redraw(lambda:
            Sphere(radius = sphere_size+0.05, resolution = (30,30)).set_color(YELLOW).move_to(
                [
                    wrap_scalar(x_tracker.get_value()), 
                    wrap_scalar(y_tracker.get_value()),
                    wrap_scalar(z_tracker.get_value()),
                ])
            ).apply_depth_test()
        
        yellow_x = always_redraw(make_x_line)
        yellow_y = always_redraw(make_y_line)
        yellow_z = always_redraw(make_z_line)
        self.play(
            the_planes_xy[4].animate.set_opacity(0.8),
            # the_planes_xz[4].animate.set_opacity(0.8),
            # the_planes_yz[4].animate.set_opacity(0.8),
            FadeIn(yellow_dot),
            FadeIn(yellow_x),
            FadeIn(yellow_y),
            FadeIn(yellow_z),
        )
        self.wait()
        self.play(x_tracker.animate.set_value(3.0))
        self.wait()
        self.play(y_tracker.animate.set_value(3.0))
        self.wait()

        the_planes_yz.set_opacity(0.8)
        the_planes_xz.set_opacity(0.8)
        self.play(
            FadeIn(pos_dot_planes_yz[7]),
            FadeIn(neg_dot_planes_yz[7]),
            FadeIn(the_planes_yz[7])
        )
        self.wait()

        self.play(
            z_tracker.animate.set_value(3.0)
        )
        self.wait()
        
        self.play(
            FadeIn(pos_dot_planes_xz[7]),
            FadeIn(neg_dot_planes_xz[7]),
            FadeIn(the_planes_xz[7])
        )
        self.wait()

        self.wait()
        
        self.play(
            FadeOut(pos_dot_planes_yz[7]),
            FadeOut(neg_dot_planes_yz[7]),
            FadeOut(the_planes_yz[7]),

            FadeOut(pos_dot_planes_xz[7]),
            FadeOut(neg_dot_planes_xz[7]),
            FadeOut(the_planes_xz[7]),

            x_tracker.animate.set_value(0.0),
            y_tracker.animate.set_value(0.0),
            z_tracker.animate.set_value(0.0),
        )
        self.wait()

        self.play(
            FadeIn(pos_dot_planes_xz[4]),
            FadeIn(neg_dot_planes_xz[4]),
            FadeIn(pos_dot_planes_yz[4]),
            FadeIn(neg_dot_planes_yz[4]),
            FadeIn(the_planes_xz[4]),
            FadeIn(the_planes_yz[4]),
        )
        self.wait()

        self.play(x_tracker.animate.set_value(9.0),run_time=2)
        self.wait()
        self.play(y_tracker.animate.set_value(9.0),run_time=2)
        self.wait()
        self.play(z_tracker.animate.set_value(9.0),run_time=2)
        self.wait(3)

        self.play(
            x_tracker.animate.set_value(0.0),
            y_tracker.animate.set_value(0.0),
            z_tracker.animate.set_value(0.0),
            run_time=2,
        )
        self.wait(3)
        self.play(
            FadeIn(pos_dot_planes_xy[:4]+pos_dot_planes_xy[5:]),
            FadeIn(neg_dot_planes_xy[:4]+neg_dot_planes_xy[5:]),
            FadeIn(neg_dot_planes_xz[:4]+neg_dot_planes_xz[5:]),
            FadeIn(neg_dot_planes_yz[:4]+pos_dot_planes_yz[5:]),
        )

        toroid_planes_xy = Group(
            ParametricSurface(
                lambda u,v: np.array([v,u,-4.5]),
                u_range=(-4.5,4.5),
                v_range=(-4.5,4.5),
                resolution=(12, 12),   
            ).set_color(YELLOW).set_opacity(0.8).apply_depth_test(),
            ParametricSurface(
                lambda u,v: np.array([v,u,4.5]),
                u_range=(-4.5,4.5),
                v_range=(-4.5,4.5),
                resolution=(12, 12),   
            ).set_color(YELLOW).set_opacity(0.8).apply_depth_test(),
        )
        toroid_planes_xz = Group(
            ParametricSurface(
                lambda u,v: np.array([v,-4.5,u]),
                u_range=(-4.5,4.5),
                v_range=(-4.5,4.5),
                resolution=(12, 12),   
            ).set_color(YELLOW).set_opacity(0.8).apply_depth_test(),
            ParametricSurface(
                lambda u,v: np.array([v,4.5,u]),
                u_range=(-4.5,4.5),
                v_range=(-4.5,4.5),
                resolution=(12, 12),   
            ).set_color(YELLOW).set_opacity(0.8).apply_depth_test(),
        )
        toroid_planes_yz = Group(
            ParametricSurface(
                lambda u,v: np.array([-4.5,v,u]),
                u_range=(-4.5,4.5),
                v_range=(-4.5,4.5),
                resolution=(12, 12),   
            ).set_color(YELLOW).set_opacity(0.8).apply_depth_test(),
            ParametricSurface(
                lambda u,v: np.array([4.5,v,u]),
                u_range=(-4.5,4.5),
                v_range=(-4.5,4.5),
                resolution=(12, 12),   
            ).set_color(YELLOW).set_opacity(0.8).apply_depth_test(),
        )
        self.wait()
        self.play(FadeIn(toroid_planes_yz))
        self.play(FadeOut(toroid_planes_yz))

        self.wait()
        self.play(FadeIn(toroid_planes_xz))
        self.play(FadeOut(toroid_planes_xz))

        self.wait()
        self.play(FadeIn(toroid_planes_xy))
        self.play(FadeOut(toroid_planes_xy))

        self.wait(3)




class DotGridBreakdown(Scene):
    def construct(self):
        sphere_size = 0.1
        frame = self.camera.frame
        frame.scale(1.8)
        frame.reorient(120,60)

        def make_planes(offset, color, plane):
            if plane == "xy":
                back = ParametricSurface(
                    lambda u,v: np.array([v,u,offset]),
                    u_range=(-4.5,4.5),
                    v_range=(-4.5,4.5),
                    resolution=(12, 12),   
                ).set_color(color).set_opacity(1).apply_depth_test()
            if plane == "xz":
                back = ParametricSurface(
                    lambda u,v: np.array([v,offset,u]),
                    u_range=(-4.5,4.5),
                    v_range=(-4.5,4.5),
                    resolution=(12, 12),   
                ).set_color(color).set_opacity(1).apply_depth_test()
            if plane == "yz":
                back = ParametricSurface(
                    lambda u,v: np.array([offset,v,u]),
                    u_range=(-4.5,4.5),
                    v_range=(-4.5,4.5),
                    resolution=(12, 12),   
                ).set_color(color).set_opacity(1).apply_depth_test()
            return back

        pos_dot_planes_xy = Group()
        pos_dot_planes_xz = Group()
        pos_dot_planes_yz = Group()
        neg_dot_planes_xy = Group()
        neg_dot_planes_xz = Group()
        neg_dot_planes_yz = Group()
        the_planes_xy = Group()
        the_planes_xz = Group()
        the_planes_yz = Group()
        for i in range(-4,5):
            pos_dot_planes_xy.add(dot_plane_pos(5,5,i,"xy").apply_depth_test())
            pos_dot_planes_xz.add(dot_plane_pos(5,5,i,"xz").apply_depth_test())
            pos_dot_planes_yz.add(dot_plane_pos(5,5,i,"yz").apply_depth_test())

            neg_dot_planes_xy.add(dot_plane_neg(5,5,i,"xy").apply_depth_test())
            neg_dot_planes_xz.add(dot_plane_neg(5,5,i,"xz").apply_depth_test())
            neg_dot_planes_yz.add(dot_plane_neg(5,5,i,"yz").apply_depth_test())
        
            the_planes_xy.add(make_planes(i,GREY,"xy"))
            the_planes_xz.add(make_planes(i,GREY,"xz"))
            the_planes_yz.add(make_planes(i,GREY,"yz"))

        self.add(
            pos_dot_planes_xy,
            neg_dot_planes_xy,
            neg_dot_planes_xz,
            neg_dot_planes_yz,
            the_planes_xy[4],
            the_planes_xz[4],
            the_planes_yz[4],
        )

        corner_group = Group()
        for plane in pos_dot_planes_xy:
            for dot in plane:
                if dot.get_center()[0] > 0 and dot.get_center()[1] > 0 and dot.get_center()[2] > 0:
                    corner_group.add(dot)
        for plane in neg_dot_planes_xy:
            for dot in plane:
                if dot.get_center()[0] > 0 and dot.get_center()[1] > 0 and dot.get_center()[2] > 0:
                    corner_group.add(dot)
        for plane in neg_dot_planes_xz:
            for dot in plane:
                if dot.get_center()[0] > 0 and dot.get_center()[1] > 0 and dot.get_center()[2] > 0:
                    corner_group.add(dot)
        for plane in neg_dot_planes_yz:
            for dot in plane:
                if dot.get_center()[0] > 0 and dot.get_center()[1] > 0 and dot.get_center()[2] > 0:
                    corner_group.add(dot)
        
        self.wait()
        self.play(
            FadeOut(corner_group)
        )
        self.wait()

        dub_xy = doubling_curve_xyz(5,0,"xy")
        dub_xz = doubling_curve_xyz(5,0,"xz")
        dub_yz = doubling_curve_xyz(5,0,"yz")

        self.play(
            ShowCreation(dub_xy.apply_depth_test())
        )
        self.play(
            ShowCreation(dub_xz.apply_depth_test())
        )
        self.play(
            ShowCreation(dub_yz.apply_depth_test())
        )
        self.wait()

        self.play(
            FadeOut(dub_xy),
            FadeOut(dub_xz),
            FadeOut(dub_yz),
        )
        self.play(FadeIn(corner_group))
        self.wait()

        cutting_plane = parametric_square(
            np.array([4,4,4]), 
            np.array([4/np.sqrt(4**2+4**2),-4/np.sqrt(4**2+4**2),0]), 
            np.array([-2/np.sqrt(2**2+2**2+4**2),-2/np.sqrt(2**2+2**2+4**2),4/np.sqrt(2**2+2**2+4**2)]),
            6
        ).set_opacity(1)
        
        def angle_between(v1, v2):
            """
            Returns the angle in radians between vectors v1 and v2.
            v1, v2: array-like
            """
            v1 = np.array(v1, dtype=float)
            v2 = np.array(v2, dtype=float)
            dot = np.dot(v1, v2)
            norm = np.linalg.norm(v1) * np.linalg.norm(v2)
            # clip value inside [-1, 1] to avoid numerical issues
            cos_theta = np.clip(dot / norm, -1.0, 1.0)
            return np.arccos(cos_theta)

        unit_l = np.array([1,1,1]) / np.linalg.norm(np.array([1,1,1]))

        box = Group(
            Line([4,4,4],[-4,4,4]),
            Line([4,4,4],[4,-4,4]),
            Line([4,4,4],[4,4,-4]),
            Line([-4,-4,-4],[4,-4,-4]),
            Line([-4,-4,-4],[-4,4,-4]),
            Line([-4,-4,-4],[-4,-4,4]),

            Line([-4,-4,4],[-4,4,4]),
            Line([-4,-4,4],[4,-4,4]),
            Line([4,-4,4],[4,-4,-4]),
            Line([4,4,-4],[-4,4,-4]),
            Line([4,4,-4],[4,-4,-4]),
            Line([-4,4,-4],[-4,4,4]),

            Line([-4,-4,-4],[4,4,4]).set_color(YELLOW)
        )

        self.wait()
        self.play(
            FadeOut(the_planes_xy[4]),
            FadeOut(the_planes_xz[4]),
            FadeOut(the_planes_yz[4]),
            FadeIn(box.apply_depth_test()),
        )
        self.wait()
        self.play(FadeIn(cutting_plane.set_opacity(0.9)))
        self.wait()

        shapes = Group(
            Group(
                Line([4,3,4],[3,4,4]).set_stroke(width=2),
                Line([4,3,4],[4,4,3]).set_stroke(width=2),
                Line([4,4,3],[3,4,4]).set_stroke(width=2),
            ).set_color(BLUE),
            Group(
                Line([4,2,4],[2,4,4]).set_stroke(width=2),
                Line([4,2,4],[4,4,2]).set_stroke(width=2),
                Line([4,4,2],[2,4,4]).set_stroke(width=2),
            ).set_color(RED),
            Group(
                Line([4,1,4],[1,4,4]).set_stroke(width=2),
                Line([4,1,4],[4,4,1]).set_stroke(width=2),
                Line([4,4,1],[1,4,4]).set_stroke(width=2),
            ).set_color(GREEN),
            Group(
                Line([4,0,4],[0,4,4]).set_stroke(width=2),
                Line([4,0,4],[4,4,0]).set_stroke(width=2),
                Line([4,4,0],[0,4,4]).set_stroke(width=2),
            ).set_color(BLUE),
            Group(
                Line([4,-1,4],[-1,4,4]).set_stroke(width=2),
                Line([4,-1,4],[4,4,-1]).set_stroke(width=2),
                Line([4,4,-1],[-1,4,4]).set_stroke(width=2),
            ).set_color(RED),
            Group(
                Line([4,-2,4],[-2,4,4]).set_stroke(width=2),
                Line([4,-2,4],[4,4,-2]).set_stroke(width=2),
                Line([4,4,-2],[-2,4,4]).set_stroke(width=2),
            ).set_color(GREEN),
            Group(
                Line([4,-3,4],[-3,4,4]).set_stroke(width=2),
                Line([4,-3,4],[4,4,-3]).set_stroke(width=2),
                Line([4,4,-3],[-3,4,4]).set_stroke(width=2),
            ).set_color(BLUE),
            Group(
                Line([4,-4,4],[-4,4,4]).set_stroke(width=2),
                Line([4,-4,4],[4,4,-4]).set_stroke(width=2),
                Line([4,4,-4],[-4,4,4]).set_stroke(width=2),
            ).set_color(RED),

            # 6-sided shapes
            Group(
                Line([4,3,-4],[3,4,-4]).set_stroke(width=2),
                Line([4,-4,3],[4,3,-4]).set_stroke(width=2),

                Line([4,-4,3],[3,-4,4]).set_stroke(width=2),
                Line([-4,3,4],[3,-4,4]).set_stroke(width=2),

                Line([-4,3,4],[-4,4,3]).set_stroke(width=2),
                Line([-4,4,3],[3,4,-4]).set_stroke(width=2),
            ).set_color(GREEN),
            Group(
                Line([4,2,-4],[2,4,-4]).set_stroke(width=2),
                Line([4,-4,2],[4,2,-4]).set_stroke(width=2),

                Line([4,-4,2],[2,-4,4]).set_stroke(width=2),
                Line([-4,2,4],[2,-4,4]).set_stroke(width=2),

                Line([-4,2,4],[-4,4,2]).set_stroke(width=2),
                Line([-4,4,2],[2,4,-4]).set_stroke(width=2),
            ).set_color(BLUE),
            Group(
                Line([4,1,-4],[1,4,-4]).set_stroke(width=2),
                Line([4,-4,1],[4,1,-4]).set_stroke(width=2),

                Line([4,-4,1],[1,-4,4]).set_stroke(width=2),
                Line([-4,1,4],[1,-4,4]).set_stroke(width=2),

                Line([-4,1,4],[-4,4,1]).set_stroke(width=2),
                Line([-4,4,1],[1,4,-4]).set_stroke(width=2),
            ).set_color(RED),
            Group(
                Line([4,0,-4],[0,4,-4]).set_stroke(width=2),
                Line([4,-4,0],[4,0,-4]).set_stroke(width=2),

                Line([4,-4,0],[0,-4,4]).set_stroke(width=2),
                Line([-4,0,4],[0,-4,4]).set_stroke(width=2),

                Line([-4,0,4],[-4,4,0]).set_stroke(width=2),
                Line([-4,4,0],[0,4,-4]).set_stroke(width=2),
            ).set_color(GREEN),
        )

        for i in range(1,13):
            plane_step = (1/3) * i
            plane_length = np.array([(4-plane_step)+0.01,(4-plane_step)+0.01,(4-plane_step)+0.01])
            cutting_plane.move_to(plane_length)
            self.add(shapes[i-1])
            for plane in pos_dot_planes_xy:
                for dot in plane:
                    unit_r = (dot.get_center() - plane_length) / np.linalg.norm(dot.get_center() - plane_length)
                    if angle_between(unit_l,unit_r) < 90*DEGREES:
                        self.remove(dot)
            for plane in neg_dot_planes_xy:
                for dot in plane:
                    unit_r = (dot.get_center() - plane_length) / np.linalg.norm(dot.get_center() - plane_length)
                    if angle_between(unit_l,unit_r) < 90*DEGREES:
                        self.remove(dot)
            for plane in neg_dot_planes_xz:
                for dot in plane:
                    unit_r = (dot.get_center() - plane_length) / np.linalg.norm(dot.get_center() - plane_length)
                    if angle_between(unit_l,unit_r) < 90*DEGREES:
                        self.remove(dot)
            for plane in neg_dot_planes_yz:
                for dot in plane:
                    unit_r = (dot.get_center() - plane_length) / np.linalg.norm(dot.get_center() - plane_length)
                    if angle_between(unit_l,unit_r) < 90*DEGREES:
                        self.remove(dot)

            self.wait(1)
            self.remove(shapes[i-1])
        
        self.add(shapes[11])

        box_div = Group(
            Line([4,0,-4],[4,0,4]),
            Line([4,-4,0],[4,4,0]),
            Line([-4,0,-4],[-4,0,4]),
            Line([-4,-4,0],[-4,4,0]),

            Line([4,-4,0],[-4,-4,0]),
            Line([4,4,0],[-4,4,0]),
            Line([0,4,-4],[0,4,4]),
            Line([0,-4,-4],[0,-4,4]),

            Line([4,0,-4],[-4,0,-4]),
            Line([4,0,4],[-4,0,4]),
            Line([0,-4,4],[0,4,4]),
            Line([0,-4,-4],[0,4,-4]),

        )
        self.play(FadeIn(box_div))

        frame.add_updater(lambda m, dt: m.increment_theta(-0.1*dt)) 

        plane_cascade = Group()
        col = [GREEN,BLUE,RED]
        for i in range(0,24):
            off = (1/3) * i
            if i < 13:
                new_plane = cutting_plane.copy().scale(i/12)
                new_plane.move_to([4-off,4-off,4-off]).set_color(col[i%3])
            if i >= 13:
                new_plane = cutting_plane.copy().scale((13-i%12)/12)
                new_plane.move_to([4-off,4-off,4-off]).set_color(col[i%3])
            plane_cascade.add(new_plane)
        self.wait(10)
        self.play(
            FadeOut(cutting_plane),
        )
        self.add(
            pos_dot_planes_xy,
            neg_dot_planes_xy,
            neg_dot_planes_xz,
            neg_dot_planes_yz,
        )
        self.play(
            FadeIn(plane_cascade),
            FadeIn(pos_dot_planes_xy),
            FadeIn(neg_dot_planes_xy),
            FadeIn(neg_dot_planes_xz),
            FadeIn(neg_dot_planes_yz),
        )
        self.wait(10)

class VectorEquilibrium(Scene):
    def construct(self):
        sphere_size = 0.1
        frame = self.camera.frame
        frame.scale(1.8)
        frame.reorient(120,60)
        axes = ThreeDAxes(
            x_range = (-10,10,1),
            y_range = (-10,10,1),
            z_range = (-10,10,1),
        ).apply_depth_test()
        def make_planes(offset, color, plane):
            if plane == "xy":
                back = ParametricSurface(
                    lambda u,v: np.array([v,u,offset]),
                    u_range=(-4.5,4.5),
                    v_range=(-4.5,4.5),
                    resolution=(12, 12),   
                ).set_color(color).set_opacity(1).apply_depth_test()
            if plane == "xz":
                back = ParametricSurface(
                    lambda u,v: np.array([v,offset,u]),
                    u_range=(-4.5,4.5),
                    v_range=(-4.5,4.5),
                    resolution=(12, 12),   
                ).set_color(color).set_opacity(1).apply_depth_test()
            if plane == "yz":
                back = ParametricSurface(
                    lambda u,v: np.array([offset,v,u]),
                    u_range=(-4.5,4.5),
                    v_range=(-4.5,4.5),
                    resolution=(12, 12),   
                ).set_color(color).set_opacity(1).apply_depth_test()
            return back

        pos_dot_planes_xy = Group()
        pos_dot_planes_xz = Group()
        pos_dot_planes_yz = Group()
        neg_dot_planes_xy = Group()
        neg_dot_planes_xz = Group()
        neg_dot_planes_yz = Group()
        the_planes_xy = Group()
        the_planes_xz = Group()
        the_planes_yz = Group()
        for i in range(-4,5):
            pos_dot_planes_xy.add(dot_plane_pos(5,5,i,"xy").apply_depth_test())
            pos_dot_planes_xz.add(dot_plane_pos(5,5,i,"xz").apply_depth_test())
            pos_dot_planes_yz.add(dot_plane_pos(5,5,i,"yz").apply_depth_test())

            neg_dot_planes_xy.add(dot_plane_neg(5,5,i,"xy").apply_depth_test())
            neg_dot_planes_xz.add(dot_plane_neg(5,5,i,"xz").apply_depth_test())
            neg_dot_planes_yz.add(dot_plane_neg(5,5,i,"yz").apply_depth_test())
        
            the_planes_xy.add(make_planes(i,GREY,"xy")).apply_depth_test()
            the_planes_xz.add(make_planes(i,GREY,"xz")).apply_depth_test()
            the_planes_yz.add(make_planes(i,GREY,"yz")).apply_depth_test()

        self.add(
            pos_dot_planes_xy,
            neg_dot_planes_xy,
            neg_dot_planes_xz,
            neg_dot_planes_yz,
            the_planes_xy[4],
            the_planes_xz[4],
            the_planes_yz[4],
        )

        corner_group = Group()
        for plane in pos_dot_planes_xy:
            for dot in plane:
                if dot.get_center()[0] > 0 and dot.get_center()[1] > 0 and dot.get_center()[2] > 0:
                    corner_group.add(dot)
        for plane in neg_dot_planes_xy:
            for dot in plane:
                if dot.get_center()[0] > 0 and dot.get_center()[1] > 0 and dot.get_center()[2] > 0:
                    corner_group.add(dot)
        for plane in neg_dot_planes_xz:
            for dot in plane:
                if dot.get_center()[0] > 0 and dot.get_center()[1] > 0 and dot.get_center()[2] > 0:
                    corner_group.add(dot)
        for plane in neg_dot_planes_yz:
            for dot in plane:
                if dot.get_center()[0] > 0 and dot.get_center()[1] > 0 and dot.get_center()[2] > 0:
                    corner_group.add(dot)
        
        self.wait()
        self.play(
            FadeOut(the_planes_xy[4]),
            FadeOut(the_planes_xz[4]),
            FadeOut(the_planes_yz[4]),
        )

        part1 = Group(
                Line(np.array([1,0,1]), np.array([1,1,0])).apply_depth_test(),
                Line(np.array([1,0,1]), np.array([1,-1,0])).apply_depth_test(),
                Line(np.array([1,0,-1]), np.array([1,1,0])).apply_depth_test(),
                Line(np.array([1,0,-1]), np.array([1,-1,0])).apply_depth_test(),

                Line(np.array([-1,0,1]), np.array([-1,1,0])).apply_depth_test(),
                Line(np.array([-1,0,1]), np.array([-1,-1,0])).apply_depth_test(),
                Line(np.array([-1,0,-1]), np.array([-1,1,0])).apply_depth_test(),
                Line(np.array([-1,0,-1]), np.array([-1,-1,0])).apply_depth_test(),
        )
        part2 = part1.copy().rotate(90*DEGREES, IN)
        part3 = part1.copy().rotate(90*DEGREES, UP)
        ve1 = Group(part1,part2,part3).scale(0.5)

        spires = Group(
            Line(np.array([1,1,0]), np.array([0,0,0])).apply_depth_test(),
            Line(np.array([1,-1,0]), np.array([0,0,0])).apply_depth_test(),
            Line(np.array([-1,1,0]), np.array([0,0,0])).apply_depth_test(),
            Line(np.array([-1,-1,0]), np.array([0,0,0])).apply_depth_test(),

            Line(np.array([1,0,1]), np.array([0,0,0])).apply_depth_test(),
            Line(np.array([1,0,-1]), np.array([0,0,0])).apply_depth_test(),
            Line(np.array([-1,0,1]), np.array([0,0,0])).apply_depth_test(),
            Line(np.array([-1,0,-1]), np.array([0,0,0])).apply_depth_test(),

            Line(np.array([0,1,1]), np.array([0,0,0])).apply_depth_test(),
            Line(np.array([0,1,-1]), np.array([0,0,0])).apply_depth_test(),
            Line(np.array([0,-1,1]), np.array([0,0,0])).apply_depth_test(),
            Line(np.array([0,-1,-1]), np.array([0,0,0])).apply_depth_test(),
        ).set_color(YELLOW)

        self.wait()
        ve_dots = make_ve_dots(GREEN,0.1)
        self.add(ve_dots)
        self.play(FadeIn(axes))
        self.wait()
        self.play(
            frame.animate.scale(0.3),
            FadeOut(pos_dot_planes_xy),
            FadeOut(neg_dot_planes_xy),
            FadeOut(neg_dot_planes_xz),
            FadeOut(neg_dot_planes_yz),
            run_time = 3
        )
        self.wait()
        frame.add_updater(lambda m, dt: m.increment_theta(-0.1*dt)) 
        self.wait(3)
        self.play(ShowCreation(ve1))
        self.wait(3)
        self.play(
            FadeIn(spires),
            spires.animate.scale(0.5)
        )
        self.wait(3)
        the_planes_xy.set_opacity(0.8)
        the_planes_xz.set_opacity(0.8)
        the_planes_yz.set_opacity(0.8)

        xy_piece = ParametricSurface(
            lambda u,v: np.array([v,u,0]),
            u_range=(-1,1),
            v_range=(-1,1),
            resolution=(12, 12),   
        ).set_color(GREY).set_opacity(0.8).apply_depth_test()
        xz_piece = ParametricSurface(
            lambda u,v: np.array([v,0,u]),
            u_range=(-1,1),
            v_range=(-1,1),
            resolution=(12, 12),   
        ).set_color(GREY).set_opacity(0.8).apply_depth_test()
        yz_piece = ParametricSurface(
            lambda u,v: np.array([0,v,u]),
            u_range=(-1,1),
            v_range=(-1,1),
            resolution=(12, 12),   
        ).set_color(GREY).set_opacity(0.8).apply_depth_test()

        pos_planes = Group(
            xy_piece,
            xz_piece,
            yz_piece,
        )


        self.play(
            FadeIn(the_planes_xy[4]),
            FadeIn(pos_dot_planes_xy[4]),
            FadeIn(neg_dot_planes_xy[4]),
        )
        self.wait(3)
        self.add(xy_piece)
        self.play(
            FadeOut(the_planes_xy[4]),
            FadeOut(pos_dot_planes_xy[4]),
            FadeOut(neg_dot_planes_xy[4]),
        )

        self.play(
            FadeIn(the_planes_xz[4]),
            FadeIn(pos_dot_planes_xz[4]),
            FadeIn(neg_dot_planes_xz[4]),
        )
        self.wait(3)
        self.add(xz_piece)
        self.play(
            FadeOut(the_planes_xz[4]),
            FadeOut(pos_dot_planes_xz[4]),
            FadeOut(neg_dot_planes_xz[4]),
        )
        
        self.play(
            FadeIn(the_planes_yz[4]),
            FadeIn(pos_dot_planes_yz[4]),
            FadeIn(neg_dot_planes_yz[4]),
        )
        self.wait(3)
        self.add(yz_piece)
        self.play(
            FadeOut(the_planes_yz[4]),
            FadeOut(pos_dot_planes_yz[4]),
            FadeOut(neg_dot_planes_yz[4]),
        )

        xy_neg1 = ParametricSurface(
            lambda u,v: np.array([v,u,0.5]),
            u_range=(-1,1),
            v_range=(-1,1),
            resolution=(12, 12),   
        ).set_color(BLACK).set_opacity(0.8).apply_depth_test()
        xy_neg2 = ParametricSurface(
            lambda u,v: np.array([v,u,-0.5]),
            u_range=(-1,1),
            v_range=(-1,1),
            resolution=(12, 12),   
        ).set_color(BLACK).set_opacity(0.8).apply_depth_test()

        xz_neg1 = ParametricSurface(
            lambda u,v: np.array([v,0.5,u]),
            u_range=(-1,1),
            v_range=(-1,1),
            resolution=(12, 12),   
        ).set_color(BLACK).set_opacity(0.8).apply_depth_test()
        xz_neg2 = ParametricSurface(
            lambda u,v: np.array([v,-0.5,u]),
            u_range=(-1,1),
            v_range=(-1,1),
            resolution=(12, 12),   
        ).set_color(BLACK).set_opacity(0.8).apply_depth_test()

        yz_neg1 = ParametricSurface(
            lambda u,v: np.array([0.5,v,u]),
            u_range=(-1,1),
            v_range=(-1,1),
            resolution=(12, 12),   
        ).set_color(BLACK).set_opacity(0.8).apply_depth_test()
        yz_neg2 = ParametricSurface(
            lambda u,v: np.array([-0.5,v,u]),
            u_range=(-1,1),
            v_range=(-1,1),
            resolution=(12, 12),   
        ).set_color(BLACK).set_opacity(0.8).apply_depth_test()

        neg_planes = Group(
            xy_neg1,
            xy_neg2,
            xz_neg1,
            xz_neg2,
            yz_neg1,
            yz_neg2,
        )
        self.wait(3)
        self.play(
            FadeIn(xy_neg1),
            FadeIn(xy_neg2),
        )
        self.wait(3)
        self.play(
            FadeIn(xz_neg1),
            FadeIn(xz_neg2),
        )
        self.wait(3)
        self.play(
            FadeIn(yz_neg1),
            FadeIn(yz_neg2),
        )
        self.wait(3)

        self.play(
            FadeOut(pos_planes)
        )
        self.wait(3)
        self.play(
            FadeOut(neg_planes),
            FadeIn(pos_planes),
        )
        self.wait()