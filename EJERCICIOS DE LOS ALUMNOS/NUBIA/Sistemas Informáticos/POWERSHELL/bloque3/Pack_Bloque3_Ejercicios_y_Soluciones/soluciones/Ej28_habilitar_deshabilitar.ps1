# SOLUCIÓN 28
Disable-ScheduledTask -TaskName 'InformeDiario09' -ErrorAction SilentlyContinue
Enable-ScheduledTask -TaskName 'InformeDiario09' -ErrorAction SilentlyContinue
