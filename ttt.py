import my_debugger_pro

debugger = my_debugger_pro.debugger()

pid = raw_input("PID Here:")

debugger.attach(int(pid))

debugger.dettach()