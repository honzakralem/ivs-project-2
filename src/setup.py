#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""!
@file setup.py
@brief Python script to download dependencies, runs only when make command is ran from "ivs-project-2/makefile"
@author Ha Pham <xphamha00>
@date 6.4.2026
"""

import os
import subprocess
import platform

venv_dir_name = "env"
os_name = platform.system()
requirements_absolute_path = os.path.abspath("src/requirements.txt")

print("Starting setup script")

if os_name == "Linux":
    
    # Ubuntu dependencies
    with open("src/ubuntu_dependencies.txt", "r") as f:
        install_line = f.readline().split()
    subprocess.run(install_line)

    # If venv does not exist
    if not os.path.isdir(f"{venv_dir_name}"):
        subprocess.run(["python3", "-m", "venv", f"{venv_dir_name}"])
    subprocess.run([f"{venv_dir_name}/bin/pip", "install", "-r", f"{requirements_absolute_path}"])

elif os_name == "Darwin":
    if not os.path.isdir(f"{venv_dir_name}"):
        subprocess.run(["python3", "-m", "venv", f"{venv_dir_name}"])
    subprocess.run([f"{venv_dir_name}/bin/pip", "install", "-r", f"{requirements_absolute_path}"])
else:
    # If venv does not exist
    if not os.path.isdir(f"{venv_dir_name}"):
        subprocess.run(["python", "-m", "venv", f"{venv_dir_name}"])
    subprocess.run([f"{venv_dir_name}\\Scripts\\pip", "install", "-r", f"{requirements_absolute_path}"])

print("Setup successful!")