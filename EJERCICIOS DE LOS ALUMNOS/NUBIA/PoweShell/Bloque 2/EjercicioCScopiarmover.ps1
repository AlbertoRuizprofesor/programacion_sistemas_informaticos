#copiar informesprocesos.txt a backup
Copy-Item C:\informesprocesos\informesprocesos.txt C:\backup\informesprocesos.txt
Get-ChildItem c:\backup

#copiar informesservicios.txt a backup
Copy-Item C:\informesservicios\informesservicios.txt C:\backup\informesservicios.txt
Get-ChildItem c:\backup

#mover backup.txt a buckup
Move-Item C:\informesservicios\backup.txt C:\backup\backup.txt
Get-ChildItem c:\backup