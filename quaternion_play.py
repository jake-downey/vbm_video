from manimlib import *
from pyquaternion import Quaternion

class Quats(Scene):
    def construct(self):
        non_zero = 0.0001
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=45*DEGREES,
            phi=45*DEGREES,
        )
        axes = ThreeDAxes()
        # Extract components
        def hyperspherical_to_quaternion(theta, phi, psi):
            """
            :param theta: Angle in range [0, π]
            :param phi: Angle in range [0, π]
            :param psi: Angle in range [0, 2π]
            :return: Quaternion (w, x, y, z)
            """
            w = np.cos(theta)
            x = np.sin(theta) * np.cos(phi)
            y = np.sin(theta) * np.sin(phi) * np.cos(psi)
            z = np.sin(theta) * np.sin(phi) * np.sin(psi)

            return Quaternion(np.array([w, x, y, z]))

        theta_val = ValueTracker(0)
        phi_val = ValueTracker(0)
        psi_val = ValueTracker(0)

        theta_val2 = ValueTracker(0)
        phi_val2 = ValueTracker(0)
        psi_val2 = ValueTracker(0)

        q3 = hyperspherical_to_quaternion(
                PI*(1/2), 
                PI*(1/8),
                0,
            )
        self.add(axes)

        its = 18
        for i in range(0,its):

            # theta_val.set_value((i/8)*TAU)
            q1 = Quaternion(q3.w, q3.x, q3.y, q3.z)
            q2 = hyperspherical_to_quaternion(
                TAU*(1/18), 
                0,
                0,
            )
            q3 = q1 * q2
            dot = Sphere(radius=0.1).move_to(
                np.array([
                    q1.x/(1-(q1.w+non_zero)), 
                    q1.y/(1-(q1.w+non_zero)), 
                    q1.z/(1-(q1.w+non_zero))])
                ).set_color(RED)
            self.add(dot)
            self.wait(0.03)


        q4 = hyperspherical_to_quaternion(
                PI*(1/2), 
                PI*(1/2),
                0,
            )
        self.add(axes)

        for i in range(0,its):

            # theta_val.set_value((i/8)*TAU)
            q1 = Quaternion(q4.w, q4.x, q4.y, q4.z)
            q2 = hyperspherical_to_quaternion(
                TAU*(1/18), 
                0,
                0,
            )
            q4 = q1 * q2
            dot = Sphere(radius=0.1).move_to(
                np.array([
                    q1.x/(1-(q1.w+non_zero)), 
                    q1.y/(1-(q1.w+non_zero)), 
                    q1.z/(1-(q1.w+non_zero))])
                ).set_color(BLUE)
            self.add(dot)
            self.wait(0.03)

        def quat_mult_curve(u, q1, q2):
            q3 = q1 * ((u/TAU) * q2)
            proj_coords = np.array([
                q3.x / (1 - q3.w), 
                q3.y / (1 - q3.w), 
                q3.z / (1 - q3.w),
            ])
            begin = q3
            return proj_coords
        
        begin = hyperspherical_to_quaternion(
                theta_val.get_value(), 
                phi_val.get_value(),
                0,
            )
        multiplier = hyperspherical_to_quaternion(
                PI*(1/8), 
                0,
                0,
            )
        curve = ParametricCurve(
                lambda u: quat_mult_curve(u,begin, multiplier),
                color = YELLOW,
                t_range = np.array([0,TAU,0.01])
            ).apply_depth_test()
        self.add(curve)

class HopfQuats(Scene):
    def construct(self):
        non_zero = 0.0001
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=45*DEGREES,
            phi=45*DEGREES,
        )
        axes = ThreeDAxes()

        def hopf_to_quaternion(zeta, phi, eta):

            w = np.cos(zeta) * np.cos(phi)
            x = np.cos(zeta) * np.sin(phi)
            y = np.sin(zeta) * np.cos(eta)
            z = np.sin(zeta) * np.sin(eta)

            return Quaternion(w, x, y, z)


        self.add(axes)

        eta_tracker = ValueTracker(0)
        delta_eta = PI/6
        its = 18

        q1 = hopf_to_quaternion(PI/4, 0, eta_tracker.get_value())

        def see_hopf_mults(which_angle, angle, q1):
            mults = Group()
            if which_angle == "eta":
                for i in range(0,its):
                    q2 = Quaternion(
                        np.cos(angle / 2),
                        0,
                        0,
                        np.sin(angle / 2),
                    )
                    q3 = Quaternion(
                        np.cos(angle / 2),
                        0,
                        0,
                        -np.sin(angle / 2),
                    )
                    q1 = q3 * q1 * q2
                    dot = Sphere(radius=0.1).move_to(
                        np.array([
                            q1.x/(1-(q1.w+non_zero)), 
                            q1.y/(1-(q1.w+non_zero)), 
                            q1.z/(1-(q1.w+non_zero))])
                        ).set_color(RED)
                    mults.add(dot)
            if which_angle == "phi":
                for i in range(0,its):
                    q2 = Quaternion(
                        np.cos(angle / 2),
                        np.sin(angle / 2),
                        0,
                        0,
                    )
                    q3 = Quaternion(
                        np.cos(angle / 2),
                        -np.sin(angle / 2),
                        0,
                        0,
                    )
                    q1 = q3 * q1 * q2
                    dot = Sphere(radius=0.1).move_to(
                        np.array([
                            q1.x/(1-(q1.w+non_zero)), 
                            q1.y/(1-(q1.w+non_zero)), 
                            q1.z/(1-(q1.w+non_zero))])
                        ).set_color(RED)
                    mults.add(dot)
            return mults

        self.add(see_hopf_mults("phi", PI/6, q1))