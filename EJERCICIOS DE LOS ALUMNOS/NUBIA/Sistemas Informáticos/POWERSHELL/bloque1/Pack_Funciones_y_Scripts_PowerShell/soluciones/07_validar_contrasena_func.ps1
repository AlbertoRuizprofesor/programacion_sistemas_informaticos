# SOLUCIÓN 7: Función Validar-Contraseña
function Validar-Contraseña {
    param([string]$Texto)
    if ($Texto.Length -lt 8) { return $false }
    if ($Texto -notmatch "\d") { return $false }
    if ($Texto -notmatch "[A-Z]") { return $false }
    return $true
}
$pwd = Read-Host "Introduce contraseña"
if (Validar-Contraseña -Texto $pwd) { Write-Host "Válida" } else { Write-Host "No válida" }
