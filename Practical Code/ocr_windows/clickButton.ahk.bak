#NoEnv
#NoTrayIcon
#SingleInstance force
#include FindClick.ahk
;~ #include headfile/lib.ahk
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory. 
;~ SetTitleMatchMode regex 
;~ TimeLock(A_ScriptName)

FileReadLine, line, ocrres.txt, 1
;~ MsgBox line=%line%

FoundPos := RegExMatch(line, "\s([0-9zZ])\s", output)
output := RegExReplace(output, "\s", "")
if(output = "Z")
{
	output := 2
}

WinActivate, Total Commander ahk_class TNASTYNAGSCREEN
WinWaitActive, Total Commander ahk_class TNASTYNAGSCREEN
send, %output%

;~ WinGetActiveTitle, title
;~ Clipboard := title . "+" . output 
;1.  127 264   2. 242 271   3. 354 268
;~ x := 0
;~ y := 0

;~ if(output = 1)
;~ {
	;~ x := 127
	;~ y := 264
;~ }
;~ if(output = 2 or output = "Z")
;~ {
	;~ x := 242
	;~ y := 271
;~ }
;~ if(output = 3)
;~ {
	;~ x := 354
	;~ y := 268
;~ }
;~ else if(output = )
;~ {
	;~ MsgBox Error_ : output=%output% 
	;~ ExitApp
;~ }

;~ ControlClick, ,Total Commander ahk_class TNASTYNAGSCREEN,,,, NA x%x% y%y% 
;~ ControlClick,  x%x% y%y%, Total Commander ahk_class TNASTYNAGSCREEN
;~ errcode:=FindClick(IMGName,"e")
;~ if errcode=0
;~ {
	;~ errcode:=FindClick(IMGNameU,"e")
	;~ if errcode=0
	;~ {
		
		;~ MsgBox, 0, , Can't find the %output% , %IMGNameU% button, 3 ; 3 is the count down time
		;~ Return
	;~ }
;~ }

ExitApp