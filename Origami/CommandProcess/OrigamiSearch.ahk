#NoEnv
#NoTrayIcon
#SingleInstance force
;~ #include lib.ahk
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory. 
SetTitleMatchMode regex 
SendMode, input
;~ TimeLock(A_ScriptName)

Loop, %0%  
{
    param := %A_Index%  ; Get the first para
	break
}

;~ MsgBox param=%param%
Send, %param%

ExitApp
