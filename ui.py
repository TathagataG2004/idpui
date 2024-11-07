
import tkinter as tk
from tkinter import ttk, messagebox

# Initializing the main application window
class CrackDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crack Detection Camera System")
        self.root.geometry("500x400")
        
        # Label for title
        self.title_label = tk.Label(root, text="Crack Detection Camera", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)
        
        # Camera control frame
        self.camera_frame = ttk.LabelFrame(root, text="Camera Control", padding=(10, 5))
        self.camera_frame.pack(fill="x", padx=20, pady=10)
        
        self.start_camera_button = ttk.Button(self.camera_frame, text="Start Camera", command=self.start_camera)
        self.start_camera_button.pack(side="left", padx=5)
        
        self.stop_camera_button = ttk.Button(self.camera_frame, text="Stop Camera", command=self.stop_camera)
        self.stop_camera_button.pack(side="left", padx=5)

        # Detection control frame
        self.detection_frame = ttk.LabelFrame(root, text="Detection Control", padding=(10, 5))
        self.detection_frame.pack(fill="x", padx=20, pady=10)

        self.start_detection_button = ttk.Button(self.detection_frame, text="Start Detection", command=self.start_detection)
        self.start_detection_button.pack(side="left", padx=5)

        self.stop_detection_button = ttk.Button(self.detection_frame, text="Stop Detection", command=self.stop_detection)
        self.stop_detection_button.pack(side="left", padx=5)

        # Settings frame
        self.settings_frame = ttk.LabelFrame(root, text="Settings", padding=(10, 5))
        self.settings_frame.pack(fill="x", padx=20, pady=10)
        
        self.sensitivity_label = ttk.Label(self.settings_frame, text="Detection Sensitivity:")
        self.sensitivity_label.pack(side="left", padx=5)
        
        self.sensitivity_slider = ttk.Scale(self.settings_frame, from_=1, to=10, orient="horizontal")
        self.sensitivity_slider.pack(side="left", fill="x", expand=True, padx=5)
        
        # Results frame
        self.results_frame = ttk.LabelFrame(root, text="Results", padding=(10, 5))
        self.results_frame.pack(fill="x", padx=20, pady=10)
        
        self.results_text = tk.Text(self.results_frame, height=5, state="disabled")
        self.results_text.pack(fill="both", expand=True)

    def start_camera(self):
        # Code to start camera goes here
        messagebox.showinfo("Camera", "Starting the camera.")
        self.log_results("Camera started.")

    def stop_camera(self):
        # Code to stop camera goes here
        messagebox.showinfo("Camera", "Stopping the camera.")
        self.log_results("Camera stopped.")

    def start_detection(self):
        # Code to start detection process goes here
        sensitivity = self.sensitivity_slider.get()
        messagebox.showinfo("Detection", f"Starting crack detection with sensitivity: {sensitivity}.")
        self.log_results("Detection started with sensitivity level: " + str(sensitivity))

    def stop_detection(self):
        # Code to stop detection process goes here
        messagebox.showinfo("Detection", "Stopping crack detection.")
        self.log_results("Detection stopped.")

    def log_results(self, message):
        # Log messages to results window
        self.results_text.config(state="normal")
        self.results_text.insert("end", message + "\n")
        self.results_text.config(state="disabled")
        self.results_text.see("end")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CrackDetectionApp(root)
    root.mainloop()
