package interfaces;

public class MainClientes {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String nombre="Alberto";
		String enterprise="MICROSOFT";
		String tipo_empresa="UNICORNIO";
		
		Clientes cliente=new Clientes(nombre);
		
		System.out.println(cliente.enviar_datos(nombre));
		System.out.println(cliente.firmar(nombre));
		System.out.println(cliente.mostrar_datos(nombre));
		System.out.println(cliente.pagar(nombre));
		
	
		Empresas empresa=new Empresas(enterprise,tipo_empresa);
		System.out.println(empresa.mostrar_datos(
				enterprise,tipo_empresa));
		System.out.println(empresa.pagar(
				enterprise));

		
		
	}
}
