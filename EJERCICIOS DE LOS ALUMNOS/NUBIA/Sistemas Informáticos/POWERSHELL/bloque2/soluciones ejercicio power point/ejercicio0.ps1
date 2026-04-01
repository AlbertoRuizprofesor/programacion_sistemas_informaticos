Get-ChildItem -Recurse | Where-Object { $_.Length -gt 0MB }
