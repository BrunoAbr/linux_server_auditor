from pathlib import Path

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
