package forumAssingment;

public class Specimen {
	private String name;
	private int cageNumber;
	private Species toa; 
	private String desc;
	public Specimen( String a, int c, Species s, String d){
		setName(a);
		setCage(c);
		setTOA(s);
		setDesc(d);
		}
	public void setName(String a){ name = a; }
	public void setCage(int c){ cageNumber = c; }
	public void setTOA(Species s){ toa = s; }
	public void setDesc(String d) { desc = d; }
	public String getName(){ return name; }
	public int getCage(){ return cageNumber; }
	public Species getTOA(){ return toa; }
	public String getDesc() {return desc;}
	public String toString(){return name + " is a " + toa + " in cage " + cageNumber;
	}
}

