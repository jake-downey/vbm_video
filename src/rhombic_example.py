from manimlib import *

class Rhombic(Scene):

    def _safe_toggle_depth(self, mob, test: bool, write: bool):
        """
        Robustly flip depth_test and depth_write for every submobject.
        Handles single wrapper and wrapper lists; skips None safely.
        """
        for m in mob.get_family():
            # single wrapper
            sw = getattr(m, "shader_wrapper", None)
            if sw is not None:
                if hasattr(sw, "depth_test"):
                    sw.depth_test = test
                if hasattr(sw, "depth_write"):
                    sw.depth_write = write
            # lists (name differs across ManimGL versions)
            for list_name in ("shader_wrapper_list", "shader_wrappers"):
                sw_list = getattr(m, list_name, None)
                if not sw_list:
                    continue
                for swx in sw_list:
                    if swx is None:
                        continue
                    if hasattr(swx, "depth_test"):
                        swx.depth_test = test
                    if hasattr(swx, "depth_write"):
                        swx.depth_write = write

    def _force_opaque_restore(self, mob):
        """
        Ensure everything is truly opaque & writes depth again.
        Also re-applies depth-test on objects that support it.
        """
        for m in mob.get_family():
            # Bring opacities back to 1 at both group and child level
            try:
                m.set_opacity(1.0)
            except Exception:
                pass
            if hasattr(m, "set_style"):
                try:
                    m.set_style(fill_opacity=1.0, stroke_opacity=1.0)
                except Exception:
                    # Surfaces usually ignore stroke props; that's fine.
                    pass
            # Re-attach GL flags on objects that expose helpers
            if hasattr(m, "apply_depth_test"):
                try:
                    m.apply_depth_test()
                except Exception:
                    pass
        # Finally, guarantee depth test/write are ON
        self._safe_toggle_depth(mob, test=True, write=True)

    def fade_out_clean(self, mob, run_time=0.8):
        """
        Fade out with depth testing/writing OFF (no silhouette), then remove.
        """
        self._safe_toggle_depth(mob, test=False, write=False)
        self.play(mob.animate.set_opacity(0.0), run_time=run_time)
        self.remove(mob)

    def fade_in_clean(self, mob, run_time=0.8):
        """
        Add back invisible, fade in with depth OFF, then hard-restore opaque.
        """
        # Start fully transparent, depth disabled during the animation
        self.add(mob)
        self._safe_toggle_depth(mob, test=False, write=False)
        # set base to 0 so child×group alpha products don't linger
        for m in mob.get_family():
            try:
                m.set_opacity(0.0)
            except Exception:
                pass
            if hasattr(m, "set_style"):
                try:
                    m.set_style(fill_opacity=0.0)  # normalize child fill
                except Exception:
                    pass
        self.play(mob.animate.set_opacity(1.0), run_time=run_time)
        # Now **force** a solid, correct restore (depth test/write back ON)
        self._force_opaque_restore(mob)

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
                resolution = (12,12),
            ).apply_depth_test()
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
                resolution = (30,30),
            ).apply_depth_test()
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
            theta=30*DEGREES,
            phi=60*DEGREES,
        )
        axes = ThreeDAxes()
        frame.scale(2)
        self.add(axes.apply_depth_test())
        # self.add(tetra_up_grid(4,4))
        # self.add(tetra_down_grid(4,4))
        # # self.add(tetrahedron_up())
        # # self.add(tetrahedron_down())
        # self.add(octahedron())

        # self.add(rhombic_dodecahedron())
        pos_rhom_xy = Group()
        neg_rhom_xy = Group()
        neg_rhom_xz = Group()
        neg_rhom_yz = Group()
        for i in range(-3,4):
            pos_rhom_xy.add(rhombic_grid(4,i,"xy" ,"pos"))

        for i in range(-3,4):
            neg_rhom_xy.add(rhombic_grid(4,i,"xy", "neg"))
        for i in range(-3,4):
            neg_rhom_xz.add(rhombic_grid(4,i,"xz", "neg"))
        for i in range(-3,4):
            neg_rhom_yz.add(rhombic_grid(4,i,"yz", "neg"))
        
        frame.add_updater(lambda m, dt: m.increment_theta(-0.1*dt))
        self.add(
            pos_rhom_xy,
            neg_rhom_xy,
            neg_rhom_xz,
            neg_rhom_yz,
        )
        self.wait(3)
        self.fade_out_clean(neg_rhom_xy, run_time=1)
        self.fade_out_clean(neg_rhom_xz, run_time=1)
        self.fade_out_clean(neg_rhom_yz, run_time=1)
        
        self.wait(3)
        self.fade_out_clean(pos_rhom_xy, run_time=1)
        self.fade_in_clean(neg_rhom_xy, run_time=1)


        self.wait(3)
        self.fade_out_clean(neg_rhom_xy, run_time=1)
        self.fade_in_clean(neg_rhom_xz, run_time=1)

        self.wait(3)
        self.fade_out_clean(neg_rhom_xz, run_time=1)
        self.fade_in_clean(neg_rhom_yz, run_time=1)

        self.wait(3)

        self.fade_in_clean(neg_rhom_xz, run_time=1)
        self.fade_in_clean(neg_rhom_xy, run_time=1)
        
        self.wait(3)

        self.fade_in_clean(pos_rhom_xy, run_time=1)
        self.wait(3)

