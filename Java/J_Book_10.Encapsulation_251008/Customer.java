package Encapsulation;

public class Customer {
    // 이름(name), 예산(budget) 두 속성 모두 private로 선언
    private String name;
    private double budget;

    public Customer(String name, double budget) {
        this.name = name;
        this.budget = budget;
    }

    // getBudget() 메서드는 budget(예산)을 반환
    public double getBudget() {
        return budget;
    }

    // buyPhone() 메서드는 PhoneStore 객체를 매개변수로 받아 고객이 핸드폰을 구매하는 기능을 구현
    public void buyPhone(PhoneStore store) {
        Phone phone = store.sellPhone("아이폰", budget);
        if (phone != null) {
            System.out.println("고객 : 핸드폰 구입이 완료되었습니다.");
        }
        else {
            System.out.println("고객 : 핸드폰을 구입하지 못했습니다.");
        }
    }
}
