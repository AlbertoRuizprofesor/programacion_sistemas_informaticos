# SOLUCIÓN 4: Tabla de multiplicar
[int]$n = Read-Host "Tabla de multiplicar de:"
for ($i = 1; $i -le 10; $i++) { Write-Host "$n x $i = $($n*$i)" }
