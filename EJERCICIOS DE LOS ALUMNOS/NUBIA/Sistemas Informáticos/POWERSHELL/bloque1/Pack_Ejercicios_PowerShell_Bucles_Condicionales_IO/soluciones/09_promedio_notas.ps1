# SOLUCIÓN 9: Promedio de notas
$entrada = Read-Host "Introduce notas separadas por comas (ej. 7,8.5,9)"
$partes = $entrada -split ","
$total = 0.0; $cuenta = 0
foreach ($p in $partes) { $total += [double]($p.Trim()); $cuenta++ }
$prom = if ($cuenta -gt 0) { $total / $cuenta } else { 0 }
Write-Host "Promedio: $prom"
