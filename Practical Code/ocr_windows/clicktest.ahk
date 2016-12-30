#NoEnv
#NoTrayIcon
#SingleInstance force
#include FindClick.ahk
;~ #include headfile/lib.ahk
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory. 
SetTitleMatchMode regex 
;~ TimeLock(A_ScriptName)

;~ FileReadLine, line, ocrres.txt, 1
;~ MsgBox line=%line%

;~ FoundPos := RegExMatch(line, "\s([0-9zZ])\s", output)


;~ output := RegExReplace(output, "\s", "")
;~ IMGName := ""
;~ IMGNameU := ""
;~ if(output = 1)
;~ {
	;~ IMGName := "1.png"
	;~ IMGNameU:= "1u.png" 
;~ }
;~ if(output = 2 or output = "Z")
;~ {
	;~ IMGName := "2.png"
	;~ IMGNameU:= "2u.png" 
;~ }
;~ if(output = 3)
;~ {
	;~ IMGName := "3.png"
	;~ IMGNameU:= "3u.png" 
;~ }

;~ if(output = )
;~ {
	;~ MsgBox Error_ : output=%output% 
	;~ ExitApp
;~ }

;~ MsgBox IMGName=%IMGName%
;~ IMGName := "./img/" . IMGName
;~ IMGNameU := "./img/" . "2u.png"

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