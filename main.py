import os
import sys
import time
import requests
import signal
from win10toast import ToastNotifier
import subprocess

# Path to the PID file
PID_FILE = "internet_checker.pid"
toaster = ToastNotifier()

def is_connected():
    """Check internet connectivity."""
    try:
        requests.head("https://www.google.com", timeout=3)
        return True
    except requests.ConnectionError:
        return False

def send_notification(status):
    """Send a desktop notification."""
    message = "You are Online! 🟢" if status else "You are Offline! 🔴"
    toaster.show_toast("Internet Status", message, duration=5)

def start_daemon():
    """Start the script as a background process."""
    if os.path.exists(PID_FILE):
        print("Service is already running. Use 'stop' to stop it.")
        return

    # Launch the script as a subprocess
    process = subprocess.Popen([sys.executable, __file__, "run"], creationflags=subprocess.CREATE_NO_WINDOW)
    with open(PID_FILE, "w") as f:
        f.write(str(process.pid))
    print("Service started.")

def stop_daemon():
    """Stop the background process."""
    if not os.path.exists(PID_FILE):
        print("Service is not running.")
        return

    with open(PID_FILE, "r") as f:
        pid = int(f.read())

    # Terminate the process
    try:
        os.kill(pid, signal.SIGTERM)
        print("Service stopped.")
    except Exception as e:
        print(f"Error stopping service: {e}")
    finally:
        os.remove(PID_FILE)

def uninstall():
    """Uninstall the script."""
    stop_daemon()
    print("Uninstalling... Remove any additional files if necessary.")

def main_loop():
    """Main loop for checking internet connectivity."""
    last_status = None
    while True:
        current_status = is_connected()
        if current_status != last_status:
            send_notification(current_status)
            last_status = current_status
        time.sleep(2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py [start|stop|uninstall|run]")
        sys.exit()

    command = sys.argv[1].lower()
    if command == "start":
        start_daemon()
    elif command == "stop":
        stop_daemon()
    elif command == "uninstall":
        uninstall()
    elif command == "run":
        main_loop()
    else:
        print("Invalid command. Use 'start', 'stop', 'uninstall', or 'run'.")
