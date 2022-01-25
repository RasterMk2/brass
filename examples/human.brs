import "stl/io"

cls Human {
	void Human(String name, int age = 0) {
		String self.name = name
		int self.age = age
	}

	void Speak(String text) {
		coutln(self.name + text)
	}

	void age() {
		self.age = self.age + 1
	}
}