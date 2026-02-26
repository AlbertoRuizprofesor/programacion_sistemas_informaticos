<# 
  PROYECTO 1
  - Crea carpetas de informes
  - Exporta procesos con >150 MB de RAM a CSV
  - Exporta servicios detenidos a TXT
  - Muestra conteos por consola
#>

#region Funciones
function Crear-Carpetas {
    param(
        [string]$RutasProcesos = "C:\Informes\Procesos",
        [string]$RutasServicios = "C:\Informes\Servicios"
    )
    # Crea las carpetas si no existen. -Force evita error si ya existen.
    foreach ($ruta in @($RutasProcesos, $RutasServicios)) {
        New-Item -ItemType Directory -Path $ruta -Force -ErrorAction SilentlyContinue | Out-Null
    }
}

function Exportar-ProcesosMas150MB {
    param(
        [string]$DestinoCsv = "C:\Informes\Procesos\procesos.csv"
    )
    # Obtén procesos, filtra >150 MB y exporta a CSV
    $procesos = Get-Process -ErrorAction SilentlyContinue |
        Where-Object { $_.WorkingSet64 -gt 150MB } |
        Select-Object Name, Id, CPU, @{Name='Memoria_MB'; Expression = { [math]::Round($_.WorkingSet64 / 1MB, 2) }}

    # Exporta y oculta salida intermedia
    $procesos | Export-Csv -Path $DestinoCsv -NoTypeInformation -Encoding utf8
    return ($procesos.Count)  # Devuelve el número total exportado
}

function Exportar-ServiciosDetenidos {
    param(
        [string]$DestinoTxt = "C:\Informes\Servicios\servicios.txt"
    )
    # Obtén servicios detenidos y exporta a TXT con formato de tabla
    $servicios = Get-Service -ErrorAction SilentlyContinue |
        Where-Object { $_.Status -eq 'Stopped' } |
        Select-Object Name, DisplayName, Status

    # Para TXT: convertimos a tabla legible
    $contenido = $servicios | Format-Table -AutoSize | Out-String
    $contenido | Set-Content -Path $DestinoTxt -Encoding UTF8
    return ($servicios.Count)
}

function Mostrar-Resumen {
    param(
        [int]$TotalProc,
        [int]$TotalServ
    )
    Write-Host "-------------------------------------------"
    Write-Host " Procesos (>150 MB) exportados: $TotalProc"
    Write-Host " Servicios detenidos exportados: $TotalServ"
    Write-Host "-------------------------------------------"
}
#endregion

#region Flujo principal
Crear-Carpetas

$conteoProc = Exportar-ProcesosMas150MB
$conteoServ = Exportar-ServiciosDetenidos

Mostrar-Resumen -TotalProc $conteoProc -TotalServ $conteoServ
#endregion
