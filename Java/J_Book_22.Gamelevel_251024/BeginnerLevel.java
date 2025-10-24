// 템플릿 메서드를 활용한 프로그램 구현하기
// 초급자 레벨 클래스 구현

package Gamelevel;

public class BeginnerLevel extends PlayerLevel{
    @Override
    public void run() {
        System.out.println("천천히 달립니다.");
    }

    @Override
    public void jump() {
        System.out.println("Jump할 줄 모르지롱.");
    }

    @Override
    public void turn() {
        System.out.println("Turn할 줄 모르지롱.");
    }

    @Override
    public void showLevelMessage() {
        System.out.println("***** 초급자 레벨입니다. *****");
    }
}
