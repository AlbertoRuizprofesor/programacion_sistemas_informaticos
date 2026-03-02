# SOLUCIÓN 12
$hosts='8.8.8.8','1.1.1.1'
$rep = foreach($h in $hosts){
  $r=Test-Connection $h -Count 4 -ErrorAction SilentlyContinue
  if($r){ [pscustomobject]@{Host=$h; MediaMs=($r.ResponseTime|Measure-Object -Average).Average} }
}
$rep | Export-Csv .\ping_medias.csv -NoTypeInformation
