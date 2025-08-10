from manimlib import *
sphere_size = 0.1

def diamond_plane_pos(num_rows, num_cols, offset_value, plane):
    sqr_group = Group()
    sqr = Square(np.sqrt(2)/2).rotate(45*DEGREES)
    col = [GREEN, RED, BLUE]
    if plane == "xy":
        for i in range (-num_cols+1, num_cols):
            for j in range(-num_rows+1, num_rows):
                diamond = sqr.copy()
                diamond.move_to([i, j, offset_value])
                diamond.set_color(col[(offset_value+i+j)%3]).set_opacity(1.0).set_stroke(BLACK)
                sqr_group.add(diamond)
    if plane == "xz":
        for i in range (-num_cols+1, num_cols):
            for j in range(-num_rows+1, num_rows):
                diamond = sqr.copy()
                diamond.move_to([i, offset_value, j]).rotate(90*DEGREES,RIGHT)
                diamond.set_color(col[(offset_value+i+j)%3]).set_opacity(1.0).set_stroke(BLACK)
                sqr_group.add(diamond)
    if plane == "yz":
        for i in range (-num_cols+1, num_cols):
            for j in range(-num_rows+1, num_rows):
                diamond = sqr.copy()

                diamond.move_to([offset_value, i, j]).rotate(90*DEGREES,UP)
                diamond.set_color(col[(offset_value+i+j)%3]).set_opacity(1.0).set_stroke(BLACK)
                sqr_group.add(diamond)
    return sqr_group

def diamond_plane_neg(num_rows, num_cols, offset_value, plane):
    sqr_group = Group()
    sqr = Square(np.sqrt(2)/2).rotate(45*DEGREES)
    col = [GREEN, RED, BLUE]
    if plane == "xy":
        for i in range (-num_cols+1, num_cols-1):
            for j in range(-num_rows+1, num_rows-1):
                diamond = sqr.copy()
                diamond.move_to([i+1/2, j+1/2, offset_value])
                diamond.set_color(WHITE).set_opacity(1.0).set_stroke(BLACK)
                sqr_group.add(diamond)
    if plane == "xz":
        for i in range (-num_cols+1, num_cols-1):
            for j in range(-num_rows+1, num_rows-1):
                diamond = sqr.copy()
                diamond.move_to([i+1/2, offset_value, j+1/2]).rotate(90*DEGREES,RIGHT)
                diamond.set_color(WHITE).set_opacity(1.0).set_stroke(BLACK)
                sqr_group.add(diamond)
    if plane == "yz":
        for i in range (-num_cols+1, num_cols-1):
            for j in range(-num_rows+1, num_rows-1):
                diamond = sqr.copy()
                diamond.move_to([offset_value, i+1/2, j+1/2]).rotate(90*DEGREES,UP)
                diamond.set_color(WHITE).set_opacity(1.0).set_stroke(BLACK)
                sqr_group.add(diamond)
    return sqr_group

def generate_number_grid_pos(num_rows, num_cols, offset_value, plane, start_num):
    number_group = Group()
    if plane == "xy":
        for i in range (-num_cols+1, num_cols):
            for j in range(-num_rows+1, num_rows):
                if (start_num+(j*4)+i)%9 == 0:
                    number = Text(str(9))
                    number.move_to([i, j, offset_value]).set_color(BLACK)
                    number_group.add(number)
                else:
                    number = Text(str((start_num+(j*4)+i)%9))
                    number.move_to([i, j, offset_value]).set_color(BLACK)
                    number_group.add(number)
    if plane == "xz":
        for i in range (-num_cols+1, num_cols):
            for j in range(-num_rows+1, num_rows):
                if (start_num+(j*7)+i)%9 == 0:
                    number = Text(str(9))
                    number.move_to([i, offset_value, j]).set_color(BLACK).rotate(90*DEGREES,RIGHT)
                    number_group.add(number)
                else:
                    number = Text(str((start_num+(j*7)+i)%9))
                    number.move_to([i, offset_value, j]).set_color(BLACK).rotate(90*DEGREES,RIGHT)
                    number_group.add(number)
    if plane == "yz":
        for i in range (-num_cols+1, num_cols):
            for j in range(-num_rows+1, num_rows):
                if (start_num+(j*7)+(i*4))%9 == 0:
                    number = Text(str(9))
                    number.move_to([offset_value, i, j]).set_color(BLACK).rotate(90*DEGREES,UP).rotate(90*DEGREES,RIGHT)
                    number_group.add(number)
                else:
                    number = Text(str((start_num+(j*7)+(i*4))%9))
                    number.move_to([offset_value, i, j]).set_color(BLACK).rotate(90*DEGREES,UP).rotate(90*DEGREES,RIGHT)
                    number_group.add(number)
    return number_group

def generate_number_grid_neg(num_rows, num_cols, offset_value, plane, start_num):
    number_group = Group()
    if plane == "xy":
        for i in range (-num_cols+1, num_cols-1):
            for j in range(-num_rows+1, num_rows-1):
                if (start_num-(j*4)-i)%9 == 0:
                    number = Text(str(9))
                    number.move_to([i+1/2, j+1/2, offset_value]).set_color(BLACK)
                    number_group.add(number)
                else:
                    number = Text(str((start_num-(j*4)-i)%9))
                    number.move_to([i+1/2, j+1/2, offset_value]).set_color(BLACK)
                    number_group.add(number)
    if plane == "xz":
        for i in range (-num_cols+1, num_cols-1):
            for j in range(-num_rows+1, num_rows-1):
                if (start_num-(j*7)-i)%9 == 0:
                    number = Text(str(9))
                    number.move_to([i+1/2, offset_value, j+1/2]).set_color(BLACK).rotate(90*DEGREES,RIGHT)
                    number_group.add(number)
                else:
                    number = Text(str((start_num-(j*7)-i)%9))
                    number.move_to([i+1/2, offset_value, j+1/2]).set_color(BLACK).rotate(90*DEGREES,RIGHT)
                    number_group.add(number)
    if plane == "yz":
        for i in range (-num_cols+1, num_cols-1):
            for j in range(-num_rows+1, num_rows-1):
                if (start_num-(j*7)-(i*4))%9 == 0:
                    number = Text(str(9))
                    number.move_to([offset_value, i+1/2, j+1/2]).set_color(BLACK).rotate(90*DEGREES,UP).rotate(90*DEGREES,RIGHT)
                    number_group.add(number)
                else:
                    number = Text(str((start_num-(j*7)-(i*4))%9))
                    number.move_to([offset_value, i+1/2, j+1/2]).set_color(BLACK).rotate(90*DEGREES,UP).rotate(90*DEGREES,RIGHT)
                    number_group.add(number)
    return number_group

