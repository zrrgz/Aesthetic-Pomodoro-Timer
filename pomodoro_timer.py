import tkinter as tk
from tkinter import ttk
import time
from PIL import Image, ImageTk
import pystray
from pystray import MenuItem as item
import threading

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")

        # Position the window in the bottom right corner
        self.position_window_bottom_right()

        self.is_running = False
        self.is_paused = False
        self.time_remaining = 0
        self.work_time = 25 * 60  # 25 minutes
        self.break_time = 5 * 60  # 5 minutes

        # Create a label for displaying the timer
        self.timer_label = tk.Label(root, text="25:00", font=("Helvetica", 48), bg="white", fg="black")
        self.timer_label.pack(pady=20)

        # Start, Pause/Resume and Reset Buttons
        self.start_button = tk.Button(root, text="Start", command=self.start_timer, bg="green", fg="white", font=("Arial", 14))
        self.start_button.pack(side="left", padx=10, pady=10)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_resume_timer, bg="orange", fg="white", font=("Arial", 14))
        self.pause_button.pack(side="left", padx=10, pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer, bg="red", fg="white", font=("Arial", 14))
        self.reset_button.pack(side="left", padx=10, pady=10)

        self.update_timer()

    def position_window_bottom_right(self):
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the position for the bottom right corner
        window_width = 400  # Adjust according to your window size
        window_height = 200  # Adjust according to your window size
        x = screen_width - window_width
        y = screen_height - window_height

        # Set the geometry of the window (width x height + x + y)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.time_remaining = self.work_time
            self.update_timer()

    def pause_resume_timer(self):
        if self.is_running:
            if not self.is_paused:
                self.is_paused = True
                self.pause_button.config(text="Resume")
            else:
                self.is_paused = False
                self.pause_button.config(text="Pause")
                self.update_timer()

    def reset_timer(self):
        self.is_running = False
        self.is_paused = False
        self.pause_button.config(text="Pause")
        self.timer_label.config(text="25:00")
        self.time_remaining = self.work_time

    def update_timer(self):
        if self.is_running and not self.is_paused:
            minutes = self.time_remaining // 60
            seconds = self.time_remaining % 60
            self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
            if self.time_remaining > 0:
                self.time_remaining -= 1
                self.root.after(1000, self.update_timer)
            else:
                # Switch to break time
                if self.time_remaining == 0 and self.is_running:
                    self.time_remaining = self.break_time
                    self.timer_label.config(text="Break Time!")
                    self.is_running = False  # Stop timer until reset
        elif not self.is_running:
            self.root.after(1000, self.update_timer)

    def on_quit(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
