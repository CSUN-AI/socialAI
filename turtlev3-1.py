from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(10):
    write(step, align='center')
    right(90)
    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color('red')
ada.shape('triangle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

for turn in range(10):
    ada.right(36)

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

for turn in range(72):
    bob.left(5)

ivy = Turtle()
ivy.shape('square')
ivy.color('green')

ivy.penup()
ivy.goto(-160, 40)
ivy.pendown()

for turn in range(60):
    ivy.right(6)

for turn in range(100):
    ada.forward(randint(1,1))
    bob.forward(randint(1,1))
    ivy.forward(randint(1,1))
