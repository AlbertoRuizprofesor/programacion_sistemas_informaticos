Get-WinEvent -LogName System | Where-Object { $_.LevelDisplayName -eq 'Error' }


