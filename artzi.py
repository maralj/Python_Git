import turtle
import math
pencil = turtle.Turtle()
def art(radius):
    c = 2*math.pi*radius
    side = int(c/10)+1
    length = c/side
    rotate = 360/90
    number = 90
    # setting defult color to blue
    color = "red"
    for k in range (number):
        print(color)
        #if k < number/2:
         #   color = "blue"
         #   print("blue ")
        #else:
    # changing color for the 2nd half
         #   color = "red"
          #  print("red")
        for i in range (side):
            pencil.pencolor(color)
            pencil.fd(length)
            pencil.lt(360/side)
        pencil.lt(rotate)
        if color == "red":
            color = "purple"
        elif color == "purple":
            color = "blue"
        elif color == "blue":
            color = "green"
        elif color == "green":
            color = "yellow"
        elif color == "yellow":
            color = "orange"
        elif color == "orange":
            color = "brown"
        elif color == "brown":
            color = "red"
            
art(100)
