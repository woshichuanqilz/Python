#NoEnv
#NoTrayIcon
#SingleInstance force
#Persistent
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

;~ Loop
;~ {
	;~ FileReadLine, line, TranslationRes.txt, A_Index
	;~ if ErrorLevel
		;~ break
	;~ MsgBox, 4, , Line #%A_Index% is "%line%".  Continue?
	;~ IfMsgBox, No
		;~ return
;~ }

;~ RunWait, %ComSpec% /c python TranslationPy.py %Clipboard% > TranslationRes.txt
;~ FileRead, Contents, TranslationRes.txt
;~ MsgBox Clipboard=%Contents%
;~ MouseGetPos, XPos, YPos
;~ ToolTip, %Clipboard% = %Contents%
ToolTip, Multiline`nTooltip, %XPos%, %YPos%
SetTimer, RemoveToolTip, 10000
return

RemoveToolTip:
SetTimer, RemoveToolTip, Off
ToolTip
return