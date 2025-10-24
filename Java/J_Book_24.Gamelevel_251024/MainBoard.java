// 템플릿 메서드를 활용한 프로그램 구현하기
// 테스트 프로그램 구현

package Gamelevel;

public class MainBoard {
    public static void main(String[] args) {
        Player player = new Player();   // 처음 생성하면 BeginnerLevel로 시작
        player.play(1);           // 초보자 플레이 (점프 1번)

        AdvancedLevel aLevel = new AdvancedLevel();
        player.upgradeLevel(aLevel);
        player.play(2);           // 중급자 플레이 (점프 2번)

        SuperLevel sLevel = new SuperLevel();
        player.upgradeLevel(sLevel);
        player.play(3);           // 고급자 플레이 (점프 3번)
    }
}
