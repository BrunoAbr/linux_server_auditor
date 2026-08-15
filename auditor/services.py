import subprocess

def get_active_services():
    result = subprocess.run(
        [
            "systemctl",
            "list-units",
            "--type=service",
            "--state=active",
            "--no-pager",
            "--no-legend"
        ],
        capture_output=True,
        text=True,
        check=True
    )
    services = []

    for line in result.stdout.splitlines():
        fields = line.split()

        if not fields:
            continue
        
        service = fields[0]

        services.append(service)

    return services

def get_failed_services():
    result = subprocess.run(
        [
            "systemctl",
            "list-units",
            "--type=service",
            "--state=failed",
            "--no-pager",
            "--no-legend"
        ],
        capture_output=True,
        text=True,
        check=True
    )

    service = []

    for line in result.stdout.splitlines():
        fields = line.split()

        if not fields:
            continue
        
        service = fields[0]

        services.append(service)

    return

def get_enabled_services():
    result = subprocess.run(
        [
            "systemctl",
            "list-unit-files",
            "--type=service",
            "--state=enabled",
            "--no-pager",
            "--no-legend"
        ],
        capture_output=True,
        text=True,
        check=True
    )

    services = []

    for line in result.stdout.splitlines():
        fields = line.split()

        if not fields:
            continue
        
        service.append(fields[0])
    
    return services


def check_failed_services(failed_services):

    if not failed_services:
        return {
            "status": "OK",
            "message": "No failed services detected",
        }

    return {
        "status": "WARNING",
        "message": f"{len(failed_services)} failed service(s) detected",
        "services": failed_services,
    }