from manimlib import *

class TransLine(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }
    def construct(self):
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=30*DEGREES,
            phi=60*DEGREES,
        )
        frame.add_updater(lambda m, dt: m.increment_theta(-0.1*dt))
        axes = ThreeDAxes()
        wire_size = 0.05
        wire1 = ParametricSurface(
            lambda u,v: np.array([
                    wire_size * np.cos(v)+1,
                    u,
                    wire_size * np.sin(v),
                ]),
                u_range = (-5, 5),
                v_range = (0, TAU),
                color = GOLD,
        )
        wire2 = ParametricSurface(
            lambda u,v: np.array([
                    wire_size * np.cos(v)-1,
                    u,
                    wire_size * np.sin(v),
                ]),
                u_range = (-5, 5),
                v_range = (0, TAU),
                color = GOLD,
        )
        
        non_zero = 0.0001
        def three_d_rotate(x,y,z,theta):
            vector = np.array([[x,y,z]])
            rot_matrix = np.array([
                [np.cos(theta), 0, np.sin(theta)],
                [0,1,0],
                [-np.sin(theta), 0, np.cos(theta)],
            ])
            new_vec = vector@rot_matrix
            proj_x = new_vec[0][0] / ((1 - new_vec[0][2]) + non_zero) 
            proj_y = new_vec[0][1] / ((1 - new_vec[0][2]) + non_zero) 

            return np.array([proj_x,0,proj_y])

        rot_angle = PI/2

        def make_electric_field(lines):
            e_field = Group()
            for i in range(0,lines):
                def set_points(u):
                    x = (np.sin(u) * np.cos((i/lines)*PI))
                    y = (np.sin(u) * np.sin((i/lines)*PI))
                    z = np.cos(u)
                    return np.array([x, y, z])
                line = ParametricCurve(
                    lambda u: three_d_rotate(set_points(u)[0],set_points(u)[1],set_points(u)[2],rot_angle),
                    color = BLUE,
                    t_range = np.array([0, TAU, 0.01])
                ).apply_depth_test()
                e_field.add(line)
            return e_field
        def make_magnetic_field(lines):
            m_field = Group()
            for i in range(0,lines):
                def set_points(u):
                    x = (np.sin((i/lines)*PI) * np.cos(u))
                    y = (np.sin((i/lines)*PI) * np.sin(u))
                    z = np.cos((i/lines)*PI)
                    return np.array([x, y, z])
                line = ParametricCurve(
                    lambda u: three_d_rotate(set_points(u)[0],set_points(u)[1],set_points(u)[2],rot_angle),
                    color = GREEN,
                    t_range = np.array([0, TAU, 0.01])
                ).apply_depth_test()
                m_field.add(line)
            return m_field



        # self.add(axes)
        self.add(wire1)
        self.add(wire2)
        current_e = make_electric_field(18)
        current_m = make_magnetic_field(18)
        self.add(current_e)
        self.add(current_m)




        # e1 = make_electric_field(18).shift(UP*2)
        # e2 = make_electric_field(18).shift(UP*4)
        # e3 = make_electric_field(18).shift(DOWN*2)
        # e4 = make_electric_field(18).shift(DOWN*4)
        # m1 = make_magnetic_field(18).shift(UP*2)
        # m2 = make_magnetic_field(18).shift(UP*4)
        # m3 = make_magnetic_field(18).shift(DOWN*2)
        # m4 = make_magnetic_field(18).shift(DOWN*4)
        # self.add(e1,e2,e3,e4,m1,m2,m3,m4)
        self.wait(12)

        # for i in range(0,20):
        #     current_e = make_electric_field(i)
        #     current_m = make_magnetic_field(i)
        #     self.add(current_e)
        #     self.add(current_m)
        #     self.wait(0.05)
        #     self.remove(current_e)
        #     self.remove(current_m)
        # self.wait(3)