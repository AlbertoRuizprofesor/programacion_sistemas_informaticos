# SOLUCIÓN 10
"--- UP ---"; Get-NetAdapter | Where-Object Status -eq Up
"--- DOWN ---"; Get-NetAdapter | Where-Object Status -eq Down
