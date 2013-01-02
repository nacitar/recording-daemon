#!/usr/bin/env python

import common
import time
import os
import sys

def main():
	ramdisk_path=common.get_ramdisk_path()
	storage_path=common.get_storage_path()

	delete_mode=True
	if len(sys.argv) == 2:
		if sys.argv[1] == "move":
			delete_mode=False
	
	print "Monitoring " + ramdisk_path + " in " + ["move","delete"][delete_mode] + " mode"

	while True:
		# get the files
		file_list=common.get_file_list(ramdisk_path)
		# Sort the files so the oldest one is first
		file_list.sort(common.modification_time_comparator)
		
		# When we start eating away at our last 2gb, we copy delete the old one
		while len(file_list) > 3:
			# pop off the oldest file
			oldest_file=file_list.pop(0)
			# remove the oldest file
			if not oldest_file.startswith("keepme_"):
				if delete_mode:
					print "Removing oldest file: " + oldest_file
					try:
						os.remove(oldest_file)
					except OSError:
						print "Ignoring error removing file."
				else: # move mode saves to large storage
					common.save_recordings(True)
		# Don't hammer the machine
		time.sleep(5)

	

if __name__ == '__main__': 
	main() 
