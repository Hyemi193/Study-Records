// 추상 클래스란?
// 추상 클래스 상속받기와 구현하기

package Abstractex;

public class DeskTop extends Computer{
    @Override
    public void display() {
        // 추상 메서드의 몸체
        System.out.println("DeskTop display()");
    }

    @Override
    public void typing() {
        // 추상 메서드의 몸체
        System.out.println("DeskTop typing()");
    }
}

// 부모인 Computer 클래스가 추상 클래스일때 자식이 모든 추상 메서드를 구현한 경우 일반 클래스가 됨 (객체 생성 가능)
