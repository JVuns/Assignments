package vehicles;

import java.util.ArrayList;

public class Main {
	public static void main(String[] args) {
		Police police = new Police("John", 34);
		PoliceCar policeCar = new PoliceCar(police);
		
		ArrayList<Object> department = new ArrayList<Object>();
		department.add(policeCar);
		System.out.println(department.get(0).toString());
	}
}
