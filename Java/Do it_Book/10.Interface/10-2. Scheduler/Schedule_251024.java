// 10 - 2 인터페이스와 다형성
// Scheduler 인터페이스 정의

package Scheduler;

public interface Scheduler {
    public void getNextCall();      // 추상메서드
    public void sendCallToAgent();  // 추상메서드
}
