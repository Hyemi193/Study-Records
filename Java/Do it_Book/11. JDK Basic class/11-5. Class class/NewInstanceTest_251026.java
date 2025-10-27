// 11 - 5 Class 클래스
// Person 클래스의 인스턴스 생성하기

package Classex;

public class NewInstanceTest {
    public static void main(String[] args) throws ClassNotFoundException,
            InstantiationException, IllegalAccessException {
            // Class.forName()과 newInstance() 메서드를 사용하는 동안 발생하는 예외 처리에 관한 것

        Person person1 = new Person();  // 생성자로 생성
        System.out.println(person1);

        Class pClass = Class.forName("Classex.Person");
        Person person2 = (Person)pClass.newInstance();  // Class 클래스의 newInstance() 메서드로 생성
        System.out.println(person2);
    }
}

/* 리플렉션(reflection) : 클래스의 자료형을 모르는 상태에서 Class 클래스를 활용하여 그 클래스의 정보를 가져오고,
이 정보를 활용하여 인스턴스를 생성하거나 메서드를 호출하는 방식*/
