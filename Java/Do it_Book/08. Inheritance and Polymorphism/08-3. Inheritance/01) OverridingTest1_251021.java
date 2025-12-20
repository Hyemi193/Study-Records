// 재정의된 calcPrice() 메서드 확인

package Inheritance;

public class OverridingTest1 {
    public static void main(String[] args) {
        Customer customerLee = new Customer(10010, "이순신");
        customerLee.bonusPoint = 1000;

        h_VIPCustomer customerKim = new h_VIPCustomer(10020, "김유신", 12345);
        customerKim.bonusPoint = 10000;

        int price = 10000;
        System.out.println(customerLee.getCustomerName() + " 님이 지불해야 하는 금액은 " +
                customerLee.calcPrice(price) + "원입니다.");    // 이순신 님이 ~ 10000원입니다.
        System.out.println(customerKim.getCustomerName() + " 님이 지불해야 하는 금액은 " +
                customerKim.calcPrice(price) + "원입니다.");    // 김유신 님이 ~ 9000원입니다.
    }
}
