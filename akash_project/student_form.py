import tkinter as tk
from tkinter import ttk, messagebox
from db import get_connection

class StudentForm(tk.Toplevel):
    def __init__(self, parent, refresh_callback, data=None):
        super().__init__(parent)
        self.refresh_callback = refresh_callback
        self.data = data
        self.title("Student Form")
        self.geometry("400x450")

        # ---------------- VARIABLES ----------------
        self.name = tk.StringVar()
        self.mobile = tk.StringVar()
        self.dob = tk.StringVar()
        self.course = tk.StringVar()
        self.gender = tk.StringVar(value="MALE")
        self.address = tk.StringVar()

        if data:
            self.name.set(data[1])
            self.mobile.set(data[2])
            self.dob.set(data[3])
            self.course.set(data[4])
            self.gender.set(data[5])
            self.address.set(data[6])  


        # ---------------- FORM ----------------
        tk.Label(self, text="Full Name").pack(anchor="w", padx=10)
        tk.Entry(self, textvariable=self.name).pack(fill="x", padx=10)

        tk.Label(self, text="Mobile").pack(anchor="w", padx=10, pady=5)
        tk.Entry(self, textvariable=self.mobile).pack(fill="x", padx=10)

        tk.Label(self, text="Date of Birth (YYYY-MM-DD)").pack(anchor="w", padx=10, pady=5)
        tk.Entry(self, textvariable=self.dob).pack(fill="x", padx=10)

        tk.Label(self, text="Course").pack(anchor="w", padx=10, pady=5)
        courses = ["BCA", "MCA", "BSc", "MSc", "BTech", "MTech"]
        ttk.Combobox(self, values=courses, textvariable=self.course).pack(fill="x", padx=10)

        tk.Label(self, text="Gender").pack(anchor="w", padx=10, pady=5)
        g_frame = tk.Frame(self)
        g_frame.pack(anchor="w", padx=10)

        tk.Radiobutton(g_frame, text="Male", variable=self.gender, value="MALE").pack(side="left")
        tk.Radiobutton(g_frame, text="Female", variable=self.gender, value="FEMALE").pack(side="left")

        tk.Label(self, text="Address").pack(anchor="w", padx=10, pady=5)
        tk.Entry(self, textvariable=self.address).pack(fill="x", padx=10)

        # ---------------- BUTTON ----------------
        btn_text = "Update Student" if data else "Add Student"
        tk.Button(self, text=btn_text, command=self.save_student).pack(pady=15)

    # ---------------- SAVE ----------------
    def save_student(self):
        if not self.name.get() or not self.mobile.get():
            messagebox.showerror("Error", "Name and Mobile required")
            return

        conn = get_connection()
        cur = conn.cursor()

        if self.data:
            cur.execute("""
                UPDATE students SET
                full_name=%s, mobile=%s, dob=%s, course=%s, gender=%s
                WHERE id=%s
            """, (
                self.name.get(),
                self.mobile.get(),
                self.dob.get(),
                self.course.get(),
                self.gender.get(),
                self.data[0]
            ))
            messagebox.showinfo("Success", "Student updated")
        else:
            cur.execute("""
                INSERT INTO students (full_name, mobile, dob, course, gender, address)
                VALUES (%s,%s,%s,%s,%s,%s)
            """, (
                self.name.get(),
                self.mobile.get(),
                self.dob.get(),
                self.course.get(),
                self.gender.get(),
                self.address.get()
            ))
            messagebox.showinfo("Success", "Student added")

        conn.commit()
        conn.close()
        self.refresh_callback()
        self.destroy()
