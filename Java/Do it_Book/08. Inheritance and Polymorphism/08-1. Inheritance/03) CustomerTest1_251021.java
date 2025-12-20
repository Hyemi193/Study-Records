package Inheritance;

public class CustomerTest1 {
    public static void main(String[] args) {
//        Customer customerJi = new Customer();

        // customerID와 customerName은 protected 변수이므로 set() 메서드로 호출
//        customerJi.setCustomerID(10010);
//        customerJi.setCustomerName("이순신");

//        customerJi.bonusPoint = 1000;
//        System.out.println(customerJi.showCusomerInfo());
//
//
        h_VIPCustomer customerKim = new h_VIPCustomer(10020, "김유신", 1002);

//        // customerID와 customerName은 protected 변수이므로 set() 메서드로 호출
//        customerKim.setCustomerID(10020);
//        customerKim.setCustomerName("김유신");
        customerKim.bonusPoint = 10000;
        System.out.println(customerKim.showCusomerInfo());
    }
}
