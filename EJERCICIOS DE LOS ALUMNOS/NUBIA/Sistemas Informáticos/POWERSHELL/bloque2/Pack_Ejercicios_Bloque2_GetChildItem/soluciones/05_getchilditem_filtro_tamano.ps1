# SOLUCIÓN 5
Get-ChildItem C:\Users\Public -Recurse | Where-Object { $_.Length -gt 1MB }
