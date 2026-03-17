$acl = Get-Acl C:\CarpetaPrueba
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule('Usuario','FullControl','Allow')$acl.SetAccessRule($rule)
Set-Acl C:\CarpetaPrueba $acl
Get-Acl C:\CarpetaPrueba | Format-List
