class LockFile:
    def __init__(self):
        self.lockfile_path = os.path.expanduser("~/.config/robo/db.lck")
                                                                             
    def is_locked(self):
        return os.path.exists(self.lockfile_path)

    def lock(self):
        if self.is_locked():
            print("Lock file already exists.")
        else:
            try:
                with open(self.lockfile_path, 'w') as lockfile:
                    lockfile.write("Locked")
                print("Lock file created successfully.")
            except Exception as e:
                print(f"Error creating lock file: {e}")

    def release(self):
        if self.is_locked():
            try:
                os.remove(self.lockfile_path)
                print("Lock file removed successfully.")
            except Exception as e:
                print(f"Error removing lock file: {e}")
        else:
            print("No lock file exists to release.")
