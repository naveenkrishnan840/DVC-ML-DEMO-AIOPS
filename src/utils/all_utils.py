import yaml
import os

def read_display(conf_path: str) -> dict:
	with open(conf_path, 'r') as yaml_file:
		content = yaml.safe_load(yaml_file)

	return content


