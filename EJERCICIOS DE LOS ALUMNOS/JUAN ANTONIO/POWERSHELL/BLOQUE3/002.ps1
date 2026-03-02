#Lista los adaptadores de red mostrando nombre y estado
Get-NetAdapter | Select-Object Name, Status
