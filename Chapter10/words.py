# words.py
#!/usr/bin/env python3
"""단어의 언어 패턴을 찾을 떄 쓸 수 있는 라이브러리.

여러 단어가 서로 어떤 연관관계가 있는지 검사하는게 어려울 때가 있다!
이 모듈은 단어가 가지는 특별한 특성을 쉽게 결정할 수 있게 해준다.

사용 가능 함수:
- palindrome: 주어진 단어가 회문(palindrome, 앞으로 읽어도 뒤부터 읽어도 똑같은 경우)인지 결정한다.
- check_anagram: 주어진 단어가 어구전철(anagrams, 똑같은 글자들로 순서만 바뀐 경우)인지 결정한다.
...
"""

def find_anagrams(word, dictionary):
    """주어진 단어의 모든 어구전철을 찾는다.

    이 함수는 '딕셔너리' 컨테이너의 원소 검사만큼 빠른 속도로 실행된다.

    Args:
        word: 대상 단어. 문자열.
        dictionary: 모든 단어가 들어있는 collections.abc.Container 컬렉션.

    Returns:
        찾은 어구전철들로 이뤄진 리스트. 아무것도 찾지 못한 경우 Empty.
    """
    ...


def find_anagrams(word: str,
                  dictionary: Container[str]) -> List[str]:
    """주어진 단어의 모든 어구전철을 찾는다.

    이 함수는 '딕셔너리' 컨테이너의 원소 검사만큼 빠른 속도로 실행된다.

    Args:
        word: 대상 단어.
        dictionary: 모든 단어가 들어있는 컬렉션.

    Returns:
        찾은 어구전철들.
    """
    ...

