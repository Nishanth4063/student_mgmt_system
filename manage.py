#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    outer_student_mgmt = os.path.join(base_dir, 'student_mgmt')

    # Add outer_student_mgmt to sys.path so 'student_mgmt.settings' resolves
    if outer_student_mgmt not in sys.path:
        sys.path.insert(0, outer_student_mgmt)
    if base_dir not in sys.path:
        sys.path.insert(0, base_dir)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'student_mgmt.settings'
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()