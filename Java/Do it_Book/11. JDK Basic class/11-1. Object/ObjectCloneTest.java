// 11 - 1 Object 클래스
// clone() 메서드로 인스턴스 복제

package Object;

// 원점을 의미하는 Point 클래스
class Point {
    int x;
    int y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public String toString() {
        return "x = " + x + "," + "y = " + y;
    }
}

class Circle implements Cloneable {     // 객체를 복제해도 된다는 의미로 Cloneable 인터페이스를 함께 선언
    Point point;
    int radius;

    Circle(int x, int y, int radius) {
        this.radius = radius;
        point = new Point(x, y);
    }

    @Override
    public String toString() {
        return "원점은 " + point + "이고," + " 반지름은 " + radius + "입니다.";
    }

    @Override
    public Object clone() throws CloneNotSupportedException {
        return super.clone();
    }
}

public class ObjectCloneTest {
    public static void main(String[] args) throws CloneNotSupportedException {
        Circle circle = new Circle(10, 20, 30);
        Circle copyCircle = (Circle)circle.clone();

        System.out.println(circle);
        System.out.println(copyCircle);
        // identitiyHashCode()는 객체 참조를 기준으로 한 고유 해시 반환
        System.out.println(System.identityHashCode(circle));
        System.out.println(System.identityHashCode(copyCircle));
    }
}
