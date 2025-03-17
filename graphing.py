import tkinter as tk
import matplotlib.pyplot as plt

class ReportsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.back_button = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame("HomePage"))
        self.back_button.pack(pady=10)

        self.report_button = tk.Button(self, text="Display Log Report", command=self.display_report)
        self.report_button.pack(pady=10)

        self.graph_button = tk.Button(self, text="Generate Graph from Logs", command=self.generate_graph)
        self.graph_button.pack(pady=10)

    def display_report(self):
        logs = monitoring.fetch_splunk_logs(...)  # Pass necessary parameters
        monitoring.display_logs_in_text_widget(logs)

    def generate_graph(self):
        logs = monitoring.fetch_splunk_logs(...)  # Pass necessary parameters
        self.display_data_as_graph(logs)

    def display_data_as_graph(self, log_data):
        # Example: count the occurrences of a specific term in the logs
        terms = {"error": log_data.count("error"), "warning": log_data.count("warning")}
        
        labels = list(terms.keys())
        counts = list(terms.values())

        plt.bar(labels, counts)
        plt.xlabel('Log Type')
        plt.ylabel('Count')
        plt.title('Log Type Distribution')
        plt.show()
