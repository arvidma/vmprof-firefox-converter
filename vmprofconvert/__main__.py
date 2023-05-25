import sys
import json
import os
import webbrowser
import urllib.parse
from vmprofconvert import convert_stats
from symbolserver import start_server 

path = sys.argv[1]
abs_path = os.path.abspath(path)

url = "https://profiler.firefox.com/from-url/http%3A%2F%2F127.0.0.1%3A5000%2Fprofile"
url += "/?symbolServer=http%3A%2F%2F127.0.0.1%3A5000%2F"

if len(sys.argv) > 2 and sys.argv[2] is not None:
    jitlogpath = sys.argv[2]
else:
    jitlogpath = ""

with open(path + ".json", "w") as output_file:
    output_file.write(json.dumps(json.loads(convert_stats(path)), indent=2))
    webbrowser.open(url, new=0, autoraise=True)
    start_server(abs_path + ".json", jitlogpath)