
package metodos;

public class MainImporte {

    public static void main(String[] args) {
    	
        // 1. Creamos un objeto de la clase Importe
        Importe calculadoraPrecio=new Importe();
        
        int importeBase = 100;
        
        // 2. Llamamos al método 'iva' y guardamos el resultado
        double resultadoIva = calculadoraPrecio.iva(importeBase);
        
        // 3. Mostramos el IVA calculado (opcional)
        System.out.println("El IVA de " + importeBase + " es: " + resultadoIva);
        
        // 4. Llamamos al método 'total' pasando el importe y el iva obtenido
        calculadoraPrecio.total(importeBase, resultadoIva);
    }
}