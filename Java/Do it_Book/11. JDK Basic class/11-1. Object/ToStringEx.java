// 11 - 1 Object 클래스
// Object 클래스의 toString() 메서드 사용

package Object;

class Book {
    int bookNumber;
    String bookTitle;

    // 책 번호와 제목을 매개변수로 입력받는 생성자
    Book(int bookNumber, String bookTitle) {
        this.bookNumber = bookNumber;
        this.bookTitle = bookTitle;
    }

// toString() 메서드 재정의
    @Override
    public String toString() {
        return bookTitle + "," + bookNumber;
    }
}
    public class ToStringEx {
        public static void main(String[] args) {
            Book book1 = new Book(200, "개미");

            System.out.println(book1);  // 인스턴스 정보(클래스 이름, 주솟값)를 출력
            System.out.println(book1.toString());   // toString() 메서드로 인스턴스 정보(클래스 이름, 주솟값)를 출력
        }
    }
