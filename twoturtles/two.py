from turtle import *
from random import randint

john = Turtle()
bob = Turtle()

while True:
  john.forward(randint(0,45))
  john.left(randint(0,120))

while True:
  bob.forward(randint(0,45))
  bob.left(randint(0,120))
