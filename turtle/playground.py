import turtle
from time import sleep

turtle.speed(1)

# Waits for canvas to move
sleep(1)

for i in range(0, 4):
    turtle.forward(20)
    turtle.left(90)

turtle.done()
