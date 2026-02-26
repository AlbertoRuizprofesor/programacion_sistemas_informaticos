# SOLUCIÓN 2
$hosts = (Read-Host "Hosts separados por comas").Split(",") | ForEach-Object { $_.Trim() } | Where-Object { $_ }
foreach ($h in $hosts) {
  $r = Test-Connection $h -Count 4 -ErrorAction SilentlyContinue
  if ($r) {
    [pscustomobject]@{Host=$h; MediaMs=($r.ResponseTime | Measure-Object -Average).Average}
  } else {
    [pscustomobject]@{Host=$h; MediaMs=$null}
  }
}
