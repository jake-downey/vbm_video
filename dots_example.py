from manimlib import *
import sys
sys.path.append("C:/Users/thund/Downloads/manim-master/manimprojects")
from funcs_dots import *

class Dots(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }
    def construct(self):
        # VARIABLES

        sphere_size = 0.1
        
        # CAMERA STUFF
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=50*DEGREES,
            phi=45*DEGREES,
        )
        # frame.add_updater(lambda m, dt: m.increment_theta(-0.1*dt))
        light = self.camera.light_source
        self.add(light)

        # INITIATORS AND UPDATERS
        x_length = ValueTracker(0)
        y_length = ValueTracker(0)
        z_length = ValueTracker(0)
        x_path = always_redraw(lambda: Line(
            [0,0,0], [x_length.get_value(),0,0]
            ).set_color(YELLOW).apply_depth_test()
            )
        y_path = always_redraw(lambda: Line(
            [x_length.get_value(),0,0], 
            [x_length.get_value(),y_length.get_value(),0]
            ).set_color(YELLOW).apply_depth_test()
            )
        z_path = always_redraw(lambda: Line(
            [x_length.get_value(),y_length.get_value(),0], 
            [x_length.get_value(),y_length.get_value(),z_length.get_value()]
            ).set_color(YELLOW).apply_depth_test()
            )
        dot_path = always_redraw(
            lambda: Sphere(radius=sphere_size+0.02).set_color(YELLOW).move_to(
                [x_length.get_value(),y_length.get_value(),z_length.get_value()]
                )
            )
        axes = ThreeDAxes(
            x_range = (-4,4,1),
            y_range = (-4,4,1),
            z_range = (-4,4,1),
        ).apply_depth_test()

        x_label = axes.x_axis.add(Tex("+1,-8", font_size=24).next_to(axes.c2p(0,4),UP))
        # SCENE STUFF

        self.add(axes, x_label)
        self.play(
            FadeIn(dot_plane_pos(4,0,"xy").apply_depth_test()),
        )
        self.add(axes.apply_depth_test())
            # dot_plane_pos(4,-4,"xy").apply_depth_test(),
            # dot_plane_pos(4,-3,"xy").apply_depth_test(),
            # dot_plane_pos(4,-2,"xy").apply_depth_test(),
            # dot_plane_pos(4,-1,"xy").apply_depth_test(),
            # dot_plane_pos(4,1,"xy").apply_depth_test(),
            # dot_plane_pos(4,2,"xy").apply_depth_test(),
            # dot_plane_pos(4,3,"xy").apply_depth_test(),
            # dot_plane_pos(4,4,"xy").apply_depth_test(),
        # self.add(vector_equilibrium(0.5).set_color(WHITE).set_opacity(0.5))
        # self.add(vector_equilibrium(1).set_opacity(0.5))
        # self.add(vector_equilibrium_neg(1))
        
        # self.add(rhombic_grid(4,0,"xy","neg",0.25))
        # self.add(rhombic_grid(4,0,"xy","pos",0.25))
        # self.add(rhombic_grid(4,0,"xy").set_opacity(0.3))

        # self.wait(1)
        # self.play(x_length.animate.set_value(1), run_time = 2)
        # # self.wait(1)
        # dots_pos = dot_plane_pos(4,0,"xy")
        # dots_neg = dot_plane_neg(4,0,"xy")
        # grid = grid_pos_xyz(4,0,"xy")[0].apply_depth_test()
        # grid2 = grid_pos_xyz(4,0,"xy")[0].apply_depth_test()
        # neg_grid = grid_neg_xyz(4,0,"xy")[0]
        # doubling = doubling_curve_xyz(3,0,"xy")
        # plane_pos = plane_pos_xyz(3,0,"xy")
        # plane_neg = plane_neg_xyz(3,0,"xy")
        # doubling_green = doubling_surface(3,0)
        # doubling_red = doubling_surface(3,1)
        # doubling_blue = doubling_surface(3,2)
        # v_e = vector_equilibrium(GREEN,1)

        # self.add(dots_pos)
        # self.add(dots_neg)
        # self.wait()
        # self.play(ShowCreation(grid), run_time=5, rate_func=linear)
        # self.play(ShowCreation(grid2), run_time=5, rate_func=linear)
        # self.add(neg_grid)
        # self.add(doubling_green)
        # self.add(doubling_red)
        # self.add(doubling_blue)
        # self.add(dot_plane_pos(4,0,"xy"))
        # self.add(dot_plane_pos(4,0,"xz"))
        # self.add(dot_plane_pos(4,0,"yz"))
        # self.camera.frame.scale(1.5)
        # self.add(axes, x_path, y_path, z_path, dot_path)
        # self.wait(1)
        # self.play(x_length.animate.set_value(2), run_time=2)
        # self.wait(1)
        # self.play(y_length.animate.set_value(2), run_time=2)
        # self.wait(1)
        # self.play(z_length.animate.set_value(2), run_time=2)
        # self.wait(1)
        # self.add(plane_pos)
        # self.add(plane_neg)

        # for i in range(-4,4): 
        #     self.add(dot_plane_pos(4,i,"xy"))


        # self.add(rhombic_grid(2,0,"xy","neg"))
        # self.add(rhombic_grid(2,1,"xy","neg"))
        # self.add(rhombic_grid(2,-1,"xy","neg"))
        # self.add(rhombic_grid(2,0,"xz","neg"))
        # self.add(rhombic_grid(2,1,"xz","neg"))
        # self.add(rhombic_grid(2,-1,"xz","neg"))
        # self.add(rhombic_grid(2,0,"yz","neg"))
        # self.add(rhombic_grid(2,1,"yz","neg"))
        # self.add(rhombic_grid(2,-1,"yz","neg"))

        # tetra_up = tetra_up_grid(1,1)
        # tetra_down = tetra_down_grid(1,1)
        # self.add(tetra_up,tetra_down)
        # grid1 = rhombic_grid(2,0,"xy","pos")
        # grid2 = rhombic_grid(2,1,"xy","pos")
        # grid3 = rhombic_grid(2,-1,"xy","pos")
        # self.add(grid1, grid2, grid3)
        # self.add(dot_plane_neg(2,0,"xy"),dot_plane_neg(2,1,"xy"),dot_plane_neg(2,-1,"xy"))
        # self.add(dot_plane_neg(2,0,"xz"),dot_plane_neg(2,1,"xz"),dot_plane_neg(2,-1,"xz"))
        # self.add(dot_plane_neg(2,0,"yz"),dot_plane_neg(2,1,"yz"),dot_plane_neg(2,-1,"yz"))
        # # # # self.add(dot_plane_neg(2,0,"xz"))
        # # # # self.add(dot_plane_neg(2,0,"yz"))
        # self.add(dot_plane_pos(2,0,"xy"),dot_plane_pos(2,1,"xy"),dot_plane_pos(2,-1,"xy"))
        # # # self.add(dot_plane_pos(2,0,"xz"))
        # # self.add(dot_plane_pos(2,0,"yz"))
        # # self.add(vector_equilibrium(RED,2))
        # # self.add(vector_equilibrium(BLUE,3))
        # self.add(octahedron().set_color(BLUE))
        # self.wait()
        # self.play(FadeOut(grid2))
        # self.wait()
        # self.play(FadeOut(tetra_up))
        # self.play(FadeOut(tetra_down))

      

        # self.wait(5)
        

