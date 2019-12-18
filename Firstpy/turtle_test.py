import time
import turtle

time.sleep(0.1)

spiral = turtle.Turtle()

for i in range(20):
    spiral.forward(i*10)
    spiral.right(144)

painter = turtle.Turtle()

painter.pencolor("blue")

for i in range(20):
    painter.forward(50)
    painter.left(123)

painter.pencolor("red")
for i in range(50):
    painter.forward(1000)
    painter.left(123)

turtle.done()

print("Hello Worold!")