from dotenv import load_dotenv
import subprocess
import json
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

def get_all_machines():
    verified_demand_machines = json.loads(run_shell_cmd(f'vastai search offers verified=true -d --raw'))
    unverified_demand_machines = json.loads(run_shell_cmd(f'vastai search offers verified=false -d --raw'))
    demand_machines = {**verified_demand_machines, **unverified_demand_machines}

    verified_bid_machines = json.loads(run_shell_cmd(f'vastai search offers verified=true -b --raw'))
    unverified_bid_machines = json.loads(run_shell_cmd(f'vastai search offers verified=false -b --raw'))
    bid_machines = {**verified_bid_machines, **unverified_bid_machines}

    all_machines = {**demand_machines, **bid_machines}

    return all_machines