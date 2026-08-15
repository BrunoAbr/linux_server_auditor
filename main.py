from auditor.system import get_system_info
from auditor.processes import (
    get_top_cpu_processes,
    get_top_memory_processes
)
from auditor.users import (
    get_regular_users,
    get_system_users,
    get_root_users,
    get_admin_users,
    check_root_users,
    check_system_users_shell,
    check_admin_users
)
from auditor.services import (
    get_active_services,
    get_failed_services,
    get_enabled_services,
    check_failed_services
)

from presentation.terminal import (
    print_system_summary,
    print_process_summary,
    print_users_summary,
    print_user_security_summary,
    print_services_summary,
    print_service_security_summary
)


def main():
    system_info = get_system_info()

    cpu_processes = get_top_cpu_processes()
    memory_processes = get_top_memory_processes()

    regular_users = get_regular_users()
    system_users = get_system_users()
    root_users = get_root_users()
    admin_users = get_admin_users()

    root_check = check_root_users()
    shell_check = check_system_users_shell()
    admin_check = check_admin_users()

    active_services = get_active_services()
    failed_services = get_failed_services()
    service_check = check_failed_services(failed_services)

    print_system_summary(system_info)

    print_process_summary(
        cpu_processes,
        memory_processes
    )

    print_users_summary(
        regular_users,
        system_users,
        root_users,
        admin_users
    )

    print_user_security_summary(
        root_check,
        shell_check,
        admin_check
    )

    print_services_summary(
        active_services,
        failed_services    
    )

    print_service_security_summary(service_check)


if __name__ == "__main__":
    main()