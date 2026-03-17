# --- PASO 1: Crear los usuarios ---
# Por defecto se crean habilitados (Enabled)
$password = ConvertTo-SecureString "1111" -AsPlainText -Force

Write-Host "Iniciando creación de usuarios..." -ForegroundColor Cyan

New-LocalUser -Name "Empleado1" -Password $password -Description "Usuario de prueba Empleado1"
Write-Host "Empleado1 creado con éxito."

New-LocalUser -Name "Empleado2" -Password $password -Description "Usuario de prueba Empleado2"
Write-Host "Empleado2 creado con éxito."

New-LocalUser -Name "Empleado3" -Password $password -Description "Usuario de prueba Empleado3"
Write-Host "Empleado3 creado con éxito."

New-LocalUser -Name "Empleado4" -Password $password -Description "Usuario de prueba Empleado4"
Write-Host "Empleado4 creado con éxito."

# --- PASO 2: Cambiar el 2 y el 4 a Disable ---
Write-Host "`nDeshabilitando Empleado 2 y Empleado 4..." -ForegroundColor Yellow

Disable-LocalUser -Name "Empleado2"
Disable-LocalUser -Name "Empleado4"

Write-Host "Empleado 2 y 4 han sido deshabilitados."

# Pausa opcional para verificar en el sistema antes de borrar
Read-Host "`nPresiona Enter para proceder al PASO 3 (Eliminar todos)"

# --- PASO 3: Eliminarlos todos ---
#Write-Host "Eliminando todos los usuarios creados..." -ForegroundColor Red

#1..4 | ForEach-Object {
#    Remove-LocalUser -Name "Empleado$_"
#    Write-Host "Empleado$_ eliminado."
#

Write-Host "`nEjercicio completado con éxito." -ForegroundColor Green