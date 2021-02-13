from turtle import *
setup()
x = 200

y = 200



def circles (nhexagon):
    radius= 50
    colour="brown"
    size_length = 6
    penup()
    pencolor (colour)
    goto (0,radius)
    pendown ()
    setheading (180)
    #circle (radius)
    def inner(*args, **kwargs):
        ff = nhexagon(*args, **kwargs)
        return ff
    
        
        
    penup()
    return inner

import turtle

@circles
def hexagon (size_length):
    pendown ()
    forward(size_length)
    right (60)
   
    
    
    circle (10)
    


for _ in range (6):
    hexagon (50)     
    #
