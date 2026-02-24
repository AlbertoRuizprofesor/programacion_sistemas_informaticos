package calculadora;

import java.awt.EventQueue;
import java.awt.FlowLayout;
import java.awt.GridLayout;

import javax.swing.AbstractButton;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;
import javax.swing.border.EmptyBorder;

public class HPCalculator extends JFrame {

	private static final long serialVersionUID = 1L;
	private JPanel contentPane;
	private JTextField operador1;
	private JTextField operador2;
	private JTextField resultado;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					HPCalculator frame = new HPCalculator();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public HPCalculator() {
		setTitle("HPCalculator");
        setSize(450, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(5, 1, 5, 3));
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		
		
        JPanel panelCampos = new JPanel(new FlowLayout());
        panelCampos.add(new JLabel("Operador 1:"));
        operador1 = new JTextField(8);
        panelCampos.add(operador1);
        panelCampos.add(new JLabel("Operador 2:"));
        operador2 = new JTextField(8);
        panelCampos.add(operador2);
        add(panelCampos);
        
        JPanel panelSumaResta = new JPanel(new FlowLayout());
        JButton sumar = new JButton("Sumar");
        JButton restar = new JButton("Restar");
        panelSumaResta.add(sumar);
        panelSumaResta.add(restar);
        add(panelSumaResta);
        
        
        JPanel panelResultado = new JPanel(new FlowLayout());
        panelResultado.add(new JLabel("Resultado:"));
        resultado = new JTextField(10);
        resultado.setEditable(false);
        panelResultado.add(resultado);
        JButton limpiar = new JButton("Limpiar");
        panelResultado.add(limpiar);
        add(panelResultado);
        
        sumar.addActionListener(e -> calcular("+"));
        restar.addActionListener(e -> calcular("-"));
        limpiar.addActionListener(e -> {
            operador1.setText("");
            operador2.setText("");
            resultado.setText("");
        });
    }

    private void calcular(String operacion) {
        try {
            double op1 = 0, op2 = 0;

            // Leer solo los campos necesarios según la operación
            if (!operacion.equals("^2") && !operacion.equals("√2")) {
                op1 = Double.parseDouble(operador1.getText());
            }
            if (!operacion.equals("^1") && !operacion.equals("√1")) {
                op2 = Double.parseDouble(operador2.getText());
            }

            double res = 0;
            switch (operacion) {
                case "+": res = op1 + op2; break;
                case "-": res = op1 - op2; break;
                case "*": res = op1 * op2; break;
                case "/": 
                    if(op2 == 0) {
                        JOptionPane.showMessageDialog(this, "No se puede dividir entre 0");
                        return;
                    }
                    res = op1 / op2; 
                    break;
                case "^1": res = Math.pow(op1, 2); break;
                case "^2": res = Math.pow(op2, 2); break;
                case "√1": 
                    if(op1 < 0) { JOptionPane.showMessageDialog(this, "Raíz no válida"); return; }
                    res = Math.sqrt(op1); 
                    break;
                case "√2": 
                    if(op2 < 0) { JOptionPane.showMessageDialog(this, "Raíz no válida"); return; }
                    res = Math.sqrt(op2); 
                    break;
            }
            resultado.setText(String.valueOf(res));
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Ingresa valores numéricos válidos");
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            CalculadoraSimple calc = new CalculadoraSimple();
            calc.setVisible(true);
        });
    }
}