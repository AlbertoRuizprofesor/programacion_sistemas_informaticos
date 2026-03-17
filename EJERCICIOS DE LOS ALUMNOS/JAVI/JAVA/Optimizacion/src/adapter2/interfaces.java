package adapter2;

//Interfaz para quien quiere resultados en Fahrenheit
interface FahrenheitTarget {
	double getTemperatureInFahrenheit();
}

//Interfaz para quien quiere resultados en Celsius
interface CelsiusTarget {
	double getTemperatureInCelsius();
}