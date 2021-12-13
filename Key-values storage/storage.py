import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def get_data():
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as f:
        read_data = f.read()
        if read_data:
            return json.loads(read_data)
        return {}


def get_values(key):
    data = get_data()
    return data.get(key)


def add_data(key, value):
    data = get_data()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open(storage_path, 'w') as f:
        json.dump(data, f, indent=4)


parser = argparse.ArgumentParser()
parser.add_argument("--key", dest="key_name", default=None)
parser.add_argument("--val", dest="value", default=None)
args = parser.parse_args()

if (args.key_name is not None) and (args.value is not None):
    add_data(args.key_name, args.value)

if (args.key_name is not None) and (args.value is None):
    list_of_values = get_values(args.key_name)
    if list_of_values is None:
        print(None)
    else:
        print(", ".join([i for i in list_of_values]))
