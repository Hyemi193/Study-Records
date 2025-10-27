// 11 - 2 String 클래스
// 두 문자열 연결

package String;

public class StringTest2 {
    public static void main(String[] args) {
        String javaStr = new String("java");
        String androidStr = new String("android");

        System.out.println(javaStr);
        System.out.println("처음 문자열 주솟값 : " + System.identityHashCode(javaStr));

        javaStr = javaStr.concat(androidStr);   // 문자열 javaStr과 문자열 androidStr을 연결하여 javaStr에 대입

        System.out.println(javaStr);
        System.out.println("연결된 문자열 주솟값 : " + System.identityHashCode(javaStr));
    }
}

// 문자열은 불변하므로 javaStr 변숫값 자체가 변하는 것이 아니라 새로운 문자열이 생성됨
