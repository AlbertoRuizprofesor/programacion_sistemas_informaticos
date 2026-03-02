# SOLUCIÓN 9
$h = Read-Host "Host"
$r = Test-Connection $h -Count 4 -ErrorAction SilentlyContinue
if($r){
  $times = $r.ResponseTime
  [pscustomobject]@{
    Host=$h
    Min=($times|Measure-Object -Minimum).Minimum
    Max=($times|Measure-Object -Maximum).Maximum
    Avg=($times|Measure-Object -Average).Average
  }
} else { Write-Warning "Sin respuesta" }
