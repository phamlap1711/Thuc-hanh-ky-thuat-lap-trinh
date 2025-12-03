print("Pham Tien Lap")
print("245752021601071")
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

painter = turtle.Turtle()
painter.fillcolor('blue')
painter.pencolor('blue')
painter.pensize(3)

def vehinhvuong(t,s):
    for i in range(4): #lặp lại 4 lần
        t.forward(s) #đi thẳng 1 đoạn s
        t.left(90) #xoay góc 90 độ
for i in range(10):
    painter.left(36)#con trở sau khi vẽ xong 1 hình thì xoay 36 độ
    vehinhvuong(painter,200)
