from pathlib import Path
import grp

def get_users():
    users = []

    passwd_file = Path("/etc/passwd")

    with passwd_file.open("r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            fields = line.split(":")

            username= fields[0]
            uid = int(fields[2])
            gid = int(fields[3])
            home = fields[5]
            shell = fields[6]

            users.append({
                "username": username,
                "uid": uid,
                "gid": gid,
                "home": home,
                "shell": shell
            })

        return users


def get_login_users():
    users = get_users()

    login_users = []

    disabled_shells = {
        "/usr/sbin/nologin",
        "/usr/bin/nologin",
        "/bin/false",
        "/usr/bin/false"
    }

    for user in users:
        if user["shell"] not in disabled_shells:
            login_users.append(users)

    return login_users

def get_root_users():
    users = get_users()

    return [
        user
        for user in users
        if user["uid"] == 0
    ]

def get_regular_users():
    users = get_users()

    return [
        user
        for user in users
        if user["uid"] >= 1000
    ]

def get_system_users():
    users = get_users()

    return [
        user
        for user in users
        if 0 < user["uid"] < 1000
    ]

def get_admin_users():
    users = get_regular_users()

    admin_users = []

    admin_groups = {
        "sudo",
        "wheel"
    }

    for user in users:
        groups = []

        for group in grp.getgrall():
            if user["username"] in group.gr_mem:
                groups.append(group.gr_name)

        if any(group in admin_groups for group in groups):
            user["groups"] = groups
            admin_users.append(user)

        return admin_users

def check_root_users():
    root_users = get_root_users()

    if len(root_users) == 1:
        return {
            "status": "OK",
            "message": "Only one user has UID 0"
        }
    return {
        "status": "CRITICAL",
        "message": f"{len(root_users)} users have UID 0"
    }

def check_system_users_shell():
    system_users = get_system_users()

    disabled_shells = {
        "/usr/sbin/nologin",
        "/usr/bin/nologin",
        "/bin/false",
        "/usr/bin/false",
    }

    users_with_shell = []

    for user in system_users:
        if user["shell"] not in disabled_shells:
            users_with_shell.append(user)

    if not users_with_shell:
        return {
            "status": "OK",
            "message": "System users have login disabled"
        }
    
    return {
        "status": "WARNING",
        "message": (
            f"{len(users_with_shell)} system users "
            "have an interactiveshell"
        ),
        "users": users_with_shell
    }

def check_admin_users():
    admin_users = get_admin_users()

    if not admin_users:
        return {
            "status": "WARNING",
            "message": "No administrative users detected"
        }

    return {
        "status": "INFO",
        "message": f"{len(admin_users)} administrative user(s) detected",
        "users": admin_users
    }
    
