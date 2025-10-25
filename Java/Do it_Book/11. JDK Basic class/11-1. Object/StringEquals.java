package Object;

public class StringEquals {
    public static void main(String[] args) {
        String str1 = new String("abc");
        String str2 = new String("abc");

        // 두 인스턴스 주솟값이 같은지 비교해 출력
        System.out.println(str1 == str2);
        // String 클래스의 equals() 메서드를 사용. 두 인스턴스의 문자열값이 같은지를 비교해 출력
        System.out.println(str1.equals(str2));
    }
}

