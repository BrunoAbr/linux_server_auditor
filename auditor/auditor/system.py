import platform
import socket
import psutil
import time

def get_system_info():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_version": platform.version(),
        "kernel": platform.release(),
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": memory.percent,
        "disk_usage": disk.percent,
        "uptime": get_uptime()
    }

def get_uptime():
    boot_time = psutil.boot_time()
    current_time = time.time()

    uptime_seconds = current_time - boot_time

    days = int(uptime_seconds // 86400)
    hours = int((uptime_seconds % 86400) // 3600)
    minutes = int((uptime_seconds % 3600) // 60)

    return f"{days}d {hours}h {minutes}m"