import ahk

ahk.start() # Ititializes a new script thread
ahk.ready() # Waits until status is True

ahk.execute('send, 12345') # Sets a to the return value of WinActive
# print ahk.get('a') # prints the HWND of the found window or 0x0 as a string
