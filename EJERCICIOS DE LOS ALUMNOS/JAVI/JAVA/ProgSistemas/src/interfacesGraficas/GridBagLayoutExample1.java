package interfacesGraficas;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class GridBagLayoutExample1 {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Formulario de Registro Completo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();

        // --- 1. CREACIÓN DE COMPONENTES ---
        
        JLabel lblNombre = new JLabel("Nombre:");
        JTextField txtNombre = new JTextField(15);
        
        JLabel lblApellidos = new JLabel("Apellidos:");
        JTextField txtApellidos = new JTextField(15);
        
        JLabel lblEdad = new JLabel("Edad:");
        JTextField txtEdad = new JTextField(15);
        
        JLabel lblDireccion = new JLabel("Dirección:");
        JTextField txtDireccion = new JTextField(15);

        JLabel lblTelefono = new JLabel("Teléfono:");
        JTextField txtTelefono = new JTextField(15);

        JLabel lblEstudios = new JLabel("Estudios previos:");
        String[] opcionesEstudios = {"", "ESO", "Bachillerato", "Grado"};
        JComboBox<String> comboEstudios = new JComboBox<>(opcionesEstudios);

        JLabel lblSituacion = new JLabel("Situación laboral:");
        String[] opcionesLaboral = {"", "Estudiante", "Desempleado", "Ocupado"};
        JComboBox<String> comboSituacion = new JComboBox<>(opcionesLaboral);

        JCheckBox chkJava = new JCheckBox("Java");
        JCheckBox chkPython = new JCheckBox("Python");

        JRadioButton rbBachillerato = new JRadioButton("Bachillerato");
        JRadioButton rbCicloMedio = new JRadioButton("Ciclo Medio");
        ButtonGroup grupoNivel = new ButtonGroup();
        grupoNivel.add(rbBachillerato);
        grupoNivel.add(rbCicloMedio);

        JRadioButton chkCicloSuperior = new JRadioButton("Ciclo Superior");
        JButton btnCargarCV = new JButton("Cargar Curriculum");

        JLabel lblComentarios = new JLabel("Comentarios:");
        JTextArea areaComentarios = new JTextArea(4, 15);
        
        JButton btnAceptar = new JButton("Aceptar");
        JButton btnCerrar = new JButton("Cerrar");

        // --- 2. POSICIONAMIENTO CON GRIDBAGLAYOUT ---
        
        gbc.insets = new Insets(8, 8, 8, 8); 
        gbc.fill = GridBagConstraints.HORIZONTAL;

        // Filas 0 a 4: TextFields (Incluyendo el nuevo Teléfono)
        gbc.gridx = 0; gbc.gridy = 0; panel.add(lblNombre, gbc);
        gbc.gridx = 1; panel.add(txtNombre, gbc);

        gbc.gridx = 0; gbc.gridy = 1; panel.add(lblApellidos, gbc);
        gbc.gridx = 1; panel.add(txtApellidos, gbc);

        gbc.gridx = 0; gbc.gridy = 2; panel.add(lblEdad, gbc);
        gbc.gridx = 1; panel.add(txtEdad, gbc);

        gbc.gridx = 0; gbc.gridy = 3; panel.add(lblDireccion, gbc);
        gbc.gridx = 1; panel.add(txtDireccion, gbc);

        // Posicionar Teléfono en la Fila 4
        gbc.gridx = 0; gbc.gridy = 4; panel.add(lblTelefono, gbc);
        gbc.gridx = 1; panel.add(txtTelefono, gbc);

        // Desplazamos los siguientes componentes (gridy aumenta en 1)
        gbc.gridx = 0; gbc.gridy = 5; panel.add(lblEstudios, gbc);
        gbc.gridx = 1; panel.add(comboEstudios, gbc);

        gbc.gridx = 0; gbc.gridy = 6; panel.add(lblSituacion, gbc);
        gbc.gridx = 1; panel.add(comboSituacion, gbc);

        gbc.gridy = 7;
        gbc.gridx = 0; panel.add(chkJava, gbc);
        gbc.gridx = 1; panel.add(chkPython, gbc);

        gbc.gridy = 8;
        gbc.gridx = 0; panel.add(rbBachillerato, gbc);
        gbc.gridx = 1; panel.add(rbCicloMedio, gbc);

        gbc.gridy = 9;
        gbc.gridx = 0; panel.add(chkCicloSuperior, gbc);
        gbc.gridx = 1; panel.add(btnCargarCV, gbc);

        gbc.gridy = 10; gbc.gridx = 0; gbc.gridwidth = 2;
        panel.add(lblComentarios, gbc);

        gbc.gridy = 11; gbc.fill = GridBagConstraints.BOTH;
        panel.add(new JScrollPane(areaComentarios), gbc);

        JPanel pnlBotones = new JPanel(new FlowLayout(FlowLayout.CENTER, 20, 10));
        pnlBotones.add(btnAceptar);
        pnlBotones.add(btnCerrar);
        
        gbc.gridy = 12; gbc.gridwidth = 2; gbc.fill = GridBagConstraints.NONE;
        gbc.anchor = GridBagConstraints.CENTER;
        panel.add(pnlBotones, gbc);

        // --- 3. LÓGICA DE EVENTOS ---

        btnAceptar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                StringBuilder sb = new StringBuilder();
                sb.append("FICHA DE REGISTRO GENERADA\n");
                sb.append("==========================\n\n");
                sb.append("NOMBRE: ").append(txtNombre.getText()).append(" ").append(txtApellidos.getText()).append("\n");
                sb.append("EDAD: ").append(txtEdad.getText()).append("\n");
                sb.append("DIRECCIÓN: ").append(txtDireccion.getText()).append("\n");
                sb.append("TELÉFONO: ").append(txtTelefono.getText()).append("\n");
                sb.append("ESTUDIOS: ").append(comboEstudios.getSelectedItem()).append("\n");
                sb.append("SITUACIÓN: ").append(comboSituacion.getSelectedItem()).append("\n");
                
                sb.append("LENGUAJES: ");
                if(chkJava.isSelected()) sb.append("[Java] ");
                if(chkPython.isSelected()) sb.append("[Python] ");
                sb.append("\n");

                sb.append("NIVEL SELECCIONADO: ");
                if(rbBachillerato.isSelected()) sb.append("Bachillerato");
                else if(rbCicloMedio.isSelected()) sb.append("Ciclo Medio");
                else sb.append("No definido");
                sb.append("\n");

                sb.append("CICLO SUPERIOR: ").append(chkCicloSuperior.isSelected() ? "Sí" : "No").append("\n");
                sb.append("\nCOMENTARIOS ADICIONALES:\n").append(areaComentarios.getText());

                JTextArea vistaResumen = new JTextArea(sb.toString());
                vistaResumen.setEditable(false);
                vistaResumen.setFont(new Font("Monospaced", Font.PLAIN, 13));
                vistaResumen.setBackground(new Color(240, 240, 240));
                
                JScrollPane scrollResumen = new JScrollPane(vistaResumen);
                scrollResumen.setPreferredSize(new Dimension(400, 350));

                JOptionPane.showMessageDialog(frame, scrollResumen, "Resumen del Formulario", JOptionPane.PLAIN_MESSAGE);
            }
        });

        btnCerrar.addActionListener(e -> System.exit(0));

        frame.add(panel);
        frame.pack();
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}

