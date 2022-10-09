from turtle import *

shape('turtle')

def star(length=100):
    for i in range(5):
        forward(length)
        right(144)

def spiral():
    length = 5
    for i in range(60):
        star(length)
        right(5)
        length += 5

spiral()

    

