import os
from subprocess import Popen, PIPE, STDOUT


def run_file_processor(process_file, text, number):
    """Make file executable and run bash file"""
    command = ["bash", process_file]
    try:
        process = Popen(command, stdout=PIPE, stderr=STDOUT)
        output = process.stdout.read()
        exitstatus = process.poll()
        if exitstatus == 0:
            result = {"status": "Success", "output": str(output)}
        else:
            result = {"status": "Failed", "output": str(output)}
    except Exception as e:
        result = {"status": "Failed", "output": str(e)}
    return result
