from tkinter import *
import os

def application():
    import application

root = Tk()
root.title("Memo App")
p = Label(root, text="Memo", bg='#660000', fg='white', font=('Georgia', 36, 'bold', 'italic'))
p.pack(expand=True)
root.configure(bg='#660000')
root.geometry('400x675+568+94')

btn_launch = Button(root, text="Start", command=application, bg='#C6A700', fg='black', padx=40, pady=10, font=('Georgia', 12, 'bold'), relief='flat')
btn_launch.pack(padx=25, pady=0)
btn_exit = Button(root, text="Exit", command=root.destroy, bg='#A9A9A9', fg='black', padx=43, pady=10, font=('Georgia', 12, 'bold'), relief='flat')
btn_exit.pack(padx=25, pady=20)

root.mainloop()