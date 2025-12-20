package Singleton;

public class CompanyTest {
    public static void main(String[] args) {
        // 클래스 이름으로 getinstance()을 호출하여 참조 변수에 대입
        Company myCompany1 = Company.getInstance();
        Company myCompany2 = Company.getInstance();

        // 두 변수가 같은 주소인지 확인
        System.out.println(myCompany1 == myCompany2);
    }
}

