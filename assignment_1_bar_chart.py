# import SimpleGraphics1
from SimpleGraphics1 import *

# user enters chart name
chart_name = input("Enter the title:")

# user enters height of bars
first_bar = float(input("Enter the value of bar 1:"))
second_bar = float(input("Enter the value of bar 2:"))
third_bar = float(input("Enter the value of bar 3:"))

# user enters colours of bar
colour_bar1 = float("Enter the colour of bar 1:")
colour_bar2 = float("Enter the colour of bar 2:")
colour_bar3 = float("Enter the colour of bar 4:")

# x coordinate of graph
x_coordinate = float(input("Enter the x-coordinate:"))

# y coordinate of graph
y_coordinate = float(input("Enter the y-coordinate:"))

# variables for width and height of chart
width_chart = 400
height_chart = 300

# displays name of user
setFont("Times", "24", "bold")
text(x_coordinate + 200, y_coordinate - 325, chart_name)

# displays lines of the graph
line(x_coordinate, y_coordinate, x_coordinate + width_chart, y_coordinate)
line(x_coordinate, y_coordinate, x_coordinate, y_coordinate - height_chart)

# fills colour of all bars + creates bar shape underneath
setFill(colour_bar1)
rect(x_coordinate + 50, y_coordinate - first_bar, 100, first_bar)

setFill(colour_bar2)
rect(x_coordinate + 150, y_coordinate - second_bar, 100, second_bar)

setFill(colour_bar3)
rect(x_coordinate + 250, y_coordinate - third_bar, 100, third_bar)
