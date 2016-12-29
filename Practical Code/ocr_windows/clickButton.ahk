#NoEnv
#NoTrayIcon
#SingleInstance force
#include FindClick.ahk
;~ #include headfile/lib.ahk
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory. 
SetTitleMatchMode regex 
;~ TimeLock(A_ScriptName)

FileReadLine, line, ocrres.txt, 1
;~ MsgBox line=%line%

FoundPos := RegExMatch(line, "\s([0-9zZ])\s", output)


output := RegExReplace(output, "\s", "")
IMGName := ""
MsgBox output=%output%
if(output = 1)
{
	IMGName := "1.png"
}
if(output = 2 or output = "Z")
{
	IMGName := "2.png"
}
if(output = 3)
{
	IMGName := "3.png"
}
MsgBox IMGName=%IMGName%
IMGName := "./img/" . IMGName

errcode:=FindClick(IMGName,"e")
if errcode=0
{
	MsgBox, 0, , Can't find the Send button, 3 ; 3 is the count down time
	Return
}

ExitApp