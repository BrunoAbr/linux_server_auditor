from auditor.system import get_system_info
from auditor.processes import (
    get_top_cpu_processes,
    get_top_memory_processes
)

def main():
    system_info = get_system_info()

    print("=" * 40)
    print("       LINUX SERVER AUDITOR")
    print("=" * 40)

    print(f"Hostname:          {system_info['hostname']}")
    print(f"OS:                {system_info['os']}")
    print(f"OS Version:        {system_info['os_version']}")
    print(f"Kernel:            {system_info['kernel']}")
    print(f"CPU Usage:         {system_info['cpu_usage']}%")
    print(f"Memory Usage:      {system_info['memory_usage']}%")
    print(f"Disk Usage:        {system_info['disk_usage']}%")
    print(f"Uptime:            {system_info['uptime']}")

    print("=" * 40)

    memory_processes = get_top_cpu_processes()
    cpu_processes = get_top_memory_processes()

    print("=" * 70)
    print("                 PROCESS AUDIT")
    print("=" * 70)

    print("\nTOP CPU PROCESSES")
    print("-" * 70)


    for process in cpu_processes:
        print(
            f"PID: {process['pid']:<8}"
            f"NAME: {process['name']:<25}"
            f"CPU: {process['cpu_percent']:>6.1f}%"
        )

    print("\nTOP MEMORY PROCESSES")
    print("=" * 70)

    for process in memory_processes:
        print(
            f"PID: {process['pid']:<8}"
            f"NAME: {process['name']:<25}"
            f"RAM: {process['memory_percent']:>6.1f}%"
        )

    print("=" * 70)

if __name__ == "__main__":
    main()
    
