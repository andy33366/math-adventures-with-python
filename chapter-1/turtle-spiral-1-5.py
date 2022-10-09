from turtle import *

shape('turtle')

def square(sideLength=5):
    for i in range(4):
        forward(sideLength)
        right(90)

def sqspiral():
    sideLength = 5
    for i in range(60):
        square(sideLength)
        right(5)
        sideLength += 5

sqspiral()
