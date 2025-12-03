print("Pham Tien lap")
print("245752021610071")
from tkinter import *

def Newfile():
    print("New File! (Tạo tệp mới.)")

def Openfile():
    print("Open File!")

def Exit_program():
    print("Exiting Program...")
    window.quit() # Lệnh thoát ứng dụng Tkinter

def Inserttext():
    print("Insert Text")

def Insertpic():
    print("Insert Picture")

print("Đây là ví dụ đơn giản về menu")

#tạo window form
window = Tk()
window.title("tk")
window.geometry("400x300")

#tạo thanh menu
menu = Menu(window)
window.config(menu=menu) # gán thanh menu vào cửa sổ gốc

#file:
filemenu = Menu(menu, tearoff=0) # tearoff=0 loại bỏ dấu gạch đứt
menu.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label="New", command=Newfile)
filemenu.add_command(label="Open", command=Openfile)
filemenu.add_separator() #tạo đường kẻ ngăn
