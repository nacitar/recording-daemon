#!/usr/bin/env python

import os
import os.path
import time

# CUSTOMIZE THESE
def get_ramdisk_path():
	""" Fast storage where we record. """
	return os.path.join("G:",os.sep,"Bandicam")

def get_storage_path():
	""" Path for "delete"-mode recording daemon that keeps data when you tell it to save.  Less space is needed as it's only on-demand. """
	return os.path.join("E:",os.sep,"Bandicam")

def get_large_storage_path():
	""" Path for "move"-mode recording daemon that keeps all data.  This place needs lots of space. """
	return os.path.join("Z:",os.sep,"Bandicam")

# END OF CUSTOMIZATION

def get_file_creation_time(filename):
	return os.path.getctime(filename)

def get_file_modification_time(filename):
	return os.path.getmtime(filename)

def get_file_list(search_path):
	file_list = []
	for filename in os.listdir(search_path):
		file_list.append(os.path.join(search_path,filename))
	return file_list

def modification_time_comparator(file_one,file_two):
	time_one=get_file_modification_time(file_one)
	time_two=get_file_modification_time(file_two)
	return int(time_one-time_two)

def save_recordings(large = False):
	ramdisk_path=get_ramdisk_path()
	storage_path=get_storage_path()
	if large:
		storage_path=get_large_storage_path()

	# get the files
	file_list=get_file_list(ramdisk_path)

	# Sort the files so the oldest one is first
	file_list.sort(modification_time_comparator)

	for filepath in file_list:
		filename=os.path.basename(filepath)
		print "Saving file "+filename

		if not filename.startswith("keepme_"):
			newname="keepme_"+filename
			newpath=os.path.join(ramdisk_path,newname)
			try:
				# move it locally so it's fast
				os.rename(filepath,newpath)
			except OSError:
				# fallback to skipping that step
				newpath=filepath
			# move it to persistent storage
			try:
				os.rename(newpath,os.path.join(storage_path,filename))
			except OSError:
				print "Ignoring error moving file to persistent storage."
			

def delete_recordings():
	ramdisk_path=get_ramdisk_path()
	storage_path=get_storage_path()

	# get the files
	file_list=get_file_list(ramdisk_path)

	# Sort the files so the oldest one is first
	file_list.sort(modification_time_comparator)

	for filepath in file_list:
		filename=os.path.basename(filepath)
		if not filename.startswith("keepme_"):
			print "Deleting file "+filename
			# remove it
			try:
				os.remove(filepath)
			except OSError:
				print "Ignoring error deleting file."
