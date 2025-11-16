from manimlib import *

sphere_size = 0.1

# FUNCTIONS

def parametric_triangle(P0,P1,P2):
    v1 = P1-P0
    v2 = P2-P0
    def conditional_range(u,v):
        if u + v <=1:
            point = P0 + u * v1 + v * v2
            return np.array([point[0],point[1],point[2]])
        else:
            return
    triangle = ParametricSurface(
        lambda u,v: conditional_range(u,v),
        u_range=(0,1),
        v_range=(0,1),
        resolution = (50,50)
    )
    return triangle

def parametric_square(center, v1, v2,edge_length):
    a = edge_length *2
    def square_surface(u,v):
        return center + a*u * v1 + a*v * v2
    square_surface = ParametricSurface(
        lambda u,v: square_surface(u,v),
        u_range=(-0.5,0.5),
        v_range=(-0.5,0.5),
        resolution = (50,50)
    )
    return square_surface

def _ico_base():
    phi = (1 + 5**0.5) / 2
    V = np.array([
        [-1,  phi,  0], [ 1,  phi,  0], [-1, -phi,  0], [ 1, -phi,  0],
        [ 0, -1,  phi], [ 0,  1,  phi], [ 0, -1, -phi], [ 0,  1, -phi],
        [ phi,  0, -1], [ phi,  0,  1], [-phi,  0, -1], [-phi,  0,  1],
    ], dtype=float)
    V /= np.linalg.norm(V, axis=1, keepdims=True)
    F = [
        (0,11,5),(0,5,1),(0,1,7),(0,7,10),(0,10,11),
        (1,5,9),(5,11,4),(11,10,2),(10,7,6),(7,1,8),
        (3,9,4),(3,4,2),(3,2,6),(3,6,8),(3,8,9),
        (4,9,5),(2,4,11),(6,2,10),(8,6,7),(9,8,1)
    ]
    return [v.copy() for v in V], list(F)

def _mid_idx(i, j, verts, cache):
    k = (i, j) if i < j else (j, i)
    if k in cache: return cache[k]
    m = (verts[i] + verts[j]) * 0.5
    m /= np.linalg.norm(m)
    verts.append(m)
    idx = len(verts) - 1
    cache[k] = idx
    return idx

def _subdivide(verts, faces, levels):
    for _ in range(int(levels)):
        cache, newF = {}, []
        for a,b,c in faces:
            ab = _mid_idx(a,b,verts,cache)
            bc = _mid_idx(b,c,verts,cache)
            ca = _mid_idx(c,a,verts,cache)
            newF += [(a,ab,ca),(b,bc,ab),(c,ca,bc),(ab,bc,ca)]
        faces = newF
    return faces

# --- One parametric triangular patch on the sphere ---
def _tri_patch_surface(v1, v2, v3, center, r, color, opacity, stroke_opacity, res, depth_test):
    v1 = v1/np.linalg.norm(v1); v2 = v2/np.linalg.norm(v2); v3 = v3/np.linalg.norm(v3)
    eps = 1e-3  # trim edges to avoid degenerate jacobians
    def f(u, v):
        # Map square → triangle: s=u, t=v*(1-u), w1=1-s-t
        s = u
        t = v*(1.0 - u)
        w1 = 1.0 - s - t
        p = w1*v1 + s*v2 + t*v3
        p /= np.linalg.norm(p)
        return center + r*p
    surf = ParametricSurface(
        f, u_range=(eps, 1.0 - eps), v_range=(eps, 1.0 - eps),
        resolution=(res, res),
    ).set_color(color).set_opacity(opacity)
    if hasattr(surf, "set_stroke"): surf.set_stroke(color, stroke_opacity)
    if depth_test and hasattr(surf, "apply_depth_test"): surf.apply_depth_test()
    return surf

# --- Public: Icosphere built from ParametricSurface faces ---
def IcoDotSurface(center=(0,0,0), r=0.06, color="#AAAAAA",
                  opacity=1.0, stroke_opacity=0.0,
                  subdivisions=1, face_resolution=6, depth_test=True):
    """
    Minimal icosphere made of ParametricSurface triangle patches.
    - subdivisions: 0→20 faces, 1→80, 2→320, 3→1280, ...
    - face_resolution: grid per triangle (6–10 is plenty for small dots)
    """
    center = np.array(center, dtype=float)
    verts, faces = _ico_base()
    faces = _subdivide(verts, faces, subdivisions)
    # scale & translate verts once
    verts = [center + r*v for v in verts]

    g = Group()
    for a,b,c in faces:
        tri = _tri_patch_surface(
            verts[a] - center, verts[b] - center, verts[c] - center,
            center, r, color, opacity, stroke_opacity, face_resolution, depth_test
        )
        g.add(tri)
    return g


