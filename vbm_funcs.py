from manimlib import *
size = 2
non_zero = .001

def mod_circle(mod, scale, font_scale):
    circle = Circle().scale(scale).set_color(WHITE)
    dot = Dot()
    r = 1.3
    dot_group = Group()
    number_group = Group()
    total_group = Group()
    for i in range(0,mod):
        new_dot=dot.copy()
        if i == 0:
            number = Tex(str(mod)).scale(font_scale)
        else:
            number = Tex(str(i)).scale(font_scale)
        new_dot.shift(
            [
                scale * np.sin(TAU * (i/mod)),
                scale * np.cos(TAU * (i/mod)),
                0
            ]
        )
        dot_group.add(new_dot)
        number.shift(
            [
                scale * r*np.sin(TAU * (i/mod)),
                scale * r*np.cos(TAU * (i/mod)),
                0
            ]            
        )
        number_group.add(number)
    total_group.add(dot_group)
    total_group.add(number_group)
    total_group.add(circle)

    return total_group

def vbm_symbol():
    circle = Circle().set_color(WHITE).scale(1.03).set_stroke(width=10)
    total_group = Group()

    line_group = Group()
    doubling = []
    number = 1
    test = 0
    while test < 9:
        if number not in doubling:
            new_line = Line(
                [
                    np.sin(TAU * (number / 9)),
                    np.cos(TAU * (number / 9)),
                    0
                ],
                [
                    np.sin(TAU * (((number * 2) % 9) / 9)),
                    np.cos(TAU * (((number * 2) % 9) / 9)),
                    0
                ],
            ).set_color(BLUE).set_stroke(width=5)
            doubling.append(number)
            line_group.add(new_line)
            number = (number * 2) % 9
            test+=1
        else:
            break
    line_group.shift(LEFT*0.025)
    new_line_group = line_group.copy()
    new_line_group.shift(RIGHT*0.05).set_color(RED)
    line1 = DashedLine(
        [
            np.sin(TAU * (0/9)),
            np.cos(TAU * (0/9)),
            0
        ],
        [
            np.sin(TAU * (3/9)),
            np.cos(TAU * (3/9)),
            0
        ],
    ).set_color(GREEN).set_stroke(width=5)
    line2 = DashedLine(
        [
            np.sin(TAU * (0/9)),
            np.cos(TAU * (0/9)),
            0
        ],
        [
            np.sin(TAU * (6/9)),
            np.cos(TAU * (6/9)),
            0
        ],
    ).set_color(GREEN).set_stroke(width=5)
    total_group.add(circle,line_group,new_line_group,line1,line2)
    return total_group

def vbm_numbers(mult, divisions, font_scale, radius):
    r = radius
    colors = [GREEN, RED, BLUE]
    number_group = Group()
    for i in range(0,divisions):
        if i == 0:
            number = Tex(str(divisions)).scale(font_scale).set_color(GREEN)
        else:
            number = Tex(str((i*mult)%divisions)).scale(font_scale).set_color(colors[i%3])
        number.shift(
            [
                r*np.sin(TAU * (i/divisions)),
                r*np.cos(TAU * (i/divisions)),
                0
            ]            
        )
        number_group.add(number)

    return number_group

def vbm_dots(mult, divisions,dot_scale,radius):
    r = radius
    colors = [GREEN, RED, BLUE]
    dot_group = Group()
    for i in range(0,divisions):
        dot = Dot().scale(dot_scale).set_color(colors[i%3])
        dot.shift(
            [
                r*np.sin(TAU * (i/divisions)),
                r*np.cos(TAU * (i/divisions)),
                0
            ]            
        )
        dot_group.add(dot)

    return dot_group

def dot_projection(mult, divisions, dot_scale):
    r = 2
    colors = [GREEN, RED, BLUE]
    dot_group = Group()
    for i in range(0,divisions):
        dot = Dot().scale(dot_scale).set_color(colors[i%3])
        dot.shift(
            [
                2*(r*np.sin(TAU * (i/divisions)) / (r-(r*np.cos(TAU * (i/divisions))+non_zero))),
                0,
                0
            ]            
        )
        dot_group.add(dot)

    return dot_group

