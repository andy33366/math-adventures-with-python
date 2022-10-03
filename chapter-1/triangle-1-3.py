from graphics import *
from turtle import *

shape('turtle')

def square(sideLength=100):
    for i in range(4):
        forward(sideLength)
        right(90)

def sqcircle():
    for i in range(60):
        square()
        right(5)

def triangle(sideLength=100):
    for i in range(3):
        forward(sideLength)
        right(120)

triangle(50)
triangle()
triangle(150)
