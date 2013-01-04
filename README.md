recording-daemon
================

A daemon and scripts to facilitate gameplay recording with a circular-array style approach such that you never miss an awesome moment.


Only a single instance of the save/delete scripts will be allowed to run at a time.  If additional instances of the same script run, they will exit.  If an instance of the other script runs, it will wait for a turn then run.


Save current recordings in ramdisk:

	./save_recordings.pyw

Delete current recordings in ramdisk:

	./delete_recordings.pyw

Start recording daemon in delete-mode (deletes oldest file when room is needed):

	./recording_daemon.py

ALTERNATIVE: Start recordings daemon in move-mode (moves oldest file to persistent storage when room is needed):

	./recording_daemon.py move

If saving and deleting isn't working, perhaps something crashed and held the lock open.  You can release the lock by using:

	./release_lock.pyw


