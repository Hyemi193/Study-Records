// 11 - 4 record 클래스
// 불변의 record 클래스 정의

package Recordclass;

    public record StudentInfo(int id, String name) {
        public static void main(String[] args) {

            Recordclass.StudentInfo studentInfo = new Recordclass.StudentInfo(12345, "최치원");
            Recordclass.StudentInfo studentInfo2 = new Recordclass.StudentInfo(12345, "최치원");

            System.out.println(studentInfo.equals(studentInfo2));
            System.out.println(studentInfo.name());
            System.out.println(studentInfo);
        }
}

// record 클래스의 사용 목적 : 필드값을 한 번 대입한 후 변하지 않고 사용하려는 것이 목적
// 자주 사용하는 get(), equals(), hashCode(), toString() 메서드와 public 생성자가 자동으로 생성되므로 편리하게 사용 가능