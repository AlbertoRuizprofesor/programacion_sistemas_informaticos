/*
package metodos;
import java.util.Scanner;

public class CajaPandora{
	public void Sumatoria(int numero1,int numero2,int numero3) {
	int suma=0;
	suma=numero1+numero2+numero3;
	System.out.println("la sumatoria es: "+suma);
	}
}
*/

package metodos;
import java.util.Scanner;

public class CajaPandora{
	public void Sumatoria(int[] numeros) {
        int suma = 0;
        for (int n : numeros) {
            suma += n;
        }
        System.out.println("La suma es: " + suma);
    }
	
}