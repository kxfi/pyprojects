import random
import turtle as turtle_module

# import colorgram


# rgb_colors = []
# colors = colorgram.extract('/Users/jeremyacheampong/Developer/Python/Day 1-100/Day18_start/hirst-painting/image.jpg', 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
    
# print(rgb_colors)

#color_list = [(254, 254, 253), (219, 254, 237), (84, 254, 155), (173, 146, 118), (254, 250, 254), (245, 39, 191), (158, 107, 56), (2, 1, 176), (151, 54, 251), (221, 254, 101)]

turtle_module.colormode(255) # change color mode to rgb 
tim = turtle_module.Turtle() 
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

def draw_dot():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
    

positions = [-200, -150, -100, -50, 0, 50, 100, 150, 200, 250]

for position in positions:
    tim.speed("fastest")
    tim.penup()
    tim.setposition(-240, position)
    draw_dot()


screen = turtle_module.Screen() # for screen to stay
screen.exitonclick()