def dot_plane_pos(num_rows, num_cols, offset_value, plane):
    dot_group = Group()
    r = sphere_size
    sphere = Sphere(radius = sphere_size, resolution = (30,30))
    col = [GREEN, RED, BLUE]
    if plane == "xy":
        for i in range (-num_cols+1, num_cols):
            for j in range(-num_rows+1, num_rows):
                dot = sphere.copy()
                dot.move_to([i, j, offset_value])
                dot.set_color(col[(offset_value+i+j)%3])
                dot_group.add(dot)
    if plane == "xz":
        for i in range (-num_cols+1, num_cols):
            for j in range(-num_rows+1, num_rows):
                dot = sphere.copy()
                dot.move_to([i, offset_value, j])
                dot.set_color(col[(offset_value+i+j)%3])
                dot_group.add(dot)
    if plane == "yz":
        for i in range (-num_cols+1, num_cols):
            for j in range(-num_rows+1, num_rows):
                dot = sphere.copy()
                dot.move_to([offset_value, i, j])
                dot.set_color(col[(offset_value+i+j)%3])
                dot_group.add(dot)
    return dot_group

def dot_plane_neg(num_rows, num_cols, offset_value, plane):
    dot_group = Group()
    r = sphere_size
    sphere = Sphere(radius = sphere_size, resolution = (30,30))
    if plane == "xy":
        for i in range (-num_cols+1, num_cols-1):
            for j in range(-num_rows+1, num_rows-1):
                dot = sphere.copy()
                dot.move_to([i+1/2, j+1/2, offset_value])
                dot.set_color(WHITE)
                dot_group.add(dot)
    if plane == "xz":
        for i in range (-num_cols+1, num_cols-1):
            for j in range(-num_rows+1, num_rows-1):
                dot = sphere.copy()
                dot.move_to([i+1/2, offset_value, j+1/2])
                dot.set_color(WHITE)
                dot_group.add(dot)
    if plane == "yz":
        for i in range (-num_cols+1, num_cols-1):
            for j in range(-num_rows+1, num_rows-1):
                dot = sphere.copy()
                dot.move_to([offset_value, i+1/2, j+1/2])
                dot.set_color(WHITE)
                dot_group.add(dot)
    return dot_group

def dot_plane_counter(num_rows, num_cols, offset_value, plane):
    dot_group = Group()
    sphere = Sphere(radius=sphere_size)
    if plane == "xy":
        for i in range (-num_cols+1, num_cols-1):
            for j in range(-num_rows+1, num_rows-1):
                dot = sphere.copy()
                dot.move_to([i+1/2, j, 1/2+offset_value])
                dot.set_color(WHITE)
                dot_group.add(dot)
        for i in range (-num_cols+1, num_cols-1):
            for j in range(-num_rows+1, num_rows-1):
                dot = sphere.copy()
                dot.move_to([i, j+1/2, 1/2+offset_value])
                dot.set_color(WHITE)
                dot_group.add(dot)
    if plane == "xz":
        for i in range (-num_cols+1, num_cols-1):
            for j in range(-num_rows+1, num_rows-1):
                dot = sphere.copy()
                dot.move_to([i+1/2, offset_value+1/2, j])
                dot.set_color(WHITE)
                dot_group.add(dot)
        for i in range (-num_cols+1, num_cols-1):
            for j in range(-num_rows+1, num_rows-1):
                dot = sphere.copy()
                dot.move_to([i, offset_value+1/2, j+1/2])
                dot.set_color(WHITE)
                dot_group.add(dot)
    if plane == "yz":
        for i in range (-num_cols+1, num_cols-1):
            for j in range(-num_rows+1, num_rows-1):
                dot = sphere.copy()
                dot.move_to([offset_value+1/2, i+1/2, j])
                dot.set_color(WHITE)
                dot_group.add(dot)
        for i in range (-num_cols+1, num_cols-1):
            for j in range(-num_rows+1, num_rows-1):
                dot = sphere.copy()
                dot.move_to([offset_value+1/2, i, j+1/2])
                dot.set_color(WHITE)
                dot_group.add(dot)
    return dot_group

def grid_pos_xyz(num_dots, offset_value, plane, stroke):
    horiz_lines = Group()
    vert_lines = Group()
    if plane == "xy":
        for i in range (-num_dots, num_dots+1):
            horiz_line = Line([num_dots, i, offset_value], [-(num_dots), i, offset_value], color = WHITE, stroke_width = stroke)
            vert_line = Line([i, num_dots, offset_value], [i, -(num_dots), offset_value], color = WHITE, stroke_width = stroke)
            horiz_lines.add(horiz_line.apply_depth_test())
            vert_lines.add(vert_line.apply_depth_test())
    if plane == "xz":
        for i in range (-num_dots, num_dots+1):
            horiz_line = Line([num_dots, offset_value, i], [-(num_dots), offset_value, i], color = WHITE, stroke_width = stroke)
            vert_line = Line([i, offset_value, num_dots], [i, offset_value, -(num_dots)], color = WHITE, stroke_width = stroke)
            horiz_lines.add(horiz_line.apply_depth_test())
            vert_lines.add(vert_line.apply_depth_test())
    if plane == "yz":
        for i in range (-num_dots, num_dots+1):
            horiz_line = Line([offset_value, num_dots, i], [offset_value, -(num_dots), i], color = WHITE, stroke_width = stroke)
            vert_line = Line([offset_value, i, num_dots], [offset_value, i, -(num_dots)], color = WHITE, stroke_width = stroke)
            horiz_lines.add(horiz_line.apply_depth_test())
            vert_lines.add(vert_line.apply_depth_test())
    return [horiz_lines, vert_lines]

