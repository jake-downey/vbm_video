from manimlib import *
import sys
sys.path.append("C:/Users/thund/Downloads/manim-master/manimprojects")
from torus_funcs import *
from dots_example import *

class CubeSort(Scene):
    def construct(self):

    ### FRAME INFORMATION

        frame = self.camera.frame
        frame.set_euler_angles(
            theta=60*DEGREES,
            phi=60*DEGREES,
        )
        frame.scale(1.5)
        # frame.add_updater(lambda m, dt: m.increment_theta(-0.1*dt))



    ### POSITIVE GRID GENERATORS

        def cube_dots_pos(num_rows, num_cols, num_z):
            
            r = sphere_size
            sphere = Sphere(radius = sphere_size, resolution = (30,30))
            col = [GREEN, RED, BLUE]
            
            xyz_group = Group()
            for k in range(-num_z,num_z+1):

                xy_group = Group()
                for i in range(-num_cols, num_cols+1):
                    
                    x_group = Group()
                    for j in range(-num_rows, num_rows+1):
                        dot = sphere.copy()
                        dot.move_to([i, j, k])
                        dot.set_color(col[(k+i+j)%3])
                        x_group.add(dot)
                    xy_group.add(x_group)

                xyz_group.add(xy_group)

            return xyz_group
        
        def cylinder_dots_pos(num_rows, num_cols, num_z):
            r = sphere_size
            non_zero = .00001
            sphere = Sphere(radius = sphere_size, resolution = (30,30))
            col = [GREEN, RED, BLUE]
            
            xyz_group = Group()
            for k in range(0,num_z):

                xy_group = Group()
                for i in range(-num_cols, num_cols+1):
                    
                    x_group = Group()
                    for j in range(0, num_rows):

                        dot = sphere.copy()
                        radius = np.sin((k / num_z) * (PI)) / (1-np.cos((k / num_z) * (PI)) + non_zero)
                        x = radius * np.sin((j / num_rows) * TAU)
                        y = radius * np.cos((j / num_rows) * TAU)
                        z = i / 2

                        dot.move_to([x, y, z])
                        dot.set_color(col[(k+i+j)%3])
                        x_group.add(dot)
                    xy_group.add(x_group)

                xyz_group.add(xy_group)

            return xyz_group

        def torus_dots_pos(e1_step, e2_step, eta_step):

            r = sphere_size
            non_zero = .00001
            sphere = Sphere(radius = sphere_size, resolution = (30,30))
            col = [GREEN, RED, BLUE]

            xyz_group = Group()
            for k in range(0,eta_step):

                xy_group = Group()
                for i in range (0, e1_step):

                    x_group = Group()
                    for j in range (0, e2_step):

                        dot = sphere.copy()

                        e1 = (i/e1_step) * 2 * PI
                        e2 = (j/e2_step) * 2 * PI
                        eta = (k/eta_step) * (PI/2)
                        
                        x = (np.cos(e1) * np.sin(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                        y = (np.sin(e1) * np.sin(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                        z = (np.cos(e2) * np.cos(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                        
                        dot.move_to([x,y,z])
                        dot.set_color(col[(k+i+j)%3])
                        x_group.add(dot)
                    xy_group.add(x_group)

                xyz_group.add(xy_group)
            return xyz_group

    ### NEGATIVE GRID GENERATORS

        def cube_dots_neg(num_rows, num_cols, num_z, plane):
            
            r = sphere_size
            sphere = Sphere(radius = sphere_size, resolution = (30,30))
            col = [GREEN, RED, BLUE]
            
            if plane == "xy":
                xyz_group = Group()
                for k in range(-num_z,num_z+1):

                    xy_group = Group()
                    for i in range(-num_cols, num_cols+1):
                        
                        x_group = Group()
                        for j in range(-num_rows, num_rows+1):
                            dot = sphere.copy()
                            dot.move_to([i+0.5, j+0.5, k])
                            dot.set_color(WHITE)
                            x_group.add(dot)
                        xy_group.add(x_group)

                    xyz_group.add(xy_group)

            if plane == "xz":
                xyz_group = Group()
                for k in range(-num_z,num_z+1):

                    xy_group = Group()
                    for i in range(-num_cols, num_cols+1):
                        
                        x_group = Group()
                        for j in range(-num_rows, num_rows+1):
                            dot = sphere.copy()
                            dot.move_to([i+0.5, j, k+0.5])
                            dot.set_color(WHITE)
                            x_group.add(dot)
                        xy_group.add(x_group)

                    xyz_group.add(xy_group)
            if plane == "yz":

                xyz_group = Group()
                for k in range(-num_z,num_z+1):

                    xy_group = Group()
                    for i in range(-num_cols, num_cols+1):
                        
                        x_group = Group()
                        for j in range(-num_rows, num_rows+1):
                            dot = sphere.copy()
                            dot.move_to([i, j+0.5, k+0.5])
                            dot.set_color(WHITE)
                            x_group.add(dot)
                        xy_group.add(x_group)

                    xyz_group.add(xy_group)

            return xyz_group

        def cylinder_dots_neg(num_rows, num_cols, num_z, plane):
            r = sphere_size
            non_zero = .00001
            sphere = Sphere(radius = sphere_size, resolution = (30,30))
            col = [GREEN, RED, BLUE]
            
            if plane == "xy":
                xyz_group = Group()
                for k in range(0,num_z):

                    xy_group = Group()
                    for i in range(-num_cols, num_cols+1):
                        
                        x_group = Group()
                        for j in range(0, num_rows):

                            dot = sphere.copy()
                            radius = np.sin((((k / num_z) * PI)) + ((1 / (2 * num_z)) * PI)) / (1-np.cos(((k / num_z) * (PI)) + ((1 / (2*num_z)) * PI)) + non_zero)
                            x = radius * np.sin(((j / num_rows) * TAU) + ((1 / (2 * num_rows)) * TAU))
                            y = radius * np.cos(((j / num_rows) * TAU) + ((1 / (2 * num_rows)) * TAU))
                            z = (i / 2)

                            dot.move_to([x, y, z])
                            dot.set_color(WHITE)
                            x_group.add(dot)
                        xy_group.add(x_group)

                    xyz_group.add(xy_group)

            if plane == "xz":
                xyz_group = Group()
                for k in range(0,num_z):

                    xy_group = Group()
                    for i in range(-num_cols, num_cols+1):
                        
                        x_group = Group()
                        for j in range(0, num_rows):

                            dot = sphere.copy()
                            radius = np.sin((k / num_z) * (PI)) / (1-np.cos(((k / num_z) * (PI))) + non_zero)
                            x = radius * np.sin(((j / num_rows) * TAU) + ((1 / (2 * num_rows)) * TAU))
                            y = radius * np.cos(((j / num_rows) * TAU) + ((1 / (2 * num_rows)) * TAU))
                            z = (i / 2) + (1/4)

                            dot.move_to([x, y, z])
                            dot.set_color(WHITE)
                            x_group.add(dot)
                        xy_group.add(x_group)

                    xyz_group.add(xy_group)

            if plane == "yz":
                xyz_group = Group()
                for k in range(0,num_z):

                    xy_group = Group()
                    for i in range(-num_cols, num_cols+1):
                        
                        x_group = Group()
                        for j in range(0, num_rows):

                            dot = sphere.copy()
                            radius = np.sin((((k / num_z) * PI)) + ((1 / (2 * num_z)) * PI)) / (1-np.cos(((k / num_z) * (PI)) + ((1 / (2*num_z)) * PI)) + non_zero)
                            x = radius * np.sin((j / num_rows) * TAU)
                            y = radius * np.cos((j / num_rows) * TAU)
                            z = (i / 2) + (1/4)

                            dot.move_to([x, y, z])
                            dot.set_color(WHITE)
                            x_group.add(dot)
                        xy_group.add(x_group)

                    xyz_group.add(xy_group)

            return xyz_group

        def torus_dots_neg(e1_step, e2_step, eta_step, plane):

            r = sphere_size
            non_zero = .00001
            sphere = Sphere(radius = sphere_size, resolution = (30,30))
            col = [GREEN, RED, BLUE]

            if plane == "xy":
                xyz_group = Group()
                for k in range(0,eta_step):

                    xy_group = Group()
                    for i in range (0, e1_step):

                        x_group = Group()
                        for j in range (0, e2_step):

                            dot = sphere.copy()

                            e1 = ((i/e1_step) * 2 * PI) + ((1 / (2 * e1_step)) * TAU)
                            e2 = ((j/e2_step) * 2 * PI) + ((1 / (2 * e2_step)) * TAU)
                            eta = ((k/eta_step) * (PI/2))
                            
                            x = (np.cos(e1) * np.sin(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                            y = (np.sin(e1) * np.sin(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                            z = (np.cos(e2) * np.cos(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                            
                            dot.move_to([x,y,z])
                            dot.set_color(WHITE)
                            x_group.add(dot)
                        xy_group.add(x_group)

                    xyz_group.add(xy_group)

            if plane == "xz":
                xyz_group = Group()
                for k in range(0,eta_step):

                    xy_group = Group()
                    for i in range (0, e1_step):

                        x_group = Group()
                        for j in range (0, e2_step):

                            dot = sphere.copy()

                            e1 = ((i/e1_step) * 2 * PI) + ((1 / (2 * e1_step)) * TAU)
                            e2 = ((j/e2_step) * 2 * PI) 
                            eta = ((k/eta_step) * (PI/2)) + ((1 / (2 * eta_step)) * (PI/2))
                            
                            x = (np.cos(e1) * np.sin(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                            y = (np.sin(e1) * np.sin(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                            z = (np.cos(e2) * np.cos(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                            
                            dot.move_to([x,y,z])
                            dot.set_color(WHITE)
                            x_group.add(dot)
                        xy_group.add(x_group)

                    xyz_group.add(xy_group)

            if plane == "yz":
                xyz_group = Group()
                for k in range(0,eta_step):

                    xy_group = Group()
                    for i in range (0, e1_step):

                        x_group = Group()
                        for j in range (0, e2_step):

                            dot = sphere.copy()

                            e1 = ((i/e1_step) * 2 * PI) 
                            e2 = ((j/e2_step) * 2 * PI) + ((1 / (2 * e2_step)) * TAU)
                            eta = ((k/eta_step) * (PI/2)) + ((1 / (2 * eta_step)) * (PI/2))
                            
                            x = (np.cos(e1) * np.sin(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                            y = (np.sin(e1) * np.sin(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                            z = (np.cos(e2) * np.cos(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                            
                            dot.move_to([x,y,z])
                            dot.set_color(WHITE)
                            x_group.add(dot)
                        xy_group.add(x_group)

                    xyz_group.add(xy_group)

            return xyz_group

    ### NATURAL SLICES

        def return_point(dot_group, x, y, z):
            point = dot_group[x][y][z]
            return point

        def return_line(dot_group, off_a, off_b, axis):
            
            if axis == "x":
                return dot_group[off_a][off_b]

            if axis == "y":
                line_group = Group()
                for i in range(0, len(dot_group[0])):
                    line_group.add(dot_group[off_b][i][off_a])
                return line_group

            if axis == "z":
                line_group = Group()
                for i in range(0, len(dot_group)):
                    line_group.add(dot_group[i][off_a][off_b])
                return line_group

        def return_plane(dot_group, offset, plane):
            if plane == "xy":
                return dot_group[offset]

            if plane == "xz":
                plane_group = Group()
                for i in range(0,len(dot_group)):
                    plane_group.add(dot_group[i][offset])
                return plane_group

            if plane == "yz":
                plane_group = Group()
                for i in range(0,len(dot_group)):
                    for j in range(0,len(dot_group[0])):
                        plane_group.add(dot_group[i][j][offset])
                return plane_group

    ### DOUBLING SLICES

        def return_doubling_line(dot_group, offset, off_axis, plane):

            if plane == "xy":
                line_group = Group()
                for i in range(0,len(dot_group[0])):
                    line_group.add(dot_group[offset][((len(dot_group[0])-1)-i)][(off_axis + i) % len(dot_group[0][0])])
                return line_group

            if plane == "xz":
                line_group = Group()
                for i in range(0,len(dot_group)): 
                    line_group.add(dot_group[(len(dot_group)-1)-i][offset % len(dot_group[0])][(off_axis + i) % len(dot_group[0][0])])
                return line_group

            if plane == "yz":
                line_group = Group()
                for i in range(0,len(dot_group)):
                    line_group.add(dot_group[(len(dot_group)-1)-i][(off_axis + i) % len(dot_group[0])][offset% len(dot_group[0][0])])
                return line_group

        def return_doubling_surface(dot_group, off_axis, plane):
            line_group = Group()
            for i in range(0,len(dot_group)):
                line_group.add(return_doubling_line(dot_group, i, -i+off_axis, plane))
            return line_group

    ### LATS, LONGS, HYPERS

        def hopf_lats(e2_step, eta_step, col, polarity, u_start, u_end):
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
                            t_range = np.array([u_start, u_end, 0.01])
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
                            t_range = np.array([u_start, u_end, 0.01])
                        ).set_stroke(width=stroke_size).apply_depth_test()
                        curve_group.add(curve)
            return curve_group

        def hopf_longs(e1_step, eta_step, col, polarity, u_start, u_end):
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
                            t_range = np.array([u_start, u_end, 0.01])
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
                            t_range = np.array([u_start, u_end, 0.01])
                        ).set_stroke(width=stroke_size).apply_depth_test()
                        curve_group.add(curve)
            return curve_group

        def hopf_hypers(e1, e2_step, col, polarity, u_start, u_end):
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
                        t_range = np.array([u_start, u_end, 0.01])
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
                        t_range = np.array([u_start, u_end, 0.01])
                    ).set_stroke(width=stroke_size).apply_depth_test()
                    curve_group.add(curve)
            return curve_group

    ### CURVE AND SURFACE GENERATORS

        def smooth_curve(points, color="#58C4DD", width=6, close_path=False):

            pts = np.array(points, dtype=float)
            if pts.shape[1] == 2:
                # lift to 3D for ManimGL's internal representation
                pts = np.column_stack([pts, np.zeros(len(pts))])

            curve = VMobject()
            # This constructs a smooth set of cubic Beziers that interpolate the anchors
            curve.set_points_smoothly(pts)
            if close_path:
                curve.close_path()

            curve.set_stroke(color=color, width=width)
            return curve

    ### TEST SCENE

        # cube_pos = cube_dots_pos(4,4,4)
        # cube_neg_xy = cube_dots_neg(4,4,4,"xy")
        # cube_neg_xz = cube_dots_neg(4,4,4,"xz")
        # cube_neg_yz = cube_dots_neg(4,4,4,"yz")
        # cylinder = cylinder_dots_pos(18,9,18)

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

        torus_pos = torus_dots_pos(36,36,18)
        torus_neg_xy = torus_dots_neg(36,36,9,"xy")
        torus_neg_xz = torus_dots_neg(36,36,9,"xz")
        torus_neg_yz = torus_dots_neg(36,36,9,"yz")
        torus_surface = surface_xy((12/18)*(PI/2), GREY)

        plane = return_plane(torus_pos,12,"xy")

        def shift_cube(along_lat, along_long, along_hyper):
            i = along_lat
            j = along_long
            k = along_hyper
            
            lats1 = hopf_lats(36, (((k+8))/18)*(PI/2), BLACK, "pos", (((i+0))/36)*TAU, (((i+1))/36)*TAU)
            lats2 = hopf_lats(36, (((k+7))/18)*(PI/2), BLACK, "pos", (((i+0))/36)*TAU, (((i+1))/36)*TAU)
            longs1 = hopf_longs(36, (((k+8))/18)*(PI/2), BLACK, "pos", (((j+8))/36)*TAU, (((j+9))/36)*TAU)
            longs2 = hopf_longs(36, (((k+7))/18)*(PI/2), BLACK, "pos", (((j+8))/36)*TAU, (((j+9))/36)*TAU)

            hypers1 = hopf_hypers((((i+0))/36)*TAU, 18, BLACK, "pos", (((k+7))/18)*(PI/2), (((k+8))/18)*(PI/2))
            hypers2 = hopf_hypers((((i+1))/36)*TAU, 18, BLACK, "pos", (((k+7))/18)*(PI/2), (((k+8))/18)*(PI/2))

            cube = Group(
                lats1[(8+j)%36],
                lats1[(9+j)%36],
                lats2[(8+j)%36],
                lats2[(9+j)%36],
                longs1[(0+i)%36],
                longs1[(1+i)%36],
                longs2[(0+i)%36],
                longs2[(1+i)%36],
                hypers1[(8+j)%18],
                hypers1[(9+j)%18],
                hypers2[(8+j)%18],
                hypers2[(9+j)%18],
            ).set_color(YELLOW)
            return cube
        self.add(plane)
        # self.add(torus_surface)

        for i in range(0,36):
            the_cube = shift_cube(i,0,0)
            self.add(the_cube)
            self.wait(0.2)
            self.remove(the_cube)
        for i in range(0,9):
            the_cube = shift_cube(0,i,0)
            self.add(the_cube)
            self.wait(0.2)
            self.remove(the_cube)
        for i in range(0,9):
            the_cube = shift_cube(0,8-i,0)
            self.add(the_cube)
            self.wait(0.2)
            self.remove(the_cube)
        for i in range(0,9):
            the_cube = shift_cube(0,-i,0)
            self.add(the_cube)
            self.wait(0.2)
            self.remove(the_cube)
        for i in range(0,9):
            the_cube = shift_cube(0,-8+i,0)
            self.add(the_cube)
            self.wait(0.2)
            self.remove(the_cube)
        for i in range(0,72):
            the_cube = shift_cube(0,0,i)
            self.add(the_cube)
            self.wait(0.2)
            self.remove(the_cube)
        







    ### ALSO TEST SCENE


        # surface = return_doubling_line(torus_pos,8,12,"xy")
        # points1 = []
        # for s in surface:
        #     points1.append(s.get_center())
        # points1.append(points1[0])

        # surface5 = return_doubling_line(torus_pos,8,30,"xy")
        # points5 = []
        # for s in surface5:
        #     points5.append(s.get_center())
        # points5.append(points5[0])

        # surface2 = return_doubling_line(torus_pos,3,-1,"xz")
        # points2 = []
        # for s in surface2:
        #     points2.append(s.get_center())

        # surface6 = return_doubling_line(torus_pos,21,-1,"xz")
        # points6 = []
        # for s in surface6:
        #     points6.append(s.get_center())

        # surface3 = return_doubling_line(torus_pos,8,-6,"yz")
        # points3 = []
        # for s in surface3:
        #     points3.append(s.get_center())

        # surface4 = return_doubling_line(torus_pos,8,-24,"yz")
        # points4 = []
        # for s in surface4:
        #     points4.append(s.get_center())

        # line1 = smooth_curve(points1).set_color(WHITE).apply_depth_test()
        # line2 = smooth_curve(points2).set_color(WHITE).apply_depth_test()
        # line3 = smooth_curve(points3).set_color(WHITE).apply_depth_test()
        # line4 = smooth_curve(points4).set_color(WHITE).apply_depth_test()
        # line5 = smooth_curve(points5).set_color(WHITE).apply_depth_test()
        # line6 = smooth_curve(points6).set_color(WHITE).apply_depth_test()


        # # self.add(torus_surface)
        # self.add(surface)
        # self.add(surface2)
        # self.add(surface3)
        # self.add(surface4)
        # self.add(surface5)
        # self.add(surface6)
        # self.add(line1)
        # self.add(line2)
        # self.add(line3)
        # self.add(line4)
        # self.add(line5)
        # self.add(line6)
        # # self.add(torus_surface)





    ### DEMO SCENE

        # # return_point example
        # self.wait(3)
        # for i in range(0,len(cube)):
        #     for j in range(0,len(cube)):
        #         for k in range(0,len(cube)):
        #             self.add(return_point(cube,i,j,k))
        #             self.wait(0.01)
        # self.wait(3)
        # self.play(FadeOut(cube))
        # self.wait()

        # # return_line example
        # for j in range(0,len(cube)):
        #     self.add(return_line(cube,4,j,"x"))
        #     self.wait(0.5)
        # self.remove(*self.mobjects)
        # for j in range(0,len(cube)):
        #     self.add(return_line(cube,4,j,"y"))
        #     self.wait(0.5)
        # self.remove(*self.mobjects)
        # for j in range(0,len(cube)):
        #     self.add(return_line(cube,4,j,"z"))
        #     self.wait(0.5)
        # self.wait(3)
        # self.remove(*self.mobjects)

        # # return_plane example
        # for j in range(0,len(cube)):
        #     self.add(return_plane(cube,j,"xy"))
        #     self.wait(0.5)
        # self.remove(*self.mobjects)
        # for j in range(0,len(cube)):
        #     self.add(return_plane(cube,j,"xz"))
        #     self.wait(0.5)
        # self.remove(*self.mobjects)
        # for j in range(0,len(cube)):
        #     self.add(return_plane(cube,j,"yz"))
        #     self.wait(0.5)
        # self.wait(3)
        # self.remove(*self.mobjects)

        # # return_doubling_line example
        # for j in range(0,len(cube)):
        #     self.add(return_doubling_line(cube,4,j,"xy"))
        #     self.wait(0.5)
        # self.remove(*self.mobjects)
        # for j in range(0,len(cube)):
        #     self.add(return_doubling_line(cube,4,j,"xz"))
        #     self.wait(0.5)
        # self.remove(*self.mobjects)
        # for j in range(0,len(cube)):
        #     self.add(return_doubling_line(cube,4,j,"yz"))
        #     self.wait(0.5)
        # self.wait(3)
        # self.remove(*self.mobjects)

        # # return_doubling_surface example
        # for j in range(0,len(cube)):
        #     self.add(return_doubling_surface(cube,j,"xy"))
        #     self.wait(0.5)
        # self.remove(*self.mobjects)
        # for j in range(0,len(cube)):
        #     self.add(return_doubling_surface(cube,j,"xz"))
        #     self.wait(0.5)
        # self.remove(*self.mobjects)
        # for j in range(0,len(cube)):
        #     self.add(return_doubling_surface(cube,j,"yz"))
        #     self.wait(0.5)
        # self.wait(3)
        # self.remove(*self.mobjects)




        

        


