package factory3;

public class abstractfactory1 {
    public static void main(String[] args) {
        // Crear una fábrica de muebles modernos
        FabricaMuebles fabricaModernos = new FabricaMueblesModernos();
        // Utilizar la fábrica para crear muebles modernos
        Silla sillaModerna = fabricaModernos.crearSilla();
        Sofa sofaModerno = fabricaModernos.crearSofa();

        sillaModerna.describir();
        sofaModerno.describir();

        // Crear una fábrica de muebles victorianos
        FabricaMuebles fabricaVictorianos = new FabricaMueblesVictorianos();
        // Utilizar la fábrica para crear muebles victorianos
        Silla sillaVictoriana = fabricaVictorianos.crearSilla();
        Sofa sofaVictoriano = fabricaVictorianos.crearSofa();

        sillaVictoriana.describir();
        sofaVictoriano.describir();
    }
}