def grid_neg_xyz(num_dots, offset_value, plane, stroke):
    horiz_lines = Group()
    vert_lines = Group()
    if plane == "xy":
        for i in range (-num_dots, num_dots):
            horiz_line = Line([num_dots+0.5, i, offset_value+0.5], [-(num_dots+0.5), i, offset_value+0.5], color = GREY, stroke_width = stroke)
            vert_line = Line([i+0.5, num_dots+0.5, offset_value+0.5], [i+0.5, -(num_dots+0.5), offset_value+0.5], color = GREY, stroke_width = stroke)
            horiz_lines.add(horiz_line.apply_depth_test())
            vert_lines.add(vert_line.apply_depth_test())
    if plane == "xz":
        for i in range (-num_dots, num_dots):
            horiz_line = Line([num_dots+0.5, offset_value+0.5, i], [-(num_dots+0.5), offset_value+0.5, i], color = GREY, stroke_width = stroke)
            vert_line = Line([i+0.5, offset_value+0.5, num_dots], [i+0.5, offset_value+0.5, -(num_dots)], color = GREY, stroke_width = stroke)
            horiz_lines.add(horiz_line.apply_depth_test())
            vert_lines.add(vert_line.apply_depth_test())
    if plane == "yz":
        for i in range (-num_dots, num_dots):
            horiz_line = Line([offset_value+0.5, num_dots+0.5, i], [offset_value+0.5, -(num_dots+0.5), i], color = GREY, stroke_width = stroke)
            vert_line = Line([offset_value+0.5, i+0.5, num_dots], [offset_value+0.5, i+0.5, -(num_dots)], color = GREY, stroke_width = stroke)
            horiz_lines.add(horiz_line.apply_depth_test())
            vert_lines.add(vert_line.apply_depth_test())

    return [horiz_lines, vert_lines]

def make_box_grid(num_dots,stroke):
    grids = Group()
    for i in range(-num_dots, num_dots+1):
        xy_grid_vert = grid_pos_xyz(num_dots,i,"xy",stroke)[0]
        xy_grid_horiz = grid_pos_xyz(num_dots,i,"xy",stroke)[1]
        xz_grid_vert = grid_pos_xyz(num_dots,i,"xz",stroke)[0]
        xz_grid_horiz = grid_pos_xyz(num_dots,i,"xz",stroke)[1]
        yz_grid_vert = grid_pos_xyz(num_dots,i,"yz",stroke)[0]
        yz_grid_horiz = grid_pos_xyz(num_dots,i,"yz",stroke)[1]
        grids.add(
            xy_grid_vert, xy_grid_horiz,
            xz_grid_vert, xz_grid_horiz,
            yz_grid_vert, yz_grid_horiz,
        )
    return grids

def doubling_curve_xyz(num_dots, offset_value, plane):
    curve_group = Group()
    col = [RED, BLUE, GREEN]
    if plane == "xy":
        for i in range (-num_dots, (num_dots)+1):
            curve = Line(
                [i, num_dots, offset_value],
                [num_dots, i, offset_value],
                color=col[(i+1+offset_value)%3]
            )
            curve_group.add(curve)
            curve2 = Line(
                [i, -num_dots, offset_value],
                [-num_dots, i, offset_value],
                color=col[(i+offset_value)%3]
            )
            curve_group.add(curve2)
    if plane == "xz":
        for i in range (-num_dots, (num_dots)+1):
            curve = Line(
                [i, offset_value, num_dots],
                [num_dots, offset_value, i],
                color=col[(i+1+offset_value)%3]
            )
            curve_group.add(curve)
            curve2 = Line(
                [i, offset_value, -num_dots],
                [-num_dots, offset_value, i],
                color=col[(i+offset_value)%3]
            )
            curve_group.add(curve2)
    if plane == "yz":
        for i in range (-num_dots, (num_dots)+1):
            curve = Line(
                [offset_value, i, num_dots],
                [offset_value, num_dots, i],
                color=col[(i+1+offset_value)%3]
            )
            curve_group.add(curve)
            curve2 = Line(
                [offset_value, i, -num_dots],
                [offset_value, -num_dots, i],
                color=col[(i+offset_value)%3]
            )
            curve_group.add(curve2)
    return curve_group

