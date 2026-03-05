package interfacesUnidad1;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Ejercicio2 extends JFrame {

    // Definimos los componentes
    private JTextField txtNombre, txtEdad, txtDireccion, txtCiudad, txtProvincia;
    private JButton btnAceptar;

    public Ejercicio2() {
        // Configuración de la ventana
        setTitle("Ejemplo JTextField con nombre y apellidos");
        setSize(450, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridBagLayout()); // Usamos GridBagLayout para que se parezca a la imagen
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5);
        gbc.fill = GridBagConstraints.HORIZONTAL;

        // Etiquetas y Campos de texto
        txtNombre = añadirCampo("Indica tu nombre:", 0, gbc);
        txtEdad = añadirCampo("Indica tu edad:", 1, gbc);
        txtDireccion = añadirCampo("Dirección:", 2, gbc);
        txtCiudad = añadirCampo("Ciudad:", 3, gbc);
        txtProvincia = añadirCampo("Provincia:", 4, gbc);

        // Botón Aceptar
        btnAceptar = new JButton("Aceptar");
        gbc.gridx = 0;
        gbc.gridy = 5;
        gbc.gridwidth = 1;
        add(btnAceptar, gbc);

        // Evento del botón
        btnAceptar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String mensaje = "Datos introducidos:\n" +
                        "Nombre: " + txtNombre.getText() + "\n" +
                        "Edad: " + txtEdad.getText() + "\n" +
                        "Dirección: " + txtDireccion.getText() + "\n" +
                        "Ciudad: " + txtCiudad.getText() + "\n" +
                        "Provincia: " + txtProvincia.getText();
                
                JOptionPane.showMessageDialog(null, mensaje, "Datos Introducidos", JOptionPane.INFORMATION_MESSAGE);
            }
        });
    }

    // Método auxiliar para no repetir código al crear etiquetas y campos
    private JTextField añadirCampo(String etiqueta, int fila, GridBagConstraints gbc) {
        gbc.gridx = 0;
        gbc.gridy = fila;
        add(new JLabel(etiqueta), gbc);

        JTextField campo = new JTextField(15);
        gbc.gridx = 1;
        add(campo, gbc);
        return campo;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new Ejercicio2().setVisible(true);
        });
    }
}