Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "C:\name & path of your .bat file" & Chr(34), 0
Set WshShell = Nothing