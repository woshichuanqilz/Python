#NoEnv
#NoTrayIcon
#SingleInstance force
;~ #include lib.ahk
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory. 
SetTitleMatchMode regex 
SendMode, input
;~ TimeLock(A_ScriptName)

count := 0

;~ para := %0%
;~ MsgBox para=%para%
Loop, %0%  
{
	
	count := count + 1
	
	if(count = 1)
	{
		CmdChoice := %A_Index% 
	}
	
	if(count = 2)
	{
		CmdContent := %A_Index%
	}
}

;~ MsgBox CmdChoice=%CmdChoice% CmdContent=%CmdContent%

if(CmdChoice = "send")
{
	Send, %CmdContent%
	Return 
}
else if(CmdChoice = "search")
{
	searchURL := "https://www.google.com.hk/?gws_rd=ssl#safe=strict&q=" . CmdContent
    Run, %searchURL%
	Return 
}



ExitApp
