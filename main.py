# The premise behind this program is that I often misplace a file, redownload it, and then move it into the same folder where the old one was originally
# Therefore, this program searches a given directory for filenames that are identical except for a small bit at the end, so that I can delete these duplicates en masse instead of manually doing it
# E.g. "Filename.jpg" vs "Filename (Copy).jpg"
# Before just blindly deleting files with similar names, the program makes sure the contents are identical
# I don't want to upload a file that will mass-delete files, so I have made it only print the duplicates at the moment
# If you run it and find that the duplicates listed are actually duplicates, then you can change it to delete them

import os
import sys
import filecmp
from pathlib import Path

def count_same_beginning_length(a, b):
	count = 0

	for i in range(min(len(a), len(b))):
		if a[i] == b[i]:
			count += 1
		else:
			break
	
	return count

def determine_near_duplicates(list, similarity_factor):
	output_list = []

	# The list is sorted alphabetically, so filenames that start the same way will be right next to each other
	i = 0
	while i < len(list) - 1:
		entry = list[i]
		entry_name, entry_ext = os.path.splitext(entry)

		duplicates = []

		j = i + 1
		last_duplicate_found = i

		while j < len(list):
			next_entry = list[j]

			next_entry_name, next_entry_ext = os.path.splitext(next_entry)

			# To be a duplicate, the extensions have to be the same
			if entry_ext != next_entry_ext:
				j = j + 1
				continue

			similarity = count_same_beginning_length(entry_name, next_entry_name)
			smallest_length = min(len(entry_name), len(next_entry_name))
			is_duplicate = similarity > (smallest_length * similarity_factor)

			if is_duplicate:
				# If e.g. there are two files named ImageA (0).jpg and ImageA.jpg, make sure that the longer one is labelled as a duplicate
				if len(next_entry) < len(entry):
					entry, next_entry = next_entry, entry
				duplicates.append(next_entry)
				last_duplicate_found = j
				j = j + 1
			else:
				break
		
		if len(duplicates) > 0:
			output_list.append((entry, duplicates))
		i = last_duplicate_found + 1

	return output_list	

if __name__ == "__main__":
	# If the first X% of two filenames is identical, then treat them as a potential duplicate
	# 70% seems reasonable at this point
	# This is just to filter the amount of comparisons we have to do, we still check file contents to make sure they're the same later
	similarity_factor = 0.7

	folder = Path(sys.argv[1])
	list = os.listdir(folder)
	list = determine_near_duplicates(list)

	for entry in list:
		original = entry[0]
		duplicates = entry[1]
		for d in duplicates:
			# Now we check whether the two files are the same
			same = filecmp.cmp(folder / original, folder / d)
			if same:
				print("Found duplicates: ")
				print("  Original: " + original)
				print("  Duplicate: " + d)
				# Uncomment this line at your own risk:
				#os.remove(d)