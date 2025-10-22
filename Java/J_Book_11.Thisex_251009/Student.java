// 빌더 패턴으로 Student 클래스 수정하기
package Thisex.builder;

public class Student {
    private int id;
    private String name;
    private int grade;
    private String major;
    private String phoneNumber;

    // Student 객체에 Builder 클래스를 매개변수로 받는 생성자를 만들고 Builder의 속성값을 Student 속성값으로 대입
    private Student(Builder builder) {
        this.id = builder.id;
        this.name = builder.name;
        this.grade = builder.grade;
        this.major = builder.major;
        this.phoneNumber = builder.phoneNumber;
    }

    // Builder 클래스를 선언해 Student 클래스의 각 속성에 값을 각각 대입해 줄 수 있는 메서드를 구현
    public static class Builder {
        private int id;
        private String name;
        private int grade;
        private String major;
        private String phoneNumber;

        // Builder 클래스의 생성자로, id와 name을 받음
        public Builder(int id, String name) {
            this.id = id;
            this.name = name;
        }

        // Student 클래스의 속성에 값을 대입해 줄 수 있는 메서드를 구현
        public Builder grade(int grade) {
            this.grade = grade;
            return this;
        }

        public Builder major(String major) {
            this.major = major;
            return this;
        }

        public Builder phoneNumber(String phoneNumber) {
            this.phoneNumber = phoneNumber;
            return this;
        }

        // build() 메서드로 Student 인스턴스를 생성해 반환
        public Student build() {
            return new Student(this);
        }
    }

    // showInfo() 메서드로 Student 객체 정보를 출력
    public void showInfo() {
        System.out.println("학번 : " + id);
        System.out.println("이름 : " + name);
        System.out.println("학년 : " + grade);
        System.out.println("전공 : " + major);
        System.out.println("전화번호 : " + phoneNumber);
    }

    // Student.Builder 내부 클래스 생성 후 각 속성값을 넣을 메서드를 호출하고 마지막에 build() 메서드를 호출
    public static void main(String[] args) {
        Student student = new Student.Builder(12345, "김원상")
                .grade(3)
                .major("컴퓨터공학")
                .phoneNumber("123-345-7890")
                .build();

        student.showInfo();
    }
}
