// 추상 클래스란?
// MyNoteBook 클래스 구현하기

package Abstractex;

public class MyNoteBook extends NoteBook{
    @Override
    public void typing() {
        System.out.println("MyNoteBook typing()");
    }
}

// 부모 클래스(Computer, NoteBook)에서 물려받은 추상 메서드들을 모두 구현했기 때문에 abstract 예약어를 사용하지 않음 (객체 생성 가능)
