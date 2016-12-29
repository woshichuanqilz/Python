#include FindClick.ahk
global g_ThreadCnt := 0

; Get Selection
IsSelectionHasReturn()
{
	IsSelect:=IsTextSelect()
;	MsgBox IsSelect=%IsSelect%
	if(IsSelect = 0)
	{
		Return false
	}

	HasEnter := false
	ClipSaved := ClipboardAll   ; Save the entire clipboard to a variable of your choice.
	; ... here make temporary use of the clipboard, such as for pasting Unicode text via Transform Unicode ...

	Clipboard := ""
	Send, ^{Insert}
	FoundPos := RegExMatch(Clipboard, "`n")
	if(FoundPos <> 0)
	{
		HasEnter := true
	}

	Clipboard := ClipSaved   ; Restore the original clipboard. Note the use of Clipboard (not ClipboardAll).

	Return HasEnter
}


; 判断是否有选区
IsTextSelect()
{
	SendMode event
	temp = %Clipboard%
	Send ^c
	if(temp = Clipboard)
	{
		;MsgBox false
		bRet = false
	}
	Else
	{
		;MsgBox true
		bRet=true
	}

	Clipboard := temp

	Return bRet
}

;copy word
CopyWord()
{
	Clipboard := ""
	Send, ^{left}
	Send, ^+{right}
	Send, ^c
	Send, {right}
	
	ClipWait, 2
	Clipboard := RegExReplace(Clipboard, "\s", "")
	Return
}

; 选中一行
SelectLine()
{
	SendMode Event
	Send {End}
	Send +{Home}
	Return
}

; 选中一行并复制
SelectAndCopyLine()
{
	SelectLine()
	Send ^c
	Return
}

; 注释
CommentSegment(CommentMark)
{
	;SendMode input
	bIsSelect:=IsTextSelect()
	;MsgBox %bIsSelect%
	if(bIsSelect="false")
	{
		FoundPos := RegExMatch(Clipboard, "\/\*")
		Send {Home}{Home}
		Send %CommentMark%
	}
	Else
	{

		ClipboardSV := Clipboard

		;MsgBox 1%ClipboardSV%
		Send ^c
		CommentMarkN := "^"CommentMark
		;CommentMarkN := "^\s*"CommentMark  ; 错误版本
		FoundPos := RegExMatch(Clipboard, "\/\*")
		If FoundPos = 0
		{
			;MsgBox 1
			Clipboard := RegExReplace(Clipboard, "\A", "/*`r`n")
;			Clipboard := RegExReplace(Clipboard, "\Z", "`r`n*/")
			Clipboard := Clipboard . "`r`n*/"
		}
		Else
		{
			;MsgBox 2
			Clipboard := RegExReplace(Clipboard, "^\/\*", "")
			Clipboard := RegExReplace(Clipboard, "`r`n\*\/", "")
			;Clipboard := RegExReplace(Clipboard, "`r`n\*\/", "")
		}

		Send ^v
		;MsgBox 1%ClipboardSV%
		Clipboard := ClipboardSV
	}

	Return
}

;__________Split Line__________
CopyTextIntoVim(bIsRefMark, szRefMark)
{
	;MsgBox %bIsRefMark%
	;MsgBox begin

	WindowClassName=Vim

	IfWinNotExist ahk_class %WindowClassName%
	{
		run D:\Program Files\Vim\vim74\gvim.exe
		WinActivate, [未命名] - GVIM
		WinActivate, [未命名] - GVIM
		Sleep 1000
		Send {Esc}
		Send {Esc}
		Send :tabnew{enter}
		Send {Esc}
		Send +{Insert}
	}

	Else
	{
		IfWinNotActive ahk_class %WindowClassName%
		WinActivate
		WinWaitActive
		Send {Esc}
		Send {Esc}
		Send :tabnew{enter}{enter}
		Send {Esc}
		Send +{Insert}
		Send {Esc}
		Sleep 500
		SendMode input
		;Send :set ft=cpp{enter}
	}

;	if(bIsRefMark = 1)
	if(0 = 1)
	{
		MsgBox, 4, , Do you want the get-set regex deal?, 3  ; 5秒超时时间。
		IfMsgBox, No
			Return  ; 用户点击了“No/否”按钮。
		IfMsgBox, Yes
		{
			Send :v/\<add\|\<set\|%szRefMark%.\{{}-{}}/d{Enter}
			Return ; 即假定超时和“No/否”一样对待。
		}
		IfMsgBox, Timeout
		{
			Send :v/\<add\|\<set\|%szRefMark%.\{{}-{}}/d{Enter}
			Return ; 即假定超时和“No/否”一样对待。
		}

		Return
	}

	Return
}



; SendClipboardToQQ
SendClipboardToQQ() ; To Pad now
{
	SetTitleMatchMode, RegEx
	
	; Get the link of the current web page
	IfWinActive, Vimperator ahk_class MozillaWindowClass
	{
		WinGetActiveTitle, title
		title := RegExReplace(title, "i) - Vimperator", "")
		Send, ^l
		Send, ^c
		Clipboard := title . "`n" . Clipboard
	}
/*
	else
	{
		WinGetActiveTitle, title
		Clipboard := title . "`n" . Clipboard
	}
*/
	
	WinShow, QQ ahk_class TXGuiFoundation
	WinActivate, QQ ahk_class TXGuiFoundation

	SendMode input
	;~ Send, 2767215800 ; ipad
	Send, wodeandroidshouji ; My Android 
	;~ Send, wodeipad

	SendMode event
	send {enter}
	Sleep 100
	send {enter}
	Sleep, 1000
	
	;~ Wintitle := "iPad"
	Wintitle := "破晓的 Android手机"
	
	WinActivate,  %Wintitle% ahk_class TXGuiFoundation
	WinWaitActive, %Wintitle% ahk_class TXGuiFoundation
;	MsgBox 
	Send ^v
	sleep, 100
	Send {Enter}

	Sleep 2000
	WinHide

	Return
}

GetScriptPathByTitle(Path := 1)
{
	WinGetActiveTitle wintitle
	wintitle := RegExReplace(wintitle, "~\\Desktop", "C:\Users\Administrator\Desktop")
	
	RegExMatch(wintitle, ".*(?= -)", strRes)
	;~ RegExMatch(wintitle, "\((.*)\)", strRes)  ; vim title
	;~ strRes1 := strRes1 . "\	" ;vim title too use strRes1 when you use vim
	;~ MsgBox strRes1=%strRes1%
	
	SplitPath, strRes, name, dir, ext, name_no_ext, drive 
	if(Path = 1)
	{
		strRes := dir
	}
	
	if(Path = 2)
	{
		strRes := name_no_ext
	}
	
	;~ MsgBox strRes=%strRes%
	Return strRes
}

GetScriptPathByTitleInScite()
{
	WinGetActiveTitle wintitle
	wintitle := RegExReplace(wintitle, "~\\Desktop", "C:\Users\Administrator\Desktop")
	RegExMatch(wintitle, ".*(?= -)", strRes)
	
	Return strRes
}

