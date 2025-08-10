from manimlib import *

class Hypersphere(Scene):
    def construct(self):

        non_zero = .001

        def four_d_rotate(w,x,y,z,theta):
            vector = np.array([[w,x,y,z]])
            rot_matrix = np.array([
                [np.cos(theta), -np.sin(theta), 0, 0],
                [np.sin(theta), np.cos(theta), 0, 0],
                [0,0,1,0],
                [0,0,0,1],
            ])
            new_vec = vector@rot_matrix
            proj_x = new_vec[0][1] / ((1 - new_vec[0][0]) + non_zero) 
            proj_y = new_vec[0][2] / ((1 - new_vec[0][0]) + non_zero) 
            proj_z = new_vec[0][3] / ((1 - new_vec[0][0]) + non_zero) 

            return np.array([proj_x,proj_y,proj_z])

        
        def test_parallels(theta_step, psi_value, r, rot_angle):
            curve_group = Group()
            for i in range (0, theta_step):
                theta = (i/theta_step) * math.pi
                def set_points(u):
                    w = r * np.cos(psi_value)
                    x = (r * np.sin(psi_value) * np.cos(theta))
                    y = (r * np.sin(psi_value) * np.sin(theta) * np.cos(u))
                    z = (r * np.sin(psi_value) * np.sin(theta) * np.sin(u))
                    return np.array([w, x, y, z])
                curve = ParametricCurve(
                    lambda u: four_d_rotate(set_points(u)[0],set_points(u)[1],set_points(u)[2],set_points(u)[3],rot_angle),
                    color = YELLOW,
                    t_range = np.array([0, TAU, 0.01])
                ).apply_depth_test()
                curve_group.add(curve)
            return curve_group

        # self.add(test_parallels(18, (6/18)*PI, 1, rotation_angle.get_value()))
        # self.add(test_parallels(18, (12/18)*PI, 1, rotation_angle.get_value()))
        # self.add(test_parallels(18, (9/18)*PI, 1, rotation_angle.get_value()))

        def parallels2(psi_step, theta_value, r):
            curve_group = Group()
            for i in range (0, psi_step):
                psi = (i/psi_step) * math.pi

                curve = ParametricCurve(
                    lambda u: np.array([
                        (r * np.sin(psi) * np.sin(theta_value) * np.sin(u)) / (1 - r * np.cos(psi) + non_zero),
                        (r * np.sin(psi) * np.sin(theta_value) * np.cos(u)) / (1 - r * np.cos(psi) + non_zero),
                        (r * np.sin(psi) * np.cos(theta_value)) / (1 - r * np.cos(psi) + non_zero),
                    ]),
                    color = PURPLE,
                    t_range = np.array([0, TAU, 0.01])
                ).apply_depth_test()
                curve_group.add(curve)
            return curve_group
        
        def test_meridians(phi_step, psi_value, r, rot_angle):
            curve_group = Group()
            for i in range (0, phi_step):
                phi = (i/phi_step) * 2 * math.pi
                def set_points(u):
                    w = r * np.cos(psi_value)
                    x = (r * np.sin(psi_value) * np.cos(u))
                    y = (r * np.sin(psi_value) * np.sin(u) * np.cos(phi))
                    z = (r * np.sin(psi_value) * np.sin(u) * np.sin(phi))
                    return np.array([w, x, y, z])
                curve = ParametricCurve(
                    lambda u: four_d_rotate(set_points(u)[0],set_points(u)[1],set_points(u)[2],set_points(u)[3],rot_angle),
                    color = BLUE,
                    t_range = np.array([0, TAU, 0.01])
                ).apply_depth_test()
                curve_group.add(curve)
            return curve_group

        # self.add(test_meridians(18, (6/18)*PI, 1, rotation_angle.get_value()))
        # self.add(test_meridians(18, (12/18)*PI, 1, rotation_angle.get_value()))
        # self.add(test_meridians(18, (9/18)*PI, 1, rotation_angle.get_value()))

        def meridians2(psi_step, phi_value, r):
            curve_group = Group()
            for i in range (0, psi_step):
                psi = (i/psi_step) * 2 * math.pi
                curve = ParametricCurve(
                    lambda u: np.array([
                        (r * np.sin(psi) * np.sin(u) * np.sin(phi_value)) / (1 - r * np.cos(psi) + non_zero),
                        (r * np.sin(psi) * np.sin(u) * np.cos(phi_value)) / (1 - r * np.cos(psi) + non_zero),
                        (r * np.sin(psi) * np.cos(u)) / (1 - r * np.cos(psi) + non_zero),
                    ]),
                    color = ORANGE,
                    t_range = np.array([0, PI, 0.01])
                ).apply_depth_test()
                curve_group.add(curve)
            return curve_group
       
        def test_hyper_meridians(phi_step, theta_value, r, rot_angle):
            curve_group = Group()
            for i in range (0, phi_step):
                phi = (i/phi_step) * 2 * math.pi
                def set_points(u):
                    w = (r * np.cos(u))
                    x = (r * np.sin(u) * np.cos(theta_value))
                    y = (r * np.sin(u) * np.sin(theta_value) * np.cos(phi))
                    z = (r * np.sin(u) * np.sin(theta_value) * np.sin(phi))
                    return np.array([w, x, y, z])
                curve = ParametricCurve(
                    lambda u: four_d_rotate(set_points(u)[0],set_points(u)[1],set_points(u)[2],set_points(u)[3],rot_angle),
                    color = RED,
                    t_range = np.array([0, TAU, 0.01])
                ).apply_depth_test()
                curve_group.add(curve)
            return curve_group
        
        # self.add(test_hyper_meridians(18, (6/18)*PI, 1, rotation_angle.get_value()))
        # self.add(test_hyper_meridians(18, (12/18)*PI, 1, rotation_angle.get_value()))
        # self.add(test_hyper_meridians(18, (9/18)*PI, 1, rotation_angle.get_value()))

        def hyper_meridians2(theta_step, phi_value, r):
            curve_group = Group()
            for i in range (0, theta_step):
                theta = (i/theta_step) * 2 * math.pi
                curve = ParametricCurve(
                    lambda u: np.array([
                        (r * np.sin(u) * np.sin(theta) * np.sin(phi_value)) / (1 - (r * np.cos(u)) + non_zero),
                        (r * np.sin(u) * np.sin(theta) * np.cos(phi_value)) / (1 - (r * np.cos(u)) + non_zero),
                        (r * np.sin(u) * np.cos(theta)) / (1 - (r * np.cos(u)) + non_zero),
                    ]),
                    color = GREEN,
                    t_range = np.array([0, PI, 0.01])
                ).apply_depth_test()
                curve_group.add(curve)
            return curve_group
        
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=45*DEGREES,
            phi=45*DEGREES,
        )
        frame.add_updater(lambda m, dt: m.increment_theta(-0.1*dt))
        axes = ThreeDAxes().apply_depth_test()

        self.add(axes)
        rotation_angle = ValueTracker(3*PI/4)
        paras1 = test_parallels(18, (6/18)*PI, 1, rotation_angle.get_value())
        paras2 = test_parallels(18, (9/18)*PI, 1, rotation_angle.get_value())
        paras3 = test_parallels(18, (12/18)*PI, 1, rotation_angle.get_value())

        merids1 = test_meridians(18, (6/18)*PI, 1, rotation_angle.get_value())
        merids2 = test_meridians(18, (9/18)*PI, 1, rotation_angle.get_value())
        merids3 = test_meridians(18, (12/18)*PI, 1, rotation_angle.get_value())

        hypers1 = test_hyper_meridians(18, (6/18)*PI/2, 1, rotation_angle.get_value())
        hypers2 = test_hyper_meridians(18, (9/18)*PI/2, 1, rotation_angle.get_value())
        hypers3 = test_hyper_meridians(18, (12/18)*PI/2, 1, rotation_angle.get_value())

        # paras1.add_updater(lambda m: m.become(test_parallels(18, (6/18)*PI, 1, rotation_angle.get_value())))
        # paras2.add_updater(lambda m: m.become(test_parallels(18, (9/18)*PI, 1, rotation_angle.get_value())))
        # paras3.add_updater(lambda m: m.become(test_parallels(18, (12/18)*PI, 1, rotation_angle.get_value())))
        # merids1.add_updater(lambda m: m.become(test_meridians(18, (6/18)*PI, 1, rotation_angle.get_value())))
        # merids2.add_updater(lambda m: m.become(test_meridians(18, (9/18)*PI, 1, rotation_angle.get_value())))
        # merids3.add_updater(lambda m: m.become(test_meridians(18, (12/18)*PI, 1, rotation_angle.get_value())))
        # hypers1.add_updater(lambda m: m.become(test_hyper_meridians(18, (6/18)*PI, 1, rotation_angle.get_value())))
        # hypers2.add_updater(lambda m: m.become(test_hyper_meridians(18, (9/18)*PI, 1, rotation_angle.get_value())))
        # hypers3.add_updater(lambda m: m.become(test_hyper_meridians(18, (12/18)*PI, 1, rotation_angle.get_value())))

        self.add(paras1, paras2, paras3)
        self.add(merids1, merids2, merids3)
        self.add(hypers1, hypers2, hypers3)
        # self.wait()
        # self.play(rotation_angle.animate.set_value(PI/2), run_time = 3, rate_func = linear)
        # self.wait()
    
