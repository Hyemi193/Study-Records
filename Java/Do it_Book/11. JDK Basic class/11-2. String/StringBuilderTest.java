// 11 - 2 String 클래스
// StringBuilder 클래스 사용

package String;

public class StringBuilderTest {
    public static void main(String[] args) {
        String javaStr = new String("Java");
        System.out.println("javaStr 문자열 주소 : " + System.identityHashCode(javaStr)); // 인스턴스가 처음 생성됐을 때 메모리 주소

        StringBuilder buffer = new StringBuilder(javaStr);  // String으로부터 StringBuilder 생성
        System.out.println("연산 전 buffer 메모리 주소 : " + System.identityHashCode(buffer));

        // 문자열 추가
        buffer.append(" and");
        buffer.append(" android");
        buffer.append(" programming is fun!!!");
        System.out.println("연산 후 buffer 메모리 주소 : " + System.identityHashCode(buffer));

        // String 클래스로 반환
        javaStr = buffer.toString();
        System.out.println(javaStr);
        System.out.println("새로 만들어진 javaStr 문자열 주소 : " + System.identityHashCode(javaStr));
    }
}
/*
String 클래스를 사용하여 문자열을 계속 연결하거나 변경하는 프로그램을 작성하면 메모리 낭비가 심함.
그래서 내부에 변경 가능한(final이 아닌) char[]를 변수로 가지고 있는 StringBuffer와 StringBuiler클래스를 사용하면
문제를 해결할 수 있음
 */
