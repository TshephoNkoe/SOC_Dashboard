import tkinter as tk

class LogsWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("View Logs")
        self.window.geometry("700x500")

        tk.Label(self.window, text="SOC Logs", font=("Arial", 18)).pack(pady=10)

        self.text_area = tk.Text(self.window, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.load_logs()

    def load_logs(self):
        try:
            with open("logs/soc.log", "r") as log_file:
                logs = log_file.read()
                self.text_area.insert(tk.END, logs)
        except FileNotFoundError:
            self.text_area.insert(tk.END, "No logs available.")
