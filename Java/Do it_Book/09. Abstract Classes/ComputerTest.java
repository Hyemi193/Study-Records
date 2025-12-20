// 추상 클래스란?
// 추상 클래스 테스트

package Abstractex;

public class ComputerTest {
    public static void main(String[] args) {
        // Computer c1 = new Computer();    // 추상 클래스는 인스턴스로 생성 불가능
        Computer c2 = new DeskTop();
        // Computer c3 = new NoteBook();    // 추상 클래스는 인스턴스로 생성 불가능
        Computer c4 = new MyNoteBook();
    }
}

/* Computer 클래스의 경우, 전원을 켜고 끄는 기능을 하는 turnOn(), turnOff()를 구현해 하위 클래스에 공유해도 무방하지만,
display(), typing()은 NoteBook인지 DeskTop인지에 따라 구현 내용이 달라지므로 Computer 클래스에서는 구현하지 않은 것 */