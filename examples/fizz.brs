import "stl/io"

void fizzBuzz(int i) {
    if(i % 15 == 0) {
        coutln("FizzBuzz")
    } elif (i % 5 == 0) {
        coutln("Buzz")
    } elif (i % 3 == 0) {
        coutln("Fizz")
    } else {
        coutln(i.toString())
    }
}

void main() {
    foreach(int i : (1)..(100)) {
        fizzBuzz(i)
    }
}