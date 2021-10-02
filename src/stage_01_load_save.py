from src.utils.all_utils import read_display
import argparse
import pandas as pd
import os

def get_data(path):
	config = read_display(path)

	remote_path_config = pd.read_csv(config["data_source"],sep=";")

	artifacts = "%s/%s" % (config["artifacts"]["artifact_dir"],config["artifacts"]["raw_local_dir"])

	# file_name = os.path.join(artifacts, config["artifacts"]["raw_local_file"])

	os.makedirs(artifacts, exist_ok=True)

	remote_path_config.to_csv(os.path.join(artifacts, config["artifacts"]["raw_local_file"]), sep=";")

	

if __name__ == '__main__':
	args = argparse.ArgumentParser()

	args.add_argument("--config", "-c", default="config/config.yaml")

	parsed_arg = args.parse_args()
	get_data(parsed_arg.config)
	print(parsed_arg)