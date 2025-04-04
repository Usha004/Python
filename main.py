from turtle import Turtle, Screen
import random

tim = Turtle()       # Creating the object using class turtle from import module
tim.shape("turtle")   #Adding shape
tim.color("red")    # Adding the Color
# for i in range(4):
#     tim.forward(100)     # Taking action to the forward
#     tim.right(90)  # To move to the other direction here on from east to south
# for j in range(4):
#     tim.forward(50)
#     tim.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

colors = ["pale turquoise", "dark turquoise", "turquoise", "medium turquoise", "light sea green", "teal" ]
def draw_shape(number_of_sides):
    angle = 360/number_of_sides
    for _ in range(number_of_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = Screen()   # To display the turtle in a screen
screen.exitonclick()   # Displays screen until we exit from the screen