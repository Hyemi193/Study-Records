// 상속을 활용해 VIPCustomer 클래스 구현
// calcPrice() 메서드 재정의

package Inheritance;

public class h_VIPCustomer extends Customer {   // VIPCustomer 클래스는 Customer 클래스를 상속받음
    private int agentID;
    double saleRatio;

//    public h_VIPCustomer() {
//        customerGrade = "VIP";    // 상위 클래스에서 private 변수이므로 ERROR
//        bonusRatio = 0.05;
//        saleRatio = 0.1;
//        System.out.println("VIPCustomer() 생성자 호출");     // 하위 클래스를 생성할 때 출력되는 콘솔 출력물
//    }

    // 명시적으로 상위 클래스 생성자 호출
    public h_VIPCustomer(int customerID, String customerName, int agentID) {
        super(customerID, customerName);
        customerGrade = "VIP";
        bonusRatio = 0.05;
        saleRatio = 0.1;
        this.agentID = agentID;
//        System.out.println("VIPCustomer(int, String, int) 생성자 호출");
    }

    public int getAgentID() {
        return agentID;
    }

    public String showVIPInfo() {
        return super.showCusomerInfo() + "담당 상담원 아이디는 " + agentID + "입니다.";
    }

    @Override
    /* 메서드 오버라이딩 : 상위 클래스에 정의한 메서드가 하위 클래스에서 구현할 내용과 맞지 않을 경우에
    하위 클래스에서 이 메서드를 재정의 하는 것
     */
    public int calcPrice(int price) {
        bonusPoint += price * bonusRatio;           // 보너스 포인트 적립
        return price - (int)(price * saleRatio);    // 할인율을 적용한 가격 반환
    }
}
