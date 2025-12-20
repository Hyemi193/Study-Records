// 템플릿 메서드
// 추상 클래스와 템플릿 메서드 구현하기

package Template;

public abstract class Car {
    public abstract void drive();
    public abstract void stop();

    public void startCar() {
        System.out.println("시동을 켭니다.");
    }

    public void turnOff() {
        System.out.println("시동을 끕니다.");
    }

    // 템플릿 메서드
    // final 예약어 사용 이유 : 상위 클래스를 상속 받은 하위 클래스에서 템플릿 메서드를 재정의 하면 안됨
    final public void run() {
        startCar();
        drive();
        stop();
        turnOff();
    }
}
