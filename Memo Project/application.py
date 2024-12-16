import json
from tkinter import *

import db


def load_notes():
    def delete_note(id_label):
        db.delete(id_label)
        for widget in scrollable_frame.winfo_children():
            widget.destroy()
        load_notes()

    notes = db.select_all()

    for i, note in enumerate(notes):
        note_frame = Frame(scrollable_frame, bg="#B93B3B", width=240, height=240, padx=20, pady=20)
        note_frame.grid(row=i//3, column=i%3, padx=15, pady=15)
        note_frame.pack_propagate(False)

        btn_frame = Frame(note_frame, bg='#B93B3B', relief='solid')
        btn_frame.pack(side=TOP, pady=0, padx=0)
        id_label = Label(btn_frame, bg='#B93B3B', fg='white', text='#'+str(note[0]), font=('Verdana', 10, 'bold'))
        id_label.pack(side=LEFT, padx=(0, 75))
        if note[-1] == 1:
            btn_delete = Button(btn_frame, text="X", command=lambda id_label=id_label: delete_note(id_label), padx=2, pady=0, bg="black", fg="white", font=('Verdana', 8, "bold"), relief="flat")
        else:
            btn_delete = Button(btn_frame, text="X", padx=2, pady=0, bg="black", fg="white", font=('Verdana', 8, "bold"), relief="flat")
        btn_delete.pack(side=RIGHT, padx=(75, 0))

        title_label = Label(note_frame, bg='#B93B3B', fg='white', text=str(note[1]), anchor="w", font=('Verdana', 11, 'bold'), relief='flat')
        title_label.pack(side=TOP, padx=0,pady=5, fill=X)

        content_text = Text(note_frame, wrap='word', width=40, height=6, bg='#B93B3B', fg='white', font=('Verdana', 9), relief='flat')
        if note[-1] == 1:
            content_text.insert('1.0', str(note[2]))
        else:
            tasks = json.loads(note[3])
            for i, task in enumerate(tasks, start=1):
                content_text.insert("end", f"{i}. {task}\n")
        content_text.configure(state='disabled')
        content_text.pack(side=TOP, padx=0, pady=10, anchor='w')

        if note[-1] == 1:
            btn_update = Button(note_frame, text='Modify', command=lambda id_label=id_label: note_popup(id_label), padx=2, pady=2, bg='black', fg='white', font=('Verdana', 10, 'bold'), relief='flat')
        else:
            btn_update = Button(note_frame, text='Modify', command=lambda id_label=id_label: todo_list_popup(id_label), padx=2, pady=2, bg='black', fg='white', font=('Verdana', 10, 'bold'), relief='flat')
        btn_update.pack(side=BOTTOM, padx=0, pady=0)


def note_popup(param=None):
    def add_note():
        note_title = field_title.get("1.0", "end-1c")
        note_content = field_content.get("1.0", "end-1c")
        db.add(note_title, note_content, None, 1)
        popup.destroy()
        load_notes()

    def edit_note():
        id = param.cget("text")[1:]
        updated_title = field_title.get("1.0", "end-1c")
        updated_content = field_content.get("1.0", "end-1c")
        db.edit(id, updated_title, updated_content, None)
        popup.destroy()
        load_notes()

    if param is not None:
        id = param.cget("text")[1:]
        prev_note = db.select(id)
        prev_title = prev_note[0][1]
        prev_content = prev_note[0][2]

    popup = Toplevel(root)
    popup.overrideredirect(True)
    popup.geometry("580x550+500+182")
    popup.config(bg='#B93B3B')

    label_title = Label(popup, text="Tile", font=("Verdana", 14), bg='#B93B3B', fg='white', anchor="w")
    label_title.pack(fill="x", pady=(60, 20), padx=60, anchor="w")
    field_title = Text(popup, bg='#FFF8DC', fg='black', font=('Verdana', 14), height=1, relief="flat")
    if param is not None:
        field_title.insert("1.0", prev_title)
    field_title.pack(pady=0, fill=X, padx=60, anchor="w")

    label_content = Label(popup, text="Content", font=('Verdana', 14), bg='#B93B3B', fg='white', anchor="w")
    label_content.pack(fill="x", pady=20, padx=60)
    field_content = Text(popup, wrap=WORD, padx=10, pady=10, bg='#FFF8DC', fg='black',font=('Verdana', 12), height=10)
    if param is not None:
        field_content.insert("1.0", prev_content)
    field_content.pack(pady=0, fill=BOTH, padx=60)

    btn_frame = Frame(popup, bg='#B93B3B')
    btn_frame.pack(side=BOTTOM, pady=(20, 60), padx=60, anchor="w")

    if param is None:
        btn_save = Button(btn_frame, text="SAVE", command=add_note, bd=1, bg="#2E7D32", fg="white", padx=20, pady=7, font=("Verdana", 10, "bold"), relief="solid")
    else:
        btn_save = Button(btn_frame, text="SAVE", command=edit_note, bd=1, bg="#2E7D32", fg="white", padx=20, pady=7, font=("Verdana", 10, "bold"), relief="solid")
    btn_save.pack(side=LEFT, padx=68)

    btn_close = Button(btn_frame, text="EXIT", command=popup.destroy, bd=1, bg="#B71C1C", fg="white", padx=15, pady=7, font=("Verdana", 10, "bold"), relief="solid")
    btn_close.pack(side=LEFT, padx=68)


def todo_list_popup(param=None):
    def add_todo_list():
        todo_title = field_title.get("1.0", "end-1c")
        todo_tasks = [line.split(" ", 1)[1] for line in listbox_task.get(0, "end") if " " in line]
        todo_tasks_json = json.dumps(todo_tasks)
        db.add(todo_title, None, todo_tasks_json, 2)
        popup.destroy()
        load_notes()

    def edit_todo_list():
        id = param.cget("text")[1:]
        updated_title = field_title.get("1.0", "end-1c")
        updated_tasks = [line.split(" ", 1)[1] for line in listbox_task.get(0, "end") if " " in line]
        todo_tasks_json = json.dumps(updated_tasks)
        db.edit(id, updated_title, None, todo_tasks_json)
        popup.destroy()
        load_notes()


    def add_task():
        task_string = field_task.get()
        if len(task_string) == 0:
            show_warning("Empty field!")
        else:
            tasks.append(task_string)
            list_update()
            field_task.delete(0, 'end')

    def delete_task():
        if len(tasks) == 0:
            show_warning("No tasks to delete!")
            return
        try:
            selected_task = " ".join(listbox_task.get(listbox_task.curselection()).split(" ")[1:])
            if selected_task in tasks:
                tasks.remove(selected_task)
                list_update()
        except:
            show_warning("No task selected!")

    def delete_all_tasks():
        if len(tasks) == 0:
            show_warning("No tasks to delete!")
        else:
            while len(tasks) != 0:
                tasks.pop()
            list_update()

    def list_update():
        clear_list()
        for idx, task in enumerate(tasks, start=1):
            listbox_task.insert('end', f"{idx}. {task}")

    def clear_list():
        listbox_task.delete(0, 'end')

    def show_warning(warning):
        field_task.configure(fg="red")
        field_task.insert(0, warning)
        popup.after(1000, clear_warning)

    def clear_warning():
        field_task.delete(0, 'end')
        field_task.configure(fg="black")

    if param is not None:
        id = param.cget("text")[1:]
        prev_note = db.select(id)
        prev_title = prev_note[0][1]
        prev_tasks = json.loads(prev_note[0][3])
        tasks = prev_tasks
    else:
        tasks = []

    popup = Toplevel(root)
    popup.overrideredirect(True)
    popup.geometry("580x550+500+182")
    popup.config(bg='#B93B3B')

    label_title = Label(popup, text="Tile", font=("Verdana", 12), bg='#B93B3B', fg='white', anchor="w")
    label_title.pack(fill="x", pady=(60, 20), padx=60, anchor="w")
    field_title = Text(popup, padx=10, pady=10, bg='#FFF8DC', fg='black', font=('Verdana', 12), height=1, )
    if param is not None:
        field_title.insert("1.0", prev_title)
    field_title.pack(pady=0, fill=X, padx=60, anchor="w")

    main_frame = Frame(popup, bg="#B93B3B")
    main_frame.pack(expand=True, fill=BOTH)

    functions_frame = Frame(main_frame, bg="#B93B3B",width=290, height=250)
    listbox_frame = Frame(main_frame, bg="#B93B3B", width=290, height=250)
    functions_frame.pack(side=LEFT, padx=0, pady=0)
    listbox_frame.pack(side=RIGHT, padx=0, pady=0)

    label_task = Label(functions_frame, text="Enter a task:", bg="#B93B3B", fg="white", font=("Verdana", 12))
    label_task.place(x=60, y=0)
    field_task = Entry(functions_frame, bd=5, relief="flat", bg="white", fg="black", font=("Verdana", 10), width=21)
    field_task.place(x=60, y=40)

    btn_add_task = Button(functions_frame, text="Add Task", command=add_task, bg="#A9A9A9", pady=3, font=("Verdana", 10), width=21, relief="flat")
    btn_add_task.place(x=60, y=110)
    btn_del_task = Button(functions_frame, text="Delete Task", command=delete_task, bg="#A9A9A9", pady=3, font=("Verdana", 10), width=21, relief="flat")
    btn_del_task.place(x=60, y=160)
    btn_del_all_tasks = Button(functions_frame, text="Delete All Tasks", command=delete_all_tasks, bg="#A9A9A9", pady=3, font=("Verdana", 10), width=21, relief="flat")
    btn_del_all_tasks.place(x=60, y=210)

    listbox_task = Listbox(listbox_frame, bd=10, width=26, height=12, selectmode='SINGLE', bg="white", fg="black", selectbackground="#FFF8DC", selectforeground="black", font=("Verdana", 10), relief="flat")
    if param is not None:
        for i, task in enumerate(prev_tasks, start=1):
            listbox_task.insert("end", f"{i}. {task}")
    listbox_task.place(x=0, y=15)

    btn_frame = Frame(popup, bg='#B93B3B')
    btn_frame.pack(side=BOTTOM, pady=(20, 60), padx=60, anchor="w")

    if param is None:
        btn_save = Button(btn_frame, text="SAVE", command=add_todo_list, bd=1, bg="#2E7D32", fg="white", padx=20, pady=7, font=("Verdana", 10, "bold"), relief="solid")
    else:
        btn_save = Button(btn_frame, text="SAVE", command=edit_todo_list, bd=1, bg="#2E7D32", fg="white", padx=20, pady=7, font=("Verdana", 10, "bold"), relief="solid")
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

btn_create_todo_list = Button(app_btn_frame, text="Create new to-do list...", command=todo_list_popup, padx=50, pady=10, bg="#35373A", fg="white", font=('Verdana', 10), relief="flat")
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