import turtle

for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.hideturtle()

export = turtle.getscreen()
export.getcanvas().postscript(file="test.dxf")

turtle.done()
