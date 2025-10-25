// 11 - 1 Object 클래스
// String 클래스의 hashCode() 메서드 사용

package Object;

public class HashCodeTest {
    public static void main(String[] args) {
        String str1 = new String("abc");
        String str2 = new String("abc");

        // abc 문자열의 해시 코드값 출력
        System.out.println(str1.hashCode());    // 96354
        System.out.println(str2.hashCode());    // 96354
    }
}
