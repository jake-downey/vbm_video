from manimlib import *

class Cylinder(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }
    def construct(self):

        # VARIABLES

        sphere_size = 0.05
        non_zero = .001

        # FUNCTIONS

        def dots_cylinder(radius, num_dots, num_rings, plane, offset):
            dot_group = Group()
            sphere = Sphere(radius=sphere_size)
            col = [GREEN, BLUE, RED]
            if plane == "xy":
                for i in range (0, num_dots):
                    for j in range(-num_rings, num_rings):
                        x = j
                        y = offset * np.sin(i / num_dots * TAU)
                        z = offset * np.cos(i / num_dots * TAU)
                        
                        vert = [x,y,z]
                        dot = sphere.copy()
                        dot.set_color(col[(1+i+j)%3])
                        dot.move_to(vert)
                        dot_group.add(dot)
            if plane == "xz":
                for i in range (0, num_dots):
                    for j in range(0, num_rings):
                        x = offset
                        y1 = j * np.sin(i / num_dots * TAU)
                        z1 = j * np.cos(i / num_dots * TAU)

                        vert1 = [x,y1,z1]
                        dot = sphere.copy()
                        dot.set_color(col[(i+j)%3])
                        dot.move_to(vert1)
                        dot_group.add(dot)
            if plane == "yz":
                for i in range (0, num_dots):
                    for j in range(-num_rings, num_rings):
                        x = i - (num_dots/2)
                        y1 = ((j + num_rings)) * np.sin(offset)
                        z1 = ((j + num_rings)) * np.cos(offset)

                        vert1 = [x,y1,z1]
                        dot = sphere.copy()
                        dot.set_color(col[(i+j)%3])
                        dot.move_to(vert1)
                        dot_group.add(dot)
            return dot_group

        def curves_cylinder(radius, num_rings, plane):
            curve_group = Group()
            if plane == "xy":
                for i in range (-num_rings, num_rings):
                    curve = ParametricCurve(
                        lambda u: np.array([
                            i,
                            radius * np.sin(u),
                            radius * np.cos(u),
                        ]),
                        color = WHITE,
                        t_range = np.array([0, TAU, 0.01])
                    )
                    curve_group.add(curve)
            if plane == "xz":
                for i in range (-num_rings, num_rings):
                    curve = ParametricCurve(
                        lambda u: np.array([
                            u,
                            radius * np.sin(i/num_rings*PI),
                            radius * np.cos(i/num_rings*PI),
                        ]),
                        color = WHITE,
                        t_range = np.array([-num_rings, num_rings, 0.01])
                    )
                    curve_group.add(curve)
            if plane == "yz":
                for i in range (-num_rings, num_rings):
                    curve = ParametricCurve(
                        lambda u: np.array([
                            0,
                            u * np.sin(i/num_rings*PI),
                            u * np.cos(i/num_rings*PI),
                        ]),
                        color = WHITE,
                        t_range = np.array([0, 9, 0.01])
                    )
                    curve_group.add(curve)
            return curve_group

        def doubling_curves(radius, num_diags, plane):
            curve_group = Group()
            col = [GREEN, BLUE, RED]
            if plane == "xy":
                for i in range (0, num_diags):
                    curve = ParametricCurve(
                        lambda u: np.array([
                            (u/PI)* num_diags / 2,
                            radius * np.sin(-u + ((i/num_diags) * TAU)),
                            radius * np.cos(-u + ((i/num_diags) * TAU)),
                        ]),
                        color = col[(i+1)%3],
                        t_range = np.array([-PI, PI, 0.01])
                    )
                    curve_group.add(curve)
            if plane == "xz":
                for i in range (0, num_diags):
                    curve = ParametricCurve(
                        lambda u: np.array([
                            0,
                            ((u/PI)*radius) * np.sin(-u + ((i/num_diags) * TAU)),
                            ((u/PI)*radius) * np.cos(-u + ((i/num_diags) * TAU)),
                        ]),
                        color = col[i%3],
                        t_range = np.array([0, TAU, 0.01])
                    )
                    curve_group.add(curve)
            if plane == "yz":
                for i in range (-num_diags, num_diags):
                    line = Line([i, 0, 0],[i-num_diags, num_diags,0]).set_color(color = col[i%3])
                    line2 = Line([i, 0, 0],[i-num_diags, -num_diags,0]).set_color(color = col[i%3])
                    curve_group.add(line)
                    curve_group.add(line2)
            return curve_group
        
        r_length = ValueTracker(0)
        theta_length = ValueTracker(0)
        z_length = ValueTracker(0)

        r_path = always_redraw(lambda: ParametricCurve(
                lambda u: np.array([
                    0,
                    0,
                    u,
                ]),
                color = YELLOW,
                t_range = np.array([0,r_length.get_value(),0.01])
            ).apply_depth_test()
        )
        theta_path = always_redraw(lambda: ParametricCurve(
                lambda u: np.array([
                    0,
                    r_length.get_value() * np.sin(u),
                    r_length.get_value() * np.cos(u),
                ]),
                color = YELLOW,
                t_range = np.array([0,theta_length.get_value(),0.01])
            ).apply_depth_test()
        )
        z_path = always_redraw(lambda: ParametricCurve(
                lambda u: np.array([
                    u,
                    r_length.get_value() * np.sin(theta_length.get_value()),
                    r_length.get_value() * np.cos(theta_length.get_value()),
                ]),
                color = YELLOW,
                t_range = np.array([0,z_length.get_value(),0.01])
            ).apply_depth_test()
        )
        dot_path = always_redraw(
            lambda: Sphere(radius=sphere_size+0.02).set_color(YELLOW).move_to([
                    z_length.get_value(),
                    r_length.get_value() * np.sin(theta_length.get_value()),
                    r_length.get_value() * np.cos(theta_length.get_value()),
                ]
            ).apply_depth_test()
        )

        axes = ThreeDAxes().apply_depth_test()

        # CAMERA STUFF

        frame = self.camera.frame
        frame.set_euler_angles(
            theta=45*DEGREES,
            phi=45*DEGREES,
        )
        # frame.add_updater(lambda m, dt: m.increment_theta(-0.1*dt))

        # INITIATORS
        # points_pos = dots_cylinder(1, 18, 9)
        # curves_pos = curves_cylinder(1, 9)
        # doubling = doubling_curves(1, 18)

        # SCENE STUFF

        # self.add(points_pos)
        # self.add(curves_pos)
        # self.add(doubling)
        # self.add(curves_cylinder(1, 9, "xy").apply_depth_test())
        # self.add(curves_cylinder(1, 9, "xz").apply_depth_test())
        # self.add(curves_cylinder(1, 9, "yz").apply_depth_test())
        self.add(dots_cylinder(1,18,9,"xy",1).apply_depth_test())
        self.add(dots_cylinder(1,18,9,"yz",0).apply_depth_test())
        self.add(dots_cylinder(1,18,9,"yz",PI).apply_depth_test())
        # self.add(r_path,theta_path,z_path,dot_path)
        # self.wait(1)
        # self.play(r_length.animate.set_value(1), run_time=2)
        # self.wait(1)
        # self.play(theta_length.animate.set_value(PI/3), run_time=2)
        # self.wait(1)
        # self.play(z_length.animate.set_value(1), run_time=2)
        # self.wait(1)

        # # self.add(dots_cylinder(1,18,9,"xz",0))
        self.add(doubling_curves(9, 18, "xz").apply_depth_test())
        self.add(doubling_curves(9, 9, "yz").apply_depth_test())
        self.add(doubling_curves(1, 18, "xy").apply_depth_test())

        