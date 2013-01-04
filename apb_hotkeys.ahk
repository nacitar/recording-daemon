#IfWinActive, APB Reloaded
#SingleInstance force
#NoEnv

; to record press f9 to activate bandicam
F10::
	; delete
	Run c:\Python27\python.exe %A_ScriptDir%\delete_recordings.pyw
	return
F11::
	; save
	Run c:\Python27\python.exe %A_ScriptDir%\save_recordings.pyw
	return

