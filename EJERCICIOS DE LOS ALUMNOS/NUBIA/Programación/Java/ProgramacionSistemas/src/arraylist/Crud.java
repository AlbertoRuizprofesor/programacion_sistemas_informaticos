package arraylist;
import java.util.ArrayList;

public class Crud {

	// MAIN (donde se ejecuta)
    public static void main(String[] args) {
        ArrayList<String> clientes = new ArrayList<>();

        clientes.add("Nubia");
        clientes.add("Noemi");
        clientes.add("Ana");
        clientes.add("Darío");
        clientes.add("Andrés");
        clientes.add("Saiyan");
        
        clientes.remove("Saiyan");
        
        clientes.set(4, "Saiyan");
               
        // Listado
        listarClientes(clientes);
        
    }
    
    // MÉTODOS
    
    // listar clientes
    public static void listarClientes(ArrayList<String> lista) {
        System.out.println("--- Lista de Clientes ---");
        for (var nom : lista) { // Java deduce que 'elemento' es un String
            System.out.println("- "+nom);
        }
    }
}