class FromInfinityCylinder(Scene):
    def construct(self):

        frame = self.camera.frame
        frame.set_euler_angles(
            theta=30*DEGREES,
            phi=60*DEGREES,
        )
        # frame.add_updater(lambda m, dt: m.increment_theta(-0.1*dt))
        axes = ThreeDAxes().apply_depth_test()
        self.add(axes)

        off_tracker = ValueTracker(0)

        def parametric_cylinder(offset, color):
            r = np.sqrt(offset**2 + 1)
            cylinder = ParametricSurface(
                lambda u,v: np.array([
                    -r*np.cos(u)+offset,
                    v,
                    r*np.sin(u),
                ]),
                u_range = (0, TAU),
                v_range = (-4, 4),
                color = color,
            )
            return cylinder
        mid_line = Line(
            np.array([off_tracker.get_value(),-4,0]),
            np.array([off_tracker.get_value(),4,0]),
        ).set_color(YELLOW).apply_depth_test()
       
        zero_cyl = parametric_cylinder(off_tracker.get_value(),RED)
        zero_cyl.add_updater(lambda m: m.become(parametric_cylinder(off_tracker.get_value(),RED)))
        mid_line.add_updater(lambda m: m.become(
            Line(
                np.array([off_tracker.get_value(),-4,0]),
                np.array([off_tracker.get_value(),4,0]),
            ).set_color(YELLOW).apply_depth_test()
        ))
        self.add(zero_cyl, mid_line)
        self.wait()
        self.play(off_tracker.animate.set_value(-50), run_time = 10)
        self.wait()
        self.play(off_tracker.animate.set_value(0), run_time = 10)
        self.wait(3)


