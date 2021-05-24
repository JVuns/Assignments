package forumAssingment;

public class Driver2 {

	public static void main(String[] args) {
		Species Tigris = new Species("Tigris", "Meow");
		Species Ursa = new Species("Ursa", "bearidk");
		Specimen bear = new Specimen("Hola", 1, Ursa, "a");
		Specimen bear2 = new Specimen("Borak", 3, Ursa, "A");
		Specimen cat = new Specimen("Thomas", 4, Tigris, "M");
		Specimen[] splist = {bear, bear2, cat};
		System.out.println(Llist.makeList(splist));
		System.out.println(bear.getTOA());
		System.out.println(Llist.makeSpeciesList(Llist.makeList(splist)));
		System.out.println(Llist.makeSpeciesListUnique(Llist.makeSpeciesList(Llist.makeList(splist))));
	}
}
