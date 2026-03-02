# SOLUCIÓN 9: Parámetros nombrados y validación
function Convertir-Temperatura {
    param(
        [Parameter(Mandatory)]
        [double]$Valor,
        [ValidateSet("C","F")]
        [string]$De,
        [ValidateSet("C","F")]
        [string]$A
    )
    if ($De -eq $A) { return $Valor }
    if ($De -eq "C" -and $A -eq "F") { return ($Valor * 9/5 + 32) }
    if ($De -eq "F" -and $A -eq "C") { return (($Valor - 32) * 5/9) }
}
$val = [double](Read-Host "Valor")
$de = Read-Host "De (C/F)"
$a = Read-Host "A (C/F)"
Write-Host "Resultado: $(Convertir-Temperatura -Valor $val -De $de -A $a)"
