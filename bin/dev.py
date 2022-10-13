#!./.venv/bin/python3

from port import load_port
import subprocess

subprocess.run(
    f"poetry run uvicorn main:app --reload --port {load_port()}", shell=True)
