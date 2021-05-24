package forumAssingment;

import java.util.*;

public class Llist {
	static LinkedList<Specimen> myLL = new LinkedList<>();
	static LinkedList<Species> myLL2 = new LinkedList<>();
	static LinkedList<Species> myLL3 = new LinkedList<>();
	public static LinkedList<Specimen> makeList(Specimen[] animals )
	{
		for(int i=0; i<animals.length; i++) {
			myLL.add(animals[i]);
		}
		return myLL;
	}
	public static LinkedList<Species> makeSpeciesList(LinkedList<Specimen> animals ){
		for(int i=0; i<animals.size(); i++) {
			myLL2.add(animals.get(i).getTOA());
		}
		return myLL2;
		
	}
	public static LinkedList<Species> makeSpeciesListUnique(LinkedList<Species> allspecies ){
		for(int i=0; i<allspecies.size(); i++) {
			Species curr = allspecies.get(i);
			if(!myLL3.contains(curr)) {
				System.out.println("added " + curr);
				myLL3.add(curr);
				
			}
		}
		return myLL3;
	}
}