def plane_pos_xyz(num_dots, offset_value, plane):
    if plane == "xy":
        plane_surf = parametric_square(
            np.array([0,0,offset_value]),
            np.array([num_dots,0,0]),
            np.array([0,num_dots,0]),
            1,
        )
    if plane == "xz":
        plane_surf = parametric_square(
            np.array([0,offset_value,0]),
            np.array([num_dots,0,0]),
            np.array([0,0,num_dots]),
            1,
        )
    if plane == "yz":
        plane_surf = parametric_square(
            np.array([offset_value,0,0]),
            np.array([0,num_dots,0]),
            np.array([0,0,num_dots]),
            1,
        )
    return plane_surf

def plane_neg_xyz(num_dots, offset_value, plane):
    if plane == "xy":
        plane_surf = parametric_square(
            np.array([0,0,offset_value+0.5]),
            np.array([num_dots,0,0]),
            np.array([0,num_dots,0]),
            1,
        )
    if plane == "xz":
        plane_surf = parametric_square(
            np.array([0,offset_value+0.5,0]),
            np.array([num_dots,0,0]),
            np.array([0,0,num_dots]),
            1,
        )
    if plane == "yz":
        plane_surf = parametric_square(
            np.array([offset_value+0.5,0,0]),
            np.array([0,num_dots,0]),
            np.array([0,0,num_dots]),
            1,
        )
    return plane_surf

def doubling_surface(num_dots, offset_value):
    col = [GREEN, RED, BLUE]

    plane_top = Polygon(
        [(num_dots),(num_dots),offset_value],
        [(num_dots),offset_value,(num_dots)],
        [offset_value,(num_dots),(num_dots)],
        fill_color = col[offset_value%3],
        fill_opacity = 0.5
    )
    plane_mid_top = Polygon(
        [(num_dots),(num_dots),(-num_dots+offset_value)],
        [(num_dots),(-num_dots+offset_value),(num_dots)],
        [(-num_dots+offset_value),(num_dots),(num_dots)],
        fill_color = col[offset_value%3],
        fill_opacity = 0.5
    )
    plane_mid = Polygon(
        [(num_dots),(-num_dots),offset_value],
        [offset_value,(-num_dots),(num_dots)],
        [(-num_dots),offset_value,(num_dots)],
        [(-num_dots),(num_dots),offset_value],
        [offset_value,(num_dots),(-num_dots)],
        [(num_dots),offset_value,(-num_dots)],
        fill_color = col[offset_value%3],
        fill_opacity = 0.5
    )
    if offset_value%3 == 0:
        plane_mid_bot = Polygon(
            [(-num_dots),(-num_dots),(num_dots+offset_value)],
            [(-num_dots),(num_dots+offset_value),(-num_dots)],
            [(num_dots+offset_value),(-num_dots),(-num_dots)],
            fill_color = col[offset_value%3],
            fill_opacity = 0.5
        )
    if offset_value%3 == 1:
        plane_mid_bot = Polygon(
            [(-num_dots),(-num_dots+offset_value),(num_dots)],
            [(-num_dots+offset_value),(-num_dots),(num_dots)],
            [(num_dots),(-num_dots),(-num_dots+offset_value)],
            [(num_dots),(-num_dots+offset_value),(-num_dots)],
            [(-num_dots+offset_value),(num_dots),(-num_dots)],
            [(-num_dots),(num_dots),(-num_dots+offset_value)],
            
            fill_color = col[offset_value%3],
            fill_opacity = 0.5
        )
    if offset_value%3 == 2:
        plane_mid_bot = Polygon(
            [(-num_dots),(-num_dots+offset_value),(num_dots)],
            [(-num_dots+offset_value),(-num_dots),(num_dots)],
            [(num_dots),(-num_dots),(-num_dots+offset_value)],
            [(num_dots),(-num_dots+offset_value),(-num_dots)],
            [(-num_dots+offset_value),(num_dots),(-num_dots)],
            [(-num_dots),(num_dots),(-num_dots+offset_value)],
            
            fill_color = col[offset_value%3],
            fill_opacity = 0.5
        )


    plane_bot = Polygon(
        [(-num_dots),(-num_dots),offset_value],
        [(-num_dots),offset_value,(-num_dots)],
        [offset_value,(-num_dots),(-num_dots)],
        fill_color = col[offset_value%3],
        fill_opacity = 0.5
    )
    plane_last = Polygon(
        [(-num_dots),(-num_dots),-num_dots+offset_value],
        [(-num_dots),-num_dots+offset_value,(-num_dots)],
        [-num_dots+offset_value,(-num_dots),(-num_dots)],
        fill_color = col[offset_value%3],
        fill_opacity = 0.5
    )
    planes = Group(plane_top, plane_mid_top, plane_mid, plane_mid_bot, plane_bot, plane_last)
    return planes




def rhombic_face(d1,d2,center):
    face = ParametricSurface(
        lambda u,v: np.array([
            center[0] + u * (d1[0] / 2) + v * (d2[0] / 2),
            center[1] + u * (d1[1] / 2) + v * (d2[1] / 2),
            center[2] + u * (d1[2] / 2) + v * (d2[2] / 2),
        ]),
        u_range=(-1,1),
        v_range=(-1,1),
    )
    return face

