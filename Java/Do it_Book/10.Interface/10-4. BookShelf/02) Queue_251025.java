// 10 - 4 인터페이스 활용
// Queue 인터페이스 정의

package Bookshelf;

public interface Queue {
    void enQueue(String title);     // 배열의 맨 마지막에 추가
    String deQueue();               // 배열의 맨 처음 항목 반환
    int getSize();                  // 현재 Queue에 있는 요소 개수 반환
}
