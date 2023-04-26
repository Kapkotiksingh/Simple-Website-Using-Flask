#  sudo apt-get install python3-tk
# Step -1
import turtle

# from turtle import Turtle, Screen

# data = Turtle()

# data.shape("turtle")
# data.color("red")

# using loop
# for _ in range(4):
#     data.forward(100)
#     data.right(90)

# data.forward(100)
# data.right(90)
# data.forward(100)
# data.right(90)
# data.forward(100)
# data.right(90)
# data.forward(100)
# data.right(90)

# screen = Screen()
# screen.exitonclick()




# Step -2

# Basic Import

# import turtle
# data = turtle.Turtle()

# from turtle import Turtle
# data = Turtle()

#  from import  *
# format(1,2,3,4)

# Aliasing models
# from turtle as t
# data = t.Turtle()

# Installing models
# pip install mode name



# Step -3

# Draw a Dashed Line

# import turtle as t
#
# data = t.Turtle()
#
# for _ in range(15):
#     data.forward(10)
#     data.penup()
#     data.forward(10)
#     data.pendown()




# Step -4

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon

# import turtle as t
# import  random
#
# data = t.Turtle()
# colors = ["light sky blue", "dark magenta", "maroon", "lime", "green", "blue violet", "medium violet red", "slate blue"]
# def draw_show(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         data.forward(100)
#         data.right(angle)
#
# for shope_side_n in range(3, 11):
#     data.color(random.choice(colors))
#     draw_show(shope_side_n)




# Step -5

# import turtle as t
# import random
#
# data = t.Turtle()
# t.colormode(255)


# colors = ["light sky blue", "dark magenta", "maroon", "lime", "green", "blue violet", "medium violet red", "slate blue"]
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
#
# directions = [0, 90, 180, 270]
# data.pensize(10)
# # data.speed(10)
#
# for _ in range(200):
#     data.color(random_color())
#     data.forward(30)
#     data.setheading(random.choice(directions))



# Step -6

# Draw a Spirograph

# import turtle as t
# import random
# from turtle import Screen
#
# data = t.Turtle()
# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
#
# data.speed("fastest")
#
#
# def drow_spirograh(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         data.color(random_color())
#         data.circle(100)
#         data.setheading(data.heading() + size_of_gap)
#
#
# drow_spirograh(5)
#
#
# screen = Screen()
# screen.exitonclick()



# Step -7

# How to Extract RGB values from image

# import colorgram
#
# rgb_color =[]
# colors = colorgram.extract("img.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
# print(rgb_color)



# Step -8

# Drawing the Dots

import turtle as turtle_model
import random

turtle_model.colormode(255)
data = turtle_model.Turtle()
data.hideturtle()
data.speed("fastest")
data.penup()
color_list = [(226, 231, 236), (58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120), (68, 105, 90), (237, 225, 233), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194), (183, 192, 201), (214, 177, 191), (19, 57, 93), (21, 68, 113), (112, 123, 149), (229, 174, 165), (172, 203, 182), (158, 205, 215), (69, 58, 47), (108, 47, 60), (53, 70, 65), (72, 64, 53)]


data.setheading(225)
data.forward(300)
data.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots+1):
    data.dot(20, random.choice(color_list))
    data.forward(50)

    if dot_count % 10 == 0:
        data.setheading(90)
        data.forward(50)
        data.setheading(180)
        data.forward(500)
        data.setheading(0)




screen = turtle_model.Screen()
screen.exitonclick()
