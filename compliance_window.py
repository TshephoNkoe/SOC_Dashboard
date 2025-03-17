import tkinter as tk
from tkinter import ttk
import database

class ComplianceWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Compliance Status")
        self.window.geometry("700x500")

        tk.Label(self.window, text="Compliance Status", font=("Arial", 18)).pack(pady=10)

        self.tree = ttk.Treeview(self.window, columns=("ID", "Policy Name", "Status"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Policy Name", text="Policy Name")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.load_compliance()

    def load_compliance(self):
        compliance_data = database.fetch_data("compliance")
        for row in compliance_data:
            self.tree.insert("", tk.END, values=row)
