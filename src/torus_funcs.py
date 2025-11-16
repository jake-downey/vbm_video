from manimlib import *

sphere_size = 0.03
stroke_size = 2
surface_opacity = .5
non_zero = 0.0001

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
    new_sphere = Sphere(radius=sphere_size, resolution = (30,30))
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
    new_sphere = Sphere(radius=sphere_size, resolution = (30,30))
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
    new_sphere = Sphere(radius=sphere_size, resolution = (30,30))
    if polarity == "pos":
        for i in range (0, eta_step):
            for j in range (0, e2_step):
                e2 = (i/e2_step) * 2 * math.pi
                eta = (j/eta_step) * 2 * math.pi/4

                x = (np.cos(e1_step) * np.sin(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                y = (np.sin(e1_step) * np.sin(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                z = (np.cos(e2) * np.cos(eta)) / (1+non_zero - np.sin(e2) * np.cos(eta))
                    
                dot = new_sphere.copy()
                dot.set_color(colors[(i+j)%3])
                dot.move_to([x,y,z]).apply_depth_test()
                dot_group.add(dot)
    if polarity == "neg":
        for i in range (0, eta_step):
            for j in range (0, e2_step):
                e2 = ((i/e2_step) * 2 * math.pi) - (((1/e2_step) * 2 * math.pi)/2)
                eta = (((j/eta_step) * 2 * math.pi) - (((1/eta_step) * 2 * math.pi)/2))/4

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
