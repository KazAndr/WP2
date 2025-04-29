import os
import json
import time
import pickle
import subprocess
import numpy as np

# Function to run a command
def run_command(command, wait=True):
    """
    Executes a command in the shell.
    If wait=True, waits for the command to complete.
    """
    if wait:
        subprocess.run(command, shell=True)
    else:
        subprocess.Popen(command, shell=True)

    return None

# Function to create a buffer
def create_buffer(image_path, buffer_size, num_blocks, key):
    """
    Creates a buffer with the specified parameters.
    """
    command = f'singularity exec {image_path} dada_db -b {buffer_size} -n {num_blocks} -k {key} > /dev/null 2>&1'
    run_command(command, wait=False)

    return None

def kill_dada_dbdedispdb(key_input, key_output):
    command_pattern = f"dada_dbdedispdb.*--key_input {key_input}.*--key_output {key_output}"
    kill_by_pattern(command_pattern)

            
def kill_dada_fildb(key_output):
    command_pattern = f"dada_fildb.*--key_output {key_output}"
    kill_by_pattern(command_pattern)


def kill_by_pattern(pattern):
    ps = subprocess.Popen(["ps", "-aef"], stdout=subprocess.PIPE)
    grep = subprocess.Popen(["grep", "-E", pattern], stdin=ps.stdout, stdout=subprocess.PIPE)
    ps.stdout.close()
    output, _ = grep.communicate()

    for line in output.decode().splitlines():
        if "grep" not in line:
            pid = int(line.split()[1])
            subprocess.run(["kill", "-9", str(pid)])
            print(f"Successfully killed process with PID {pid}.")
       

# Function to kill a buffer
def kill_buffer(image_path, key):
    """
    Terminates a buffer with the specified key.
    """
    command = f'singularity exec {image_path} dada_db -d -k {key} > /dev/null 2>&1'
    run_command(command, wait=False)

    return None

def load_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config

def load_time_keeper(filename):
    with open(filename, 'rb') as dump_file:
        time_keeper = pickle.load(dump_file)
        
    time.sleep(0.5)  # Pause for some time after loading
    return time_keeper

def save_time_keeper(filename, time_keeper):
    with open(filename, 'wb') as dump_file:
        pickle.dump(time_keeper, dump_file)
    
    time.sleep(0.5)  # Pause for some time after saving
    return None


def normalize_image_to_255(data):
    normalized_data = (data - np.min(data)) / (np.max(data) - np.min(data))
    scaled_data = (normalized_data * 255).astype(np.uint8)
    return scaled_data


def convert_to_milliseconds(data):
    converted_data = {}
    for key, value in data.items():
        if isinstance(value, (int, float)):
            # Convert single float/int values
            converted_data[key] = value * 1000
        elif isinstance(value, list) and all(isinstance(item, tuple) for item in value):
            # Convert lists of tuples
            converted_data[key] = [(item[0] * 1000, item[1] * 1000, item[2] * 1000) for item in value]
        else:
            # Keep the value as is if it does not match the expected types
            converted_data[key] = value
    return converted_data