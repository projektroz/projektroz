#!/usr/bin/env python
import os
import subprocess
import sys
import threading


def run_entrypoint():
    subprocess.call("chmod +x migration.sh", shell=True)
    script_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "migration.sh"
    )
    print(f"Running migration script at: {script_path}")
    subprocess.call("dos2unix migration.sh", shell=True)
    if os.path.exists(script_path):
        print(f"Script {script_path} exists")
        if os.access(script_path, os.X_OK):
            print(f"Script {script_path} is executable")
            subprocess.call(script_path, shell=True)
        else:
            print(f"Script {script_path} is not executable")
    else:
        print(f"Script {script_path} does not exist")


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    if sys.argv[1] == "runserver":
        threading.Thread(target=run_entrypoint).start()
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