def rhombic_dodecahedron():
    face_group = Group()
    face1 = rhombic_face([0.5,0.5,0.5],[0.5,0.5,-0.5],[0.5,-0.5,0])
    face2 = rhombic_face([0.5,-0.5,0.5],[0.5,-0.5,-0.5],[0.5, 0.5,0])
    face3 = rhombic_face([-0.5,0.5,0.5],[-0.5,0.5,-0.5],[-0.5,-0.5,0])
    face4 = rhombic_face([-0.5,-0.5,0.5],[-0.5,-0.5,-0.5],[-0.5,0.5,0])

    face5 = rhombic_face([-0.5,0.5,0.5],[0.5,0.5,0.5],[0,-0.5,0.5])
    face6 = rhombic_face([0.5,-0.5,0.5],[0.5,0.5,0.5],[-0.5,0, 0.5])
    face7 = rhombic_face([-0.5,-0.5,0.5],[0.5,-0.5,0.5],[0,0.5,0.5])
    face8 = rhombic_face([-0.5,-0.5,0.5],[-0.5,0.5,0.5],[0.5,0,0.5])

    face9 = rhombic_face([-0.5,0.5,-0.5],[0.5,0.5,-0.5],[0,-0.5,-0.5])
    face10 = rhombic_face([0.5,-0.5,-0.5],[0.5,0.5,-0.5],[-0.5,0, -0.5])
    face11 = rhombic_face([-0.5,-0.5,-0.5],[0.5,-0.5,-0.5],[0,0.5,-0.5])
    face12 = rhombic_face([-0.5,-0.5,-0.5],[-0.5,0.5,-0.5],[0.5,0,-0.5])

    face_group.add(face1,face2,face3,face4,face5,face6,face7,face8,face9,face10,face11,face12)
    face_group.set_color(BLUE)

    return face_group

def rhombic_grid(num_dots, offset, plane, polarity):
    grid_group = Group()
    new_rhom = rhombic_dodecahedron().scale(0.5)
    col = [GREEN, RED, BLUE]
    if plane == "xy":
        if polarity == "pos":
            for i in range(-num_dots+1,num_dots):
                for j in range(-num_dots+1,num_dots):
                    next_rhom = new_rhom.copy()
                    next_rhom.set_color(col[(offset+i+j)%3])
                    next_rhom.move_to([i,j,offset])
                    grid_group.add(next_rhom)
        if polarity == "neg":
            for i in range(-num_dots+1,num_dots-1):
                for j in range(-num_dots+1,num_dots-1):
                    next_rhom = new_rhom.copy()
                    next_rhom.set_color(WHITE)
                    next_rhom.move_to([i+0.5,j+0.5,offset])
                    grid_group.add(next_rhom)
            next_rhom = new_rhom.copy().move_to([(num_dots-2)+0.5,(num_dots-2)+0.5,offset]).set_color(WHITE)
            grid_group.add(next_rhom)
    if plane == "xz":
        if polarity == "pos":
            for i in range(-num_dots+1,num_dots):
                for j in range(-num_dots+1,num_dots):
                    next_rhom = new_rhom.copy()
                    next_rhom.set_color(col[(offset+i+j)%3])
                    next_rhom.move_to([i,offset,j])
                    grid_group.add(next_rhom)
        if polarity == "neg":
            for i in range(-num_dots+1,num_dots-1):
                for j in range(-num_dots+1,num_dots-1):
                    next_rhom = new_rhom.copy()
                    next_rhom.set_color(WHITE)
                    next_rhom.move_to([i+0.5,offset,j+0.5])
                    grid_group.add(next_rhom)
            next_rhom = new_rhom.copy().move_to([(num_dots-2)+0.5,offset,(num_dots-2)+0.5]).set_color(WHITE)
            grid_group.add(next_rhom)
    if plane == "yz":
        if polarity == "pos":
            for i in range(-num_dots+1,num_dots):
                for j in range(-num_dots+1,num_dots):
                    next_rhom = new_rhom.copy()
                    next_rhom.set_color(col[(offset+i+j)%3])
                    next_rhom.move_to([offset,i,j])
                    grid_group.add(next_rhom)
        if polarity == "neg":
            for i in range(-num_dots+1,num_dots-1):
                for j in range(-num_dots+1,num_dots-1):
                    next_rhom = new_rhom.copy()
                    next_rhom.set_color(WHITE)
                    next_rhom.move_to([offset,i+0.5,j+0.5])
                    grid_group.add(next_rhom)
            next_rhom = new_rhom.copy().move_to([offset,(num_dots-2)+0.5,(num_dots-2)+0.5]).set_color(WHITE)
            grid_group.add(next_rhom)
    return grid_group
    
