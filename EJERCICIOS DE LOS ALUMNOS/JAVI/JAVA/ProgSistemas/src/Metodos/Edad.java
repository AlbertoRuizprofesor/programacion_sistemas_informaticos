package Metodos;

public class Edad {
    
    
    public int nac;
    
    
    public int calcularEdad() {
        return 2026 - nac;
    }
    
    
    public String mayorEdad() {
        
        if (calcularEdad() >= 18) {
            return "Eres mayor de edad.";
        } else {
            return "NO eres mayor de edad.";
        }
    }
    
    public void resultados() {
        System.out.println("Hola, tu edad es de: " + calcularEdad());
        
        System.out.println(mayorEdad());
    }
}