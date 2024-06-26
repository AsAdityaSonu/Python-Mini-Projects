import pywhatkit
import time

phone_number = '+917814226245'
message = 'Hello'
time_interval = 60  

# Get the current time
current_time = time.localtime()
hours = current_time.tm_hour
minutes = current_time.tm_min

for i in range(5):  
    minutes += time_interval // 60
    if minutes >= 60:
        minutes -= 60
        hours += 1
    if hours >= 24:
        hours = 0

    pywhatkit.sendwhatmsg(phone_number, message, hours, minutes)
    time.sleep(time_interval)