package perator;

public class OperationEx3 {
    public static void main(String[] args) {
        int num1 = 10;
        int i = 2;

        boolean value = ((num1 = num1 + 10) < 10) && ((i = i +2) < 10);
        // 논리 곱에서 앞 항의 결괏값이 거짓이므로 이 문장은 실행되지 않음
        System.out.println(value);
        System.out.println(num1);
        System.out.println(i);

        value = ((num1 = num1 + 10) > 10) || ((i = i +2) < 10);
        // 논리 합에서 앞 항의 결괏값이 참이므로 이 문장은 실행되지 않음
        System.out.println(value);
        System.out.println(num1);
        System.out.println(i);
    }
}
        /* 단락 회로 평가(Short Circuit Evaluation : SCE) : 논리 곱 연산과 합 연산을 할 때 두 항을 모두 실행하지 않더라도
           결괏값을 알 수 있는 경우에, 나머지 항은 실행되지 않는 것 */



