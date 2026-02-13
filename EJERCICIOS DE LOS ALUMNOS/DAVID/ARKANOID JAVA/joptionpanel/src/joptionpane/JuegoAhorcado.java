package joptionpane;

import javax.swing.*;
import java.awt.*;
import java.util.Random;

public class JuegoAhorcado extends JFrame {
    // Lista de palabras para el juego
    private final String[] BANCO_PALABRAS = {
        "JAVA", "PROGRAMACION", "BANCO", "CLIENTE", "OBJETO", 
        "INTERFAZ", "CODIGO", "SWING", "HERENCIA", "CLASE"
    };
    
    private String palabraSecreta;
    private StringBuilder palabraOculta;
    private int errores = 0;
    private final int MAX_ERRORES = 6;
    private Random random = new Random();

    private PanelDibujo panelDibujo;
    private JLabel etiquetaPalabra;
    private JTextField campoLetra;
    private JButton botonIntentar;

    public JuegoAhorcado() {
        setTitle("Juego del Ahorcado Dinámico");
        setSize(400, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // Seleccionar palabra inicial
        seleccionarNuevaPalabra();

        // --- Interfaz ---
        panelDibujo = new PanelDibujo();
        add(panelDibujo, BorderLayout.CENTER);

        JPanel panelInferior = new JPanel(new GridLayout(3, 1));
        
        etiquetaPalabra = new JLabel(palabraOculta.toString(), SwingConstants.CENTER);
        etiquetaPalabra.setFont(new Font("Monospaced", Font.BOLD, 30));
        
        JPanel panelEntrada = new JPanel();
        campoLetra = new JTextField(2);
        botonIntentar = new JButton("Intentar");
        
        // Hacer que funcione al presionar "Enter" también
        campoLetra.addActionListener(e -> procesarIntento());
        botonIntentar.addActionListener(e -> procesarIntento());

        panelEntrada.add(new JLabel("Letra: "));
        panelEntrada.add(campoLetra);
        panelEntrada.add(botonIntentar);

        panelInferior.add(etiquetaPalabra);
        panelInferior.add(panelEntrada);
        add(panelInferior, BorderLayout.SOUTH);

        setVisible(true);
    }

    private void seleccionarNuevaPalabra() {
        // Elige una palabra al azar del array
        palabraSecreta = BANCO_PALABRAS[random.nextInt(BANCO_PALABRAS.length)];
        // Crea los guiones bajos según el largo de la palabra
        palabraOculta = new StringBuilder("_ ".repeat(palabraSecreta.length()));
    }

    private void procesarIntento() {
        String texto = campoLetra.getText().toUpperCase();
        campoLetra.setText("");

        if (texto.isEmpty()) return;
        char letra = texto.charAt(0);

        // Lógica de búsqueda
        boolean acierto = false;
        for (int i = 0; i < palabraSecreta.length(); i++) {
            if (palabraSecreta.charAt(i) == letra) {
                // Si la letra no había sido descubierta aún
                if (palabraOculta.charAt(i * 2) == '_') {
                    palabraOculta.setCharAt(i * 2, letra);
                    acierto = true;
                } else {
                    acierto = true; // Ya estaba, pero no cuenta como error
                }
            }
        }

        if (!acierto) {
            errores++;
            panelDibujo.repaint();
        }

        etiquetaPalabra.setText(palabraOculta.toString());
        verificarEstado();
    }

    private void verificarEstado() {
        if (!palabraOculta.toString().contains("_")) {
            JOptionPane.showMessageDialog(this, "¡Felicidades! Ganaste con: " + palabraSecreta);
            reiniciarJuego();
        } else if (errores >= MAX_ERRORES) {
            JOptionPane.showMessageDialog(this, "¡Perdiste! La palabra era: " + palabraSecreta);
            reiniciarJuego();
        }
    }

    private void reiniciarJuego() {
        errores = 0;
        seleccionarNuevaPalabra();
        etiquetaPalabra.setText(palabraOculta.toString());
        panelDibujo.repaint();
    }

    // El panel de dibujo se mantiene igual
    class PanelDibujo extends JPanel {
        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            Graphics2D g2 = (Graphics2D) g;
            g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
            g2.setStroke(new BasicStroke(3));

            g2.drawLine(20, 250, 150, 250); // base
            g2.drawLine(50, 250, 50, 20);   // poste
            g2.drawLine(50, 20, 150, 20);   // travesaño
            g2.drawLine(150, 20, 150, 50);  // soga

            if (errores >= 1) g2.drawOval(130, 50, 40, 40);      // Cabeza
            if (errores >= 2) g2.drawLine(150, 90, 150, 170);   // Cuerpo
            if (errores >= 3) g2.drawLine(150, 110, 120, 140);  // Brazo izq
            if (errores >= 4) g2.drawLine(150, 110, 180, 140);  // Brazo der
            if (errores >= 5) g2.drawLine(150, 170, 120, 210);  // Pierna izq
            if (errores >= 6) g2.drawLine(150, 170, 180, 210);  // Pierna der
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(JuegoAhorcado::new);
    }
}