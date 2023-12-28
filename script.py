from dotenv import load_dotenv
import subprocess
import os

# Load variables from .env file
load_dotenv()

def run_shell_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except subprocess.CalledProcessError as e:
        print("Error executing the command:", e)
        print("Command output (stderr):", e.stderr)
    return result.stdout

def login_vast():
    key = os.getenv('VAST_KEY')
    return run_shell_cmd(f'vastai set api-key {key}')

print(login_vast())