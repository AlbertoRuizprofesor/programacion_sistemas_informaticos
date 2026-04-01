# SOLUCIÓN 18
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624} -ErrorAction SilentlyContinue |
  Where-Object { $_.Properties[5].Value -eq 'alberto' } |
  Select-Object TimeCreated, @{n='User';e={$_.Properties[5].Value}}
