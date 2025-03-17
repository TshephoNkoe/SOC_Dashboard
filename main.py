import tkinter as tk
import threading  # For running monitoring in a separate thread
import time # For simulating monitoring delay
from ttkbootstrap import Style, ttk
from monitoring import access_splunk_home  # From monitoring.py
from network import monitor_network_traffic, check_open_ports  # From network.py
from detection import get_alerts  # From detection.py
from mitigation import run_mitigation  # From mitigation.py
from pentesting import run_pentest  # From pentesting.py
from tkinter import simpledialog, messagebox  # Add simpledialog explicitly



class SOCApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NSFAS SOC Dashboard")
        self.geometry("1000x700")
        self.style = Style("flatly")

        # Add a menu bar
        self.create_menu_bar()

        # Add a status bar
        self.status_bar = ttk.Label(self, text="Welcome to NSFAS SOC Tool", anchor="w", bootstyle="secondary")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Container for frames
        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Create frames for each page
        self.frames = {}
        for Page in (HomePage, MonitoringPage, SplunkPage, NetworkPage, VulnerabilityPage, MitigationPage, PentestPage):
            page_name = Page.__name__
            frame = Page(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame("HomePage")

    def create_menu_bar(self):
        menu_bar = tk.Menu(self)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Home", command=lambda: self.show_frame("HomePage"))
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Features menu
        features_menu = tk.Menu(menu_bar, tearoff=0)
        features_menu.add_command(label="Monitoring", command=lambda: self.show_frame("MonitoringPage"))
        features_menu.add_command(label="Splunk", command=lambda: self.show_frame("SplunkPage"))
        features_menu.add_command(label="Network Traffic", command=lambda: self.show_frame("NetworkPage"))
        features_menu.add_command(label="Vulnerability Detection", command=lambda: self.show_frame("VulnerabilityPage"))
        features_menu.add_command(label="Mitigation", command=lambda: self.show_frame("MitigationPage"))
        features_menu.add_command(label="Pentesting", command=lambda: self.show_frame("PentestPage"))
        menu_bar.add_cascade(label="Features", menu=features_menu)

        self.config(menu=menu_bar)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def update_status_bar(self, message):
        self.status_bar.config(text=message)

class HomePage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        header = ttk.Label(self, text="NSFAS SOC Dashboard", font=("Arial", 28, "bold"), bootstyle="info")
        header.pack(pady=20)

        description = ttk.Label(self, text="Select a feature from the menu or buttons below:", font=("Arial", 16))
        description.pack(pady=10)

        # Navigation buttons
        for text, page in [("Monitoring", "MonitoringPage"),
                           ("Access Splunk", "SplunkPage"),
                           ("Network Traffic", "NetworkPage"),
                           ("Vulnerability Detection", "VulnerabilityPage"),
                           ("Mitigation", "MitigationPage"),
                           ("Pentesting", "PentestPage")]:
            button = ttk.Button(self, text=text, command=lambda p=page: controller.show_frame(p), bootstyle="primary")
            button.pack(pady=10)

class VulnerabilityPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        header = ttk.Label(self, text="Vulnerability Detection", font=("Arial", 20), bootstyle="info")
        header.pack(pady=20)

        scan_button = ttk.Button(self, text="Scan Open Ports", command=self.scan_open_ports, bootstyle="success")
        scan_button.pack(pady=10)

        back_button = ttk.Button(self, text="Back to Dashboard", command=lambda: controller.show_frame("HomePage"), bootstyle="secondary")
        back_button.pack(pady=10)

    def scan_open_ports(self):
        # Ask for the target IP address
        target_ip = tk.simpledialog.askstring("Input", "Enter the target IP address:")
        if target_ip:
            open_ports = check_open_ports(target_ip)  # From network.py
            if open_ports:
                ports = ", ".join(map(str, open_ports))
                tk.messagebox.showinfo("Open Ports Found", f"Open ports: {ports}")
            else:
                tk.messagebox.showinfo("No Open Ports", "No open ports detected.")
        else:
            tk.messagebox.showwarning("Invalid Input", "Please enter a valid IP address.")
    def save_log(message):
        conn = sqlite3.connect('cybersecurity_tool.db')
        c = conn.cursor()
        c.execute("INSERT INTO logs (log_message) VALUES (?)", (message,))
        conn.commit()
        conn.close()

class MonitoringPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        header = ttk.Label(self, text="Monitoring", font=("Arial", 20), bootstyle="info")
        header.pack(pady=20)

        monitor_button = ttk.Button(self, text="Fetch Alerts", command=self.fetch_alerts, bootstyle="success")
        monitor_button.pack(pady=10)

        back_button = ttk.Button(self, text="Back to Dashboard", command=lambda: controller.show_frame("HomePage"), bootstyle="secondary")
        back_button.pack(pady=10)

    def fetch_alerts(self):
        alerts = get_alerts()  # Fetch from detection.py
        alert_messages = "\n".join([f"{alert[1]}: {alert[2]}" for alert in alerts])
        tk.messagebox.showinfo("Alerts", alert_messages)

class SplunkPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        header = ttk.Label(self, text="Splunk Integration", font=("Arial", 20), bootstyle="info")
        header.pack(pady=20)

        back_button = ttk.Button(self, text="Back to Dashboard", command=lambda: controller.show_frame("HomePage"), bootstyle="secondary")
        back_button.pack(pady=10)

class NetworkPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.monitoring = False
        self.threshold = 1000000  # Default threshold in bytes

        header = ttk.Label(self, text="Network Traffic", font=("Arial", 20), bootstyle="info")
        header.pack(pady=20)

        self.threshold_entry = ttk.Entry(self)
        self.threshold_entry.insert(0, str(self.threshold))
        self.threshold_entry.pack(pady=5)

        self.set_threshold_button = ttk.Button(self, text="Set Threshold", command=self.set_threshold, bootstyle="info")
        self.set_threshold_button.pack(pady=5)

        self.traffic_label = ttk.Label(self, text="Traffic Data: Not Available", font=("Arial", 14))
        self.traffic_label.pack(pady=10)

        self.monitor_button = ttk.Button(self, text="Start Monitoring", command=self.toggle_monitoring, bootstyle="success")
        self.monitor_button.pack(pady=10)

        back_button = ttk.Button(self, text="Back to Dashboard", command=lambda: controller.show_frame("HomePage"), bootstyle="secondary")
        back_button.pack(pady=10)

    def set_threshold(self):
        try:
            self.threshold = int(self.threshold_entry.get())
            tk.messagebox.showinfo("Threshold Set", f"Threshold set to {self.threshold} bytes.")
        except ValueError:
            tk.messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def toggle_monitoring(self):
        if self.monitoring:
            self.monitoring = False
            self.monitor_button.config(text="Start Monitoring")
        else:
            self.monitoring = True
            self.monitor_button.config(text="Stop Monitoring")
            threading.Thread(target=self.update_traffic).start()

    def update_traffic(self):
        while self.monitoring:
            traffic = monitor_network_traffic()
            total_traffic = traffic['bytes_sent'] + traffic['bytes_recv']
            self.traffic_label.config(
                text=f"Sent: {traffic['bytes_sent']} bytes | Received: {traffic['bytes_recv']} bytes"
            )
            # Save to database
            save_log(f"Traffic - Sent: {traffic['bytes_sent']}, Received: {traffic['bytes_recv']}")

            if total_traffic > self.threshold:
                tk.messagebox.showwarning("Traffic Alert", f"Traffic exceeded the threshold! ({total_traffic} bytes)")

            time.sleep(1)



class MitigationPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        header = ttk.Label(self, text="Mitigation", font=("Arial", 20), bootstyle="info")
        header.pack(pady=20)

        run_button = ttk.Button(self, text="Run Mitigation", command=run_mitigation, bootstyle="success")
        run_button.pack(pady=10)

        back_button = ttk.Button(self, text="Back to Dashboard", command=lambda: controller.show_frame("HomePage"), bootstyle="secondary")
        back_button.pack(pady=10)

class PentestPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        header = ttk.Label(self, text="Pentesting", font=("Arial", 20), bootstyle="info")
        header.pack(pady=20)

        pentest_button = ttk.Button(self, text="Run Pentest", command=run_pentest, bootstyle="success")
        pentest_button.pack(pady=10)

        back_button = ttk.Button(self, text="Back to Dashboard", command=lambda: controller.show_frame("HomePage"), bootstyle="secondary")
        back_button.pack(pady=10)

if __name__ == "__main__":
    app = SOCApp()
    app.mainloop()
