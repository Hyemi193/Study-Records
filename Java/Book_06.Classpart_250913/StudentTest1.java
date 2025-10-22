package classpart;

// 인스턴스 여러 개 생성

public class StudentTest1 {
    public static void main(String[] args) {
        Student student1 = new Student();       // 첫 번째 학생 생성
        student1.studentName = "안연수";         // 멤버 변수 사용
        System.out.println(student1.getStudentName());      // 메서드 사용
        Student student2 = new Student();       // 두 번째 학생 생성
        student2.studentName = "안승연";
        System.out.println(student2.getStudentName());
    }
}
