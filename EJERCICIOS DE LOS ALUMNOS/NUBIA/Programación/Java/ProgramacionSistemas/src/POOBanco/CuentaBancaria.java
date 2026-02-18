package POOBanco;

public class CuentaBancaria extends Banco{
	private String noCuenta;
	private String saldoInicial;
	
	public CuentaBancaria(String nombreBanco, String noCuenta, String saldoInicial) {
	super(nombreBanco);
		this.noCuenta=noCuenta;
		this.saldoInicial=saldoInicial;
	}

	public String getNoCuenta() {
		return noCuenta;
	}

	public void setNoCuenta(String noCuenta) {
		this.noCuenta = noCuenta;
	}

	public String getSaldoInicial() {
		return saldoInicial;
	}

	public void setSaldoInicial(String saldoInicial) {
		this.saldoInicial = saldoInicial;
	}
	

}
