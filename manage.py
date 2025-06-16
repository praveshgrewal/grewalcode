#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grewalcode.settings')  # ✅ Make sure this is correct

    try:
        from django.core.management import execute_from_command_line

        # 🟡 First, run the command (e.g., migrate)
        execute_from_command_line(sys.argv)

        # ✅ After migrate, try to create superuser
        if 'migrate' in sys.argv:
            import django
            django.setup()

            from django.contrib.auth import get_user_model
            User = get_user_model()

            username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
            email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
            password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

            if username and password and not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username=username, email=email, password=password)
                print("✅ Superuser created.")
            else:
                print("ℹ️ Superuser already exists or environment variables not set.")

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django."
        ) from exc

if __name__ == '__main__':
    main()
