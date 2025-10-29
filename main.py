import psutil
from datetime import datetime
import csv
import os

def get_system_info():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cpu = psutil.cpu_percent(interval=1) 
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent 
    
    return [now, cpu, memory, disk]

def write_log(data):
    filename = "log.csv"
    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="") as f:
        writer = csv.writer(f)
        if (not file_exists) or os.stat(filename).st_size == 0:
            writer.writerow(["Timestamp", "CPU", "Memory", "Disk"])
        writer.writerow(data)
        
if __name__ == "__main__":
    row = get_system_info()
    write_log(row)
    print("Logged:", row)