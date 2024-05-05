import colorgram
from turtle import Turtle, Screen
from random import randint, choice
import turtle

rgb_colors = []
# Extract 30 colors from image
# colors = colorgram.extract('hirst3.jpeg', 30)
# colors = colorgram.extract('marcosOndruska.jpeg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))
#
# print(rgb_colors)
tim = Turtle()
tim.shape("triangle")
turtle.colormode(255)
tim.speed("fastest")
tim.penup()
tim.goto(-250, 250)

color_list = [(161, 17, 53), (24, 105, 154), (198, 81, 24), (155, 49, 96), (208, 159, 105), (49, 170, 125), (30, 133, 83), (216, 204, 126), (9, 107, 33), (229, 89, 42), (224, 124, 143), (204, 84, 112), (111, 185, 149), (212, 232, 218), (238, 216, 224), (156, 22, 13), (181, 135, 55), (10, 93, 106), (237, 158, 173), (126, 166, 189), (77, 85, 17), (156, 212, 180), (93, 20, 46), (233, 172, 160), (14, 73, 27), (85, 41, 18), (19, 61, 87), (40, 60, 107)]
color_list1 = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220)]
color_listMO = [(10, 37, 52), (34, 12, 9), (154, 93, 67), (198, 130, 101), (57, 32, 40), (186, 108, 76), (64, 97, 123), (139, 150, 174), (112, 81, 90), (175, 150, 161), (74, 92, 85), (14, 26, 24), (88, 48, 58), (21, 77, 96), (112, 123, 155), (107, 43, 31), (155, 111, 121), (49, 61, 86), (22, 85, 69), (184, 185, 210), (208, 180, 191), (227, 176, 165), (89, 68, 28), (231, 197, 133), (159, 135, 77), (146, 162, 158)]
def random_color():
    return choice(color_list)

number_of_dots = 100
counter = 1
for _ in range(0, number_of_dots):
    tim.pendown()
    tim.dot(20, random_color())
    tim.penup()
    if counter % 10 != 0:
        tim.forward(50)
    elif counter / 10 % 2 != 0:
        tim.right(90)
        tim.forward(50)
        tim.right(90)
    else:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
    counter += 1

tim.hideturtle()

screen = Screen()
screen.exitonclick()