package forumAssingment;

public class Genus {
	private String genusName;

	public Genus(String genusName) {
		this.genusName = genusName;
	}

	public String getGenusName() {
		return genusName;
	}

	public void setGenusName(String genusName) {
		this.genusName = genusName;
	}

	@Override
	public String toString() {
		return "Genus [genusName=" + genusName + "]";
	}
}
