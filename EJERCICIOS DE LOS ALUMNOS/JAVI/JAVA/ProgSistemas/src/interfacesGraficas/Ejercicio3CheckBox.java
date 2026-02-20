package interfacesGraficas;

import javax.swing.*;

public class Ejercicio3CheckBox extends JFrame {

	private JCheckBox checkBox, checkBox2, checkBox3, checkBox4;

	public Ejercicio3CheckBox() {

		setTitle("Ejemplo JCheckBox");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLayout(null); // ⭐ IMPORTANTE

		checkBox = new JCheckBox("Aceptar términos y condiciones. ");
		checkBox.setBounds(30, 30, 220, 30);

		checkBox2 = new JCheckBox("Acepta que estás alelao. ");
		checkBox2.setBounds(30, 70, 220, 30);
		
		checkBox3 = new JCheckBox("Acepta que Hacienda te roba. ");
		checkBox3.setBounds(30, 110, 220, 30);

		checkBox4 = new JCheckBox("Acepta o no aceptes. ");
		checkBox4.setBounds(30, 150, 220, 30);


		add(checkBox);
		add(checkBox2);
		add(checkBox3);
		add(checkBox4);

		setSize(300, 250);
		setLocationRelativeTo(null);

	}

	public static void main(String[] args) {

		SwingUtilities.invokeLater(() -> {

			new Ejercicio3CheckBox().setVisible(true);

		});

	}

}