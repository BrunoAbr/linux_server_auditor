import psutil

def get_processes():
    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "username", "cpu_percent", "memory_percent"]
    ):
        try:
            cpu_percent = process.cpu_percent(interval=0.1)

            processes.append({
                "pid": process.info["pid"],
                "name": process.info["name"],
                "username": process.info["username"],
                "cpu_percent": cpu_percent,
                "memory_percent": process.info["memory_percent"]
            })
        except (psutil.NoSuchProcess, psutil.AcessDenied):
            continue

    return processes

def get_top_cpu_processes(limit=10):
    processes = get_processes()

    processes.sort(
        key=lambda process: process["cpu_percent"] or 0,
        reverse=True
    )

    return processes[:limit]

def get_top_memory_processes(limit=10):
    processes = get_processes()

    processes.sort(
        key=lambda process: process["memory_percent"] or 0,
        reverse=True
    )

    return processes[:limit]