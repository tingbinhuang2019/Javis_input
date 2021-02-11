# Import dependencies needed to run the script
import pandas as pd
import os
import sys


def read_input_file():

	res = ""
	# Read the list of files in 'input' directory
	input_files = []
	for (dirpath, dirnames, filenames) in os.walk('input'):
	    input_files.extend(filenames)
	    break

	# System will exit if there is no file
	if len(input_files) == 0:
	    res = '$$$Please provide a file.'

	if input_files[-1].endswith('.csv') or input_files[-1].endswith('.txt'):

		# Read file from the 'input' directory
		csv_file = pd.read_csv("input/" + input_files[-1])
		temp_list = csv_file[csv_file.columns[0]]

		# Check if csv file has more than one column
		csv_list = temp_list if len(csv_file.columns) == 1 else csv_file[csv_file.columns[1]]
		res = csv_list
	else:
		res = "$$$Please provide a csv or txt file"

	return res
	

