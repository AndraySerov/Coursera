import os
import tempfile
import argparse
import json


f = open('key_value_storage.json', 'r+')
contacts = json.load(f)


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open('key_value_storage.json', 'w') as f:
    json.dump(contacts, f)
