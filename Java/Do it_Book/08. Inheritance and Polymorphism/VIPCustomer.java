// VIPCustomer 클래스 구현하기

package Inheritance;

public class VIPCustomer {
    // customer 클래스와 겹치는 인스턴스 변수
    private int customerID;
    private String customerName;
    private String customerGrade;
    int bonusPoint;
    double bonusRatio;

    // VIP 고객 관련 기능을 구현할 때만 필요한 인스턴스 변수
    private int agentID;    // VIP 고객 담당 상담원 아이디
    double saleRatio;       // 할인률

    // 디폴트 생성자
    public VIPCustomer() {
        customerGrade = "VIP";      // 고객 등급 VIP
        bonusRatio = 0.05;          // 보너스 적립률 5%
        saleRatio = 0.01;           // 할인율 10%
    }

    public int calcPrice(int price) {
        bonusPoint += price * bonusRatio;
        return price - (int)(price * saleRatio);    // 할인율 적용
    }

    // VIP고객에게만 필요한 메서드
    public int getAgentID() {
        return agentID;
    }

    public String showCustomerInfo() {
        return customerName + " 님의 등급은 " + customerGrade + "이며, 보너스 포인트는 " + bonusPoint + "입니다.";
    }
}
