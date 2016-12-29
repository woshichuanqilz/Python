import re
import subprocess

def MsgProcess(cmdString):
#Trim the Useless Word
    # cmdString = re.sub(r"[^a-zA-Z]+done.{0,1}$", "", cmdString)
# Send CMD
    # m = re.search(r"(send[^a-zA-Z]+)", cmdString, flags=re.IGNORECASE)
    m = re.search(r"(.*?(?=[ |,]))", cmdString, flags=re.IGNORECASE)
    if m is None:
        print 'M Is None'
        return
    else:
#Get The Command Type Of The Command 
        CmdChoice = m.group(1)
        CmdChoice = CmdChoice.lower()
#Clear the Command Choice 
        CmdContent = re.sub(r"^..*?\b\s*", "", cmdString)
#Clear the Over
        CmdContent = re.sub(r"[^a-zA-Z]over$", "", CmdContent, flags=re.IGNORECASE)

        p = subprocess.Popen([r"./CommandProcess/OrigamiProcess", CmdChoice, CmdContent])
        # if CmdChoice.lower() == "send":
            # # p = subprocess.Popen([r"OrigamiSend", CmdContent])
            # p = subprocess.Popen([r"./CommandProcess/OrigamiSend", CmdPara])
        # elif CmdChoice.lower() == "search":
            # p = subprocess.Popen([r"OrigamiSend", CmdContent])

# Test Command
# cmdString="search I love you over"
# MsgProcess(cmdString)