;__________Split Line__________
OpenFilePathByTC(OpenPath := "")
{
	IfWinActive, Total Commander (x64) 8.51a - NOT REGISTERED
	{
		ToolTip, hehe
		WinMinimize, A
	}
	
	WinGetActiveTitle wintitle
	wintitle := RegExReplace(wintitle, "~\\Desktop", "C:\Users\Administrator\Desktop")
	RegExMatch(wintitle, "[a-zA-Z]:\\.*\\.*?(?=( |\)))", strRes, 1)
	;~ MsgBox wintitle=%wintitle%
	If InStr( FileExist(strRes), "D" )
	{
		;MsgBox, %wintitle%` is a Folder
		strRes = %strRes%\
	}

	if(OpenPath = "")
	{
		SplitPath, strRes,, dir
		QuoteAWord(dir)
	}
	else if(OpenPath = "A")
	{
		dir := OpenPath
	}
	
	; you can use the previous func to get the dir
	;~ MsgBox dir=%dir%
	Run TOTALCMD64.EXE %dir%
	WinActivate, ahk_class TTOTAL_CMD

	Return
}

;===================================================================================================================
Fun_Ev_ComboChoose(ChooseNum)		;运行或退出
{
    SendMessage, 0x147, 0, 0, ComboBox1, A
    ChoicePos = %ErrorLevel%
    ChoicePos += 1
    If (ChoicePos = ChooseNum)
        Control, Choose, 1, ComboBox1, A
    Else
        Control, Choose, %ChooseNum%, ComboBox1, A
    Return
}


;===================================================================================================================
GetWindowControlList(WindowTitle := "A")
{
	SetTitleMatchMode, regex
	WinGet, WindowControlList, ControlList, %WindowTitle%

	FileAppend,`n -------------------------------, WindowControlList.txt
	FileAppend,`n WindowTile = %WindowTitle%, WindowControlList.txt

	Loop, Parse, WindowControlList, `n
	{
		FileAppend,`n %A_LoopField%, WindowControlList.txt
	}

	Return
}


; Set The Content And Read
ReadTheContent(Content)
{
	;~ SetTitleMatchMode, 3
	;~ WindowTitle := "朗读女 7.0"
	;~ DetectHiddenWindows, On
	;~ WinMinimize, %WindowTitle%
	;~ WinActivate, %WindowTitle%
	;~ ControlSetText, RichEdit20A4, %Content%, %WindowTitle%
	;~ ControlClick, Button83, %WindowTitle%,,,, NA x15 y15
	
	SetTitleMatchMode, RegEx
	WindowTitle := "朗读女 7.0  [ 朗读女软件简介.txt ] "
	
	ControlSetText, RichEdit20A4, LockWorkStation, 朗读女 7.0
    Sleep, 500
	ControlClick, Button83, 朗读女 7.0,,,, NA x15 y15
}


; active Vimperator
ActiveVimperator()
{
	Send !f
	Sleep 50
	Send {esc}
	Sleep 50
	Send !f
	Sleep 50
	Send {esc}
	Return
}


; 加密算法
RC4(RC4Data,RC4Pass)
{
global RC4Result
ATrim = %A_AutoTrim%
AutoTrim, Off
BLines = %A_BatchLines%
SetBatchLines, -1
StringLen, RC4PassLen, RC4Pass
Loop, 256
  {
	a := A_Index - 1
	Transform, ModVal, Mod, %a%, %RC4PassLen%
	ModVal ++
	StringMid, C, RC4Pass, %ModVal%, 1
	Transform, AscVar, Asc, %C%
	Key%a% = %AscVar%
	sBox%a% = %a%
  }
b = 0
Loop, 256
  {
	a := A_Index - 1
	TempVar := b + sBox%a% + Key%a%
	Transform, b, Mod, %TempVar%, 256
	T := sBox%a%
	sBox%a% := sBox%b%
	sBox%b% = %T%
  }
StringLen, DataLen, RC4Data
RC4Result =
i = 0
j = 0
Loop, %DataLen%
  {
	TmpVar := i + 1
	Transform, i, Mod, %TmpVar%, 256
	TmpVar := sBox%i% + j
	Transform, j, Mod, %TmpVar%, 256
	TmpVar := sBox%i% + sBox%j%
	Transform, TmpVar2, Mod, %TmpVar%, 256
	k := sBox%TmpVar2%
	StringMid, TmpVar, RC4Data, %A_Index%, 1
	Transform, AscVar, Asc, %TmpVar%
	Transform, C, BitXOr, %AscVar%, %k%
	IfEqual, C, 0
		C = %k%
	Transform, ChrVar, Chr, %C%
	RC4Result = %RC4Result%%ChrVar%
  }
AutoTrim, %ATrim%
SetBatchLines, %BLines%
Return RC4Result
}


GetNumberOfFolder(FilePath)
{
	count := 0
	Loop, %FilePath%,,1
	{
	  if A_LoopFileAttrib contains H,R,S
		  continue
	  count += 1
	}
	
	return count
}


RestartExplorer()
{
	WinGet, h, ID, ahk_class Progman	        ; use ahk_class WorkerW for XP
	PostMessage, 0x12, 0, 0, , ahk_id %h%		;wm_quit
	sleep, 25
	Run, "%windir%\explorer.exe"
	return
}


DisableTaskMgr()
{
	Regwrite, REG_DWORD, HKEY_CURRENT_USER,SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System, DisableTaskMgr, 1
	return
}

EnableTaskMgr()
{
	Regwrite, REG_DWORD, HKEY_CURRENT_USER,SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System, DisableTaskMgr, 0
	return
}


SelectWord()
{
	Send, {CTRLDOWN}{LEFT}{SHIFTDOWN}{RIGHT}{CTRLUP}{SHIFTUP}
	Return
}

GetSelectWord()
{
	SelectWord()
	Send, ^c
	Clipboard := RegExReplace(Clipboard, "\s+$", "")
	Return Clipboard
}

GetCurrentListContent()
{
	;LV_GetText(RowTextC1, A_EventInfo)  ; Get the text from the row's first field.
	LV_GetText(RowTextC2, A_EventInfo, 2)
	;ToolTip KeyWord: %RowTextC1%`, Content: %RowTextC2%
	
	ToolTip, Content: %RowTextC2%
	SetTimer, RemoveToolTip, 5000
	return

	RemoveToolTip:
	SetTimer, RemoveToolTip, Off
	ToolTip
	return
}


MsgBoxMarkLine(linenumber)
{
	MsgBox LineNumer=%linenumber%
	Return
}

;===================================================================================================================
;Toggle process
ToggleProcess(FullFileName)
{
	SplitPath, FullFileName, name, dir, ext, name_no_ext, drive 
	
	IsExist := ProcessExist(name)
	
	if(IsExist = 0)
	{
		Run, %FullFileName%
		Return
	}
	
	Process, Close, %name%
	
	Return 
}


;===================================================================================================================
;Restart The Process
RestartProcess(FullFileName)
{
	SplitPath, FullFileName, name, dir, ext, name_no_ext, drive 
	Process, Close, %name%
	Sleep, 2000 
	Run, %FullFileName%
	Return
}

;===================================================================================================================
;If Process Exist 0 is noexist program exist
ProcessExist(Name)
{
	Process,Exist,%Name%
	return Errorlevel
}


; English Character
IsEnglishCharacter(string)
{
	IsEnglish = true 
	FoundPos := RegExMatch(string, "[a-zA-Z0-9,.!?]")
	
	if(FoundPos = 0)
	{
		IsEnglish = false
	}
	
	Return IsEnglish
}


; Complie script 
ComplieScript(fullfilename)
{
	SplitPath, fullfilename, name, dir, ext, name_no_ext, drive 
	
	Process, Close, %name_no_ext%.exe
	Process, Close, AutoHotkeyU64.exe

	fullpath = "%fullpath%"
	cmdline  = .\CommonCmd\compileAHK.bat
	cmdline  = %cmdline%%A_Space%%name%
	exefile  = %dir%\%name_no_ext%.exe

	RunWait %cmdline%
	;~ MsgBox exefile=%exefile%
	;~ Run, %exefile%
	MsgBox, 0, , Compile Done, 1 ; 3 is the count down time
	Return exefile
}

; Compile and Run Script 
ComplieAndRunScript(fullfilename)
{
	Exefile := ComplieScript(fullfilename)
	;~ MsgBox Exefile=%Exefile%
	Run, %Exefile%
	Return
}

; Mouse is over certain window
MouseIsOver(WinTitle) {
    MouseGetPos,,, Win
    return WinExist(WinTitle . " ahk_id " . Win)
}


; Check the class of active window control
; *Example*
;#If ActiveControlIsOfClass("Edit")
;^BS::Send ^+{Left}{Del}
;^Del::Send ^+{Right}{Del}
ActiveControlIsOfClass(Class) {
    ControlGetFocus, FocusedControl, A
    ControlGet, FocusedControlHwnd, Hwnd,, %FocusedControl%, A
    WinGetClass, FocusedControlClass, ahk_id %FocusedControlHwnd%
    return (FocusedControlClass=Class)
}

; Open Certain QQ Friend
OpenQQFriend(QQ_Num)
{
	WinShow, QQ ahk_class TXGuiFoundation
	WinActivate, QQ ahk_class TXGuiFoundation

	SendMode input
	Send %QQ_Num%

	SendMode event
	send {enter}
	Sleep, 2000
	Return
}

; Get the Chat Content for Certain friend 
GetChatContent(QQ_Num)
{
	OpenQQFriend(QQ_Num)
	Send, {Tab}
	Send, ^a^c
	ClipWait
	ChatContent := Clipboard
	Return ChatContent
}

; Get the content of a certain friend 
GetLastChatContent(QQ_Num)
{
	ChatContent := GetChatContent(QQ_Num)
;	MsgBox ChatContent=%ChatContent%
	
	Loop, Parse, ChatContent, `n, `r
	{
		if A_loopfield 
		{
			LastChatContent := A_loopfield
		}
	}
	
	Return LastChatContent
}


; The script is running
VoicePromptForRunningScript()
{
	; Set the content for read.
	SplitPath, A_ScriptName, name, dir, ext, name_no_ext, drive 
	static ReadContent := name_no_ext . "is running."
	ToolTip, %ReadContent%, 800, 450
;	SetTimer, Running, 5000  
	Return 
	
;	Running:
;	ReadTheContent(ReadContent)
;	Return
}

; filecopytoclipboard
FileToClipboard(PathToCopy,Method="copy")
{
FileCount:=0
PathLength:=0

; Count files and total string length
Loop,Parse,PathToCopy,`n,`r
  {
  FileCount++
  PathLength+=StrLen(A_LoopField)
  }

pid:=DllCall("GetCurrentProcessId","uint")
hwnd:=WinExist("ahk_pid " . pid)
; 0x42 = GMEM_MOVEABLE(0x2) | GMEM_ZEROINIT(0x40)
hPath := DllCall("GlobalAlloc","uint",0x42,"uint",20 + (PathLength + FileCount + 1) * 2,"UPtr")
pPath := DllCall("GlobalLock","UPtr",hPath)
NumPut(20,pPath+0),pPath += 16 ; DROPFILES.pFiles = offset of file list
NumPut(1,pPath+0),pPath += 4 ; fWide = 0 -->ANSI,fWide = 1 -->Unicode
Offset:=0
Loop,Parse,PathToCopy,`n,`r ; Rows are delimited by linefeeds (`r`n).
  offset += StrPut(A_LoopField,pPath+offset,StrLen(A_LoopField)+1,"UTF-16") * 2

DllCall("GlobalUnlock","UPtr",hPath)
DllCall("OpenClipboard","UPtr",hwnd)
DllCall("EmptyClipboard")
DllCall("SetClipboardData","uint",0xF,"UPtr",hPath) ; 0xF = CF_HDROP

; Write Preferred DropEffect structure to clipboard to switch between copy/cut operations
; 0x42 = GMEM_MOVEABLE(0x2) | GMEM_ZEROINIT(0x40)
mem := DllCall("GlobalAlloc","uint",0x42,"uint",4,"UPtr")
str := DllCall("GlobalLock","UPtr",mem)

if (Method="copy")
  DllCall("RtlFillMemory","UPtr",str,"uint",1,"UChar",0x05)
else if (Method="cut")
  DllCall("RtlFillMemory","UPtr",str,"uint",1,"UChar",0x02)
else
  {
  DllCall("CloseClipboard")
  return
  }

DllCall("GlobalUnlock","UPtr",mem)

cfFormat := DllCall("RegisterClipboardFormat","Str","Preferred DropEffect")
DllCall("SetClipboardData","uint",cfFormat,"UPtr",mem)
DllCall("CloseClipboard")
return
}

; Nircmd
OperateOnMonitor(Status) ; Status should be on or off  ; The right method to use the function is OperateOnMonitor("off")
{
    OpMonitor := "nircmd monitor "
    Operate := OpMonitor . Status
    Run, %Operate% 

    Return
}


; InpoutProcess
InputProcess(ByRef OriStr, IniFile) ; Set default parameter
{
	Loop
	{
		if(A_Index = 1)
		{
			FileReadLine, INI_INFO, %IniFile%, 1
			IniInfoArray := StrSplit(INI_INFO, "|")
			Delimiters := IniInfoArray[1]
			NullMark := IniInfoArray[2]
			continue
		}
		
		FileReadLine, line, %IniFile%, %A_Index%
		if ErrorLevel
			break
		
;		MsgBox Delimiters=%Delimiters%
		word_array := StrSplit(line, Delimiters)
		MyRegEx := "i)"word_array[1]               ; Add the case ignore automately
		RepRes := word_array[2]
		
		if(RepRes = NullMark) 
		{
			RepRes := ""
		}
		
		StringReplace, OriStr, OriStr, ``r``n, `r`n, All
		
		MsgBox %MyRegEx%----------%RepRes%
		if(MyRegEx = "i)``r``n")
		{
			OriStr := RegExReplace(OriStr, "`r`n", RepRes)
		}
		else
		{
			OriStr := RegExReplace(OriStr, MyRegEx, RepRes)
		}
		
	}	
	
	Return
}

; isDoublePress
isDoublePress(ms = 300) { ; Set default value here
	Return (A_ThisHotKey = A_PriorHotKey) && (A_TimeSincePriorHotkey <= ms)
}

; IsAWord
IsAWord(CheckString)
{
	FoundPos := RegExMatch(CheckString, "^\b[^\s]+\b$")
	Return % FoundPos = 1
}

;===================================================================================================================
;Turn to the Origin Pos of the string
;~ CntToHeadStr(OriString)
;~ {
	;~ length := StrLen(OriString)
	;~ Send, {left %length%}
	;~ Return
;~ }

;===================================================================================================================
;Jump to the Origin of the string
CntRepPos(OriString, Mark := "\barg\b")
{
	; Cnt the mark position
	FoundPos := RegExMatch(OriString, Mark)
	MoveCnt := FoundPos
	
	;Rep the mark
	OriString := RegExReplace(OriString, Mark, "*")
	
	;
	length := strlen(OriString)
	Send, %OriString%{left %length%}{right %MoveCnt%}
	
	Return 
}


;===================================================================================================================
;IsWord Do or do sth else, check clipboard
IsAWordDo(Operate = "")
{
	SendMode, Input
    res := IsAWord(Clipboard)
	RepWord := "T"
	
	if(res = 1)
	{
		RepWord := Clipboard 
	}
	
	Operate := RegExReplace(Operate, "{X}", RepWord)
	
	CntRepPos(Operate)
	
	Return
}


; Clear the Class of the progrma of in the title.
RemoveTheProgramInTitle(ByRef SrcStr)
{
	SrcStr := RegExReplace(SrcStr, "(?<=[^\s]) - .*", "")
	Return
}


;===================================================================================================================
;Window Active
WindowActive(RegExMatchTitle, WindowClass, ExePath)
{
	SetTitleMatchMode, RegEx
	DetectHiddenWindows, on
	if(WindowClass = "")
	{
		FullTitle := RegExMatchTitle
	}
	else 
	{
		FullTitle := RegExMatchTitle . " ahk_class " . WindowClass
	}


	IfWinNotExist, %FullTitle% ;  ahk_class Clover_WidgetWin_0
	{
		run %ExePath%
		Sleep, 500
		;~ MsgBox 3
	}
	Else
	{
		IfWinActive, %FullTitle%
		{
			;~ MsgBox 1
			WinMinimize, A
			Return
		}
		else
		{
			;~ MsgBox %FullTitle%
			WinActivate, %FullTitle%
			
			CoordMode, mouse, Screen
			WinGetPos, X, Y, w, h, A  ; "A" to get the active window's pos.
			
			X := X + (w / 2)
			Y := Y + (h / 2)
			;~ MouseMove, X, Y
			
			Return
		}
		Return 
	}

}

;===================================================================================================================
;Run certain file for a while
RunFileForAWhile(FileFullPath, WindowName, HoldTime := 10000)
{
	Run, %FileFullPath%
	SetTimer, gTimeOut_CloseProcess, %HoldTime%
	Return
	
	gTimeOut_CloseProcess:
	{
		;~ MsgBox FileFullPath=%FileFullPath%
		;~ MsgBox WindowName=%WindowName%
		SplitPath, FileFullPath, name, dir, ext, name_no_ext, drive 
		
		;~ WinTitle := name . ".*" . WindowName
		WinTitle := "- Windows 照片查看器"
		;~ MsgBox WinTitle=%WinTitle%
		SetTitleMatchMode, regex
		WinClose, %WinTitle%
		SetTimer, gTimeOut_CloseProcess, Delete
		Return
	}
}

;===================================================================================================================
;Open Visual Studio Cmd window 
OpenVsCmdWindow()
{
	Send, !z
	Return
}

;===================================================================================================================
;Open Execuate Visual Studio CmdLine Commmand
ExeVSCmd(RegExTitle, Cmd)
{
	SetTitleMatchMode, Regex
	WinRegTitle := RegExTitle . ".*" . "Microsoft Visual Studio"
    Sleep, 1000 
	WinActivate, %WinRegTitle%
	WinWaitActive, %WinRegTitle%, , 2
	OpenVsCmdWindow()
	Sleep, 1000 
	Send, %Cmd%{Enter}
	Return
}

;===================================================================================================================
;Upper the drive name of the FullPath
UpperDriverName(FullPath)
{
	FoundPos := RegExMatch(FullPath, "[a-z]:", LowerDriver)
	StringUpper, UpperDriver, LowerDriver
	FullPath := RegExReplace(FullPath, "[a-z]:", UpperDriver)
	Return 
}

;===================================================================================================================
;Upper string
MyStringUpper(ByRef lowerstr)
{
    StringUpper, lowerstr, lowerstr
    Return
}

;===================================================================================================================
;WaitForPicShow
WaitForPicShow(PicPath, ClickTimeWant := 1)
{
    ClickTime := 0
    Loop
    {
        errorcode := FindClick(PicPath, "n") 
        if(errorcode <> 0)
        {
			FindClick(PicPath, "e") 
            ClickTime++ 
        }
        
		If ((ClickTime <> 0) And (ClickTime = ClickTimeWant))
        {
            Return
        }
		
		Sleep, 500
    }
	
	Return
}

;===================================================================================================================
;Save ClipBoard For 10 sec
SaveClipBoardForCertainTime()
{
	global g_ClipSaved := ClipboardAll   ; Save the entire clipboard to a variable of your choice.
	SetTimer, gReturnValue, 5000 ;10000
	return
	
	gReturnValue:
	{
		Clipboard := g_ClipSaved   ; Restore the original clipboard. Note the use of Clipboard (not ClipboardAll).
		ClipSaved =   ; Free the memory in case the clipboard was very large.
		SetTimer, gReturnValue, Off ;10000
		Return
	}
	
}


;===================================================================================================================
;Timer with func which can pass para
SetTimerEx(period, func, params*)
{
    static s_timers, s_next_tick, s_timer, s_index, s_max_index
 
    if !s_timers  ; Init timers array and ensure script is #persistent.
        s_timers := Object(), n:="OnMessage",%n%(0)
 
    if (func = "!") ; Internal use.
    {
        ; This is a workaround for the timer-tick sub not being able to see itself
        ; in v2 (since it is local to the function, which is not running).
        SetTimer timer-tick, % period
        return
    }
 
    if !IsFunc(func)
        return
 
    ; Create a timer.
    timer           := {base: {stop: "Timer_Stop"}}
    timer.run_once  := period < 0
    timer.period    := period := Abs(period)
    timer.next_run  := next_run := A_TickCount + period
    timer.func      := func
    timer.params    := params
 
    ; If the timer is not set to run before next_run, set it:
    if (!s_next_tick || s_next_tick > next_run)
    {
        s_next_tick := next_run
        SetTimer timer-tick, % -period
    }
 
    return s_timers.Insert(timer) ? timer : 0
 
timer-tick:
    s_next_tick := "X" ; greater than any number
    s_index := 1
    While s_timer := s_timers[s_index]
    {
        if (s_timer.next_run <= A_TickCount)
        {
            if s_timer.next_run  ; Timer has not been disabled.
            {
                ; Update next run time before calling func in case it takes a while.
                s_timer.next_run := s_timer.run_once ? "" : A_TickCount + s_timer.period
                ; Call function.
                static s_f
                s_f := s_timer.func, %s_f%(s_timer.params*)
            }
            if !s_timer.next_run  ; Timer was run-once (disabled above) or previously disabled.
            {
                ; Remove both our references to this timer:
                s_timers._Remove(s_index)
                s_timer := ""
                ; Continue without incrementing s_index.
                continue
            }
        }
        ; Determine when the next timer should fire.
        if (s_next_tick > s_timer.next_run)
            s_next_tick := s_timer.next_run
        s_index += 1
    }
    s_timer := ""
    ; Set main timer for next sub-timer which should be fired, if any.
    if (s_next_tick != "X")
        SetTimerEx(s_next_tick > A_TickCount ? A_TickCount-s_next_tick : -1, "!")
    return
}
 
Timer_Stop(timer) {
    timer.next_run := 0
}


;===================================================================================================================
;Save Clipboard as a file
SaveClipBoardPic(WorkScreenShot_Pic)
{
	ClipSaved := ClipboardAll
	QuotedString(WorkScreenShot_Pic)
	
	Send, {PrintScreen}
	ClipWait, 2
	;~ WorkScreenShot_Pic := """" . A_WorkingDir . "\WorkRecord\WorkScreenShot\" . A_MM . "-" .  A_DD  . "_" .  A_Hour  . "_" . A_Min .  ".png" . """"
	nircmd_cmd:="nircmd.exe" . " clipboard saveimage " . WorkScreenShot_Pic ; 这里把clipboard里面的png保存了一下。
	RunWait,%nircmd_cmd%
	Clipboard := ClipSaved
	Return 
}

;===================================================================================================================
;Quoted the String
QuotedString(ByRef UnquotedString)
{
	FoundPos := RegExMatch(UnquotedString, "^""")
	;~ MsgBox FoundPos=%FoundPos%
	if(FoundPos = 0)
	{
		UnquotedString := """" . UnquotedString . """"		
		Return
	}
	
	Return
}

;===================================================================================================================
;Move the window

LeftHalfWindow(Wintitle := "A")
{
	SysGet, area, MonitorWorkArea
	w:=((areaRight-areaLeft)/2)
	h:=(areaBottom-areaTop)

	WinRestore, %Wintitle%
	WinMove, %Wintitle%, , 0, 0,%w%,%h%
	Return 
}

RightHalfWindow(Wintitle := "A")
{
	SysGet, area, MonitorWorkArea
	w:=((areaRight-areaLeft)/2)
	h:=(areaBottom-areaTop)

	WinRestore, %Wintitle%
	WinMove, %Wintitle%, , w, 0, w, h	;Middle of screen is same as w.
	Return 
}

TopHalfWindow(Wintitle := "A")
{
	SysGet, area, MonitorWorkArea
	w:=(areaRight-areaLeft)
	h:=((areaBottom-areaTop)/2)

	WinRestore, %Wintitle%
	WinMove, %Wintitle%, , 0, 0, w, h
	Return 
}

BottomHalfWindow(Wintitle := "A")
{
	SysGet, area, MonitorWorkArea
	w:=(areaRight-areaLeft)
	h:=((areaBottom-areaTop)/2)

	WinRestore, %Wintitle%
	WinMove, %Wintitle%, , 0, h, w, h	;Middle of screen is same as h.
	Return 
}

TopRightWindow(Wintitle := "A")
{
	SysGet, area, MonitorWorkArea
	w:=((areaRight-areaLeft)/2)
	h:=(areaBottom-areaTop)
	h:=h/2

	WinRestore, %Wintitle%
	;~ MsgBox w=%w%, h=%h%
	WinMove, %Wintitle%, , w, 0, w, h	;Middle of screen is same as w
	Return 
}

;===================================================================================================================
;SplitScreenWithTop2Window
SplitScreenWithTop2Window()
{
	;~ WinGet, id, list
	;~ FirstWindowGetMark := 0
	;~ LeftWindowTitle := ""
	;~ RightWindowTitle := ""
	;~ IniRead, SplitWinListVar, InitFile.ini, SplitWindowList, SplitWindow
	;~ Loop, %id%
	;~ {
		;~ this_id := id%A_Index%
		;~ WinGetTitle, this_title, ahk_id %this_id%
		
		;~ Pos := RegExMatch(this_title, SplitWinListVar)
		;~ if((Pos <> 0) and (FirstWindowGetMark = 0))
		;~ {
			;~ LeftWindowTitle := this_title
			;~ FirstWindowGetMark := 1
			;~ continue
		;~ }
		
		;~ if((Pos <> 0) and (FirstWindowGetMark = 1))
		;~ {
			;~ RightWindowTitle := this_title
			;~ break
		;~ }
	;~ }

	RightHalfWindow()
	
	Sleep, 100
	Send, !{tab}
	Sleep, 100
	
	LeftHalfWindow()

	Return 
}

;===================================================================================================================
;Send mail to gmail
SendMail(EmailTo, MailContent)
{
	NameSpace := "http://schemas.microsoft.com/cdo/configuration/"
    Email := ComObjCreate("CDO.Message")
    Email.From := "513278236@qq.com"
    ;Email.To := "513278236@kindle.cn"
    ;~ Email.To := "513278236@qq.com"
    ;~ Email.To := "imlegendlzz@gmail.com"
	Email.To := EmailTo
    Email.Subject := "Greeting Geek"
    Email.Htmlbody := MailContent
    ;FullFilePath := "C:\temp.txt"

    ;~ Email.AddAttachment(FullFilePath)
    Email.Configuration.Fields.Item(NameSpace "sendusing") := 2
    Email.Configuration.Fields.Item(NameSpace "smtpserver") := "smtp.qq.com" ;SMTP服务器地址
    Email.Configuration.Fields.Item(NameSpace "smtpserverport") := 25
    Email.Configuration.Fields.Item(NameSpace "smtpauthenticate") := 1
    Email.Configuration.Fields.Item(NameSpace "sendusername") := "513278236@qq.com" ;邮箱账号
    Email.Configuration.Fields.Item(NameSpace "sendpassword") := "woshichuanqilz72" ;邮箱密码
    Email.Configuration.Fields.update
    Email.send
    

    MsgBox, 0, , Send Success, 1 ; 3 is the count down time
    Return
}

;===================================================================================================================
;Search in the youdao dic
TranslateCurrentWordByYDDic()
{
	;~ g_ThreadCnt++
	
	Send, ^c
	Send, +!w
	WinWaitActive, 有道词典 ahk_class YodaoMainWndClass
	WinMove, 有道词典 ahk_class YodaoMainWndClass, ,0, 0
	Send, ^v
	Sleep, 100
	Send, {Enter}
	;~ Sleep, 10000
	
	;~ Sleep, 5000
	;~ if(g_ThreadCnt = 2)
	;~ {
		;~ g_ThreadCnt--
		;~ Exit
	;~ }
	
	;~ Send, +!w
	;~ WinMinimize, 有道词典 ahk_class YodaoMainWndClass
	Return
}

;===================================================================================================================
;Add BackSlash
PathAddBackSlash(ByRef FilePath)
{
	;~ MsgBox 22FilePath=%FilePath%
	FoundPos := RegExMatch(FilePath, ".*\\$")
	if(FoundPos = 0)
	{
		;~ MsgBox 33FilePath=%FilePath%
		FilePath := FilePath . "\"
	}
	;~ MsgBox 11FilePath=%FilePath%

	Return
}


;===================================================================================================================
;Get Explorer Path
GetExplorerPathCrossSystem()
{
	ControlGetText, FilePath_Win10, ToolbarWindow323, A
    stringreplace, FilePath_Win10, FilePath_Win10, 地址:%A_space%, , All
	;~ MsgBox FilePath_Win10=%FilePath_Win10%
	
	ControlGetText, FilePath_XP, ToolbarWindow322, A
    stringreplace, FilePath_XP, FilePath_XP, 地址:%A_space%, , All
	;~ MsgBox FilePath_XP=%FilePath_XP%
	
	IfExist, %FilePath_Win10%
	{
		;~ MsgBox 222
		FilePath := FilePath_Win10
	}
	IfExist, %FilePath_XP%
	{
		FilePath := FilePath_XP
	}
	
	if(FilePath = "")
	{
		Return "*InvalidPath*"
	}
	
    PathAddBackSlash(FilePath)
	;~ MsgBox FilePath=%FilePath%
	Return FilePath
}

;===================================================================================================================
;Hide Ext
ToggleHideExt()
{
	RegRead, HiddenFiles_Status, HKEY_CURRENT_USER, Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced, HideFileExt
	If HiddenFiles_Status = 1 
	RegWrite, REG_DWORD, HKEY_CURRENT_USER, Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced, HideFileExt, 0
	Else 
	RegWrite, REG_DWORD, HKEY_CURRENT_USER, Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced, HideFileExt, 1
	Sleep, 500 
	send, {F5}
	
	Return
}

;===================================================================================================================
;Rename a file
;~ FileMove, C:\Users\Administrator\Desktop\abc.txt, C:\Users\Administrator\Desktop\hijk.sql



;===================================================================================================================
;Label separate. WTF, I failed , label can't be used in the headfile.

/*
gTimeOut_CloseProcess:
{
	SetTitleMatchMode, regex
	WinClose, 10.png - Windows 照片查看器
	SetTimer, gTimeOut_CloseProcess, Delete
	Return
}
*/

;===================================================================================================================
;CopyLink, easy key combine
CopyLink()
{
	Send, ^l
	Send, ^c
	Return
}

PasteLink()
{
	Send, ^l
	Send, ^v
	Send, {enter}
	Return
}


/*
 *
 *		Dictionary Function, AKA Associative Array or Associative Memory.
 *		Data Structure: DictName = key1:value1|key2:value2|key3:value3...
 */
;*******FUNCTION********************
;Example:
;~ dictName = Ben:11|Ellie:9|Ian:6|Will:1


;~ MsgBox % Dict(dictName,"Ben")
;~ MsgBox % Dict(dictName,"Ellie")
;~ MsgBox % Dict(dictName,"Ian") 
;~ MsgBox % Dict(dictName,"Will")

Dict(dictName,key) {
	keyPos := InStr(dictName,key)
	dictStr2 := SubStr(dictName,keyPos)
	IfInString , dictStr2 , | 
	{
		endPos := InStr(dictStr2, "|")
	}else{
		endPos := StrLen(dictStr2)+1
	}
	startPos := StrLen(key)+2
	returnValue := SubStr(dictStr2,startPos,(endPos-startPos))
    return returnValue
}

QuoteAWord(ByRef Word) ; Quotation
{
	Word := RegExReplace(Word, "^", """")
	Word := RegExReplace(Word, "$", """")
	;~ Word := """" . Word . """"
	Return
}

;===================================================================================================================
;Start process
StartProcess(FullFileName)
{
	SplitPath, FullFileName, name, dir, ext, name_no_ext, drive 
	Process, Exist, %name% ; check to see if AutoHotkey.exe is running
	{
	If ! errorLevel
		{
		IfExist, %FullFileName%
			Run, %FullFileName%
		Return
		}
	else
		{
		Return
		}
	}
	
	Return
}

;===================================================================================================================
;No responding just for test
CheckRespoding(WindowID)
{
	;~ MsgBox WindowID=%WindowID%
	NR_temp =0 ; init
	TimeOut = 100 ; milliseconds to wait before deciding it is not responding - 100 ms seems reliable under 100% usage
	; WM_NULL =0x0000
	; SMTO_ABORTIFHUNG =0x0002
	;~ WinGet, wid, ID, 计算器 ; retrieve the ID of a window to check
	Responding := DllCall("SendMessageTimeout", "UInt", WindowID, "UInt", 0x0000, "Int", 0, "Int", 0, "UInt", 0x0002, "UInt", TimeOut, "UInt *", NR_temp)
	If Responding = 1 ; 1= responding, 0 = Not Responding
	  return "Responding"
	Else
	  return "Not Responding"
}

;===================================================================================================================
;Send AltTab
SendAltTab()
{
	Send {Alt Down}{Tab}
    Sleep 100
    Send {Alt Up}
	Return
}

;===================================================================================================================
;Get the first para 
; NOTICE can't be used in the lib I don't know why
GetInputPara(ByRef Para)
{
	Loop, %0%  ; For each parameter:
	{
		Para := %A_Index%  ; Fetch the contents of the variable whose name is contained in A_Index.
		break
	}
	
	Return
}


;===================================================================================================================
;RunCurrentExefile
RunCurrentExefile()
{
	Path := GetScriptPathByTitleInScite()
	Run, % RegExReplace(heh, ".ahk$", ".exe")
	Return
}


;======================================================================================== ===========================
;Open Current path in Console
OpenCPInConsole()
{
	PathNow := GetScriptPathByTitle()
	;~ MsgBox PathNow=%PathNow%
	;~ Clipboard := PathNow
	QuoteAWord(PathNow)
	;~ MsgBox PathNow=%PathNow%
	Sleep, 500
	;~ MsgBox PathNow=%PathNow%
	Run, cmder /start %PathNow%
	Return
}

;===================================================================================================================
;Current Time
GetTimeNow()
{
	;~ Return CurrentTime := A_Mon . "~" . A_DD . "_" . A_Hour . "-" . A_Min . "-" . A_Sec
	Return CurrentTime := A_Mon . A_DD . A_Hour .  A_Min . A_Sec
}

;===================================================================================================================
;Resize active window
ResizeActiveWindow()
{
	WinGet, WinStatus , MinMax, A
	;~ ToolTip WinStatus=%WinStatus%
	if(WinStatus = 0) 
		WinMaximize, A
	if(WinStatus = 1) 
		WinRestore, A
	Return
}


;===================================================================================================================
;toggle capslock
ToggleCapslock()
{
    if GetKeyState("CapsLock", "T") = 1
     {
       SetCapsLockState, off
     }
    else if GetKeyState("CapsLock", "F") = 0
     {
       SetCapsLockState, on
     }
	 
	Return
}

;===================================================================================================================
; In means 多久之后显示 out means 多久之后消失 
/* 

 Function:  ShowTooltip 

            Show the tooltip and automatically dismiss it. 



 Parameters: 

            Text       - Text to show. If omitted or empty, any existing tooltip will be hidden. 

            X,Y      - Coordinates on which to show tooltip. Affected by CoordMode. Optional. 

            In, Out  - Time in milliseconds for tooltip to show and to disappear. 

                     - If TimeOut is 0, tooltip will never be dismissed. Optional. 

            bControl - Set to TRUE to associate the tooltip with control currently under the mouse. 

                     - That means that Tooltip will not be shown if control has changed. By default, false 

            Nr          - Tooltip number, by default 19. Multiple tooltips can exist with different settings. 



 About: 

            o v2.0 by HotKeyIt 

 */ 

ShowToolTip(Text="", X="",Y="", In=500, Out=1500, bControl=0, Nr=19){ 

   static 

   If (Text=""){ 

      MouseGetPos,,,_win,_ctrl 

      ControlGet,hCtrl,HWND,,%_ctrl%,ahk_id %_win% 

      If ((T_Text%Nr% && !T_%Nr% && T_In%Nr%<A_TickCount && (!T_Ctrl%Nr% or (T_Ctrl%Nr% && hCtrl=T_Ctrl%Nr%))) || (T_%Nr% && T_Out%Nr%<A_TickCount && !((T_Text%Nr%:="") . (T_X%Nr%:="") . (T_Y%Nr%:="") . (T_In%Nr%:="") . (T_Out%Nr%:="") . (T_%Nr%:="") . (T_Ctrl%Nr%:="")))) 

         ToolTip % T_Text%Nr%,% T_X%Nr%,% T_Y%Nr%,% Nr+(T_Text%Nr% ? ((T_%Nr%:=1)-1) : 0) 

      Return (!T_%Nr% ? T_In%Nr% : (T_Out%Nr%>A_TickCount ? T_Out%Nr% : "")) 

   } else if (bControl=1){ 

      MouseGetPos,,,_win,_ctrl 

      ControlGet,T_Ctrl%Nr%,HWND,,%_ctrl%,ahk_id %_win% 

   } else T_Ctrl%Nr%:=0 

   T_Text%Nr%:=text,T_X%Nr%:= X,T_Y%Nr%:= Y,T_In%Nr%:=Round(A_TickCount+In),T_Out%Nr%:=(Out ? Round(A_TickCount+In+Out) : 9223372036854775807) 

   ShowToolTip: 

      NextTimer= 

      Loop 20 

         If (ErrorLevel:=ShowToolTip("","","","","","",A_Index)) 

            If (!NextTimer || NextTimer+A_TickCount>ErrorLevel) 

               NextTimer:=(ErrorLevel-A_TickCount<0) ? "" : (ErrorLevel-A_TickCount+10) 

      SetTimer, ShowToolTip,% NextTimer ? (-1*(NextTimer+10)) : "Off" 

   Return 

}


;===================================================================================================================
;Close and shutdown the monitor
CloseAndShutdownMonitor()
{
    Sleep, 200

    DllCall("LockWorkStation")

    Sleep, 200

    SendMessage,0x112,0xF170,2,,Program Manager

    Return 
}

;===================================================================================================================
;Count of folder
CountOfFolder()
{
	countoffolder = 0
	Loop, .\captureimg\*.*
	{
		countoffolder := A_Index
	}
	Return
}
;===================================================================================================================
;Is desktop now
IsDesktop()
{
	MouseGetPos,,,win
	WinGetClass, class, ahk_id %win%
	If class in Progman,WorkerW
		return 1
	else
		return 0
	Return
}

;===================================================================================================================
;Wrap the special key
WrapKey(ByRef Key)
{
	if (StrLen(Key) > 1)
	{
		Key := "`{" . Key . "`}"
	}

	return 
}


;===================================================================================================================
;Send key timely
SendKeyTimely(Key, TimeInterval, FirstTrigger, Start = 1)
{
	if (StrLen(Key) > 1)
	{
		Key := "`{" . Key . "`}"
	}
	
	if (Start = 1)
	{
		if (FirstTrigger = 1)
		{
			Send, %Key%
		}
        SetTimerEx(TimeInterval, "SendKey", Key)
	}
	else
	{
		Timer_Stop(SendKey)
	}
    
    Return 
}

;===================================================================================================================
;SendKey
SendKey(Key)
{
    Send, %Key%
	return
}

;===================================================================================================================
;KeepKeyDown

KeepKeyDown(key)
{
    WrapKey(key)
    Send, {%key% down}
    SetTimerEx(500, "LabelKeepDown", key)
	
	Return 
}

LabelKeepDown(key)
{
    GetKeyState, KeyState, %key%  ; Right mouse button.
    if (KeyState = "U")
    {
        Send, {%key% down}
    }
    ToolTip,  KeyState=%KeyState%
    Return
}


;===================================================================================================================
;ToolTipEX()
ToolTipEX(text, x = 0, y = 0, elasptime = 3)
{
	
	
	elasptime := elasptime * 1000 ; Get the real time
	;~ MsgBox %text% , %x% , %y%, %elasptime%
	
	if (x = 0)
	{
		ToolTip, %text%
	}
	else
	{
		ToolTip, %text%, %x%, %y% 
	}
	
	SetTimer, CloseTip, %elasptime% 
	SetTimerEx(elasptime, "CloseTip", "")
	
	Return 
}

CloseTip()
{
	ToolTip
	Return
}
;===================================================================================================================
;~ ;
;~ Close:
;~ {
	
	;~ Return
;~ }

;===================================================================================================================
;CalCB
;~ CalcCB(Expr)
;~ {
	;~ ExprInit()
	;~ CalRes := ExprEval(ExprCompile(Expr))
	;~ Clipboard := CalRes
;~ }

; Next Window
NextWindowSameClass(WindowClass)
{
	;~ WinGetClass, CurrentActive, A
	WinGet, Instances, Count, ahk_class %WindowClass%
	If Instances > 1
		WinSet, Bottom,, A
	WinActivate, ahk_class %WindowClass%
	return
}

; Previous Window
PreviousWindowsSameClass(WindowClass)
{
	;~ WinGetClass, CurrentActive, A
	WinGet, Instances, Count, ahk_class %WindowClass%
	If Instances > 1
		WinActivateBottom, ahk_class %WindowClass%
	return
} 

; 
GetCurrentTime(ByRef time)
{
	FormatTime, time,, MM/dd/yy hh:mm tt 
	;~ Send  Ticket Assigned To%A_Space% - TTA %Time%{left 24}
	Return
}

;===================================================================================================================
; tell you a story
TellYouAStory(story := "Hello world")
{
    Loop, parse, story, %A_Space%
    {
        Random, num , 1, 3
        sltime :=  num * 1000
        delaytime := num * 300
        Sleep, %sltime%
        ;~ MsgBox, Color number %A_Index% is %A_LoopField%.
        SetKeyDelay,  %delaytime%
        Send, %A_LoopField%
        Send, %A_Space%
    }
	
	Return 
}

;===================================================================================================================
; Tell you a story in CHN

TellYouAChnStory(story := "Hello world", talktime := 1)
{
	SetDefaultKeyboard(0x0804) ; CHN (USA)
	SetKeyDelay, 500
	
	talktime := talktime * 200
	
	Loop, parse, story, %A_Space%
    {
        Random, num , 1, 3
        sltime :=  num * talktime
        delaytime := num * 200
        Sleep, %sltime%
        ;~ MsgBox, Color number %A_Index% is %A_LoopField%.
        SetKeyDelay,  %delaytime%
        Send, %A_LoopField%
        Send, %A_Space%
    }
	Return 
}



;===================================================================================================================
; 
; Win 10
;~ SetDefaultKeyboard(0x0409) ; English (USA)
;~ Sleep, 5000
;~ SetDefaultKeyboard(0x0804) ; CHN (sougou)

SetDefaultKeyboard(Lan := "E"){
	Global
	SPI_SETDEFAULTINPUTLANG := 0x005A
	SPIF_SENDWININICHANGE := 2
 
	;~ if(Lan := "C")
	if(Lan == "C")
	{
		LocaleID := 0x0804
	}
	else
	{
		LocaleID := 0x0409
	}
	
	;~ MsgBox LocaleID=%LocaleID%
	
	Lan := DllCall("LoadKeyboardLayout", "Str", Format("{:08x}", LocaleID), "Int", 0)
	VarSetCapacity(Lan%LocaleID%, 4, 0)
	NumPut(LocaleID, Lan%LocaleID%)
	DllCall("SystemParametersInfo", "UInt", SPI_SETDEFAULTINPUTLANG, "UInt", 0, "UPtr", &Lan%LocaleID%, "UInt", SPIF_SENDWININICHANGE)
 
	WinGet, windows, List
	Loop %windows% {
		PostMessage 0x50, 0, %Lan%, , % "ahk_id " windows%A_Index%
	}
}

PlayMusic(music)
{
	run, %music%
	WinGetActiveTitle, title
	Sleep, 2000
	WinMinimize, %title%
}


;===================================================================================================================
;Call Altrun
AltRun(cmd)
{
	send, !w
	Sleep, 500
	SetKeyDelay, 500
	Send, %cmd%	
	send, {enter}
}


;===================================================================================================================
;

/*
HASH types:
1 - MD2
2 - MD5
3 - SHA
4 - SHA256 - not supported on XP,2000
5 - SHA384 - not supported on XP,2000
6 - SHA512 - not supported on XP,2000
*/
HashFile(filePath,hashType=2)
{
	PROV_RSA_AES := 24
	CRYPT_VERIFYCONTEXT := 0xF0000000
	BUFF_SIZE := 1024 * 1024 ; 1 MB
	HP_HASHVAL := 0x0002
	HP_HASHSIZE := 0x0004
	
	HASH_ALG := hashType = 1 ? (CALG_MD2 := 32769) : HASH_ALG
	HASH_ALG := hashType = 2 ? (CALG_MD5 := 32771) : HASH_ALG
	HASH_ALG := hashType = 3 ? (CALG_SHA := 32772) : HASH_ALG
	HASH_ALG := hashType = 4 ? (CALG_SHA_256 := 32780) : HASH_ALG	;Vista+ only
	HASH_ALG := hashType = 5 ? (CALG_SHA_384 := 32781) : HASH_ALG	;Vista+ only
	HASH_ALG := hashType = 6 ? (CALG_SHA_512 := 32782) : HASH_ALG	;Vista+ only
	
	f := FileOpen(filePath,"r","CP0")
	if !IsObject(f)
		return 0
	if !hModule := DllCall( "GetModuleHandleW", "str", "Advapi32.dll", "Ptr" )
		hModule := DllCall( "LoadLibraryW", "str", "Advapi32.dll", "Ptr" )
	if !dllCall("Advapi32\CryptAcquireContextW"
				,"Ptr*",hCryptProv
				,"Uint",0
				,"Uint",0
				,"Uint",PROV_RSA_AES
				,"UInt",CRYPT_VERIFYCONTEXT )
		Goto,FreeHandles
	
	if !dllCall("Advapi32\CryptCreateHash"
				,"Ptr",hCryptProv
				,"Uint",HASH_ALG
				,"Uint",0
				,"Uint",0
				,"Ptr*",hHash )
		Goto,FreeHandles
	
	VarSetCapacity(read_buf,BUFF_SIZE,0)
	
    hCryptHashData := DllCall("GetProcAddress", "Ptr", hModule, "AStr", "CryptHashData", "Ptr")
	While (cbCount := f.RawRead(read_buf, BUFF_SIZE))
	{
		if (cbCount = 0)
			break
		
		if !dllCall(hCryptHashData
					,"Ptr",hHash
					,"Ptr",&read_buf
					,"Uint",cbCount
					,"Uint",0 )
			Goto,FreeHandles
	}
	
	if !dllCall("Advapi32\CryptGetHashParam"
				,"Ptr",hHash
				,"Uint",HP_HASHSIZE
				,"Uint*",HashLen
				,"Uint*",HashLenSize := 4
				,"UInt",0 ) 
		Goto,FreeHandles
		
	VarSetCapacity(pbHash,HashLen,0)
	if !dllCall("Advapi32\CryptGetHashParam"
				,"Ptr",hHash
				,"Uint",HP_HASHVAL
				,"Ptr",&pbHash
				,"Uint*",HashLen
				,"UInt",0 )
		Goto,FreeHandles	
	
	SetFormat,integer,Hex
	loop,%HashLen%
	{
		num := numget(pbHash,A_index-1,"UChar")
		hashval .= substr((num >> 4),0) . substr((num & 0xf),0)
	}
	SetFormat,integer,D
		
FreeHandles:
	f.Close()
	DllCall("FreeLibrary", "Ptr", hModule)
	dllCall("Advapi32\CryptDestroyHash","Ptr",hHash)
	dllCall("Advapi32\CryptReleaseContext","Ptr",hCryptProv,"UInt",0)
	return hashval
}

;===================================================================================================================
;
GetImageSize(ByRef width, ByRef height, ImagePath)
{
	gui,add,picture,hwndmypic,%ImagePath%
	controlgetpos,,,width,height,,ahk_id %mypic%
	;~ msgbox %width%  %height%
}


;===================================================================================================================
;Show Image
ShowImage(ImagePath, x, y)
{
	GetImageSize(width, height, ImagePath)

	;~ GUI, 1:+AlwaysOnTop -Border -SysMenu +Owner -Caption +ToolWindow
	;~ GUI, 1: Add, Picture, x0 y0 , %ImagePath%
	;~ GUI, 1:show, NoActivate X200 Y200 w%w% h%y%, dropDesk
	;~ MsgBox width=%width%
	
	;~ GUI, 1:+AlwaysOnTop -Border -SysMenu +Owner -Caption +ToolWindow
	GUI, 1: -Border -SysMenu -Caption +ToolWindow +Owner 
	GUI, 1: Add, Picture, x0 y0 w%width% h%height%, %ImagePath%
	Gui, 1: Add, Button, x218 y87, 开始运行
	GUI, 1:show, NoActivate x%x% y%y% w%width% h%height%, dropDesk
	Return 
}


;===================================================================================================================
;Get file modified time
GetFileModTime(filepath)
{
FileGetTime, TimeString, %filepath%
FormatTime, TimeRes, %TimeString%, dd

Return TimeRes
}

;===================================================================================================================
;Time Lock
TimeLock(filename)
{
	;~ MsgBox %A_DD%
	;~ MsgBox % GetFileModTime(filename)
	if (A_DD <> GetFileModTime(filename))
	{
		MsgBox Free Trial Period Expired
		ExitApp
	}
}


;===================================================================================================================
;Loop the folder recursive
; Get All the folder
GetFolderList(Folder := ".")
{
	;~ #SingleInstance, Force
	;~ FileSelectFolder, Folder
	;~ IfEqual,Folder,, IfNotEqual,ErrorLevel,0, Return
	Folder := "."
	FolderList := ""
	Loop, %Folder%\*.*,2,1
	{
	  SubFolders := False, fPath := A_LoopFileLongPath
	  Loop, %fPath%\*.*,2,0
	   {
		 SubFolders := True
		 Break
	   }
	  If ! SubFolders
		   FolderList .= fPath "`n"
		   
	;~ Operation should be added here.
    ;~ FoundPos := RegExMatch(fPath, "test")
    ;~ if(FoundPos <> 0)
    ;~ {
        FileDelete, %fPath%
        ;~ MsgBox %A_LoopFileLongPath%
    ;~ }
	}
	MsgBox,% FolderList
	
	Return 
}


;===================================================================================================================
;
GetFileList()
{
	Loop, *.* ,1,1
	{
		;~ MsgBox %A_LoopFileLongPath%
		FoundPos := RegExMatch(A_LoopFileLongPath, "justfortest")
		if(FoundPos <> 0)
		{
			;~ FileDelete, %fPath%
			MsgBox %A_LoopFileLongPath%
		}
		;~ FolderList .= fPath "`n"
	}

	Return 
}


;===================================================================================================================
;Log Function
MyLog(msg, ScriptName := "test", DeleteOriginFile := 0)
{
	
	if(DeleteOriginFile = 1)
	{
		FileDelete, %logfile%
	}
	
	logfile := ScriptName . ".log"
	FileAppend, %msg%`n, %logfile%
	
	Return 
}


;===================================================================================================================
;DateDiff
DateDiff(EDate, EDueDate)
{
	;~ EDate   = 20061218125619
	;~ EDueDate= 20061219152619
	EnvSub EDate, EDueDate, D

	Return 
}


;===================================================================================================================
;Get the GetProcessPath 
;~ Msgbox % GetProcessPath( "Autohotkey.exe" )
GetProcessPath(exe) {
	for process in ComObjGet("winmgmts:").ExecQuery("Select * from Win32_Process where name ='" exe "'")
		return process.ExecutablePath
}


;===================================================================================================================
; Process Manager can't be 
TaskManager()
{
	strComputer := "."
	objWMIService := ComObjGet("winmgmts:\\" . strComputer . "\root\cimv2")
	colProcesses := objWMIService.ExecQuery("Select * From Win32_Process")._NewEnum

	Gui, Add, ListView, x2 y0 w400 h500 vMyLV,Process Name|WorkingSetSize|Priority|ThreadCount
	GuiControl, -Redraw, MyLV 

	While colProcesses[objProcess]
		LV_Add("",objProcess.Name , objProcess.WorkingSetSize , objProcess.Priority , objProcess.ThreadCount)

	GuiControl, +Redraw, MyLV 
	LV_ModifyCol(1,160)
	Gui, Show, w400 h500, Process List
	Return

	GuiClose:
	ExitApp
	
	Return 
}


; get selected file fullpath
GetFullPathofSelectedFile()
{
Sleep, 5000
SetKeyDelay, 100
; Get name
Send, {f2}
Send, ^a
Send, ^c
Send, {esc}
filename := Clipboard

; Get the path
Send, {AppsKey}
;~ Sleep, 300
Send, r
WinWaitActive,  属性
ControlGetText, path, Edit4,  属性
WinClose, A

; Concat the string
fullpath := path . "\" .  filename
;~ MsgBox 1
fullpath := RegExReplace(fullpath, "\\\\", "\")
Clipboard := fullpath
;~ MsgBox fullpath=%fullpath%
Return fullpath
}

;Rerun
RerunTheScript()
{
		WinGetActiveTitle var_title
		; 终止
		pathname := GetScriptPathByTitle()
		fullname := GetScriptPathByTitle(0)
		filename := GetScriptPathByTitle(2)
		filenamesuffix = %filename%.ahk
		;~ MsgBox filename=%filename%
		;~ MsgBox filenamesuffix=%filenamesuffix%
		Process, Close, %filename%.exe

		Process, Close, AutoHotkeyU64.exe

		cmdline = .\CommonCmd\compileAHK.bat
		cmdline := cmdline . A_Space . """" . fullname . """"
		;~ MsgBox cmdline=%cmdline%
		Clipboard := cmdline
		exefile = %pathname%\%filename%.exe

		RunWait, %cmdline%

		;~ Sleep 4000
		;~ MsgBox, 0, , , 3
		;~ MsgBox exefile=%exefile%
		Run %exefile%

		MsgBox, 0, , 重启%filename%成功, 1
		Return 
}

