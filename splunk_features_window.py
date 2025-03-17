import tkinter as tk

class SplunkFeaturesWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Splunk Features")
        self.window.geometry("700x500")

        tk.Label(self.window, text="Splunk Features", font=("Arial", 18)).pack(pady=10)

        features = (
            "- Centralized Logging and Indexing\n"
            "- Advanced Analytics and Machine Learning\n"
            "- Real-time Alerts and Dashboards\n"
            "- Integration with SOAR for Automation\n"
            "- Powerful Search Capabilities\n"
        )

        text_area = tk.Text(self.window, wrap=tk.WORD)
        text_area.insert(tk.END, features)
        text_area.config(state=tk.DISABLED)
        text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
