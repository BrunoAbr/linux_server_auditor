from auditor.system import get_system_info

def main():
    system_info = get_system_info()

    print("=" * 40)
    print("       LINUX SERVER AUDITOR")
    print("=" * 40)

    print(f"Hostname:          {system_info['hostname']}")
    print(f" OS:               {system_info['os']}")
    print(f"OS Version:        {system_info['os_version']}")
    print(f"Kernel:            {system_info['kernel']}")
    print(f"CPU Usage:         {system_info['cpu_usage']}%")
    print(f"Memory Usage:      {system_info['memory_usage']}%")
    print(f"Disk Usage:        {system_info['disk_usage']}%")
    print(f"Uptime:            {system_info['uptime']}")

    print("=" * 40)

if __name__ == "__main__":
    main()
    