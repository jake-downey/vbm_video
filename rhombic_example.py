from manimlib import *

class Rhombic(Scene):
    def construct(self):

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
                            new_rhom.move_to([i+0.5,j+0.5,offset])
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
                            new_rhom.move_to([i+0.5,offset,j+0.5])
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
                            new_rhom.move_to([offset,i+0.5,j+0.5])
                            grid_group.add(next_rhom)
                    next_rhom = new_rhom.copy().move_to([offset,(num_dots-2)+0.5,(num_dots-2)+0.5]).set_color(WHITE)
                    grid_group.add(next_rhom)
            return grid_group
        
        def equilateral_triangle(P0,P1,P2):
            v1 = P1-P0
            v2 = P2-P0
            def parametric_triangle(u,v):
                if u + v <=1:
                    point = P0 + u * v1 + v * v2
                    return np.array([point[0],point[1],point[2]])
                else:
                    return
            triangle = ParametricSurface(
                lambda u,v: parametric_triangle(u,v),
                u_range=(0,1),
                v_range=(0,1),
            )
            return triangle

        def tetrahedron_up():
            face_group = Group()
            face1 = equilateral_triangle(np.array([0,0,1]),np.array([0,-1,0]),np.array([1,0,0]))
            face2 = equilateral_triangle(np.array([1,-1,1]),np.array([0,-1,0]),np.array([1,0,0]))
            face3 = equilateral_triangle(np.array([1,-1,1]),np.array([0,-1,0]),np.array([0,0,1]))
            face4 = equilateral_triangle(np.array([1,-1,1]),np.array([0,0,1]),np.array([1,0,0]))
            face_group.add(face1,face2,face3,face4)
            return face_group

        def tetrahedron_down():
            face_group = Group()
            face1 = equilateral_triangle(np.array([0,0,-1]),np.array([0,-1,0]),np.array([1,0,0]))
            face2 = equilateral_triangle(np.array([1,-1,-1]),np.array([0,-1,0]),np.array([1,0,0]))
            face3 = equilateral_triangle(np.array([1,-1,-1]),np.array([0,-1,0]),np.array([0,0,-1]))
            face4 = equilateral_triangle(np.array([1,-1,-1]),np.array([0,0,-1]),np.array([1,0,0]))
            face_group.add(face1,face2,face3,face4)
            return face_group
        
        def tetra_up_grid(num_dots, offset):
            tetra_group = Group()
            tetra = tetrahedron_up()
            tetra1 = tetra.copy()
            tetra2 = tetra.copy().shift(LEFT + UP)
            tetra3 = tetra.copy().shift(UP + IN)
            tetra4 = tetra.copy().shift(LEFT + IN)
            tetra_group.add(tetra1, tetra2, tetra3, tetra4)
            tetra_group.set_color(RED)
            return tetra_group

        def tetra_down_grid(num_dots, offset):
            tetra_group = Group()
            tetra = tetrahedron_down()
            tetra1 = tetra.copy()
            tetra2 = tetra.copy().shift(LEFT+UP)
            tetra3 = tetra.copy().shift(UP + OUT)
            tetra4 = tetra.copy().shift(LEFT + OUT)
            tetra_group.add(tetra1, tetra2, tetra3, tetra4)
            tetra_group.set_color(GREEN)
            return tetra_group

        def octahedron():
            face_group = Group()
            face1 = equilateral_triangle(np.array([0,0,-1]),np.array([0,-1,0]),np.array([1,0,0]))
            face2 = equilateral_triangle(np.array([0,0,-1]),np.array([0,-1,0]),np.array([-1,0,0]))
            face3 = equilateral_triangle(np.array([0,0,-1]),np.array([0,1,0]),np.array([-1,0,0]))
            face4 = equilateral_triangle(np.array([0,0,-1]),np.array([0,1,0]),np.array([1,0,0]))
            face5 = equilateral_triangle(np.array([0,0,1]),np.array([0,-1,0]),np.array([1,0,0]))
            face6 = equilateral_triangle(np.array([0,0,1]),np.array([0,-1,0]),np.array([-1,0,0]))
            face7 = equilateral_triangle(np.array([0,0,1]),np.array([0,1,0]),np.array([-1,0,0]))
            face8 = equilateral_triangle(np.array([0,0,1]),np.array([0,1,0]),np.array([1,0,0]))
            face_group.add(face1,face2,face3,face4,face5,face6,face7,face8)
            return face_group
        

        frame = self.camera.frame
        frame.set_euler_angles(
            theta=45*DEGREES,
            phi=45*DEGREES,
        )
        axes = ThreeDAxes()

        self.add(axes.apply_depth_test())
        self.add(tetra_up_grid(1,1))
        self.add(tetra_down_grid(1,1))
        # self.add(tetrahedron_up())
        # self.add(tetrahedron_down())
        self.add(octahedron())

        # self.add(rhombic_dodecahedron())

        # self.add(rhombic_grid(3,0,"xy" ,"pos"))
        # self.add(rhombic_grid(3,1,"xy" ,"pos"))
        # self.add(rhombic_grid(3,2,"xy" ,"pos"))
        # self.add(rhombic_grid(3,0,"xy", "neg"))

