import psutil
import time
import datetime

def get_system_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    network = psutil.net_io_counters().bytes_sent
    time_now = time.strftime("%H:%M:%S", time.localtime())
    
    syslogstore = []
    start_time = datetime.datetime.now()
    with open('/var/log/syslog', 'r') as syslog:
        lines = syslog.readlines()
        for line in lines:
            # Extract the timestamp from the log
            log_time_str = ' '.join(line.split(' ')[0:4])
            log_time = datetime.datetime.strptime(log_time_str, '%b %d %H:%M:%S')
            log_time = log_time.replace(year=start_time.year)  # Add the current year to the log time
            
            # If the log time is within the last second, add it to the list
            if (start_time - log_time).total_seconds() <= 1:
                syslogstore.append(line.strip())
    
    return cpu, memory, disk, network, time_now, syslogstore   

while True:
    cpu, memory, disk, network, time_now, syslogstore = get_system_metrics()
    print(cpu, memory, disk, network, time_now, syslogstore)
