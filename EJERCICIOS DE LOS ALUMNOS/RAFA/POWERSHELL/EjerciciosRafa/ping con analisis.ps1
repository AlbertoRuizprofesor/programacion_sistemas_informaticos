$h = Read-Host "Introduce un host"
$datos = Test-Connection $host -Count 4
[pscustomobject]@{
    Host = $h
    Min = ($datos | Measure-Object ResponseTime -Minimum).Minimum
    Max = ($datos | Measure-Object ResponseTime -Maximum).Maximum
    Media = [math]::Round(($datos | Measure-Object ResponseTime -Average).Average, 1)
}
