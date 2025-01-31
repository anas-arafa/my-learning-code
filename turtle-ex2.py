import turtle

t=turtle.Screen()
a=turtle.Turtle()
a.shape("turtle")
a.fillcolor("red")
a.begin_fill()
a.color("green")
for x in range(5):
    a.lt(144)
    a.fd(100)
a.end_fill()
turtle.done()
