# SOLUCIÓN 33
$hosts='8.8.8.8','1.1.1.1'
$datos = foreach($h in $hosts){
  $r=Test-Connection $h -Count 4 -ErrorAction SilentlyContinue
  if($r){ [pscustomobject]@{Host=$h; MediaMs=($r.ResponseTime|Measure-Object -Average).Average} }
}
$datos | Export-Csv .\diag_red.csv -NoTypeInformation
