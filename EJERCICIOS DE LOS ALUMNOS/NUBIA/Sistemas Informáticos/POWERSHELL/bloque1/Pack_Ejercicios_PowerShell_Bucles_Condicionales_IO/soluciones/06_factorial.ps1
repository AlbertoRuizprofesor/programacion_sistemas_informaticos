# SOLUCIÓN 6: Factorial con while
[int]$n = Read-Host "Introduce un entero >= 0"
if ($n -lt 0){ Write-Host "Debe ser >= 0"; exit }
$result=1;$i=1
while($i -le $n){ $result*=$i; $i++ }
Write-Host "$n! = $result"
