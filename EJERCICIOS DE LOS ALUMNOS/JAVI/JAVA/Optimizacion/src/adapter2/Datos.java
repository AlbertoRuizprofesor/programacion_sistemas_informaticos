package adapter2;

//Representa una medida en Celsius
class CelsiusTemperature {
	private double value;

	public CelsiusTemperature(double value) {
		this.value = value;
	}

	public double getValue() {
		return value;
	}
}

//Representa una medida en Fahrenheit
class FahrenheitTemperature {
	private double value;

	public FahrenheitTemperature(double value) {
		this.value = value;
	}

	public double getValue() {
		return value;
	}
}