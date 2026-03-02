Get-ChildItem -Path "C:\Users\2-DAW" -Recurse |
 Where-Object { $_.Length -gt 10MB }