def vbm_projection(mult, divisions, font_scale):
    r = 2
    colors = [GREEN, RED, BLUE]
    number_group = Group()
    for i in range(0,divisions):
        if i % 9 == 0:
            number = Text(str(9)).scale(font_scale).set_color(GREEN)
        else:
            number = Text(str((i*mult)%9)).scale(font_scale).set_color(colors[i%3])
        number.shift(
            [
                2*(r*np.sin(TAU * (i/divisions)) / (r-(r*np.cos(TAU * (i/divisions))+non_zero))),
                0,
                0
            ]            
        )
        number_group.add(number)

    return number_group

def number_string(mult):
    r = 1.3
    number_group = Group()
    for i in range(0,9):
        if i == 0:
            number = Tex(
                str(9)+str(9)+str(9)+
                str(9)+str(9)+str(9)+
                str(9)+str(9)+str(9)
            ).scale(0.4)
            number2 = number.copy()
            number.next_to(
                [
                    r*np.sin(TAU * (i/9)),
                    r*np.cos(TAU * (i/9)),
                    0
                ], RIGHT        
            )
            number_group.add(number)
            number2.next_to(
                [
                    r*np.sin(TAU * (i/9)),
                    r*np.cos(TAU * (i/9)),
                    0
                ], LEFT       
            )
            number_group.add(number,number2)
        if i == 3:
            number = Tex(
                str((1*i*mult)%9)+str((2*i*mult)%9)+
                str(9)+str((4*i*mult)%9)+str((5*i*mult)%9)+
                str(9)+str((7*i*mult)%9)+str((8*i*mult)%9)+str(9)
            ).scale(0.4)
        if i == 6:
            number = Tex(
                str(9)+str((8*i*mult)%9)+str((7*i*mult)%9)+
                str(9)+str((5*i*mult)%9)+str((4*i*mult)%9)+
                str(9)+str((2*i*mult)%9)+str((1*i*mult)%9)
            ).scale(0.4)
        if i == 1 or i == 2 or i == 4:
            number = Tex(
                str((1*i*mult)%9)+str((2*i*mult)%9)+
                str((3*i*mult)%9)+str((4*i*mult)%9)+str((5*i*mult)%9)+
                str((6*i*mult)%9)+str((7*i*mult)%9)+str((8*i*mult)%9)+str(9)
            ).scale(0.4)
        if i == 5 or i == 7 or i == 8:
            number = Tex(
                str(9)+str((8*i*mult)%9)+str((7*i*mult)%9)+
                str((6*i*mult)%9)+str((5*i*mult)%9)+str((4*i*mult)%9)+
                str((3*i*mult)%9)+str((2*i*mult)%9)+str((1*i*mult)%9)
            ).scale(0.4)
        if i == 1 or i == 2 or i == 3 or i == 4:
            number.next_to(
                [
                    r*np.sin(TAU * (i/9)),
                    r*np.cos(TAU * (i/9)),
                    0
                ], RIGHT        
            )
            number_group.add(number)
        if i == 5 or i == 6 or i == 7 or i == 8:
            number.next_to(
                [
                    r*np.sin(TAU * (i/9)),
                    r*np.cos(TAU * (i/9)),
                    0
                ], LEFT       
            )
            number_group.add(number)
    return number_group

def vbm_families(start):
    line_group = Group()
    colors = [GREEN,RED,BLUE]
    number = start
    for i in range(0,3):
        new_line = Line(
            [
                np.sin(TAU * (((start+i*3)%9) / 9)),
                np.cos(TAU * (((start+i*3)%9) / 9)),
                0
            ],
            [
                np.sin(TAU * (((start+i*3+3)%9) / 9)),
                np.cos(TAU * (((start+i*3+3)%9) / 9)),
                0
            ],
        ).set_stroke(width=5)
        line_group.add(new_line)
    line_group.set_color(colors[start % 3])

    return line_group

def doubling_sequence(mod, mult, start,scale):
    line_group = Group()
    doubling = []
    number = start
    test = 0
    while test < mod:
        if number not in doubling:
            new_line = Line(
                [
                    scale*np.sin(TAU * ((number )/ mod)),
                    scale*np.cos(TAU * (number / mod)),
                    0
                ],
                [
                    scale*np.sin(TAU * (((number * mult) % mod) / mod)),
                    scale*np.cos(TAU * (((number * mult) % mod) / mod)),
                    0
                ],
            )
            doubling.append(number)
            line_group.add(new_line)
            number = (number * mult) % mod
            test+=1
        else:
            break
    return line_group

