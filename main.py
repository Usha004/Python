# import another_module
# print(another_module.another_variable)
#
# from turtle import Turtle,Screen
# """constructing an object using inbuilt class turtle"""
# timmy = Turtle()
# print(timmy)
# """here timmy is an object which we crated using the class Turtle()"""
# timmy.shape("turtle")
# timmy.color("coral")
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("pokomon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

table.align = "l"
print(table)










