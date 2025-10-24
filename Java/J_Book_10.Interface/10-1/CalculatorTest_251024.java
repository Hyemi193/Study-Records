// 10 - 1 인터페이스란?
// CompleteCalc 클래스 실행

package Interfaceex;

public class CalculatorTest {
    public static void main(String[] args) {
        int num1 = 10;
        int num2 = 5;

        // Calculator 클래스는 추상 클래서, Calc 인터페이스는 추상 메서드만으로 선언했기에 인스턴스 생성 불가능
        CompleteCalc calc = new CompleteCalc();
        System.out.println(calc.add(num1, num2));
        System.out.println(calc.substract(num1, num2));
        System.out.println(calc.times(num1, num2));
        System.out.println(calc.divide(num1, num2));
        calc.showInfo();
    }
}
