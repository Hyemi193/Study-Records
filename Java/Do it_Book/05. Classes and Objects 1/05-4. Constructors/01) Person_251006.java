package Constructor;

// 생성자 생성

public class Person {
    String name;
    float height;
    float weight;

    // 기본 생성자
    public Person() {}

    public Person(String pname, float pheight, float pweight) {
        name = pname;       // 사람 이름을 매개변수로 입력받아서 Person 클래스를 생성하는 생성자를 구현
        height = pheight;
        weight = pweight;
    }
}
