from tkinter import *

import db


def load_notes():
    notes = db.select_all()

    for i, note in enumerate(notes):
        note_frame = Frame(scrollable_frame, bg="#B93B3B", width=240, height=240, padx=20, pady=20)
        note_frame.grid(row=i//3, column=i%3, padx=15, pady=15)
        note_frame.pack_propagate(False)

        btn_frame = Frame(note_frame, bg='#B93B3B', relief='solid')
        btn_frame.pack(side=TOP, pady=0, padx=0)
        id_label = Label(btn_frame, bg='#B93B3B', fg='white', text='#'+str(note[0]), font=('Verdana', 10, 'bold'))
        id_label.pack(side=LEFT, padx=(0, 75))
        btn_delete = Button(btn_frame, text="X", padx=2, pady=0, bg="black", fg="white", font=('Verdana', 8, "bold"), relief="flat")
        btn_delete.pack(side=RIGHT, padx=(75, 0))

        title_label = Label(note_frame, bg='#B93B3B', fg='white', text=str(note[1]), anchor="w", font=('Verdana', 11, 'bold'), relief='flat')
        title_label.pack(side=TOP, padx=0,pady=5, fill=X)

        content_text = Text(note_frame, wrap='word', width=40, height=6, bg='#B93B3B', fg='white', font=('Verdana', 9), relief='flat')
        content_text.insert('1.0', str(note[2]))
        content_text.configure(state='disabled')
        content_text.pack(side=TOP, padx=0, pady=10, anchor='w')

        btn_update = Button(note_frame, text='Modify', padx=2, pady=2, bg='black', fg='white', font=('Verdana', 10, 'bold'), relief='flat')
        btn_update.pack(side=BOTTOM, padx=0, pady=0)


def note_popup():
    def add_note():
        note_title = field_title.get("1.0", "end-1c")
        note_content = field_content.get("1.0", "end-1c")
        db.add(note_title, note_content, None, 1)
        popup.destroy()
        load_notes()

    popup = Toplevel(root)
    popup.overrideredirect(True)
    popup.geometry("580x550+500+182")
    popup.config(bg='#B93B3B')

    label_title = Label(popup, text="Tile", font=("Verdana", 14), bg='#B93B3B', fg='white', anchor="w")
    label_title.pack(fill="x", pady=(60, 20), padx=60, anchor="w")
    field_title = Text(popup, bg='#FFF8DC', fg='black', font=('Verdana', 14), height=1, relief="flat")
    field_title.pack(pady=0, fill=X, padx=60, anchor="w")

    label_content = Label(popup, text="Content", font=('Verdana', 14), bg='#B93B3B', fg='white', anchor="w")
    label_content.pack(fill="x", pady=20, padx=60)
    field_content = Text(popup, wrap=WORD, padx=10, pady=10, bg='#FFF8DC', fg='black',font=('Verdana', 12), height=10)
    field_content.pack(pady=0, fill=BOTH, padx=60)

    btn_frame = Frame(popup, bg='#B93B3B')
    btn_frame.pack(side=BOTTOM, pady=(20, 60), padx=60, anchor="w")

    btn_save = Button(btn_frame, text="SAVE", command=add_note, bd=1, bg="#2E7D32", fg="white", padx=20, pady=7, font=("Verdana", 10, "bold"), relief="solid")
    btn_save.pack(side=LEFT, padx=68)

    btn_close = Button(btn_frame, text="EXIT", command=popup.destroy, bd=1, bg="#B71C1C", fg="white", padx=15, pady=7, font=("Verdana", 10, "bold"), relief="solid")
    btn_close.pack(side=LEFT, padx=68)




db.db_setup()

root = Tk()
root.title("Memo")
root.configure(bg="#242528")
root.geometry('1100x675+218+94')

app_btn_frame = Frame(root, bg='#242528', height=100, bd=1, relief='flat')
app_btn_frame.pack(side=TOP, pady=60, padx=200, fill=X)

btn_create_note = Button(app_btn_frame, text="Create new note...", command=note_popup, padx=70, pady=10, bg="#35373A", fg="white", font=('Verdana', 10), relief="flat")
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

load_notes()

bottom_frame = Frame(root, bg='#242528', height=100, bd=1, relief="flat")
bottom_frame.pack(side=BOTTOM, pady=60)
btn_exit = Button(bottom_frame, text="EXIT", command=root.destroy, padx=10, pady=5, bg="red", fg="white", font=('Verdana', 10, "bold"), relief="flat")
btn_exit.pack(side=RIGHT, padx=60)

root.mainloop()