from turtle import *

#we want to draw a house

#step 1: draw a square 

width(7)
color("blue")
speed(10)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color ("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#draw a windows
penup()
left(30)
forward(25)
left(90)
forward(25)
pendown()
begin_fill()
forward(35)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
end_fill()


#draw a windows two
penup()
right(90)
forward(120)
pendown()
begin_fill()
forward(35)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
end_fill()


exitonclick()