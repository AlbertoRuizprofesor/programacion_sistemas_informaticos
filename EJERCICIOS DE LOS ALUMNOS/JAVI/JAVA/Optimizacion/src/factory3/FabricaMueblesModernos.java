package factory3;

class FabricaMueblesModernos implements FabricaMuebles {
	@Override
	public Silla crearSilla() {
		return new SillaModerna();
	}

	@Override
	public Sofa crearSofa() {
		return new SofaModerno();
	}
}
