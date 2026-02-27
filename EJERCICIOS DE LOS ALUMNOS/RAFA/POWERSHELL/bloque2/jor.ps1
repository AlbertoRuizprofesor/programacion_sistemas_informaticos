Get-Process | Where-Object { $_.CPU -gt 100 }
Start-Process calc.exe
Get-Process calc
#Stop-Process -Name notepad

