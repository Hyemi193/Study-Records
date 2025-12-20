package classpart;

// 학생 이름과 주소를 출력하는 메서드

public class Student {
    int studentID;
    String studentName;
    int grade;
    String address;

    public void showStudentInfo() {
        System.out.println(studentName + "," + address);    // 이름, 주소 출력
    }

    // 학생 이름을 반환하는 메서드 구현
    public String getStudentName() {
        return studentName;
    }

    // 학생 이름을 부여하는 메서드 구현
    public void setStudentName(String name) {
        studentName = name;
    }

    // Student 클래스에 main() 함수 추가하기
    public static void main(String[] args) {
        Student studentAhn = new Student();     // Student 클래스 생성
        studentAhn.studentName = "안연수";

        System.out.println(studentAhn.studentName);
        System.out.println(studentAhn.getStudentName());
    }
}

