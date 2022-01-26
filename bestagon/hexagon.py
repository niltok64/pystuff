from turtle import *

def hexagon(size):
  for i in range(6):
    forward(size)
    left(60)

hexagon(100)
x = -10
y = -30
penup()
goto(x, y)
pendown()
style = ('Courier', 10, 'italic')
write("hexagons are the bestagons", font=style)
