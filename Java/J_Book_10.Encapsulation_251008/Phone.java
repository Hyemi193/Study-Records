// 핸드폰 클래스 구현

package Encapsulation;

public class Phone {
    // 모델(model), 가격(price) 두 인스턴스 변수를 private으로 선언
    private String model;
    private double price;

    public Phone(String model, double price) {
        this.model = model;
        this.price = price;
    }
    public String getModel() {
        return model;
    }
    public double getPrice() {
        return price;
    }
}
