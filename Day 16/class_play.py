# import another_module
#
# print(another_module.another_variable)
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

"""
Information comes from docs.python.org/3/library/turtle.html
"""

from prettytable import PrettyTable # figure out how to install packages on vscode
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table.align)
# table.align["Pokemon Name"] = 'l'
table.align = 'l'
print(table.align)

print(table)