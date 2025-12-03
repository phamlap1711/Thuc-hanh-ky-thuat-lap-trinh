print("Pham Tien Lap")
print("245752021610071")
import tkinter as tk

def hien_ket_qua():
    selection = "Bạn đã chọn: " + str(var.get())
    label_ketqua.config(text=selection)

window = tk.Tk()
window.title("Radio Button")
window.geometry("300x200")

var = tk.IntVar()   # biến kiểu số nguyên

R1 = tk.Radiobutton(window, text="Lựa chọn 1", variable=var, value=1, command=hien_ket_qua)
R1.place(x=40, y=30)

R2 = tk.Radiobutton(window, text="Lựa chọn 2", variable=var, value=2, command=hien_ket_qua)
R2.place(x=40, y=80)

R3 = tk.Radiobutton(window, text="Lựa chọn 3", variable=var, value=3, command=hien_ket_qua)
R3.place(x=40, y=130)

label_ketqua = tk.Label(window)
label_ketqua.pack()

window.mainloop()
