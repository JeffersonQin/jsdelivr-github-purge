import os
import json
import requests

config = {}

with open('config.json', 'r', encoding='utf8') as f:
	config = json.load(f)

print('configuration: ', config)
path_len = len(config['path'])

for root, dirs, files in os.walk(config['path'], topdown=False):
	relative_path = root[path_len:]
	if relative_path.startswith('.'): continue
	for name in files:
		file_path = os.path.join(relative_path, name)
		print(file_path)
		url = f'https://purge.jsdelivr.net/gh/{config["repo"]}@{config["version"]}/{file_path}'
		print(url)
		response = requests.get(url).json()
		print(response)
