# SOLUCIÓN 8
$hosts = 'google.com','microsoft.com','github.com'
$medias = foreach($h in $hosts){
  $r = Test-Connection $h -Count 4 -ErrorAction SilentlyContinue
  if($r){ [pscustomobject]@{Host=$h; Media=($r.ResponseTime|Measure-Object -Average).Average} }
}
$medias | Sort-Object Media -Descending | Select-Object -First 1
