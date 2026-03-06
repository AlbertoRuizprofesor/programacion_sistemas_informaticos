# SOLUCIÓN 23
Get-EventLog -LogName System -Newest 100 | Out-File .\system_100.txt -Encoding utf8
