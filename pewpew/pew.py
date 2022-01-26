from turtle import *
from random import randint

color_input = input('what da color? ')

w = Screen()
turtles = []
while True:
  john1 = Turtle()
  john1.color(color_input)
  x = randint(-200, 200)
  y = randint(-200, 200)
  john1.goto(x, y)
  left(y)
  turtles.append(john1)
w.update()
