// 11 - 3 enum
// enum을 활용해 상수 사용하기

package Enumclass;

public enum GameLevel {
    BEGINNER_LEVEL(1, "초보자"),
    ADVANCED_LEVEL(2, "숙련자"),
    SUPER_LEVEL(3, "고수");

    // 상수가 가질 수 있는 속성을 인스턴스 변수로 선언
    private int level;
    private String hint;

    GameLevel (int level, String hint) {
        // 각 상수의 속성을 초기화
        this.level = level;
        this.hint = hint;
    }

    public int getLevel() {
        return level;
    }

    public String getHint() {
        return hint;
    }

// enum에서 toString() 메서드 사용
    public String toString() {
        return getHint();
    }

// enum의 values() 메서드 활용
    public static void main(String[] args) {
        /*GameLevel[] gameLevels = GameLevel.values();
        for (GameLevel level : gameLevels) {
            System.out.println(level);
        }*/

// ValueOf() 메서드로 상숫값 참조
        GameLevel gameLevel = GameLevel.valueOf("BEGINNER_LEVEL");
        System.out.println(gameLevel.getLevel());
        System.out.println(gameLevel.getHint());
    }
}

// enum : 상수들의 집합을 정의하는 특별한 클래스
// toString() : 객체를 문자열로 변환할 때 호출되는 메서드
// valueOf() : enum 상수를 문자열로 찾아서 반환하는 메서드