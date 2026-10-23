import os
import sys

# Windows UTF-8 reconfigure
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from django.core.management import call_command


def seed_all():
    call_command("seed_lessons")


if __name__ == "__main__":
    seed_all()
