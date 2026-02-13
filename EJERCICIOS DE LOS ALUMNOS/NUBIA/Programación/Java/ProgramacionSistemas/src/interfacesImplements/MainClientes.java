package interfacesImplements;

public class MainClientes {
	public static void main(String [] args) {
		
		String nombre="Nubia";
		String enterprise="Microsoft";
		String tipoEmpresa="Unicornio";
			
		Clientes cliente=new Clientes(nombre);
		System.out.println(cliente.enviarDatos(nombre));
		System.out.println(cliente.firmar(nombre));
		System.out.println(cliente.mostrarDatos(nombre));
		System.out.println(cliente.pagar(nombre));
		
		Empresa empresa=new Empresa(enterprise,tipoEmpresa);
		System.out.println(empresa.mostrarDatos(enterprise,tipoEmpresa));
		System.out.println(empresa.pagar(enterprise));	
		}

}

