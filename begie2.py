from turtle import *
from random import*

def click_draw(x,y):
    goto(x,y)
    pendown()
    a=randint(0,7)
    color(colors_list[a])
    begin_fill()
    circle(25)
    end_fill()
    penup()
    
colors_list = ['red','bisque','royalblue', 'orange','limegreen','tomato','green','olive']
    
ht()
penup()
speed(0)

onscreenclick( click_draw )