def tetrahedron_up(edge_length):
    a = edge_length
    face_group = Group()
    face1 = parametric_triangle(np.array([a*0,a*0,a*1]),np.array([a*0,a*-1,a*0]),np.array([a*1,a*0,a*0]))
    face2 = parametric_triangle(np.array([a*1,a*-1,a*1]),np.array([a*0,a*-1,a*0]),np.array([a*1,a*0,a*0]))
    face3 = parametric_triangle(np.array([a*1,a*-1,a*1]),np.array([a*0,a*-1,a*0]),np.array([a*0,a*0,a*1]))
    face4 = parametric_triangle(np.array([a*1,a*-1,a*1]),np.array([a*0,a*0,a*1]),np.array([a*1,a*0,a*0]))
    face_group.add(face1,face2,face3,face4)
    return face_group

def tetrahedron_down(edge_length):
    a = edge_length
    face_group = Group()
    face1 = parametric_triangle(np.array([a*0,a*0,a*-1]),np.array([a*0,a*-1,a*0]),np.array([a*1,a*0,a*0]))
    face2 = parametric_triangle(np.array([a*1,a*-1,a*-1]),np.array([a*0,a*-1,a*0]),np.array([a*1,a*0,a*0]))
    face3 = parametric_triangle(np.array([a*1,a*-1,a*-1]),np.array([a*0,a*-1,a*0]),np.array([a*0,a*0,a*-1]))
    face4 = parametric_triangle(np.array([a*1,a*-1,a*-1]),np.array([a*0,a*0,a*-1]),np.array([a*1,a*0,a*0]))
    face_group.add(face1,face2,face3,face4)
    return face_group

def tetra_up_grid(col, edge_length):
    tetra_group = Group()
    tetra = tetrahedron_up(edge_length).set_color(col)
    tetra1 = tetra.copy().set_color(col)
    tetra2 = tetra.copy().shift(edge_length*LEFT + edge_length*UP).set_color(col)
    tetra3 = tetra.copy().shift(edge_length*UP + edge_length*IN).set_color(col)
    tetra4 = tetra.copy().shift(edge_length*LEFT + edge_length*IN).set_color(col)
    tetra_group.add(tetra1, tetra2, tetra3, tetra4)
    tetra_group.set_color(RED)
    return tetra_group

def tetra_down_grid(num_dots, offset, edge_length):
    tetra_group = Group()
    tetra = tetrahedron_down(edge_length)
    tetra1 = tetra.copy()
    tetra2 = tetra.copy().shift(edge_length*LEFT+edge_length*UP)
    tetra3 = tetra.copy().shift(edge_length*UP + edge_length*OUT)
    tetra4 = tetra.copy().shift(edge_length*LEFT + edge_length*OUT)
    tetra_group.add(tetra1, tetra2, tetra3, tetra4)
    tetra_group.set_color(GREEN)
    return tetra_group

def octahedron(edge_length):
    a = edge_length
    face_group = Group()
    face1 = parametric_triangle(np.array([a*0,a*0,a*-1]),np.array([a*0,a*-1,a*0]),np.array([a*1,a*0,a*0]))
    face2 = parametric_triangle(np.array([a*0,a*0,a*-1]),np.array([a*0,a*-1,a*0]),np.array([a*-1,a*0,a*0]))
    face3 = parametric_triangle(np.array([a*0,a*0,a*-1]),np.array([a*0,a*1,a*0]),np.array([a*-1,a*0,a*0]))
    face4 = parametric_triangle(np.array([a*0,a*0,a*-1]),np.array([a*0,a*1,a*0]),np.array([a*1,a*0,a*0]))
    face5 = parametric_triangle(np.array([a*0,a*0,a*1]),np.array([a*0,a*-1,a*0]),np.array([a*1,a*0,a*0]))
    face6 = parametric_triangle(np.array([a*0,a*0,a*1]),np.array([a*0,a*-1,a*0]),np.array([a*-1,a*0,a*0]))
    face7 = parametric_triangle(np.array([a*0,a*0,a*1]),np.array([a*0,a*1,a*0]),np.array([a*-1,a*0,a*0]))
    face8 = parametric_triangle(np.array([a*0,a*0,a*1]),np.array([a*0,a*1,a*0]),np.array([a*1,a*0,a*0]))
    face_group.add(face1,face2,face3,face4,face5,face6,face7,face8)
    return face_group

