// studentName 변수 사용하기

package Staticex;

public class StudentTest5 {
    public static void main(String[] args) {
        System.out.println(Student2.getSerialNum());    // 인스턴스 생성 없이 호출 가능
        // 클래스 메서드 내부에서 지역 변수와 클래스 변수는 사용할 수 있지만, 인스턴스 변수는 사용 불가능

    }
}
