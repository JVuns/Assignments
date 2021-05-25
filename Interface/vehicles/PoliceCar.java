package vehicles;

public class PoliceCar extends LandVehicle implements isEmergency{
	Police police;
	
	public PoliceCar(Police police) {
		super();
		this.police = police;
	}
	
	@Override
	public void soundSiren() {
		System.out.println("TeeeToooTeeeTooo");
		
	}

	@Override
	public String toString() {
		return "PoliceCar \t Driver: " + police.name;
	}

}