def half_octahedron(which_oct, edge_length):
    a = edge_length
    face_group = Group()
    if which_oct == 1:
        base = parametric_square(np.array([a*1,0,0]),np.array([0,a*1,a*1]),np.array([0,-a*1,a*1]),a*1)
        face1 = parametric_triangle(np.array([0,0,0]), np.array([a*1,a*1,0]), np.array([a*1,0,a*1]))
        face2 = parametric_triangle(np.array([0,0,0]), np.array([a*1,-a*1,0]), np.array([a*1,0,a*1]))
        face3= parametric_triangle(np.array([0,0,0]), np.array([a*1,a*1,0]), np.array([a*1,0,-a*1]))
        face4= parametric_triangle(np.array([0,0,0]), np.array([a*1,-a*1,0]), np.array([a*1,0,-a*1]))
        face_group.add(base,face1,face2,face3,face4)
    if which_oct == 2:
        base = parametric_square(np.array([-a*1,0,0]),np.array([0,a*1,a*1]),np.array([0,-a*1,a*1]),a*1)
        face1 = parametric_triangle(np.array([0,0,0]), np.array([-a*1,a*1,0]), np.array([-a*1,0,a*1]))
        face2 = parametric_triangle(np.array([0,0,0]), np.array([-a*1,-a*1,0]), np.array([-a*1,0,a*1]))
        face3= parametric_triangle(np.array([0,0,0]), np.array([-a*1,a*1,0]), np.array([-a*1,0,-a*1]))
        face4= parametric_triangle(np.array([0,0,0]), np.array([-a*1,-a*1,0]), np.array([-a*1,0,-a*1]))
        face_group.add(base,face1,face2,face3,face4)
    if which_oct == 3:
        base = parametric_square(np.array([0,a*1,0]),np.array([a*1,0,a*1]),np.array([-a*1,0,a*1]),a*1)
        face1 = parametric_triangle(np.array([0,0,0]), np.array([-a*1,a*1,0]), np.array([0,a*1,a*1]))
        face2 = parametric_triangle(np.array([0,0,0]), np.array([a*1,a*1,0]), np.array([0,a*1,a*1]))
        face3= parametric_triangle(np.array([0,0,0]), np.array([-a*1,a*1,0]), np.array([0,a*1,-a*1]))
        face4= parametric_triangle(np.array([0,0,0]), np.array([a*1,a*1,0]), np.array([0,a*1,-a*1]))
        face_group.add(base,face1,face2,face3,face4)
    if which_oct == 4:
        base = parametric_square(np.array([0,-a*1,0]),np.array([a*1,0,a*1]),np.array([-a*1,0,a*1]),a*1)
        face1 = parametric_triangle(np.array([0,0,0]), np.array([-a*1,-a*1,0]), np.array([0,-a*1,a*1]))
        face2 = parametric_triangle(np.array([0,0,0]), np.array([a*1,-a*1,0]), np.array([0,-a*1,a*1]))
        face3= parametric_triangle(np.array([0,0,0]), np.array([-a*1,-a*1,0]), np.array([0,-a*1,-a*1]))
        face4= parametric_triangle(np.array([0,0,0]), np.array([a*1,-a*1,0]), np.array([0,-a*1,-a*1]))
        face_group.add(base,face1,face2,face3,face4)
    if which_oct == 5:
        base = parametric_square(np.array([0,0,a*1]),np.array([a*1,a*1,0]),np.array([-a*1,a*1,0]),a*1)
        face1 = parametric_triangle(np.array([0,0,0]), np.array([-a*1,0,a*1]), np.array([0,a*1,a*1]))
        face2 = parametric_triangle(np.array([0,0,0]), np.array([-a*1,0,a*1]), np.array([0,-a*1,a*1]))
        face3= parametric_triangle(np.array([0,0,0]), np.array([a*1,0,a*1]), np.array([0,a*1,a*1]))
        face4= parametric_triangle(np.array([0,0,0]), np.array([a*1,0,a*1]), np.array([0,-a*1,a*1]))
        face_group.add(base,face1,face2,face3,face4)
    if which_oct == 6:
        base = parametric_square(np.array([0,0,-a*1]),np.array([a*1,a*1,0]),np.array([-a*1,a*1,0]),a*1)
        face1 = parametric_triangle(np.array([0,0,0]), np.array([-a*1,0,-a*1]), np.array([0,a*1,-a*1]))
        face2 = parametric_triangle(np.array([0,0,0]), np.array([-a*1,0,-a*1]), np.array([0,-a*1,-a*1]))
        face3= parametric_triangle(np.array([0,0,0]), np.array([a*1,0,-a*1]), np.array([0,a*1,-a*1]))
        face4= parametric_triangle(np.array([0,0,0]), np.array([a*1,0,-a*1]), np.array([0,-a*1,-a*1]))
        face_group.add(base,face1,face2,face3,face4)
    return face_group

