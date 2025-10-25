import json

def setup_dir_tree(_file_manager:object, _cd_:str, _user:str) -> tuple[str, str]:
    _file_manager.reload()

    usrs = _file_manager.join_path(b"home", b"usrs")
    user = _file_manager.join_path(usrs, _user.encode("utf-8"))
    user_config = user + b"_config.aos"

    aosdusr = _file_manager.join_path(b"home", b"aosdusr.aos")

    out = _file_manager.get_file(aosdusr)

    if out is not None:
        # User found
        _user = json.loads(out.decode("utf-8"))["user"]
        _user = _user.replace("_config.aos", "")
        _cd_ = _user
        _user = _user.split("\\")
        _user = _user[len(_user) - 1]
        return (_cd_, _user)

    utemp = input("Sorry this OS user data seems to not be present, please specify the user you want to log into\n: ")

    user = _file_manager.join_path(b"home", b"usrs", utemp.encode("utf-8"))

    user_config = user + b"_config.aos"

    out = _file_manager.get_file(user_config)

    if out is not None:
        # User found
        return (user, user)
    else:
        print("No Such user found! Creating user", _user)
        # Create user admin
        user = _file_manager.join_path(usrs, _user.encode("utf-8"))
        user_config = user + b"_config.aos"
        user_config_data = {
        "name": _user,
        "default": True,
        "password": None
        }

        aosdusr_data = {
            "user": user_config.decode("utf-8")
        }

        out = _file_manager.write_file(user_config, json.dumps(user_config_data).encode("utf-16"), [0x0, 0x5, 0x6, [None]])

        if not out == 0:
            print("Error,", out)
            return None

        out = _file_manager.write_file(aosdusr, json.dumps(aosdusr_data).encode("utf-8"), [0x0, 0x5, 0x6, [None]])

        if not out == 0:
            print("Error,", out)
            return None

        out = _file_manager.mk_dir(user)

        if not out == 0:
            print("Error,", out)
            return None

        out = _file_manager.mk_dir(_file_manager.join_path(user, b"Downloads"))

        if not out == 0:
            print("Error,", out)
            return None

        out = _file_manager.mk_dir(_file_manager.join_path(user, b"Desktop"))

        if not out == 0:
            print("Error,", out)
            return None

        out = _file_manager.mk_dir(_file_manager.join_path(user, b"Documents"))

        if not out == 0:
            print("Error,", out)
            return None

        print("Done!")
        return user.decode("utf-8"), _user
