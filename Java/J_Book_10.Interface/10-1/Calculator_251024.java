// 10 - 1 인터페이스란?
// Calculator 클래스에서 인터페이스 구현

package Interfaceex;

public abstract class Calculator implements Calc {   // 추상클래스
    @Override
    public int add(int num1, int num2) {
        return num1 + num2;
    }

    @Override
    public int substract(int num1, int num2) {
        return num1 - num2;
    }
}
