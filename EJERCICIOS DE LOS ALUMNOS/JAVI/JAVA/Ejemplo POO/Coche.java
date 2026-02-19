interface Electrico {
    void cargarBateria();
}

// 1. Superclase (Padre)
abstract class Vehiculo {
    private final String marca;
    // Atributo Estático: El contador global de la "fábrica"
    private static int contadorVehiculos = 0;

    Vehiculo(String marca) {
        this.marca = marca;
        contadorVehiculos++; // Registra cada nuevo vehículo
    }
    // Getter

    public String getMarca() {
        return marca;
    }

    // Método Estático: Acceso al contador global
    public static int getTotalVehiculos() {
        return contadorVehiculos;
    }

    // Método abstracto: cada hijo DEBE decidir cómo hacerlo
    abstract void conducir();
}

// 2. Herencia: Coche hereda de Vehiculo
class Coche extends Vehiculo {
    Coche(String marca) {
        super(marca);
    }

    @Override
    void conducir() {
        System.out.println("Conduciendo el " + getMarca() + " con volante y 4 ruedas.");
    }
}

// 2. Herencia: Moto hereda de Vehiculo
class Moto extends Vehiculo {
    Moto(String marca) {
        super(marca);
    }

    @Override
    void conducir() {
        System.out.println("Conduciendo la " + getMarca() + " con manillar e inclinándose.");
    }
}

// 3. Patinete.
class Patinete extends Vehiculo implements Electrico {
    Patinete(String marca) {
        super(marca);
    }

    @Override
    void conducir() {
        System.out.println("Montando en " + getMarca() + " con batería baja.");
    }

    @Override
    public void cargarBateria() {
        System.out.println("Cargando batería " + getMarca());
    }
}
