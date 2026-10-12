# imports SimpleGraphics
from SimpleGraphics1 import *

# prints chart creation menu
print("Chart Creation Menu")
print("   1. Pie Chart")
print("   2. Bar Chart")
chart_type = input("Select your chart type >> ")

# creates pie chart
if chart_type == "1":
    pie_title = input("Enter the title of the chart: ")
    setFont("Times", 24, "bold")
    text(420, 50, pie_title)

    # list of sector names/values
    sector_names = []
    sector_values = []

    # gets number of sectors and total value
    pie_sectors = int(input("Enter the number of sectors (2 to 6): "))
    pie_total = float(input("Enter the total value of all sectors: "))

    # for loop for sector value and names, stores them in lists
    for i in range(pie_sectors - 1):
        name = input(f"Label sector {i + 1}: ")
        value1 = int(input(f"Enter the value of the {name} sector: "))

        sector_names.append(name)
        sector_values.append(value1)

    # gets the name of final sector and stores it in list
    last_name = input(f"Label sector {pie_sectors}: ")
    sector_names.append(last_name)

    # calculates the remaining value for final sector and stores it in list
    last_value = pie_total - sum(sector_values)
    sector_values.append(last_value)

    # draw pie chart
    colours = ["purple", "red", "blue", "pink", "green", "violet"]
    start_angle = 0

    # for loop/calculates each sector angle and draws its slice
    for i in range(pie_sectors):
        angle = (sector_values[i] / pie_total) * 360

        setFill(colours[i])
        pieSlice(190, 100, 450, 450, start_angle, angle)

        start_angle = start_angle + angle

    # draw legend
    legend_x = 735
    legend_y = 120
    square_size = 40
    spacing = 75
    setFont("Times", "12")

    # draws + spaces the legend far right
    for i in range(pie_sectors):
        y = legend_y + i * spacing

        setFill(colours[i])
        rect(legend_x, y, square_size, square_size)

        setFill("black")
        text(legend_x + 20, y - 12, sector_names[i])

#  draws bar chart
elif chart_type == "2":
    bar_title = input("Enter the title of the chart: ")

    # chart coordinates/variables
    chart_x = 85
    chart_y = 500
    chart_width = 650
    chart_height = 400

    # list of bar names and values
    bar_names = []
    bar_values = []

    # gets bar chart settings from user
    bar_number = int(input("Enter the number of bars (2 to 6): "))
    gridline = int(input("Enter the gridline interval (10 to 100): "))
    y_axis = input("Enter the label for the Y-Axis: ")

    # for loop to enter name and value
    for i in range(bar_number):
        name = input(f"Label bar {i + 1}: ")
        value = int(input(f"Enter the value of bar {name}: "))
        bar_names.append(name)
        bar_values.append(value)

    # chart background is white
    setFill("white")
    setOutline("black")
    rect(chart_x, chart_y - chart_height, chart_width, chart_height)

    # draws the y-axis
    line(chart_x, chart_y - chart_height, chart_x, chart_y)
    # draws the x_axis
    line(chart_x, chart_y, chart_x + chart_width, chart_y)

    # sets font/size for gridline numbers
    setFont("Times", 10)

    # draws horizontal gridlines and displays their values
    for value in range(0, 401, gridline):
        y = chart_y - (value / 400) * chart_height

        setOutline("black")
        line(chart_x, y, chart_x + chart_width, y)

        setFill("black")
        text(chart_x + chart_width + 20, y, str(value))

    # draw bars
    colours = ["purple", "red", "blue", "pink", "violet", "green"]
    bar_spacing = chart_width / bar_number
    bar_width = bar_spacing * 0.8

    # sets font/size for bar labels/values
    setFont(12)

    # calculates and draws each bar with its label and values
    for i in range(bar_number):
        bar_height = (bar_values[i] / 400) * chart_height

        # calculates position of the bar
        x = chart_x + i * bar_spacing + (bar_spacing - bar_width) / 2
        y = chart_y - bar_height

        # draws bar with assigned colour
        setFill(colours[i])
        rect(x, y, bar_width, bar_height)

        # creates bar name below x-axis
        setOutline("black")
        setFont(12)
        text(x + bar_width / 2, chart_y + 18, bar_names[i])

        # creates value near the top of the bar
        setOutline("black")
        setFont("Times", 12, "bold")
        text(x + bar_width / 2, y + 12, str(bar_values[i]))

    # creates y-axis label
    setOutline("black")
    setFont("Times", 12, "bold")
    text(chart_x - 40, chart_y - chart_height / 2, y_axis)

    # draws title
    setOutline("black")
    setFont("Times", 25, "bold")
    text(chart_x + chart_width / 2, chart_y - chart_height - 20, bar_title)
