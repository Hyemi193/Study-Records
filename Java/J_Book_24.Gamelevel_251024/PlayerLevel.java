// 템플릿 메서드를 활용한 프로그램 구현하기
// PlayerLevel 추상 클래스 구현

package Gamelevel;

public abstract class PlayerLevel {
    public abstract void run();
    public abstract void jump();
    public abstract void turn();
    public abstract void showLevelMessage();

    // 템플릿 메서드
    final public void go(int count) {   // 재정의되면 안 되므로 final로 선언
        run();
        for (int i = 0; i < count; i++) {
            jump();
        }
        turn();
    }
}
