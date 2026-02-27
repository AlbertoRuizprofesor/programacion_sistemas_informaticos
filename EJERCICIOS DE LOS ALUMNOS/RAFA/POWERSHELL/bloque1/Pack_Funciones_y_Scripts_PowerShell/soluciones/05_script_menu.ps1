# SOLUCIÓN 5: Script con varias funciones + menú
function Saludar {
    $n = Read-Host "Tu nombre"
    Write-Host "¡Hola, $n!"
}
function Sumar {
    $a = [double](Read-Host "A"); $b = [double](Read-Host "B")
    Write-Host "Suma: $($a + $b)"
}
function Menu {
    do {
        Write-Host "1) Saludar"; Write-Host "2) Sumar"; Write-Host "3) Salir"
        $op = Read-Host "Opción"
        switch ($op) {
            "1" { Saludar }
            "2" { Sumar }
            "3" { Write-Host "Adiós" }
            Default { Write-Host "Opción no válida" }
        }
    } while ($op -ne "3")
}
Menu
