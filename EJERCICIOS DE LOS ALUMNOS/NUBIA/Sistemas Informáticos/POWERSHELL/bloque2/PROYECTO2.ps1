<# 
  PROYECTO 2
  - Crea carpetas de informes
  - Lista archivos >50 MB en C:\ y exporta a CSV
  - Lista servicios en ejecución y exporta a TXT
  - Muestra conteos por consola
#>

#region Funciones
function Crear-Carpetas {
    param(
        [string]$RutasArchivos = "C:\Informes\Archivos",
        [string]$RutasServicios = "C:\Informes\Servicios"
    )
    foreach ($ruta in @($RutasArchivos, $RutasServicios)) {
        New-Item -ItemType Directory -Path $ruta -Force -ErrorAction SilentlyContinue | Out-Null
    }
}

function Exportar-ArchivosGrandes {
    param(
        [string]$RutaBusqueda = "C:\",
        [string]$DestinoCsv   = "C:\Informes\Archivos\archivos_grandes.csv"
    )
    # Busca archivos >50 MB en C:\ (evita errores y puntos de reanálisis)
    $archivos = Get-ChildItem -Path $RutaBusqueda -Recurse -File -Force `
        -ErrorAction SilentlyContinue -Attributes !ReparsePoint |
        Where-Object { $_.Length -gt 50MB } |
        Select-Object FullName,
            Length,
            @{Name='Tamano_MB'; Expression = { [math]::Round($_.Length / 1MB, 2) }}

    $archivos | Export-Csv -Path $DestinoCsv -NoTypeInformation -Encoding utf8

    # Ejemplo de uso del operador -f para mostrar tamaño en MB con 2 decimales (sólo por consola, opcional)
    # Muestra una vista previa de los primeros 5
    if ($archivos.Count -gt 0) {
        Write-Host "Vista previa (5 primeros):"
        $archivos | Select-Object -First 5 | ForEach-Object {
            Write-Host (" - {0}  ({1:N2} MB)" -f $_.FullName, $_.Tamano_MB)
        }
    }

    return ($archivos.Count)
}

function Exportar-ServiciosActivos {
    param(
        [string]$DestinoTxt = "C:\Informes\Servicios\servicios_activos.txt"
    )
    $servicios = Get-Service -ErrorAction SilentlyContinue |
        Where-Object { $_.Status -eq 'Running' } |
        Select-Object Name, DisplayName, Status

    $contenido = $servicios | Format-Table -AutoSize | Out-String
    $contenido | Set-Content -Path $DestinoTxt -Encoding UTF8

    return ($servicios.Count)
}

function Mostrar-Resumen {
    param(
        [int]$TotalArchivos,
        [int]$TotalServicios
    )
    Write-Host "-------------------------------------------"
    Write-Host " Archivos (>50 MB) exportados: $TotalArchivos"
    Write-Host " Servicios en ejecución exportados: $TotalServicios"
    Write-Host "-------------------------------------------"
}
#endregion

#region Flujo principal
Crear-Carpetas

$conteoArchivos  = Exportar-ArchivosGrandes
$conteoServicios = Exportar-ServiciosActivos

Mostrar-Resumen -TotalArchivos $conteoArchivos -TotalServicios $conteoServicios
#endregion
