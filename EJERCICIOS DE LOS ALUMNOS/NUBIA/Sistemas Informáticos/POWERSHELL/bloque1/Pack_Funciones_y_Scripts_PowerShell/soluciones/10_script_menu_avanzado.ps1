# SOLUCIÓN 10: Menú avanzado con funciones
function Calcular-Factorial {
    param([int]$N)
    if ($N -lt 0) { throw "N debe ser >= 0" }
    $r = 1; for ($i=1;$i -le $N;$i++){ $r*=$i }; return $r
}
function Convertir-Temperatura {
    param(
        [Parameter(Mandatory)][double]$Valor,
        [ValidateSet("C","F")][string]$De,
        [ValidateSet("C","F")][string]$A
    )
    if ($De -eq $A) { return $Valor }
    if ($De -eq "C" -and $A -eq "F") { return ($Valor * 9/5 + 32) }
    if ($De -eq "F" -and $A -eq "C") { return (($Valor - 32) * 5/9) }
}
function Menu {
    do {
        Write-Host "1) Factorial"; Write-Host "2) Convertir temperatura"; Write-Host "3) Salir"
        $op = Read-Host "Opción"
        switch ($op) {
            "1" { $n = [int](Read-Host "n (>=0)"); Write-Host "$n! = $(Calcular-Factorial -N $n)" }
            "2" {
                $v = [double](Read-Host "Valor"); $de = Read-Host "De (C/F)"; $a = Read-Host "A (C/F)"
                Write-Host "Resultado: $(Convertir-Temperatura -Valor $v -De $de -A $a)"
            }
            "3" { Write-Host "Adiós" }
            Default { Write-Host "Opción no válida" }
        }
    } while ($op -ne "3")
}
Menu
