#!/usr/bin/env python
import os
import sys
import subprocess
import threading

def run_entrypoint():
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'migration.sh')
    print(f"Running migration script at: {script_path}")
    subprocess.call(script_path)

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
