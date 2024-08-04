import tinytuya
import time
import pywhatkit
from datetime import datetime, timedelta

# Connect to Device
s = tinytuya.OutletDevice(
    dev_id='', # check your device details by scan() in tinytuya
    address='',
    local_key='', 
    version=3.4
)

# WhatsApp configuration
phone_number = '' #reciver number
waiting_time_to_send = 18  # Time in seconds before sending the message
close_tab = True
waiting_time_to_close = 30  # Time in seconds before closing the browser tab

# Get initial status
last_status = s.status()['dps']['1']
print("TUYA SMART DEVICE STATUS ALERT RUNNING")
while True:
    # Get current status
    current_status = s.status()['dps']['1']
    
    # Check if the status has changed
    if current_status != last_status:
        if current_status:
            message = "State changed: ON"
        else:
            message = "State changed: OFF"
        
        # Calculate the send time
        send_time = datetime.now() + timedelta(minutes=2)
        time_hour = send_time.hour
        time_minute = send_time.minute

        # Send WhatsApp message
        pywhatkit.sendwhatmsg(phone_number, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
        
        # Update the last status
        last_status = current_status
    
    # Wait for a short period before checking again
    time.sleep(1)
