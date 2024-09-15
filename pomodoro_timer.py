import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import time
import pystray
from pystray import MenuItem as item

# Pomodoro Timer class
class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Aesthetic Pomodoro Timer")
        self.root.geometry("300x500")

        # Time variables
        self.work_time = 25 * 60  # 25 minutes
        self.break_time = 5 * 60  # 5 minutes
        self.current_time = self.work_time
        self.is_running = False
        self.is_break = False

        # Define themes with stylish color combinations
        self.themes = {
            "Sunny Day": {"bg": "#fffae6", "fg": "#ff6b6b", "button_bg": "#f0a500", "button_fg": "#ffffff", "font": "Lobster"},
            "Ocean Breeze": {"bg": "#d1f2eb", "fg": "#1a535c", "button_bg": "#4ecdc4", "button_fg": "#ffffff", "font": "Pacifico"},
            "Lavender Bliss": {"bg": "#e6e6fa", "fg": "#6a0572", "button_bg": "#93329e", "button_fg": "#ffffff", "font": "Montserrat"},
            "Midnight Blue": {"bg": "#1a1a2e", "fg": "#e94560", "button_bg": "#16213e", "button_fg": "#ffffff", "font": "Lobster"},
            "Minty Fresh": {"bg": "#dff9fb", "fg": "#38ada9", "button_bg": "#78e08f", "button_fg": "#ffffff", "font": "Pacifico"},
            "Rosewood": {"bg": "#ffe4e1", "fg": "#ff6b81", "button_bg": "#ff4757", "button_fg": "#ffffff", "font": "Lobster"},
            "Emerald": {"bg": "#d1f2a5", "fg": "#2ecc71", "button_bg": "#27ae60", "button_fg": "#ffffff", "font": "Pacifico"},
            "Desert Sunset": {"bg": "#fad0c4", "fg": "#ff6b81", "button_bg": "#e17055", "button_fg": "#ffffff", "font": "Lobster"},
            "Royal Blue": {"bg": "#ebf5fb", "fg": "#2980b9", "button_bg": "#3498db", "button_fg": "#ffffff", "font": "Montserrat"},
            "Tropical Paradise": {"bg": "#ff9ff3", "fg": "#f368e0", "button_bg": "#833471", "button_fg": "#ffffff", "font": "Lobster"},
            "Dark Forest": {"bg": "#2f3640", "fg": "#44bd32", "button_bg": "#4cd137", "button_fg": "#ffffff", "font": "Pacifico"},
            "Neon Night": {"bg": "#1B1464", "fg": "#c8d6e5", "button_bg": "#00d2d3", "button_fg": "#ffffff", "font": "Montserrat"},
            "Cotton Candy": {"bg": "#ffcccc", "fg": "#ff6b81", "button_bg": "#ff9ff3", "button_fg": "#ffffff", "font": "Pacifico"},
            "Autumn Blaze": {"bg": "#ffbe76", "fg": "#d35400", "button_bg": "#e74c3c", "button_fg": "#ffffff", "font": "Montserrat"},
            "Frozen Lake": {"bg": "#dff9fb", "fg": "#2d98da", "button_bg": "#1e3799", "button_fg": "#ffffff", "font": "Pacifico"}
        }

        # Default theme
        self.current_theme = "Sunny Day"

        # Create the UI first
        self.create_ui()

        # Apply the default theme after the UI is created
        self.apply_theme(self.themes[self.current_theme])

        # Create the tray icon
        self.icon_image = Image.open("icon.png")  # Ensure you have an icon.png
        self.icon = pystray.Icon("Pomodoro Timer", self.icon_image, menu=pystray.Menu(
            item('Show', self.show_window),
            item('Exit', self.exit_app)
        ))

    def create_ui(self):
        # Aesthetic label
        self.label = tk.Label(self.root, text="Pomodoro Timer", font=("Helvetica", 18, "bold"))
        self.label.pack(pady=20)

        # Timer display
        self.time_label = tk.Label(self.root, text=self.format_time(self.current_time), font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        # Control buttons
        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer, width=10, font=("Helvetica", 12))
        self.start_button.pack(pady=10)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_timer, width=10, font=("Helvetica", 12))
        self.reset_button.pack(pady=10)

        # Theme dropdown
        self.theme_label = tk.Label(self.root, text="Choose Theme", font=("Helvetica", 12))
        self.theme_label.pack(pady=10)

        self.theme_combo = ttk.Combobox(self.root, values=list(self.themes.keys()), state="readonly", font=("Helvetica", 10))
        self.theme_combo.set(self.current_theme)
        self.theme_combo.pack(pady=5)
        self.theme_combo.bind("<<ComboboxSelected>>", self.change_theme)

    def apply_theme(self, theme):
        """Apply a given theme to the UI elements."""
        self.root.configure(bg=theme["bg"])
        self.label.configure(bg=theme["bg"], fg=theme["fg"], font=(theme["font"], 18, "bold"))
        self.time_label.configure(bg=theme["bg"], fg=theme["fg"], font=(theme["font"], 48))
        self.start_button.configure(bg=theme["button_bg"], fg=theme["button_fg"], font=(theme["font"], 12))
        self.reset_button.configure(bg=theme["button_bg"], fg=theme["button_fg"], font=(theme["font"], 12))
        self.theme_label.configure(bg=theme["bg"], fg=theme["fg"], font=(theme["font"], 12))

    def change_theme(self, event):
        """Handle theme change event."""
        selected_theme = self.theme_combo.get()
        self.current_theme = selected_theme
        self.apply_theme(self.themes[selected_theme])

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.update_timer()

    def reset_timer(self):
        self.is_running = False
        self.current_time = self.work_time if not self.is_break else self.break_time
        self.time_label.config(text=self.format_time(self.current_time))

    def update_timer(self):
        if self.is_running:
            if self.current_time > 0:
                self.current_time -= 1
                self.time_label.config(text=self.format_time(self.current_time))
                self.root.after(1000, self.update_timer)
            else:
                if not self.is_break:
                    self.current_time = self.break_time
                    self.is_break = True
                    messagebox.showinfo("Break Time!", "Take a 5-minute break!")
                else:
                    self.current_time = self.work_time
                    self.is_break = False
                    messagebox.showinfo("Back to Work!", "Time to get back to work!")
                self.reset_timer()

    def format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        return f"{mins:02}:{secs:02}"

    def hide_window(self):
        self.root.withdraw()

    def show_window(self, icon, item):
        self.root.deiconify()

    def exit_app(self, icon, item):
        self.is_running = False
        self.icon.stop()
        self.root.quit()

    def on_closing(self):
        self.hide_window()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
