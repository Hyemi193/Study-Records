package Constructor;

// 생성자 테스트

public class PersonTest {
    public static void main(String[] args) {
        // 디폴트 생성자로 클래스를 생성한 후 인스턴스 변숫값을 따로 초기화
        Person personKim = new Person();
        personKim.name = "김유신";
        personKim.weight = 85.5F;
        personKim.height = 180.0F;

        // 인스턴스 변수를 초기화하는 동시에 클래스 생성
        Person personLee = new Person("이순신", 175, 75);
    }
}
