package joptionpane;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.Random;

public class ArkanoidNivelesDinamicos extends JPanel implements ActionListener {

    private final int ANCHO = 600;
    private final int ALTO = 450;
    private Timer timer;
    private boolean juegoActivo = true;
    private int nivelActual = 1;
    private int puntuacion = 0;

    // Barra
    private int paddleX = 250;
    private final int paddleY = 400;
    private final int PADDLE_ANCHO = 100;
    private final int PADDLE_VEL = 7;
    private boolean movIzq = false, movDer = false;

    // Pelota
    private int ballX = 300, ballY = 300;
    private int ballDX = 3, ballDY = -3;
    private final int BALL_SIZE = 15;

    // Bloques
    private ArrayList<Rectangle> bloques;
    
    public ArkanoidNivelesDinamicos() {
        this.setPreferredSize(new Dimension(ANCHO, ALTO));
        this.setBackground(Color.BLACK);
        this.setFocusable(true);
        
        iniciarNivel(nivelActual);

        timer = new Timer(15, this);
        timer.start();

        this.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (e.getKeyChar() == 'c' || e.getKeyChar() == 'C') movIzq = true;
                if (e.getKeyChar() == 'v' || e.getKeyChar() == 'V') movDer = true;
                if (!juegoActivo && (e.getKeyChar() == 'r' || e.getKeyChar() == 'R')) {
                    reiniciarJuegoCompleto();
                }
            }
            @Override
            public void keyReleased(KeyEvent e) {
                if (e.getKeyChar() == 'c' || e.getKeyChar() == 'C') movIzq = false;
                if (e.getKeyChar() == 'v' || e.getKeyChar() == 'V') movDer = false;
            }
        });
    }

    private void iniciarNivel(int nivel) {
        bloques = new ArrayList<>();
        int anchoB = 60;
        int altoB = 20;
        int espacio = 5;

        // CAMBIO DE DISPOSICIÓN SEGÚN EL NIVEL
        switch (nivel) {
            case 1: // Formato Clásico (Rectángulo)
                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 8; j++) {
                        bloques.add(new Rectangle(j * (anchoB + espacio) + 40, i * (altoB + espacio) + 50, anchoB, altoB));
                    }
                }
                break;
            case 2: // Formato Pirámide
                for (int i = 0; i < 5; i++) {
                    for (int j = i; j < 8 - i; j++) {
                        bloques.add(new Rectangle(j * (anchoB + espacio) + 40, i * (altoB + espacio) + 50, anchoB, altoB));
                    }
                }
                break;
            case 3: // Dos torres laterales
                for (int i = 0; i < 6; i++) {
                    for (int j = 0; j < 2; j++) {
                        bloques.add(new Rectangle(j * (anchoB + espacio) + 40, i * (altoB + espacio) + 50, anchoB, altoB));
                        bloques.add(new Rectangle((j+6) * (anchoB + espacio) + 40, i * (altoB + espacio) + 50, anchoB, altoB));
                    }
                }
                break;
            default: // Niveles superiores: Aleatorio
                Random rnd = new Random();
                for (int i = 0; i < 5; i++) {
                    for (int j = 0; j < 8; j++) {
                        if (rnd.nextBoolean()) {
                            bloques.add(new Rectangle(j * (anchoB + espacio) + 40, i * (altoB + espacio) + 50, anchoB, altoB));
                        }
                    }
                }
                break;
        }

        // Reset posiciones
        ballX = 300; ballY = 300;
        ballDY = -3;
        paddleX = 250;
    }

    private void reiniciarJuegoCompleto() {
        nivelActual = 1;
        puntuacion = 0;
        iniciarNivel(nivelActual);
        juegoActivo = true;
        timer.start();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (!juegoActivo) return;

        if (movIzq && paddleX > 0) paddleX -= PADDLE_VEL;
        if (movDer && paddleX < ANCHO - PADDLE_ANCHO) paddleX += PADDLE_VEL;

        ballX += ballDX; ballY += ballDY;

        if (ballX <= 0 || ballX >= ANCHO - BALL_SIZE) ballDX = -ballDX;
        if (ballY <= 0) ballDY = -ballDY;

        Rectangle rPelota = new Rectangle(ballX, ballY, BALL_SIZE, BALL_SIZE);
        Rectangle rBarra = new Rectangle(paddleX, paddleY, PADDLE_ANCHO, 10);
        
        if (rPelota.intersects(rBarra)) {
            ballDY = -Math.abs(ballDY);
        }

        for (int i = 0; i < bloques.size(); i++) {
            if (rPelota.intersects(bloques.get(i))) {
                bloques.remove(i);
                puntuacion += 50 * nivelActual; // Más puntos en niveles altos
                ballDY = -ballDY;
                break;
            }
        }

        if (bloques.isEmpty()) {
            nivelActual++;
            iniciarNivel(nivelActual);
        }

        if (ballY > ALTO) {
            juegoActivo = false;
            timer.stop();
        }
        repaint();
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;

        if (juegoActivo) {
            g2.setColor(Color.CYAN);
            g2.fillRoundRect(paddleX, paddleY, PADDLE_ANCHO, 10, 5, 5);

            g2.setColor(Color.WHITE);
            g2.fillOval(ballX, ballY, BALL_SIZE, BALL_SIZE);

            for (Rectangle b : bloques) {
                // Color cambia según la fila
                g2.setColor(Color.getHSBColor((float)b.y / 200, 0.7f, 0.9f));
                g2.fill(b);
                g2.setColor(Color.BLACK);
                g2.draw(b);
            }

            g2.setColor(Color.WHITE);
            g2.setFont(new Font("Monospaced", Font.BOLD, 16));
            g2.drawString("Nivel: " + nivelActual + " | Puntos: " + puntuacion, 20, 30);

        } else {
            g2.setColor(Color.RED);
            g2.setFont(new Font("Arial", Font.BOLD, 40));
            g2.drawString("GAME OVER", 180, 200);
            g2.setColor(Color.WHITE);
            g2.setFont(new Font("Arial", Font.PLAIN, 20));
            g2.drawString("Puntuación Final: " + puntuacion, 210, 240);
            g2.drawString("Presiona 'R' para Reiniciar", 185, 280);
        }
    }

    public static void main(String[] args) {
        JFrame f = new JFrame("Arkanoid Dinámico - C/V");
        f.add(new ArkanoidNivelesDinamicos());
        f.pack();
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setLocationRelativeTo(null);
        f.setVisible(true);
    }
}