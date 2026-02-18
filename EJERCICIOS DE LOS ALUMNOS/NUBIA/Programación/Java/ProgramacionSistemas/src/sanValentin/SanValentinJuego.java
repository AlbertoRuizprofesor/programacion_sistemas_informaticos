package sanValentin;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SanValentinJuego extends JFrame {

	    private int vidas = 3;
	    private int preguntaActual = 0;

	    // --- PERSONALIZA TUS PREGUNTAS AQUÍ ---
	    private String[][] preguntas = {
	        {"¿Dónde quedamos por primera vez?", "tapio"},
	        {"¿Cuál es mi tipo de comida favorita?", "japonesa"},
	        {"¿Qué le encanta al cuchurrumín que le hagan?", "masajitos"},
	        {"¿Quién es lo más bonito del mundo?", "Darío"}
	    };

	    private JLabel lblPregunta, lblVidas, lblMensaje;
	    private JTextField txtRespuesta;
	    private JButton btnResponder;
	    private JPanel panelPrincipal;

	    public SanValentinJuego() {
	        // Configuración de la ventana
	        setTitle("❤️ Preguntas sobre nosotros❤️");
	        setSize(500, 400);
	        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	        setLocationRelativeTo(null);
	        setResizable(false);

	        // Panel con color rosa romántico
	        panelPrincipal = new JPanel();
	        panelPrincipal.setBackground(new Color(255, 204, 229)); // Rosa pastel
	        panelPrincipal.setLayout(new BoxLayout(panelPrincipal, BoxLayout.Y_AXIS));
	        
	        // Elementos visuales
	        lblVidas = new JLabel("Vidas: " + "❤️".repeat(vidas));
	        lblVidas.setFont(new Font("Serif", Font.BOLD, 20));
	        lblVidas.setAlignmentX(Component.CENTER_ALIGNMENT);

	        lblPregunta = new JLabel("¡Hola mi amorchiwich! ¿Listo para jugar?");
	        lblPregunta.setFont(new Font("Serif", Font.ITALIC, 18));
	        lblPregunta.setBorder(BorderFactory.createEmptyBorder(20, 10, 20, 10));
	        lblPregunta.setAlignmentX(Component.CENTER_ALIGNMENT);

	        txtRespuesta = new JTextField();
	        txtRespuesta.setMaximumSize(new Dimension(300, 30));
	        txtRespuesta.setHorizontalAlignment(JTextField.CENTER);

	        btnResponder = new JButton("Confirmar Respuesta 💖");
	        btnResponder.setBackground(new Color(255, 102, 178));
	        btnResponder.setForeground(Color.WHITE);
	        btnResponder.setFocusPainted(false);
	        btnResponder.setAlignmentX(Component.CENTER_ALIGNMENT);

	        lblMensaje = new JLabel("Responde correctamente para ganar");
	        lblMensaje.setAlignmentX(Component.CENTER_ALIGNMENT);

	        // Agregar al panel
	        panelPrincipal.add(Box.createVerticalGlue());
	        panelPrincipal.add(lblVidas);
	        panelPrincipal.add(lblPregunta);
	        panelPrincipal.add(txtRespuesta);
	        panelPrincipal.add(Box.createRigidArea(new Dimension(0, 15)));
	        panelPrincipal.add(btnResponder);
	        panelPrincipal.add(Box.createRigidArea(new Dimension(0, 15)));
	        panelPrincipal.add(lblMensaje);
	        panelPrincipal.add(Box.createVerticalGlue());

	        add(panelPrincipal);

	        // Lógica del botón
	        actualizarPregunta();
	        btnResponder.addActionListener(new ActionListener() {
	            @Override
	            public void actionPerformed(ActionEvent e) {
	                verificarRespuesta();
	            }
	        });
	    }

	    private void actualizarPregunta() {
	        if (preguntaActual < preguntas.length) {
	            lblPregunta.setText("Pregunta " + (preguntaActual + 1) + ": " + preguntas[preguntaActual][0]);
	            txtRespuesta.setText("");
	        } else {
	            ganar();
	        }
	    }

	    private void verificarRespuesta() {
	        String respuestaUsuario = txtRespuesta.getText().toLowerCase().trim();
	        String respuestaCorrecta = preguntas[preguntaActual][1].toLowerCase();

	        if (respuestaUsuario.equals(respuestaCorrecta)) {
	            preguntaActual++;
	            lblMensaje.setText("¡Correcto! Eres el mejor ❤️");
	            actualizarPregunta();
	        } else {
	            vidas--;
	            lblVidas.setText("Vidas: " + "❤️".repeat(Math.max(0, vidas)));
	            if (vidas <= 0) {
	                perder();
	            } else {
	                lblMensaje.setText("¡Ups! Inténtalo de nuevo, amor.");
	            }
	        }
	    }

	    private void ganar() {
	        JOptionPane.showMessageDialog(this, 
	            "¡FELICIDADES MI VIDA! \n\nHas demostrado que nos conoces a la perfección.\n" +
	            "Tu premio es: un ataque de besitos ¡Te amo muchísimo!", 
	            "❤️ San Valentín ❤️", JOptionPane.INFORMATION_MESSAGE);
	        System.exit(0);
	    }

	    private void perder() {
	        JOptionPane.showMessageDialog(this, 
	            "Te has quedado sin vidas... 💔\nPero como te amo, te daré otra oportunidad.", 
	            "Oh no...", JOptionPane.ERROR_MESSAGE);
	        vidas = 3;
	        preguntaActual = 0;
	        lblVidas.setText("Vidas: ❤️❤️❤️");
	        actualizarPregunta();
	    }

	    public static void main(String[] args) {
	        SwingUtilities.invokeLater(() -> {
	            new SanValentinJuego().setVisible(true);
	        });
	    }
	}


