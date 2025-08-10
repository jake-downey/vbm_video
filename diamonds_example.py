from manimlib import *
import sys
sys.path.append("C:/Users/thund/Downloads/manim-master/manimprojects")
from diamond_funcs import *
from vbm_funcs import *
from dots_example import *

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
        ).set_color(GREY).set_opacity(0.9).apply_depth_test()
        plane_xz = ParametricSurface(
            lambda u,v: np.array([u,0,v]),
            u_range=(-4.5,4.5),
            v_range=(-4.5,4.5),
        ).set_color(GREY).set_opacity(0.9).apply_depth_test()
        plane_yz = ParametricSurface(
            lambda u,v: np.array([0,u,v]),
            u_range=(-4.5,4.5),
            v_range=(-4.5,4.5),
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

        pos_xz_plane = dot_plane_pos(5,5,0,"xz").apply_depth_test()
        neg_xz_plane = dot_plane_neg(5,5,0,"xz").apply_depth_test()

        self.play(
            FadeIn(pos_xz_plane),
            FadeIn(neg_xz_plane),
            FadeIn(plane_xz),
        )
        self.wait()

        pos_yz_plane = dot_plane_pos(5,5,0,"yz").apply_depth_test()
        neg_yz_plane = dot_plane_neg(5,5,0,"yz").apply_depth_test()

        self.play(
            FadeIn(pos_yz_plane),
            FadeIn(neg_yz_plane),
            FadeIn(plane_yz),
        )
        self.wait()
        
        frame.add_updater(lambda m, dt: m.increment_theta(-0.1*dt))
