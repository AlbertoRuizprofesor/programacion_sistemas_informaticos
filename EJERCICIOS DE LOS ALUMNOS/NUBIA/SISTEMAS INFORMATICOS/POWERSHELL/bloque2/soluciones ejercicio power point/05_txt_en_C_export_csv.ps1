# Buscar .txt en C:\ y exportar a CSV (simplificado con -File)
Get-ChildItem C:\ -Filter *.txt -Recurse -File -ErrorAction SilentlyContinue |
  Select-Object FullName, Length, LastWriteTime |
  Export-Csv .\txt_en_C.csv -NoTypeInformation
