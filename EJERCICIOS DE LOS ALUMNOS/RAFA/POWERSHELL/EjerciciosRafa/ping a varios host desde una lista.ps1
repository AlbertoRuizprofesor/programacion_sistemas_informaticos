$hosts = Get-Content "C:\Users\2-DAW\Documents\GitHub\programacion_sistemas_informaticos\EJERCICIOS DE LOS ALUMNOS\RAFA\POWERSHELL\EjerciciosRafa\hosts.txt.txt"
foreach ($h in $hosts) {
    try {
        $media = (Test-Connection $h -Count 4 -ErrorAction Stop | Measure-Object ResponseTime -Average).Average
        "{0}: {1:N1} ms" -f $h, $media
    } catch {
        "{0}: sin respuesta" -f $h
    }
}
