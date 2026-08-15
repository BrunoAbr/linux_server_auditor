def print_system_summary(system_info):
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

def print_process_summary(cpu_processes, memory_processes):
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
    print("-" * 70)

    for process in memory_processes:
        print(
            f"PID: {process['pid']:<8}"
            f"NAME: {process['name']:<25}"
            f"RAM: {process['memory_percent']:>6.1f}%"
        )

    print("=" * 70)


def print_users_summary(
    regular_users,
    system_users,
    root_users,
    admin_users,
):
    print("=" * 60)
    print("                 USER AUDIT")
    print("=" * 60)

    print("\nREGULAR USERS")
    print("-" * 60)

    for user in regular_users:
        print(
            f"USER: {user['username']:<20}"
            f"UID: {user['uid']:<8}"
            f"SHELL: {user['shell']}"
        )

    print("\nSYSTEM USERS")
    print("-" * 60)

    for user in system_users:
        print(
            f"USER: {user['username']:<20}"
            f"UID: {user['uid']}"
        )

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

def print_check(check):
    status = check["status"]
    message = check["message"]

    print(f"[{status}] {message}")


def print_user_security_summary(
    root_check,
    shell_check,
    admin_check,
):
    print("=" * 60)
    print("                  USER SECURITY")
    print("=" * 60)

    print_check(root_check)
    print_check(shell_check)
    print_check(admin_check)

    print("=" * 60)

def print_services_summary(active_services, failed_services):
    print("=" * 60)
    print("                  SERVICE AUDIT")
    print("=" * 60)

    print("\nACTIVE SERVICES")
    print("-" * 60)

    for service in active_services:
        print(service)

    print("\nFAILED SERVICES")
    print("-" * 60)

    if failed_services:
        for service in failed_services:
            print(f"[FAILED] {service}")
    else:
        print("[OK] No failed services detected")

    print("=" * 60)


def print_service_security_summary(service_check):
    print("=" * 60)
    print("                SERVICE SECURITY")
    print("=" * 60)

    status = service_check["status"]
    message = service_check["message"]

    print(f"[{status}] {message}")

    if "services" in service_check:
        for service in service_check["services"]:
            print(f"    - {service}")

    print("=" * 60)