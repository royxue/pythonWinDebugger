from ctypes import *
from my_debugger_defines import * 

kernel32=windll.kernel32
class debugger():
	def __init__(self):
		pass

	def load(self,path_to_exe):
		#deCreation flag => how to create process
		creation_flags = DEBUG_PROCESS
		#see GUI define it CREATE_NEW_CONSOLE
		
		startupinfo=STARTUPINFO()
		process_infomation = PROCESS_INFORMATION()

		startupinfo.dwFlags=0x1
		startupinfo.wShowWindow=0x0
		#start process shown as a separate window 

		startupinfo.cb=sizeof(startupinfo)
		if kernel32.CreateProcessA(path_to_exe,None,None,None,None,creation_flags,None,None,byref(startupinfo),byref(process_infomation)):
			print "[*]We have successfully launch thr process"
			print "[*]PID:%d"%process_infomation.dwProcessId
		else:
			print "[*]Error:0x%08x."%kernel32.GetLastError()

			