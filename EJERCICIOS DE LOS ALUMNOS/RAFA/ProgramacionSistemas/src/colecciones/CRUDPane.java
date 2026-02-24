package colecciones;

import java.util.ArrayList;
import javax.swing.JOptionPane;

public class CRUDPane {

    static ArrayList<String> lista = new ArrayList<>();

    public static void main(String[] args) {

        int opcion;

        do {
            String menu = """
                    ----- CRUD -----
                    0. Crear lista de ejemplo
                    1. Añadir
                    2. Eliminar
                    3. Modificar
                    4. Buscar
                    5. Listado
                    6. Salir
                    """;

            opcion = Integer.parseInt(
                    JOptionPane.showInputDialog(menu + "\n¿Qué quieres hacer?")
            );

            switch (opcion) {
                case 0:
                    crearLista();
                    break;
                case 1:
                    agregar();
                    break;
                case 2:
                    eliminar();
                    break;
                case 3:
                    modificar();
                    break;
                case 4:
                    buscar();
                    break;
                case 5:
                    listado();
                    break;
                case 6:
                    JOptionPane.showMessageDialog(null, "Saliendo del programa...");
                    break;
                default:
                    JOptionPane.showMessageDialog(null, "Opción no válida.");
            }

        } while (opcion != 6);
    }

    public static void crearLista() {
        lista.clear();
        lista.add("minerva");
        lista.add("diana");
        lista.add("rafa");
        JOptionPane.showMessageDialog(null, "Lista creada con nombres de ejemplo.");
    }

    public static void agregar() {
        String nombre = JOptionPane.showInputDialog("Nombre a añadir:");
        if (nombre != null && !nombre.isEmpty()) {
            lista.add(nombre);
            JOptionPane.showMessageDialog(null, "Nombre guardado.");
        }
    }

    public static void eliminar() {
        String nombre = JOptionPane.showInputDialog("Nombre a eliminar:");
        if (lista.remove(nombre)) {
            JOptionPane.showMessageDialog(null, "Nombre eliminado.");
        } else {
            JOptionPane.showMessageDialog(null, "No encontrado.");
        }
    }

    public static void modificar() {
        String nombre = JOptionPane.showInputDialog("Nombre a modificar:");
        int posicion = lista.indexOf(nombre);

        if (posicion != -1) {
            String nuevo = JOptionPane.showInputDialog("Nuevo nombre:");
            lista.set(posicion, nuevo);
            JOptionPane.showMessageDialog(null, "Nombre modificado.");
        } else {
            JOptionPane.showMessageDialog(null, "No encontrado.");
        }
    }

    public static void buscar() {
        String nombre = JOptionPane.showInputDialog("Nombre a buscar:");
        int posicion = lista.indexOf(nombre);

        if (posicion != -1) {
            JOptionPane.showMessageDialog(null,
                    "Encontrado en la posición: " + posicion);
        } else {
            JOptionPane.showMessageDialog(null, "No encontrado.");
        }
    }

    public static void listado() {
        if (lista.isEmpty()) {
            JOptionPane.showMessageDialog(null, "La lista está vacía.");
        } else {
            StringBuilder sb = new StringBuilder("Listado de nombres:\n");
            for (int i = 0; i < lista.size(); i++) {
                sb.append(i + 1).append(". ").append(lista.get(i)).append("\n");
            }
            JOptionPane.showMessageDialog(null, sb.toString());
        }
    }
}
