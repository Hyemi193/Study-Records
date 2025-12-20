// 추상클래스란?
// NoteBook 클래스 구현하기

package Abstractex;

public abstract class NoteBook extends Computer{
    @Override
    public void display() {
        System.out.println("NoteBook display()");
    }
}

// 부모 클래스가 추상 클래스일때 자식이 일부만 구현한 경우 자식도 추상 클래스가 됨 (객체 생성 불가능)
