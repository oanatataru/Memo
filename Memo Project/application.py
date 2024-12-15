from tkinter import *



root = Tk()
root.title("Memo")
root.configure(bg="#242528")
root.geometry('1100x675+218+94')

app_btn_frame = Frame(root, bg='#242528', height=100, bd=1, relief='flat')
app_btn_frame.pack(side=TOP, pady=60, padx=200, fill=X)

btn_create_note = Button(app_btn_frame, text="Create new note...", padx=70, pady=10, bg="#35373A", fg="white", font=('Verdana', 10), relief="flat")
btn_create_note.pack(side=LEFT, padx=60)

btn_create_todo_list = Button(app_btn_frame, text="Create new to-do list...", padx=50, pady=10, bg="#35373A", fg="white", font=('Verdana', 10), relief="flat")
btn_create_todo_list.pack(side=LEFT)

frame = Frame(root, width=800, height=350)
frame.pack(side=TOP)
canvas = Canvas(frame, bg='#242528', width=800, height=350, highlightthickness=0)
canvas.pack(side=LEFT, fill=BOTH, expand=True)
vbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
vbar.pack(side=RIGHT, fill=Y)
canvas.config(yscrollcommand=vbar.set)
scrollable_frame = Frame(canvas, bg="#242528")
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

def configure_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", configure_scroll_region)



bottom_frame = Frame(root, bg='#242528', height=100, bd=1, relief="flat")
bottom_frame.pack(side=BOTTOM, pady=60)
btn_exit = Button(bottom_frame, text="EXIT", command=root.destroy, padx=10, pady=5, bg="red", fg="white", font=('Verdana', 10, "bold"), relief="flat")
btn_exit.pack(side=RIGHT, padx=60)

root.mainloop()