// 향상된 for문 사용하기

package Array;

public class EnhancedForLoop {
    public static void main(String[] args) {
        String[] strArray = {"Java", "Android", "C", "JavaScript", "Python"};

        // 배열의 처음에서 끝까지 모든 요소를 참조할 때 사용
        for (String lang : strArray) {  // 변수(lang)에는 배열의 각 요소 대입
            System.out.println(lang);
        }
    }
}
