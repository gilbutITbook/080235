#
# 아이템 84
#
# words.py
#
class Player:
    """게임 플레이어를 표현한다

    하위클래스는 `tick` 메서드를 오버라이드해서 플레이어의 파워 레벨 등에 맞는
    움직임 애니메이션을 제공할 수 있다

    공개 애트리뷰트:
    - power: 사용하지 않은 파워업들(0과 1사이의 float)
    - coins: 현재 레벨에서 발견한 코인 개수(integer)
    """
    ...

def palindrome(word):
    """Return True 주어진 단어가 회문인 경우"""
    return word == word[::-1]

assert palindrome('tacocat')
assert not palindrome('banana')
