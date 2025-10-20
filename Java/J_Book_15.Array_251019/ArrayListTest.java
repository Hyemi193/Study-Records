// ArrayList 클래스 사용하기

package Array;
import java.util.ArrayList;     // ArrayList 클래스를 임포트함

public class ArrayListTest {
    public static void main(String[] args) {
        // ArrayList 선언
        ArrayList<Book> library = new ArrayList<Book> ();

        // add() 메서드로 요솟값 추가
        library.add(new Book("태백산맥", "조정래"));
        library.add(new Book("데미안", "헤르만 헤세"));
        library.add(new Book("어떻게 살 것인가", "유시민"));
        library.add(new Book("토지", "박경리"));
        library.add(new Book("어린왕자", "생텍쥐페리"));

        // 배열에 추가된 요소 개수만큼 출력
        for (int i = 0; i < library.size(); i++) {  // size() : 배열에 추가된 요소 전체 개수를 반환
            Book book = library.get(i); // get() : 요소를 하나 가져오는 메서드
            book.showBookInfo();
        }
        System.out.println();   // 행 출력 끝난 후 한 줄 띄움

        System.out.println("=== 향상된 for문 사용 ===");
        for (Book book : library) {
            book.showBookInfo();
        }
    }
}
