public class Main {
    public static void main(String[] args) {
        // 1. Creamos el array con UN solo objeto de cada tipo
        Vehiculo[] misVehiculos = {
                new Coche("Ferrari"),
                new Moto("Ducati"),
                new Patinete("Xiaomi")
        };

        // 2. El bucle recorre cada uno UNA SOLA VEZ
        for (Vehiculo v : misVehiculos) {

            v.conducir(); // Imprime: "Conduciendo el [Marca]..."

            // 3. Solo si es eléctrico, imprime la línea extra de carga
            if (v instanceof Electrico) {
                ((Electrico) v).cargarBateria();
            }

            // Un separador para que en consola se vea ordenado
            System.out.println("---");
        }

        // 5. RESULTADO GLOBAL (Uso de static)
        System.out.println("INVENTARIO FINAL: Se han registrado "
                + Vehiculo.getTotalVehiculos() + " vehículos.");
    }
}
