package Hiding;

public class StudentTest {
    public static void main(String[] args) {
        Student studentLee = new Student();

        // 오류발생 : private 외부 클래스 접근 불가능
        // studentLee.studentName = "이상원";

        // setStudentName() 메서드를 활용해 private 변수에 접근 가능
        studentLee.setStudentName("이상원");

        System.out.println(studentLee.getStudentName());
    }
}
