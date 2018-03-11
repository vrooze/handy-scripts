#!/usr/bin/env python3

try:
    # For Python 3.0 and later
    import urllib.request
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json, shutil

def get_jsonparsed_data(url):
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

url = ("https://plex.tv/api/downloads/1.json")
data = get_jsonparsed_data(url)

for item in data['computer']['Linux']['releases']:
    if item['distro'] == 'ubuntu' and 'x86_64' in item['build']:
        
        filename = item['url'].split('/')[-1]
        print("Downloading the file " + filename)
        with urllib.request.urlopen(item['url']) as response, open(filename, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
            print("File downloaded ready for installing")
            print("Please run: sudo dpkg -i " + filename);
