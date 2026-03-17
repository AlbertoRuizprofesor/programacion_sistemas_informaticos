package adapter2;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		System.out.println("¿Qué conversión desea realizar?");
		System.out.println("1. De Celsius a Fahrenheit");
		System.out.println("2. De Fahrenheit a Celsius");
		int opcion = scanner.nextInt();

		if (opcion == 1) {
			System.out.print("Introduzca los grados Celsius: ");
			double valor = scanner.nextDouble();

			// FLUJO: Input -> Objeto Celsius -> Adaptador -> Resultado Fahrenheit
			CelsiusTemperature cTemp = new CelsiusTemperature(valor);
			TemperatureAdapter adapter = new TemperatureAdapter(cTemp);

			System.out.println("Resultado: " + adapter.getTemperatureInFahrenheit() + " °F");

		} else if (opcion == 2) {
			System.out.print("Introduzca los grados Fahrenheit: ");
			double valor = scanner.nextDouble();

			// FLUJO: Input -> Objeto Fahrenheit -> Adaptador -> Resultado Celsius
			FahrenheitTemperature fTemp = new FahrenheitTemperature(valor);
			TemperatureAdapter adapter = new TemperatureAdapter(fTemp);

			System.out.println("Resultado: " + adapter.getTemperatureInCelsius() + " °C");

		} else {
			System.out.println("Opción no válida.");
		}

		scanner.close();
	}
}