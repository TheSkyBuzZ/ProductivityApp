import time, datetime
import psutil

#Ingresar el PID del proceso
pid = int(input("Enter process ID: "))

#warning, nose para que me sirve?
def warning ():
    cpu_usage = psutil.cpu_percent(interval=1)

    if cpu_usage > 50:
        print("Cpu usage is above 50%", cpu_usage)
    
    mem_usage = psutil.virtual_memory().percent

    if mem_usage > 50:
        print("Memory Usage is above 50%", mem_usage)

#monitorizar
def monitor ():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d - %H:%M:%S")

    try:
        p = psutil.Process(pid)
        cpu = p.cpu_percent(interval=1) / psutil.cpu_count()

        memory_mb = p.memory_full_info().rss / (1024*1024)
        memory = p.memory_percent()

        print(f"{timestamp} - PID: {pid} | CPU: {cpu}% | Memory: {memory_mb:.2f}MB ({memory:.2f}%)")

    except psutil.NoSuchProcess:
        print("Process not found. Check PID and try again.")

        return False
    return True

#Ciclo para llamar a las funciones en intervalos
while True:
    if not monitor():
        break 
    warning()
    time.sleep(1)