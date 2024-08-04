# Device Status Monitor

This script monitors the status of a Tuya smart device and sends a WhatsApp message when the status changes.

## Features

- Connects to a Tuya smart device
- Monitors the device status continuously
- Sends a WhatsApp message when the device status changes
- Uses `pywhatkit` for WhatsApp messaging

## Requirements

- Python 3.x
- `tinytuya`
- `pywhatkit`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/device-status-monitor.git
    cd device-status-monitor
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Update the script with your Tuya device credentials and WhatsApp configuration.
2. Run the script:
    ```bash
    python monitor_device.py
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
