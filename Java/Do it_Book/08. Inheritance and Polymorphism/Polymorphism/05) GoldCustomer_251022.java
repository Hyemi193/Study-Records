// GoldCustomer 클래스 추가

package Witharraylist;

public class GoldCustomer extends Customer{
    double saleRatio;

    public GoldCustomer(int customerID, String customerName) {
        super(customerID, customerName);
        customerGrade = "Gold";
        bonusRatio = 0.02;
        saleRatio = 0.1;
    }

    // 재정의한 메서드
    @Override
    public int calcPrice(int price) {
        bonusPoint += price * bonusRatio;
        return price - (int)(price * saleRatio);
    }
}
