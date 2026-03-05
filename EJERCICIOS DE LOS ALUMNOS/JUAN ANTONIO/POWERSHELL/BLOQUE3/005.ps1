#Hace 2 ping a google.com, office.com y github.com
$hosts = "google.com","office.com","github.com"
foreach ($h in $hosts) {
    Test-Connection $h -Count 2 | Select-Object Address, ResponseTime
}
