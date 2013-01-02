recording-daemon
================

A daemon and scripts to facilitate gameplay recording with a circular-array style approach such that you never miss an awesome moment.


Save current recordings in ramdisk:

	./save_recordings.py

Delete current recordings in ramdisk:

	./delete_recordings.py

Start recording daemon in delete-mode (deletes oldest file when room is needed):

	./recording_daemon.py

ALTERNATIVE: Start recordings daemon in move-mode (moves oldest file to persistent storage when room is needed):

	./recording_daemon.py move

