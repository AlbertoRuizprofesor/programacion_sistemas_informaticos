# SOLUCIÓN 35
cls
$root='C:\Informes'; New-Item $root -ItemType Directory -Force | Out-Null
$r=Test-Connection 8.8.8.8 -Count 4 -ErrorAction SilentlyContinue
$media= if($r){($r.ResponseTime|Measure-Object -Average).Average}else{$null}
[pscustomobject]@{Host='8.8.8.8'; MediaMs=$media} | Export-Csv "$root\ping.csv" -NoTypeInformation
Get-EventLog -LogName System -Newest 50 | Select-Object TimeGenerated, Source, EventID, Message | Export-Csv "$root\system50.csv" -NoTypeInformation
"Informe generado: $(Get-Date -Format s)" | Out-File "$root\README.txt" -Encoding utf8
