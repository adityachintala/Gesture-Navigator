import subprocess
import json

f = open("userDefinedControls.json", "r")
data = json.load(f)

subprocess.run([
            "explorer.exe",
            "microsoft.windows.photos:"
        ])