def addition_sequence(mod, mult, start, scale):
    line_group = Group()
    adding = []
    number = start
    test = 0
    while test < mod:
        if number not in adding:
            new_line = Line(
                [
                    scale*np.sin(TAU * ((number )/ mod)),
                    scale*np.cos(TAU * (number / mod)),
                    0
                ],
                [
                    scale*np.sin(TAU * (((number + mult) % mod) / mod)),
                    scale*np.cos(TAU * (((number + mult) % mod) / mod)),
                    0
                ],
            )
            adding.append(number)
            line_group.add(new_line)
            number = (number + mult) % mod
            test+=1
        else:
            break
    return line_group

def halving_sequence(mod, scale):
    line_group = Group()
    doubling = []
    number = 1
    test = 0
    while test < mod:
        if number not in doubling:
            new_line = Line(
                [
                    scale*np.sin(TAU * (number / mod)),
                    scale*np.cos(TAU * (number / mod)),
                    0
                ],
                [
                    scale*np.sin(TAU * (((number * 5) % mod) / mod)),
                    scale*np.cos(TAU * (((number * 5) % mod) / mod)),
                    0
                ],
            )
            doubling.append(number)
            line_group.add(new_line)
            number = (number * 5) % mod
            test+=1
        else:
            break
    return line_group

def number_polarities_pos(nums_function, font_scale):
    polarity_group = Group()
    counter = 0
    for num in nums_function:
        if counter == 1 or counter == 4 or counter == 7:
            polarity = Tex(r"+").scale(font_scale).set_color(RED)
            polarity.next_to(num,LEFT,buff=0.07)
            polarity_group.add(polarity)
        if counter == 0  or counter == 3 or counter == 6:
            polarity = Tex(r"+").scale(font_scale).set_color(GREEN)
            polarity.next_to(num,LEFT,buff=0.07)
            polarity_group.add(polarity)
        if counter == 2 or counter == 5 or counter == 8:
            polarity = Tex(r"+").scale(font_scale).set_color(BLUE)
            polarity.next_to(num,LEFT,buff=0.07)
            polarity_group.add(polarity)
        counter = (counter + 1) % 9
    return polarity_group

def symbol_polarities_pos(nums_function, font_scale):
    polarity_group = Group()
    counter = 0
    for num in nums_function:
        if counter == 1 or counter == 4 or counter == 7:
            polarity = Tex(r"\bullet").scale(font_scale).set_color(RED)
            polarity.next_to(num,DR,buff=0.05).shift(UP*0.1)
            polarity_group.add(polarity)
        if counter == 0  or counter == 3 or counter == 6:
            polarity = Tex(r"\bullet").scale(font_scale).set_color(GREEN)
            polarity.next_to(num,DR,buff=0.05).shift(UP*0.1)
            polarity_group.add(polarity)
        if counter == 2 or counter == 5 or counter == 8:
            polarity = Tex(r"\bullet").scale(font_scale).set_color(BLUE)
            polarity.next_to(num,DR,buff=0.05).shift(UP*0.1)
            polarity_group.add(polarity)
        counter = (counter + 1) % 9
    return polarity_group
def symbol_polarities_neg(nums_function,font_scale):
    polarity_group = Group()
    counter = 0
    for num in nums_function:
        polarity = Tex(r"\circ").scale(font_scale).set_color(WHITE)
        polarity.next_to(num,DR,buff=0.05).shift(UP*0.1)
        polarity_group.add(polarity)
    counter = (counter + 1) % 9
    return polarity_group

def number_polarities_neg(nums_function,font_scale):
    polarity_group = Group()
    counter = 0
    for num in nums_function:
        polarity = Tex(r"-").scale(font_scale).set_color(WHITE)
        polarity.next_to(num,LEFT,buff=0.07)
        polarity_group.add(polarity)
    counter = (counter + 1) % 9
    return polarity_group

def projection_lines(divisions):
    colors = [GREEN, RED, BLUE]
    line_group = Group()
    for i in range(0,divisions):
        disp = 100
        radius = 2+disp
        x = radius * np.sin(TAU * (i/divisions))
        y = radius * np.cos(TAU * (i/divisions))
        point = np.array(
            [
                x,
                y-disp,
                0
            ]            
        )
        line = Line(
            point,
            np.array([0,2,0]),
        ).set_stroke(width=1.0)
        line_group.add(line)

    return line_group