class FromInfinitySphere(Scene):
    def construct(self):

        frame = self.camera.frame
        frame.set_euler_angles(
            theta=30*DEGREES,
            phi=60*DEGREES,
        )
        # frame.add_updater(lambda m, dt: m.increment_theta(-0.1*dt))
        axes = ThreeDAxes().apply_depth_test()
        self.add(axes)

        off_tracker = ValueTracker(0)

        def parametric_sphere(offset, color):
            r = np.sqrt(offset**2 + 1)
            sphere = ParametricSurface(
                lambda u,v: np.array([
                    -r*(np.cos(u)*np.sin(v))+offset,
                    r*(np.sin(u)*np.sin(v)),
                    r*np.cos(v),
                ]),
                u_range = (0,PI),
                v_range = (0, PI),
                color = color,
            ).set_opacity(0.5).apply_depth_test()
            return sphere
        mid_point = Sphere(radius=0.1).shift(np.array([off_tracker.get_value(),0,0]))
        mid_point.set_color(YELLOW)

        zero_sphere = parametric_sphere(off_tracker.get_value(),RED)
        zero_sphere.add_updater(lambda m: m.become(parametric_sphere(off_tracker.get_value(),RED)))
        mid_point.add_updater(lambda m: m.become(
            Sphere(radius=0.1).move_to(np.array([off_tracker.get_value(),0,0])).set_color(YELLOW)
        ))
        self.add(zero_sphere)
        self.add(mid_point)
        self.wait()
        self.play(off_tracker.animate.set_value(-50), run_time = 10)
        self.wait()
        self.play(off_tracker.animate.set_value(0), run_time = 10)
        self.wait(3)
