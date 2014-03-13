#coding: utf-8
#WINAPI

#OpenProcess() 获取进程句柄
# dwDesiredAccess表示我们索要什么类型的访问权限 => PROCESS_ALL_ACCESS
# bInheritHandle => False
# dwProcessId => PID

#Bool DebugActiveProcess()
# DWORD dwProcessId 附加进程PID

#Bool WaitForDebugEvent() 附加之后调试器在进程中循环等待调试事件
# LPDEBUG_EVENT lpDebugEvent 结构体指针 描述具体的调试事件.
# dwMilliseconds 等待下一个调试事件发生的时间上限 => INFINITE 无限

#Bool ContinueDebugEvent 目标进程恢复到原来的状态
# dwProcessId ThreadId 调试器捕获事件的瞬间
# dwContinueStatus 目标进程的下一个动作 DBG_CONTINUE 继续执行 DBG_EXCEPTION_NOT_HANDLED 继续处理捕获的异常事件

from ctypes import *
from my_debugger_defines import *

kernel32 = windll.kernel32

class debugger():

	def __init__(self):
		self.h_process = None
		self.pid = None
		self.debugger_active = False

	def load(self,path_to_exe):

		print "Sucessful launched the process"
		print "PID: %d" % process_information.dwProcessId

		self.h_process = self.open_process(process_information.dwProcessId)

	def open_process(self,pid):
	 	h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS,False,pid)
	 	return h_process

	def attach(self,pid):
	 	h_process = self.open_process(pid)
	 	if kernel32.DebugActiveProcess(pid):
	 		self.debugger_active=True
	 		self.pid = int(pid)
	 		#self.run()
	 	else:
	 		print "Unable to attach porcess"

	def run(self):

	 	while self.debugger_active == True:
	 		self.get_debug_event()

	def get_debug_event(self):
	 	debug_event = DEBUG_EVENT()
	 	continue_status = DBG_CONTINUE

	 	if kernel32.WaitForDebugEvent(byref(debug_event),INFINITE):
	 		raw_input("Press a key to continue")
	 		self.debugger_active=False
	 		kernel32.ContinueDebugEvent(\
	 			debug_event.dwProcessId,\
	 			debug_event.dwThreadId,\
	 			continue_status)

	def dettach(self):

	 	if kernel32.DebugActiveProcessStop(self.pid):
	 		print "Finish debugging"
	 		return True
	 	else:
	 		print "Error Occured"
	 		return False