def vector_equilibrium(edge_length, col1, col2):
    tetra_top = Group()
    tetra = tetrahedron_up(edge_length)
    tetra1 = tetrahedron_up(edge_length).shift(edge_length*UP)
    tetra2 = tetrahedron_up(edge_length).shift(edge_length*LEFT)
    tetra3 = tetrahedron_up(edge_length).shift(edge_length*IN)
    tetra4 = tetrahedron_up(edge_length).shift(edge_length*IN+edge_length*LEFT+edge_length*UP)
    tetra_top.add(
        tetra1, 
        tetra2, 
        tetra3, 
        tetra4
    )
    tetra_top.set_color(col1)

    tetra_bottom = Group()
    tetra = tetrahedron_down(edge_length)
    tetra1 = tetrahedron_down(edge_length).shift(edge_length*UP)
    tetra2 = tetrahedron_down(edge_length).shift(edge_length*LEFT)
    tetra3 = tetrahedron_down(edge_length).shift(edge_length*OUT)
    tetra4 = tetrahedron_down(edge_length).shift(edge_length*OUT+edge_length*LEFT+edge_length*UP)
    tetra_bottom.add(
        tetra1, 
        tetra2, 
        tetra3, 
        tetra4
    )
    tetra_bottom.set_color(col2)

    vector_eq = Group(tetra_top, tetra_bottom)

    return vector_eq

def vector_equilibrium_neg(edge_length):
    tetra_top = Group()
    tetra = tetrahedron_down(edge_length)
    tetra1 = tetra.copy().shift(edge_length*UP)
    tetra2 = tetra.copy().shift(edge_length*LEFT)
    tetra3 = tetra.copy().shift(edge_length*IN)
    tetra4 = tetra.copy().shift(edge_length*IN+edge_length*LEFT+edge_length*UP)
    tetra_top.add(
        tetra1, 
        tetra2, 
        tetra3, 
        tetra4
    )
    tetra_top.set_color(RED)

    tetra_bottom = Group()
    tetra = tetrahedron_up(edge_length)
    tetra1 = tetra.copy().shift(edge_length*UP)
    tetra2 = tetra.copy().shift(edge_length*LEFT)
    tetra3 = tetra.copy().shift(edge_length*OUT)
    tetra4 = tetra.copy().shift(edge_length*OUT+edge_length*LEFT+edge_length*UP)
    tetra_bottom.add(
        tetra1, 
        tetra2, 
        tetra3, 
        tetra4
    )
    tetra_bottom.set_color(GREEN)

    vector_eq = Group(*tetra_top, *tetra_bottom)

    return vector_eq

def make_ve_dots(center_color,sphere_size):
    
    dot1 = Sphere(radius=sphere_size).move_to([0.5,0.5,0]).set_color(WHITE).apply_depth_test()
    dot2 = Sphere(radius=sphere_size).move_to([-0.5,0.5,0]).set_color(WHITE).apply_depth_test()
    dot3 = Sphere(radius=sphere_size).move_to([0.5,-0.5,0]).set_color(WHITE).apply_depth_test()
    dot4 = Sphere(radius=sphere_size).move_to([-0.5,-0.5,0]).set_color(WHITE).apply_depth_test()

    dot5 = Sphere(radius=sphere_size).move_to([0.5,0,0.5]).set_color(WHITE).apply_depth_test()
    dot6 = Sphere(radius=sphere_size).move_to([-0.5,0,0.5]).set_color(WHITE).apply_depth_test()
    dot7 = Sphere(radius=sphere_size).move_to([0.5,0,-0.5]).set_color(WHITE).apply_depth_test()
    dot8 = Sphere(radius=sphere_size).move_to([-0.5,0,-0.5]).set_color(WHITE).apply_depth_test()

    dot9 = Sphere(radius=sphere_size).move_to([0,0.5,0.5]).set_color(WHITE).apply_depth_test()
    dot10 = Sphere(radius=sphere_size).move_to([0,-0.5,0.5]).set_color(WHITE).apply_depth_test()
    dot11 = Sphere(radius=sphere_size).move_to([0,0.5,-0.5]).set_color(WHITE).apply_depth_test()
    dot12 = Sphere(radius=sphere_size).move_to([0,-0.5,-0.5]).set_color(WHITE).apply_depth_test()

    dot_center = Sphere(radius=sphere_size).set_color(center_color).apply_depth_test()

    vector_dots = Group(dot1,dot2,dot3,dot4,dot5,dot6,dot7,dot8,dot9,dot10,dot11,dot12,dot_center)
    return vector_dots

def half_octa_grid(col, edge_length):
    octa_group = Group()
    for i in range(0,7):
        octa = half_octahedron(i, edge_length).set_color(col)
        octa_group.add(octa)
    return octa_group

def dot_box_pos(num_dots):
    dot_box = Group()
    for i in range(-num_dots+1,num_dots):
        dot_plane = dot_plane_pos(num_dots, num_dots, i, "xy")
        dot_box.add(dot_plane)
    return dot_box

def dot_box_neg(num_dots):
    dot_box = Group()
    for i in range(-num_dots+2,num_dots-1):
        dot_plane = dot_plane_neg(num_dots, num_dots, i, "xy")
        dot_box.add(dot_plane)
    for i in range(-num_dots+2,num_dots-1):
        dot_plane = dot_plane_neg(num_dots, num_dots, i, "xz")
        dot_box.add(dot_plane)
    for i in range(-num_dots+2,num_dots-1):
        dot_plane = dot_plane_neg(num_dots, num_dots, i, "yz")
        dot_box.add(dot_plane)
    return dot_box