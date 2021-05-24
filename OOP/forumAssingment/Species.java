package forumAssingment;

public class Species extends Genus{
	private String speciesName;
	public Species( String s, String g ){
		super(g);
		setSpeciesName(s);
	}
	public void setSpeciesName(String s){ speciesName = s; }
	public String getSpeciesName(){ return speciesName; }
	public String toString(){
		return "Species: " + getGenusName() + " " + speciesName;
	}
	public boolean equals(Species s){
		return speciesName.equals(s.getSpeciesName());
	}
}

