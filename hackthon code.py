import tkinter as tk
from tkinter import ttk, messagebox

class FacultyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Faculty Self-Appraisal System")
        self.geometry("700x600")
        self.resizable(False, False)
        self.create_login_ui()

    def create_login_ui(self):
        self.clear_window()

        tk.Label(self, text="Login", font=("Arial", 20)).pack(pady=20)
        tk.Label(self, text="Email").pack()
        self.email_entry = tk.Entry(self, width=30)
        self.email_entry.pack()

        tk.Label(self, text="Password").pack()
        self.password_entry = tk.Entry(self, show="*", width=30)
        self.password_entry.pack()

        tk.Button(self, text="Login", command=self.login).pack(pady=10)
        tk.Button(self, text="Register", command=self.create_register_ui).pack()

    def create_register_ui(self):
        self.clear_window()

        tk.Label(self, text="Register", font=("Arial", 20)).pack(pady=20)
        labels = ["Name", "Email", "Password", "Employee Code"]
        self.reg_entries = {}

        for label in labels:
            tk.Label(self, text=label).pack()
            entry = tk.Entry(self, width=30, show="*" if label == "Password" else "")
            entry.pack()
            self.reg_entries[label] = entry

        tk.Label(self, text="Role").pack()
        self.role_var = tk.StringVar(value="faculty")
        ttk.Combobox(self, textvariable=self.role_var, values=["faculty", "admin"], width=27).pack()

        tk.Button(self, text="Submit", command=self.register).pack(pady=10)
        tk.Button(self, text="Back to Login", command=self.create_login_ui).pack()

    def create_faculty_form_ui(self):
        self.clear_window()

        tk.Label(self, text="Self-Appraisal Form", font=("Arial", 18)).pack(pady=10)
        self.form_fields = {}

        fields = [
            "Research Publications", "Seminars Attended", "Projects Worked On",
            "Lectures Delivered", "Date of Submission (YYYY-MM-DD)"
        ]

        for field in fields:
            tk.Label(self, text=field).pack()
            entry = tk.Entry(self, width=50)
            entry.pack()
            self.form_fields[field] = entry

        tk.Button(self, text="Submit Appraisal", command=self.submit_appraisal).pack(pady=15)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        # Here you should verify with backend
        if email and password:
            if "admin" in email:
                messagebox.showinfo("Login", "Logged in as Admin (UI not yet built)")
            else:
                messagebox.showinfo("Login", "Login Successful as Faculty")
                self.create_faculty_form_ui()
        else:
            messagebox.showerror("Error", "Email or Password cannot be empty")

    def register(self):
        name = self.reg_entries["Name"].get()
        email = self.reg_entries["Email"].get()
        password = self.reg_entries["Password"].get()
        emp_code = self.reg_entries["Employee Code"].get()
        role = self.role_var.get()
        # Send this to backend for storage
        if all([name, email, password, emp_code]):
            messagebox.showinfo("Registered", f"Registered Successfully as {role}")
            self.create_login_ui()
        else:
            messagebox.showerror("Error", "All fields are required")

    def submit_appraisal(self):
        data = {key: entry.get() for key, entry in self.form_fields.items()}
        # Send this to backend/database
        if all(data.values()):
            messagebox.showinfo("Submitted", "Appraisal submitted successfully")
            self.create_login_ui()
        else:
            messagebox.showerror("Error", "All fields must be filled")

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == '__main__':
    app = FacultyApp()
    app.mainloop()