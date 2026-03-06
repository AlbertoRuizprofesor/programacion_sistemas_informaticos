# SOLUCIÓN 10: Adivina el número
$oculto = Get-Random -Minimum 1 -Maximum 21
do {
  [int]$intento = Read-Host "Adivina el número (1..20)"
  if ($intento -lt $oculto) { Write-Host "Más alto" }
  elseif ($intento -gt $oculto) { Write-Host "Más bajo" }
  else { Write-Host "¡Correcto! Era $oculto" }
} while ($intento -ne $oculto)
