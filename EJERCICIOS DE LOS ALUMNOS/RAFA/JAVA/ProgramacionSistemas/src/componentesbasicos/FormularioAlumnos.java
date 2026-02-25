package componentesbasicos;
import javax.swing.*;
import java.awt.*;

public class FormularioAlumnos extends JFrame {

    private JTextField tfNombre, tfApellidos, tfEdad, tfDireccion, tfTelefono, tfComentarios;
    private JComboBox<String> cbEstudios, cbSituacion;
    private JCheckBox cbJava, cbPython;
    private JRadioButton rbBachillerato, rbCicloMedio, rbCicloSuperior;
    private JButton btnCargar, btnCerrar, btnAceptar;
    private ButtonGroup grupoCiclos;

    public FormularioAlumnos() {
        setTitle("Formulario para Alumnos de FP");
        setSize(500, 450);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout(10,10));

        // Panel principal para los campos
        JPanel panelCampos = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5,5,5,5);
        gbc.fill = GridBagConstraints.HORIZONTAL;

        // Fila 0 - Nombre
        gbc.gridx = 0; gbc.gridy = 0;
        panelCampos.add(new JLabel("Nombre:"), gbc);
        tfNombre = new JTextField(20);
        gbc.gridx = 1; gbc.gridy = 0;
        panelCampos.add(tfNombre, gbc);

        // Fila 1 - Apellidos
        gbc.gridx = 0; gbc.gridy = 1;
        panelCampos.add(new JLabel("Apellidos:"), gbc);
        tfApellidos = new JTextField(20);
        gbc.gridx = 1; gbc.gridy = 1;
        panelCampos.add(tfApellidos, gbc);

        // Fila 2 - Edad
        gbc.gridx = 0; gbc.gridy = 2;
        panelCampos.add(new JLabel("Edad:"), gbc);
        tfEdad = new JTextField(20);
        gbc.gridx = 1; gbc.gridy = 2;
        panelCampos.add(tfEdad, gbc);

        // Fila 3 - Dirección
        gbc.gridx = 0; gbc.gridy = 3;
        panelCampos.add(new JLabel("Dirección:"), gbc);
        tfDireccion = new JTextField(20);
        gbc.gridx = 1; gbc.gridy = 3;
        panelCampos.add(tfDireccion, gbc);

        // Fila 4 - Teléfono
        gbc.gridx = 0; gbc.gridy = 4;
        panelCampos.add(new JLabel("Teléfono:"), gbc);
        tfTelefono = new JTextField(20);
        gbc.gridx = 1; gbc.gridy = 4;
        panelCampos.add(tfTelefono, gbc);

        // Fila 5 - Estudios Previos
        gbc.gridx = 0; gbc.gridy = 5;
        panelCampos.add(new JLabel("Estudios Previos:"), gbc);
        String[] estudios = {"Sin estudios previos", "Bachillerato", "Ciclo Medio", "Ciclo Superior"};
        cbEstudios = new JComboBox<>(estudios);
        gbc.gridx = 1; gbc.gridy = 5;
        panelCampos.add(cbEstudios, gbc);

        // Fila 6 - Situación laboral
        gbc.gridx = 0; gbc.gridy = 6;
        panelCampos.add(new JLabel("Situación laboral:"), gbc);
        String[] situacion = {"Desempleado", "Trabajando", "Prácticas"};
        cbSituacion = new JComboBox<>(situacion);
        gbc.gridx = 1; gbc.gridy = 6;
        panelCampos.add(cbSituacion, gbc);

        // Fila 7 - Comentarios
        gbc.gridx = 0; gbc.gridy = 7;
        panelCampos.add(new JLabel("Comentarios:"), gbc);
        tfComentarios = new JTextField(20);
        gbc.gridx = 1; gbc.gridy = 7;
        panelCampos.add(tfComentarios, gbc);

        // Fila 8 - Checkboxes
        gbc.gridx = 0; gbc.gridy = 8;
        cbJava = new JCheckBox("Java");
        cbPython = new JCheckBox("Python");
        JPanel panelLenguajes = new JPanel();
        panelLenguajes.add(cbJava);
        panelLenguajes.add(cbPython);
        panelCampos.add(new JLabel("Lenguajes:"), gbc);
        gbc.gridx = 1; gbc.gridy = 8;
        panelCampos.add(panelLenguajes, gbc);

        // Fila 9 - Radio Buttons
        gbc.gridx = 0; gbc.gridy = 9;
        rbBachillerato = new JRadioButton("Bachillerato");
        rbCicloMedio = new JRadioButton("Ciclo Medio");
        rbCicloSuperior = new JRadioButton("Ciclo Superior");
        grupoCiclos = new ButtonGroup();
        grupoCiclos.add(rbBachillerato);
        grupoCiclos.add(rbCicloMedio);
        grupoCiclos.add(rbCicloSuperior);
        JPanel panelCiclos = new JPanel();
        panelCiclos.add(rbBachillerato);
        panelCiclos.add(rbCicloMedio);
        panelCiclos.add(rbCicloSuperior);
        panelCampos.add(new JLabel("Ciclo:"), gbc);
        gbc.gridx = 1; gbc.gridy = 9;
        panelCampos.add(panelCiclos, gbc);

        add(panelCampos, BorderLayout.CENTER);

        // Panel sur para botones
        JPanel panelBotones = new JPanel();
        btnCargar = new JButton("Cargar Curriculum");
        btnCerrar = new JButton("Cerrar");
        btnAceptar = new JButton("Aceptar");
        panelBotones.add(btnCargar);
        panelBotones.add(btnCerrar);
        panelBotones.add(btnAceptar);
        add(panelBotones, BorderLayout.SOUTH);

        // Acciones
        btnCerrar.addActionListener(e -> System.exit(0));
        btnAceptar.addActionListener(e -> mostrarDatos());
    }

    private void mostrarDatos() {
        String lenguajes = "";
        if (cbJava.isSelected()) lenguajes += "Java";
        if (cbPython.isSelected()) lenguajes += (lenguajes.isEmpty() ? "" : ", ") + "Python";

        String ciclo = rbBachillerato.isSelected() ? "Bachillerato" :
                       rbCicloMedio.isSelected() ? "Ciclo Medio" :
                       rbCicloSuperior.isSelected() ? "Ciclo Superior" : "";

        String datos = "Nombre: " + tfNombre.getText() +
                       "\nApellidos: " + tfApellidos.getText() +
                       "\nEdad: " + tfEdad.getText() +
                       "\nDirección: " + tfDireccion.getText() +
                       "\nTeléfono: " + tfTelefono.getText() +
                       "\nEstudios Previos: " + cbEstudios.getSelectedItem() +
                       "\nSituación Laboral: " + cbSituacion.getSelectedItem() +
                       "\nLenguajes: " + lenguajes +
                       "\nCiclo: " + ciclo +
                       "\nComentarios: " + tfComentarios.getText();
        JOptionPane.showMessageDialog(this, datos, "Datos del Alumno", JOptionPane.INFORMATION_MESSAGE);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new FormularioAlumnos().setVisible(true));
    }
}