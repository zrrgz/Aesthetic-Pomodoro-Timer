# Aesthetic Pomodoro Timer

An aesthetically pleasing Pomodoro Timer built with Python and Tkinter, featuring customizable themes and fonts. This app helps you improve productivity by following the Pomodoro technique.

## Features

- Customizable work and break times
- 15 different beautiful themes
- Intuitive, user-friendly interface
- Runs in the background (tray icon)
- Standalone executable for easy distribution

### Prerequisites

- Python
- `tkinter`, `pystray`, `Pillow`

### Run the Application (Python)

1. Clone the repository:
   ```bash
   git clone https://github.com/zrrgz/Aesthetic-Pomodoro-Timer.git
2. Navigate to the project directory:
   ```bash
   cd Aesthetic-Pomodoro-Timer
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the application:
   ```bash
   python pomodoro_timer.py

### Build a Standalone Executable
To build a standalone executable (without needing Python installed), use PyInstaller:
```bash
pyinstaller --noconsole --onefile pomodoro_timer.py
You can find the executable in the dist folder.

### Usage
Start the timer for 25 minutes of focused work.
Take a 5-minute break when prompted.
Enjoy different themes by selecting from the dropdown menu!
### Contributing
We welcome contributions! Here's how you can help:

Fork the repository
Create a new branch (git checkout -b feature/my-feature)
Commit your changes (git commit -m 'Add some feature')
Push to the branch (git push origin feature/my-feature)
Create a new Pull Request
### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
PyInstaller
Tkinter

