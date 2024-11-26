# Internet Connectivity Checker Service

This Python script monitors your internet connectivity and sends desktop notifications whenever the connection status changes (online or offline). It runs silently as a background service and can be managed via simple commands.

---

## Features

- Real-time monitoring of internet connectivity.
- Sends desktop notifications:
  - 🟢 **Online** notification.
  - 🔴 **Offline** notification.
- Runs as a lightweight, background service.
- Logs activity for debugging and tracking.
- Simple command-line interface for managing the service.

---

## Requirements

- **Python 3.7 or later**
- **Dependencies**:
  - `requests`
  - `win10toast`

---

## Installation

### Download the Script
Copy the script file (`main.py`) to your desired location.

### Install Required Packages  
Run the following command to install the required Python packages:

```bash
pip install requests win10toast
