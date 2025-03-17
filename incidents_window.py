import tkinter as tk
from tkinter import ttk
import database

class IncidentsWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Manage Incidents")
        self.window.geometry("700x500")

        tk.Label(self.window, text="Incident Management", font=("Arial", 18)).pack(pady=10)

        self.tree = ttk.Treeview(self.window, columns=("ID", "Timestamp", "Description", "Status"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Timestamp", text="Timestamp")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.report_frame = tk.Frame(self.window)
        self.report_frame.pack(pady=10)

        tk.Label(self.report_frame, text="Description:").grid(row=0, column=0, padx=5)
        self.description_entry = tk.Entry(self.report_frame, width=50)
        self.description_entry.grid(row=0, column=1, padx=5)
        tk.Button(self.report_frame, text="Report", command=self.report_incident).grid(row=0, column=2, padx=5)

        self.load_incidents()

    def load_incidents(self):
        incidents = database.fetch_data("incidents")
        for row in incidents:
            self.tree.insert("", tk.END, values=row)

    def report_incident(self):
        description = self.description_entry.get()
        if description.strip():
            database.insert_incident(description)
            self.load_incidents()
            self.description_entry.delete(0, tk.END)
        else:
            tk.messagebox.showerror("Error", "Description cannot be empty.")
