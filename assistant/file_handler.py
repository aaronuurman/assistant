#!/usr/bin/env python3
import os

def find_sub_folder(parent_path, sub_path):
	"""Find a sub directory from parent folder.

	Returns:
	If folder contains sub directory then full path to sub directory is returned.
	Else None is returned.
	"""

	folders = []

	# r=root, d=directories, f = files
	for r, d, f in os.walk(parent_path):
		for folder in d:
			folders.append(os.path.join(r, folder))

	result = [x for x in folders if sub_path in x]

	if not result:
		return None

	return result[0]

def write_to_file(full_path, data):
	"""Write string data into file."""
	
	file = open(full_path, "w")
	file.write(data)
	file.close()