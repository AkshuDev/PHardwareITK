def setup_dir_tree(_file_manager:object, _cd_:str, _user:str) -> tuple[str, str, str]:
    _file_manager.reload()  # Reload the file manager to ensure it has the latest state

    if not _file_manager.dir_exists(_file_manager.join_path(_cd_.encode("utf-8"), b"usrs")):
        _file_manager.mk_dir(_file_manager.join_path(_cd_.encode("utf-8"), b"usrs"))  # Create the usrs directory if it doesn't exist

    dirs = _file_manager.list_dir(_file_manager.join_path(_cd_.encode("utf-8"), b"usrs").decode('utf-8'))  # List the files in the usrs directory
    new_user = False

    if len(dirs) == 1:
        print("No users found, creating default user...")
        new_user = True
        _file_manager.mk_dir(_file_manager.join_path(_cd_.encode("utf-8"), b"usrs", _user.encode("utf-8")))
    else:
        if _user not in dirs:
            _user = dirs[0]  # If no user is specified, use the first user found
            index = 1
            while not _user == "__dir_marker__":
                if index == len(dirs):
                    print("No users found, creating default user...")
                    _file_manager.mk_dir(_file_manager.join_path(_cd_.encode("utf-8"), b"usrs", _user.encode("utf-8")))
                    _user = "admin"
                    break
                _user = dirs[index]
                index += 1

        # Check if the user directory exists
        if not _file_manager.dir_exists(_file_manager.join_path(_cd_.encode("utf-8"), b"usrs", _user.encode("utf-8"))):
            print(f"User '{_user}' exists but the directory doesn't, creating user directory...")
            _file_manager.mk_dir(_file_manager.join_path(_cd_.encode("utf-8"), b"usrs", _user.encode("utf-8")))
            new_user = True

    # Create folders documents, downloads, and desktop for the user
    if new_user:
        _file_manager.mk_dir(_file_manager.join_path(_cd_.encode("utf-8"), b"usrs", _user.encode("utf-8"), b"documents"))
        _file_manager.mk_dir(_file_manager.join_path(_cd_.encode("utf-8"), b"usrs", _user.encode("utf-8"), b"downloads"))
        _file_manager.mk_dir(_file_manager.join_path(_cd_.encode("utf-8"), b"usrs", _user.encode("utf-8"), b"desktop"))

    _cd_ = _file_manager.join_path(_cd_.encode("utf-8"), b"usrs", _user.encode("utf-8")).decode("utf-8")
    _cd_backup = _file_manager.join_path(b"home", b"usrs").decode("utf-8")

    return (_cd_, _user, _cd_backup)