package interface2;

public class MainCalculadora {
    public static void main(String[] args) {

        Calculadora calculadora = new Calculadora(); // crear objeto
        calculadora.mostrar(20,2); // llamar método
        
        Sumadora sumadora = new Sumadora(); // crea el objeto
        sumadora.mostrar(10,30); // llamo al metodo
    }
}
