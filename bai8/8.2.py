print("Pham Tien Lap")
print("245752021610071")
import turtle, random

colors = ['red','green','blue','orange','purple','pink','yellow']
painter = turtle.Turtle()
painter.pensize(10)

for i in range(12):
    color = random.choice(colors)
    painter.pencolor(color)
    painter.circle(100)
    painter.left(30)
    painter.setposition(0,0)
