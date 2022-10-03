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

def polygon(sideNum=3, sideLength=100):
    #formula for internal degrees of a polygon
    intdegree = ((sideNum - 2) * 180)/(sideNum)
    #subtracting intdegree from 180 gives exterior degree of a polygon
    degree = intdegree - 180
    for i in range(sideNum):
        forward(sideLength)
        right(degree)
polygon(7, 50)
polygon()
polygon(4, 150)
