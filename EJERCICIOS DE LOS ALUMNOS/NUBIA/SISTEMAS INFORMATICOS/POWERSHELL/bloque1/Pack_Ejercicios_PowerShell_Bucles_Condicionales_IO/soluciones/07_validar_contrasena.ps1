# SOLUCIÓN 7: Validación de contraseña
$pwd = Read-Host "Introduce una contraseña"
if ($pwd.Length -lt 8) { Write-Host "Debe tener al menos 8 caracteres" }
elseif ($pwd -notmatch "\d") { Write-Host "Debe contener al menos un número" }
else { Write-Host "Contraseña válida" }
