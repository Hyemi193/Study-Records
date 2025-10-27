// 12 - 1 제네릭이란?
// GenericPrinter<T> 클래스 정의

package Generics;

public class GenericPrinter<T> {
    private T material;     // T자료형으로 선언한 변수

    public void setMaterial(T material) {
        this.material = material;
    }

    public T getMaterial() {
        return material;        // T 자료형 변수 material을 반환하는 제네릭 메서드
    }

    public String toString() {
        return material.toString();
    }
}
