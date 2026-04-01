# SOLUCIÓN 5: Pares e impares hasta N
[int]$n = Read-Host "Introduce N"
$pares=0;$impares=0
for ($i=1;$i -le $n;$i++){ if ($i%2 -eq 0){$pares++} else {$impares++} }
Write-Host "Entre 1 y $n hay $pares pares y $impares impares"
