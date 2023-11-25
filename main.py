'''
-----------------------------------------------------------------------
File: main.py
Creation Time: Nov 24th 2023 7:04 pm
Author: Saurabh Zinjad
Developer Email: zinjadsaurabh1997@gmail.com
Copyright (c) 2023 Saurabh Zinjad. All rights reserved | GitHub: Ztrimus
-----------------------------------------------------------------------
'''

import argparse
from src.scripts.auto_apply_pipeline import run_autoapply_pipeline

# Create an argument parser
parser = argparse.ArgumentParser()

# Add the required arguments

parser.add_argument('-u', "--url", default="https://www.squarespace.com/careers/jobs/5369485?ref=Simplify", help='URL of the job posting')
parser.add_argument('-m', "--master_data", default="master_data/saurabh_profile.json", help='Path of user\'s master data file.')

# Parse the arguments
args = parser.parse_args()

run_autoapply_pipeline(args.url, args.master_data)