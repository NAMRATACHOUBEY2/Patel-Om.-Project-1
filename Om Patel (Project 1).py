import turtle
turtle.penup()
turtle.setposition(-200, 200)
turtle.pendown()
turtle.pencolor('red')
#write the color of pen in inverted commas
turtle.circle(100)
turtle.penup()
#write the location to fill the gap
turtle.goto(-200, -200)
turtle.pendown()
turtle.pencolor('green')
#write the color of pen in inverted commas
turtle.circle(200)

turtle.pencolor()
