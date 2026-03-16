package facade;

public class FacadeAuto {
    private Motor motor;
    private BombaCombustible bombaCombustible;
    private AireAcondicionado aireAcondicionado;

    public FacadeAuto() {
        this.motor = new Motor();
        this.bombaCombustible = new BombaCombustible();
        this.aireAcondicionado = new AireAcondicionado();
    }

    public void encenderAuto() {
        bombaCombustible.bombear();
        motor.encender();
        aireAcondicionado.encender();
        System.out.println("Auto encendido.");
    }

    public void apagarAuto() {
        aireAcondicionado.apagar();
        motor.apagar();
        System.out.println("Auto apagado.");
    }
}

