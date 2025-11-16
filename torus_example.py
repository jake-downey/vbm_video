from manimlib import *

class Torus(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }
    def construct(self):
        
        # VARIABLES

        sphere_size = 0.05
        stroke_size = 2
        surface_opacity = .5
        non_zero = 0.0001

        # FUNCTIONS

        def hopf_verts_pos(e1_step,e2_step,eta_step,plane):

            dot_group = Group()
            sphere = Sphere(radius=sphere_size, resolution = (30,30))
            colors = [BLUE, GREEN, RED]
            if plane == "xy":
                for i in range (0, e1_step):
                    for j in range(0, e2_step):
                        e1 = (i/e1_step) * 2 * math.pi
                        e2 = (j/e2_step) * 4 * math.pi
                        x = (np.cos((e1+e2)/2) * np.sin(eta_step))
                        y = (np.sin((e1+e2)/2) * np.sin(eta_step))
                        z = (np.cos((e2-e1)/2) * np.cos(eta_step))
                        w = (np.sin((e2-e1)/2) * np.cos(eta_step))

                        proj_x = x/(1-w+non_zero)
                        proj_y = y/(1-w+non_zero)
                        proj_z = z/(1-w+non_zero)

                        vert = [proj_x, proj_y, proj_z]
                        dot = sphere.copy()
                        dot.set_color(colors[j%3])
                        dot.move_to(vert)
                        dot_group.add(dot)
            return dot_group

        def hopf_verts_neg(e1_step,e2_step,eta_step):
            dot_group = Group()
            sphere = Sphere(radius=sphere_size, resolution = (30,30))
            for i in range (0, e1_step):
                for j in range(0, e2_step):
                    e1 = (i/e1_step) * 2 * math.pi - (((1/e1_step) * 2 * math.pi)/2)
                    e2 = (j/e2_step) * 4 * math.pi
                    x = (np.cos((e1+e2)/2) * np.sin(eta_step))
                    y = (np.sin((e1+e2)/2) * np.sin(eta_step))
                    z = (np.cos((e2-e1)/2) * np.cos(eta_step))
                    w = (np.sin((e2-e1)/2) * np.cos(eta_step))

                    proj_x = x/(1-w+non_zero)
                    proj_y = y/(1-w+non_zero)
                    proj_z = z/(1-w+non_zero)
                    vert = [proj_x,proj_y,proj_z]
                   
                    dot = sphere.copy()
                    dot.set_color(WHITE)
                    dot.move_to(vert)
                    dot_group.add(dot)
            return dot_group
        
        def hopf_curves(e2_step, eta_step):
              curve_group = Group()
              colors = [BLUE, GREEN, RED]
              for i in range (0, e2_step):
                      e2 = (i/e2_step) * 4 * math.pi
                      curve = ParametricCurve(
                          lambda u: np.array([
                              (np.cos((u+e2)/2) * np.sin(eta_step)) / (1+non_zero - (np.sin((e2-u)/2) * np.cos(eta_step))),
                              (np.sin((u+e2)/2) * np.sin(eta_step)) / (1+non_zero - (np.sin((e2-u)/2) * np.cos(eta_step))),
                              (np.cos((e2-u)/2) * np.cos(eta_step)) / (1+non_zero - (np.sin((e2-u)/2) * np.cos(eta_step)))
                          ]),
                          color = colors[i%3],
                          t_range = np.array([0, TAU, 0.01])
                      ).apply_depth_test()
                      curve_group.add(curve)
              return curve_group
       
        def hopf_lats(e2_step, eta_step, col, polarity):
            if polarity == "pos":
                curve_group = Group()
                for i in range (0, e2_step):
                        e2 = (i/e2_step) * 2 * math.pi
                        curve = ParametricCurve(
                            lambda u: np.array([
                                (np.cos(u) * np.sin(eta_step)) / (1+non_zero - np.sin(e2) * np.cos(eta_step)),
                                (np.sin(u) * np.sin(eta_step)) / (1+non_zero - np.sin(e2) * np.cos(eta_step)),
                                (np.cos(e2) * np.cos(eta_step)) / (1+non_zero - np.sin(e2) * np.cos(eta_step))
                            ]),
                            color = col,
                            t_range = np.array([0, TAU, 0.01])
                        ).set_stroke(width=stroke_size).apply_depth_test()
                        curve_group.add(curve)
            if polarity == "neg":
                curve_group = Group()
                for i in range (0, e2_step):
                        e2 = (i/e2_step) * 2 * math.pi - (((1/e2_step) * 2 * PI)/2)
                        curve = ParametricCurve(
                            lambda u: np.array([
                                (np.cos(u) * np.sin(eta_step)) / (1+non_zero - np.sin(e2) * np.cos(eta_step)),
                                (np.sin(u) * np.sin(eta_step)) / (1+non_zero - np.sin(e2) * np.cos(eta_step)),
                                (np.cos(e2) * np.cos(eta_step)) / (1+non_zero - np.sin(e2) * np.cos(eta_step))
                            ]),
                            color = col,
                            t_range = np.array([0, TAU, 0.01])
                        ).set_stroke(width=stroke_size).apply_depth_test()
                        curve_group.add(curve)
            return curve_group

        def hopf_longs(e1_step, eta_step, col, polarity):
            if polarity == "pos":
                curve_group = Group()
                for i in range (0, e1_step):
                        e1 = (i/e1_step) * 2 * math.pi
                        curve = ParametricCurve(
                            lambda u: np.array([
                                (np.cos(e1) * np.sin(eta_step)) / (1+non_zero - np.sin(u) * np.cos(eta_step)),
                                (np.sin(e1) * np.sin(eta_step)) / (1+non_zero - np.sin(u) * np.cos(eta_step)),
                                (np.cos(u) * np.cos(eta_step)) / (1+non_zero - np.sin(u) * np.cos(eta_step))
                            ]),
                            color = col,
                            t_range = np.array([0, TAU, 0.01])
                        ).set_stroke(width=stroke_size).apply_depth_test()
                        curve_group.add(curve)
            if polarity == "neg":
                curve_group = Group()
                for i in range (0, e1_step):
                        e1 = ((i/e1_step) * 2 * math.pi) - (((1/e1_step) * 2 * PI)/2)
                        curve = ParametricCurve(
                            lambda u: np.array([
                                (np.cos(e1) * np.sin(eta_step)) / (1+non_zero - np.sin(u) * np.cos(eta_step)),
                                (np.sin(e1) * np.sin(eta_step)) / (1+non_zero - np.sin(u) * np.cos(eta_step)),
                                (np.cos(u) * np.cos(eta_step)) / (1+non_zero - np.sin(u) * np.cos(eta_step))
                            ]),
                            color = col,
                            t_range = np.array([0, TAU, 0.01])
                        ).set_stroke(width=stroke_size).apply_depth_test()
                        curve_group.add(curve)
            return curve_group
       
        def hopf_hypers(e1, e2_step, col, polarity):
            if polarity == "pos":
                curve_group = Group()
                for i in range (0, e2_step):
                    e2 = (i / e2_step) * PI
                    curve = ParametricCurve(
                        lambda u: np.array([
                            (np.cos(e1) * np.sin(u)) / (1+non_zero - np.sin(e2) * np.cos(u)),
                            (np.sin(e1) * np.sin(u)) / (1+non_zero - np.sin(e2) * np.cos(u)),
                            (np.cos(e2) * np.cos(u)) / (1+non_zero - np.sin(e2) * np.cos(u))
                        ]),
                        color = col,
                        t_range = np.array([0, TAU, 0.01])
                    ).set_stroke(width=stroke_size).apply_depth_test()
                    curve_group.add(curve)
            if polarity == "neg":
                curve_group = Group()
                for i in range (0, e2_step):
                    e2 = ((i / e2_step) * PI) - (((1 / e2_step) * PI)/2)
                    curve = ParametricCurve(
                        lambda u: np.array([
                            (np.cos(e1) * np.sin(u)) / (1+non_zero - np.sin(e2) * np.cos(u)),
                            (np.sin(e1) * np.sin(u)) / (1+non_zero - np.sin(e2) * np.cos(u)),
                            (np.cos(e2) * np.cos(u)) / (1+non_zero - np.sin(e2) * np.cos(u))
                        ]),
                        color = col,
                        t_range = np.array([0, TAU, 0.01])
                    ).set_stroke(width=stroke_size).apply_depth_test()
                    curve_group.add(curve)
            return curve_group

        def hopf_points_xy(e1_step,e2_step, eta_step, polarity):
            dot_group = Group()
            colors = [BLUE,GREEN,RED]
            new_sphere = Sphere(radius=sphere_size, resolution = (10,10))
            if polarity == "pos":
                for i in range (0, e1_step):
                    for j in range (0, e2_step):
                        e1 = (i/e1_step) * 2 * math.pi
                        e2 = (j/e2_step) * 2 * math.pi

                        x = (np.cos(e1) * np.sin(eta_step)) / (1+non_zero - np.sin(e2) * np.cos(eta_step))
                        y = (np.sin(e1) * np.sin(eta_step)) / (1+non_zero - np.sin(e2) * np.cos(eta_step))
                        z = (np.cos(e2) * np.cos(eta_step)) / (1+non_zero - np.sin(e2) * np.cos(eta_step))
                            
                        dot = new_sphere.copy()
                        dot.set_color(colors[(i+j)%3])
                        dot.move_to([x,y,z]).apply_depth_test()
                        dot_group.add(dot)
            if polarity == "neg":
                for i in range (0, e1_step):
                    for j in range (0, e2_step):
                        e1 = ((i/e1_step) * 2 * math.pi) - (((1/e1_step) * 2 * math.pi)/2)
                        e2 = ((j/e2_step) * 2 * math.pi) - (((1/e2_step) * 2 * math.pi)/2)

                        x = (np.cos(e1) * np.sin(eta_step)) / (1+non_zero - np.sin(e2) * np.cos(eta_step))
                        y = (np.sin(e1) * np.sin(eta_step)) / (1+non_zero - np.sin(e2) * np.cos(eta_step))
                        z = (np.cos(e2) * np.cos(eta_step)) / (1+non_zero - np.sin(e2) * np.cos(eta_step))
                            
                        dot = new_sphere.copy()
                        dot.set_color(WHITE)
                        dot.move_to([x,y,z]).apply_depth_test()
                        dot_group.add(dot)
            return dot_group

        def hopf_points_yz(e1_step,e2_step, eta_step, polarity):
            dot_group = Group()
            colors = [BLUE,GREEN,RED]
            new_sphere = Sphere(radius=sphere_size)
            if polarity == "pos":
                for i in range (0, e1_step):
                    for j in range (0, eta_step):
                        e1 = (i/e1_step) * 2 * math.pi
                        eta = (j/eta_step) * 2 * math.pi

                        x = (np.cos(e1) * np.sin(eta)) / (1+non_zero - np.sin(e2_step) * np.cos(eta))
                        y = (np.sin(e1) * np.sin(eta)) / (1+non_zero - np.sin(e2_step) * np.cos(eta))
                        z = (np.cos(e2_step) * np.cos(eta)) / (1+non_zero - np.sin(e2_step) * np.cos(eta))
                            
                        dot = new_sphere.copy()
                        dot.set_color(colors[(i+j)%3])
                        dot.move_to([x,y,z]).apply_depth_test()
                        dot_group.add(dot)
            if polarity == "neg":
                for i in range (0, e1_step):
                    for j in range (0, eta_step):
                        e1 = ((i/e1_step) * 2 * math.pi) - (((1/e1_step) * 2 * math.pi)/2)
                        eta = ((j/eta_step) * 2 * math.pi) - (((1/eta_step) * 2 * math.pi)/2)

                        x = (np.cos(e1) * np.sin(eta)) / (1+non_zero - np.sin(e2_step) * np.cos(eta))
                        y = (np.sin(e1) * np.sin(eta)) / (1+non_zero - np.sin(e2_step) * np.cos(eta))
                        z = (np.cos(e2_step) * np.cos(eta)) / (1+non_zero - np.sin(e2_step) * np.cos(eta))
                            
                        dot = new_sphere.copy()
                        dot.set_color(WHITE)
                        dot.move_to([x,y,z]).apply_depth_test()
                        dot_group.add(dot)
            return dot_group

        def hopf_points_xz(e1_step,e2_step, eta_step, polarity):
            dot_group = Group()
            colors = [BLUE,GREEN,RED]
            new_sphere = Sphere(radius=sphere_size)
            if polarity == "pos":
                for i in range (0, e2_step):
                    for j in range (0, eta_step):
                        e2 = (i/e2_step) * 2 * math.pi
                        eta = (j/eta_step) * 2 * math.pi

                        x = (np.cos(e1_step) * np.sin(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                        y = (np.sin(e1_step) * np.sin(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                        z = (np.cos(e2) * np.cos(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                            
                        dot = new_sphere.copy()
                        dot.set_color(colors[(i+j)%3])
                        dot.move_to([x,y,z]).apply_depth_test()
                        dot_group.add(dot)
            if polarity == "neg":
                for i in range (0, e2_step):
                    for j in range (0, eta_step):
                        e2 = ((i/e2_step) * 2 * math.pi) - (((1/e2_step) * 2 * math.pi)/2)
                        eta = ((j/eta_step) * 2 * math.pi) - (((1/eta_step) * 2 * math.pi)/2)

                        x = (np.cos(e1_step) * np.sin(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                        y = (np.sin(e1_step) * np.sin(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                        z = (np.cos(e2) * np.cos(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                            
                        dot = new_sphere.copy()
                        dot.set_color(WHITE)
                        dot.move_to([x,y,z]).apply_depth_test()
                        dot_group.add(dot)
            return dot_group

        def surface_xy(eta_step, col):
            xy_surface = ParametricSurface(
                lambda u,v: np.array([
                    (np.cos(u) * np.sin(eta_step)) / (1+non_zero - np.sin(v) * np.cos(eta_step)),
                    (np.sin(u) * np.sin(eta_step)) / (1+non_zero - np.sin(v) * np.cos(eta_step)),
                    (np.cos(v) * np.cos(eta_step)) / (1+non_zero - np.sin(v) * np.cos(eta_step))
                ]),
                u_range = (0, TAU),
                v_range = (0, TAU),
                color = col,
            )
            xy_surface.apply_depth_test()
            return xy_surface

        def surface_xz(e2_step, col):
            xz_surface = ParametricSurface(
                lambda u,v: np.array([
                    (np.cos(u) * np.sin(v)) / (1+non_zero - np.sin(e2_step) * np.cos(v)),
                    (np.sin(u) * np.sin(v)) / (1+non_zero - np.sin(e2_step) * np.cos(v)),
                    (np.cos(e2_step) * np.cos(v)) / (1+non_zero - np.sin(e2_step) * np.cos(v))
                ]),
                u_range = (0, TAU/2),
                v_range = (0, TAU),
                color = col,
            ).apply_depth_test()
            xz_surface.set_opacity(surface_opacity)
            return xz_surface
       
        def surface_yz(e1_step, col):
            yz_surface = ParametricSurface(
                lambda u,v: np.array([
                    (np.cos(e1_step) * np.sin(v)) / (1+non_zero - np.sin(u) * np.cos(v)),
                    (np.sin(e1_step) * np.sin(v)) / (1+non_zero - np.sin(u) * np.cos(v)),
                    (np.cos(u) * np.cos(v)) / (1+non_zero - np.sin(u) * np.cos(v))
                ]),
                u_range = (0, TAU/2),
                v_range = (0, TAU),
                color = col,
            )
            yz_surface.set_opacity(surface_opacity)
            yz_surface.apply_depth_test()
            return yz_surface
        
        def doubling_surface(eta_step, col):
            surface = ParametricSurface(
                lambda u, v: np.array([
                    (np.cos((u+v)/2) * np.sin(eta_step)) / (1+non_zero - (np.sin((v-u)/2) * np.cos(eta_step))),
                    (np.sin((u+v)/2) * np.sin(eta_step)) / (1+non_zero - (np.sin((v-u)/2) * np.cos(eta_step))),
                    (np.cos((v-u)/2) * np.cos(eta_step)) / (1+non_zero - (np.sin((v-u)/2) * np.cos(eta_step)))
                ]),
                u_range=(0, 2 * TAU/12),
                v_range=(0, 2 * TAU),
                color=col,
            )
            surface.set_opacity(0.7)
            surface.apply_depth_test()
            return surface
        
        # TRACKERS
        
        eta_step_tracker = ValueTracker(PI/4)
        eta_length = ValueTracker(PI/2)
        e1_length = ValueTracker(0)
        e2_length = ValueTracker(0) 
 
        # INITIALISERS

        xy_points_pos = hopf_points_xy(18,18, eta_step_tracker.get_value(),"pos")
        xy_points_neg = hopf_points_xy(18,18, eta_step_tracker.get_value(),"neg")
        yz_points_pos = hopf_points_yz(18, eta_step_tracker.get_value(),18,"pos")
        yz_points_neg = hopf_points_yz(18, eta_step_tracker.get_value(),18,"neg")
        xz_points_pos = hopf_points_xz(eta_step_tracker.get_value(),18,18,"pos")
        xz_points_neg = hopf_points_xz(eta_step_tracker.get_value(),18,18,"neg")
        hopf_points_pos = always_redraw(lambda: hopf_verts_pos(18, 18, eta_step_tracker.get_value(),"xy"))
        hopf_points_neg = always_redraw(lambda: hopf_verts_neg(18, 18, eta_step_tracker.get_value()))

        latitudes_pos = hopf_lats(18, eta_step_tracker.get_value(), WHITE, "pos")
        latitudes_neg = hopf_lats(18, eta_step_tracker.get_value(), BLUE, "neg")
        longitudes_pos = hopf_longs(18, eta_step_tracker.get_value(), WHITE, "pos")
        longitudes_neg = hopf_longs(18, eta_step_tracker.get_value(), BLUE, "neg")
        hypers_pos = hopf_hypers(PI/3, 18, WHITE, "pos")
        hypers_neg = hopf_hypers(PI/3, 18, BLUE, "neg")
        curves = hopf_curves(36, eta_step_tracker.get_value())

        xy = surface_xy(eta_step_tracker.get_value(), WHITE)
        xz = surface_xz(PI/3, RED)
        yz = surface_yz(PI/3, GREEN)
        surface_doubling = doubling_surface(eta_step_tracker.get_value(), RED)

        eta_path = always_redraw(lambda: ParametricCurve(
                lambda u: np.array([
                    (np.cos(0) * np.sin(u)) / (1+non_zero - np.sin(0) * np.cos(u)),
                    (np.sin(0) * np.sin(u)) / (1+non_zero - np.sin(0) * np.cos(u)),
                    (np.cos(0) * np.cos(u)) / (1+non_zero - np.sin(0) * np.cos(u))
                ]),
                color = YELLOW,
                t_range = np.array([PI/2, eta_length.get_value(), 0.01])
            ).apply_depth_test()
        )
        e2_path = always_redraw(lambda: ParametricCurve(
                lambda u: np.array([
                        (np.cos(0) * np.sin(eta_length.get_value())) / (1+non_zero - np.sin(u) * np.cos(eta_length.get_value())),
                        (np.sin(0) * np.sin(eta_length.get_value())) / (1+non_zero - np.sin(u) * np.cos(eta_length.get_value())),
                        (np.cos(u) * np.cos(eta_length.get_value())) / (1+non_zero - np.sin(u) * np.cos(eta_length.get_value()))
                ]),
                color = YELLOW,
                t_range = np.array([0,e2_length.get_value(),0.01])
            ).apply_depth_test()
        )
        e1_path = always_redraw(lambda: ParametricCurve(
                lambda u: np.array([
                        (np.cos(u) * np.sin(eta_length.get_value())) / (1+non_zero - np.sin(e2_length.get_value()) * np.cos(eta_length.get_value())),
                        (np.sin(u) * np.sin(eta_length.get_value())) / (1+non_zero - np.sin(e2_length.get_value()) * np.cos(eta_length.get_value())),
                        (np.cos(e2_length.get_value()) * np.cos(eta_length.get_value())) / (1+non_zero - np.sin(e2_length.get_value()) * np.cos(eta_length.get_value()))
                ]),
                color = YELLOW,
                t_range = np.array([0,e1_length.get_value(),0.01])
            ).apply_depth_test()
        )
        dot_path = always_redraw(
                lambda: Sphere(radius=sphere_size+0.02).set_color(YELLOW).move_to([
                        (np.cos(e1_length.get_value()) * np.sin(eta_length.get_value())) / (1+non_zero - np.sin(e2_length.get_value()) * np.cos(eta_length.get_value())),
                        (np.sin(e1_length.get_value()) * np.sin(eta_length.get_value())) / (1+non_zero - np.sin(e2_length.get_value()) * np.cos(eta_length.get_value())),
                        (np.cos(e2_length.get_value()) * np.cos(eta_length.get_value())) / (1+non_zero - np.sin(e2_length.get_value()) * np.cos(eta_length.get_value()))
                    ]
                ).apply_depth_test()
            )

        # CAMERA STUFF

        frame = self.camera.frame
        frame.set_euler_angles(
            theta=45*DEGREES,
            phi=45*DEGREES,
        )
        # frame.add_updater(lambda m, dt: m.increment_theta(-0.1*dt))

        # SCENE STUFF
        # self.add(surface_xy(PI/3,BLUE))

        # self.add(eta_path, e1_path, e2_path, dot_path)
        # self.add(latitudes_pos)
        # self.add(latitudes_neg)
        # self.add(longitudes_pos)
        # self.add(longitudes_neg)
        # self.add(hypers_pos)
        # self.add(hypers_neg)
        # self.play(eta_length.animate.set_value(PI/3))
        # self.wait()
        # self.play(e2_length.animate.set_value(PI/3))
        # self.wait()
        # self.play(e1_length.animate.set_value(PI/3))
        # self.wait()
        # self.add(hopf_points_pos)
        # self.add(hopf_points_neg)
        self.add(xy_points_pos)
        self.add(xy_points_neg)
        # self.add(curves)
        # self.add(yz_points_pos)
        # self.add(yz_points_neg)
        # self.add(xz_points_pos)
        # self.add(xz_points_neg)
        # self.play(ShowCreation(curves))
        # self.add(latitudes_pos)
        # self.add(latitudes_neg)
        # self.add(longitudes_pos)
        # self.add(longitudes_neg)

        # self.add(xy)
        # self.add(xz)
        # self.add(yz)
        # # self.add(surface_doubling)
        # self.play(eta_step_tracker.animate.set_value(-PI), rate_func=linear, run_time = 10)
        # self.play(eta_step_tracker.animate.set_value(PI), run_time = 10)

        # self.wait(3)

