import subprocess
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ['fastapi', 'flask', 'django']:
        framework = sys.argv[1]

        match framework:
            case 'fastapi':
                command = f"uvicorn example-{framework}.app:app --reload --port 8000"
            case 'flask':
                command = f"python -m example-{framework}.app"
            case 'django':
                command = f"python example-{framework}/manage.py runserver 0.0.0.0:8000"

        subprocess.run(command, shell=True, check=True)
    else:
        print("Usage: python manage.py [fastapi|flask|django]")
