package adapter2;

class TemperatureAdapter implements FahrenheitTarget, CelsiusTarget {
	private CelsiusTemperature celsiusTemp;
	private FahrenheitTemperature fahrenheitTemp;

	// Constructor para adaptar de Celsius a Fahrenheit
	public TemperatureAdapter(CelsiusTemperature celsiusTemp) {
		this.celsiusTemp = celsiusTemp;
	}

	// Constructor para adaptar de Fahrenheit a Celsius
	public TemperatureAdapter(FahrenheitTemperature fahrenheitTemp) {
		this.fahrenheitTemp = fahrenheitTemp;
	}

	@Override
	public double getTemperatureInFahrenheit() {
		// Lógica: Si tengo Celsius, convierto a F. Si ya tengo F, lo devuelvo.
		if (celsiusTemp != null) {
			return (celsiusTemp.getValue() * 9 / 5) + 32;
		}
		return fahrenheitTemp.getValue();
	}

	@Override
	public double getTemperatureInCelsius() {
		// Lógica: Si tengo Fahrenheit, convierto a C. Si ya tengo C, lo devuelvo.
		if (fahrenheitTemp != null) {
			return (fahrenheitTemp.getValue() - 32) * 5 / 9;
		}
		return celsiusTemp.getValue();
	}
}


