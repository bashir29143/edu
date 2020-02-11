import os
import tempfile
import time
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val')
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def add_to_dict(key, value, dictionary):
	if (key in dictionary):
		dictionary[key] = dictionary[key] + ', ' + str(value)
	else:
		dictionary[key] = str(value)

def from_dict(key, dictionary):
	if (key in dictionary):
		return dictionary[key]
	else:
		return ''


if os.path.isfile(storage_path):
	with open(storage_path, 'r') as f:
		dict = json.load(f)
else:
	dict = {}


if args.val:
	with open(storage_path, 'w') as f:
		add_to_dict(args.key, args.val, dict)
		json.dump(dict,f)

else:
	print(from_dict(args.key, dict))
