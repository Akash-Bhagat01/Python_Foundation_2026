import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def submit_form():
    data = f"""
Full Name : {full_name.get()}
Mobile    : {mobile.get()}
DOB       : {dob.get()}
Course    : {course.get()}
Gender    : {gender.get()}
Address   : {address.get("1.0", tk.END).strip()}
"""
    messagebox.showinfo("Form Data", data)

def open_popup():
    pop = tk.Toplevel(root)
    pop.title("Popup")
    pop.geometry("250x120")
    tk.Label(pop, text="Form submitted successfully ✅").pack(pady=20)
    tk.Button(pop, text="Close", command=pop.destroy).pack()

# ---------- Main Window ----------
root = tk.Tk()
root.title("Student Registration Form Akash")
root.geometry("520x520")

# ---------- Variables ----------
full_name = tk.StringVar()
mobile = tk.StringVar()
dob = tk.StringVar()
course = tk.StringVar(value="Select Course")
gender = tk.StringVar(value="Male")
# ---------- Full Name ----------
tk.Label(root, text="Full Name").pack(anchor="w", padx=10)
tk.Entry(root, textvariable=full_name).pack(fill="x", padx=10)

# ---------- Mobile ----------
tk.Label(root, text="Mobile").pack(anchor="w", padx=10, pady=(8,0))
tk.Entry(root, textvariable=mobile).pack(fill="x", padx=10)

# ---------- DOB ----------
tk.Label(root, text="Date of Birth (DD-MM-YYYY)").pack(anchor="w", padx=10, pady=(8,0))
tk.Entry(root, textvariable=dob).pack(fill="x", padx=10)

# ---------- Course Dropdown ----------
tk.Label(root, text="Course").pack(anchor="w", padx=10, pady=(8,0))
courses = ["BCA", "MCA", "BSc", "MSc", "MBA"]
ttk.Combobox(root, values=courses, textvariable=course, state="readonly").pack(fill="x", padx=10)

# ---------- Gender ----------
tk.Label(root, text="Gender").pack(anchor="w", padx=10, pady=(8,0))
tk.Radiobutton(root, text="Male", variable=gender, value="Male").pack(anchor="w", padx=20)
tk.Radiobutton(root, text="Female", variable=gender, value="Female").pack(anchor="w", padx=20)

# ---------- Address ----------
tk.Label(root, text="Address").pack(anchor="w", padx=10, pady=(8,0))
address = tk.Text(root, height=4)
address.pack(fill="x", padx=10)

# ---------- Buttons ----------
tk.Button(root, text="Submit", command=submit_form).pack(pady=10)
tk.Button(root, text="Popup Message", command=open_popup).pack()
tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()
