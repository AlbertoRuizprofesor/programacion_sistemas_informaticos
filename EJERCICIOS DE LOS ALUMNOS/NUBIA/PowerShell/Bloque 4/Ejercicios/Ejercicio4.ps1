$acl = Get-Acl "C:\prueba" 

$rule = New-Object System.Security.AccessControl.FileSystemAccessRule("Usuario","Read","Allow") 

$acl.AddAccessRule($rule) 

Set-Acl "C:\prueba" $acl