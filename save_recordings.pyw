#!/usr/bin/env python

import os
import os.path

import common

def main():
	if common.get_lock("s"):
		try:
			common.save_recordings()	
		finally:
			common.release_lock()

if __name__ == '__main__': 
	main() 
