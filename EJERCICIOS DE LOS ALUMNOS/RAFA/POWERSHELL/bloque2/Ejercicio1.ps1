Write-Host "Archivos mayores a 10MB en el directorio C:\"
Get-ChildItem c:\ -Recurse | Where-Object { $_.Length -gt 10MB }
|
Select-Object FullName, @{
    Name = "Tamaño (MB)"
    Expression = { "{0:N2}" -f ($_.Length / 1MB) }
}

