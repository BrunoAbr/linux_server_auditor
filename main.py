from auditor.system import get_system_info
from auditor.processes import (
    get_top_cpu_processes,
    get_top_memory_processes
)
from auditor.users import (
    get_users,
    get_login_users,
    get_root_users,
    get_admin_users,
    get_system_users,
    get_regular_users
)

def auditor_summary():
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
    
def cpu_processes_summary():
    
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

def users_summary():

    regular_users = get_regular_users()
    system_users = get_system_users()
    root_users = get_root_users()
    admin_users = get_admin_users()

    print("=" * 60)
    print("                 USER AUDIT")
    print("=" * 60)

    print("\nREGULAR USERs")
    print("-" * 60)

    for user in regular_users:
        print(
            f"USER: {user['username']:<20}"
            f"UID {user['uid']:<8}"
            f"SHELL: {user['shell']}"
        )

    print("\nSYSTEM SUSERS")
    print("-" * 60)

    for user in system_users:
        print(
            f"USER: {user['username']:<20}"
            f"UID {user['uid']}"
        )

    print("=" * 60)

    print("\nROOT USERS")
    print("-" * 60)

    for user in root_users:
        print(
            f"USER: {user['username']:<20}"
            f"UID: {user['uid']}"
        )

    print("\nADMIN USERS")
    print("-" * 60)

    for user in admin_users:
        print(
            f"USER: {user['username']:<20}"
            f"GROUPS: {', '.join(user['groups'])}"
        )

    print("=" * 60)

def main():
    auditor_summary()
    cpu_processes_summary()
    users_summary()


if __name__ == "__main__":
    main()
    
