import tkinter as tk
from tkinter import ttk, messagebox
from db import get_connection
from student_form import StudentForm

# ------------------ MAIN WINDOW ------------------
root = tk.Tk()
root.title("Student Management System")
root.geometry("1100x500")

# ------------------ TABLE ------------------
columns = ("id", "name", "mobile", "dob", "course", "gender", "address")

tree = ttk.Treeview(root, columns=columns, show="headings")

tree.heading("id", text="ID")
tree.heading("name", text="NAME")
tree.heading("mobile", text="MOBILE")
tree.heading("dob", text="DOB")
tree.heading("course", text="COURSE")
tree.heading("gender", text="GENDER")
tree.heading("address", text="ADDRESS")

tree.column("id", width=50, anchor="center")
tree.column("name", width=150)
tree.column("mobile", width=120)
tree.column("dob", width=100)
tree.column("course", width=100)
tree.column("gender", width=80)
tree.column("address", width=250)

tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# ------------------ FUNCTIONS ------------------
def load_students():
    tree.delete(*tree.get_children())

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, full_name, mobile, dob, course, gender, address
        FROM students
        ORDER BY id DESC
    """)

    for row in cur.fetchall():
        tree.insert("", tk.END, values=row)

    conn.close()


def add_student():
    StudentForm(root, load_students)


def edit_student():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Select a student to edit")
        return

    data = tree.item(selected, "values")
    StudentForm(root, load_students, data)


def delete_student():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Select a student to delete")
        return

    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this student?")
    if confirm:
        student_id = tree.item(selected, "values")[0]

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM students WHERE id = %s", (student_id,))
        conn.commit()
        conn.close()

        load_students()
        messagebox.showinfo("Success", "Student deleted successfully")


# ------------------ BUTTONS ------------------
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="➕ Add Student", width=15, command=add_student).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="✏ Edit Student", width=15, command=edit_student).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="🗑 Delete Student", width=15, command=delete_student).grid(row=0, column=2, padx=10)
tk.Button(btn_frame, text="🔄 Refresh", width=15, command=load_students).grid(row=0, column=3, padx=10)

# ------------------ LOAD DATA ------------------
load_students()

root.mainloop()
