// 템플릿 메서드
// 추상 메서드 테스트하기

package Template;

public class CarTest {
    public static void main(String[] args) {
        System.out.println("=== 자율 주행하는 자동차 ===");
        Car myCar = new AICar();
        myCar.run();

        System.out.println("=== 사람이 운전하는 자동차 ===");
        Car herCar = new ManualCar();
        herCar.run();
    }
}

// 템플릿 메서드 : 메서드 실행 순서와 시나리오를 정의 하는 것
//
