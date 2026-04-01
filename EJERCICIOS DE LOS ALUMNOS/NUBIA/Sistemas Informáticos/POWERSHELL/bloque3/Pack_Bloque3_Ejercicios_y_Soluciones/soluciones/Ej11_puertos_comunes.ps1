# SOLUCIÓN 11
foreach($p in 80,443){
  $r = Test-NetConnection -ComputerName github.com -Port $p
  [pscustomobject]@{Puerto=$p; Abierto=$r.TcpTestSucceeded}
}
