#
# 아이템 43
#
class FrequencyList(list):
    def __init__(self, members):
        super().__init__(members)

    def frequency(self):
        counts = {}
        for item in self:
            counts[item] = counts.get(item, 0) + 1
        return counts

foo = FrequencyList(['a', 'b', 'a', 'c', 'b', 'a', 'd'])
print('길이: ', len(foo))

foo.pop()
print('pop한 다음:', repr(foo))
print('빈도:', foo.frequency())

#
class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

bar = [1, 2, 3]
bar[0]

class IndexableNode(BinaryNode):
    def _traverse(self):
        if self.left is not None:
            yield from self.left._traverse()
        yield self
        if self.right is not None:
            yield from self.right._traverse()

    def __getitem__(self, index):
        for i, item in enumerate(self._traverse()):
            if i == index:
                return item.value
        raise IndexError(f'인덱스 범위 초과: {index}')

tree = IndexableNode(
    10,
    left=IndexableNode(
        5,
        left=IndexableNode(2),
        right=IndexableNode(
            6,
            right=IndexableNode(7))),
    right=IndexableNode(
        15,
        left=IndexableNode(11)))

print('LRR:', tree.left.right.right.value)
print('인덱스 0:', tree[0])
print('인덱스 1:', tree[1])
print('11이 트리 안에 있나?', 11 in tree)
print('17이 트리 안에 있나?', 17 in tree)
print('트리:', list(tree))

#
class SequenceNode(IndexableNode):
    def __len__(self):
        for count, _ in enumerate(self._traverse(), 1):
            pass
        return count

tree = SequenceNode(
    10,
    left=SequenceNode(
        5,
        left=SequenceNode(2),
        right=SequenceNode(
            6,
            right=SequenceNode(7))),
    right=SequenceNode(
        15,
        left=SequenceNode(11))
)

print('트리 길이:', len(tree))

#
from collections.abc import Sequence

class BadType(Sequence):
    pass

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#foo = BadType()

#
class BetterNode(SequenceNode, Sequence):
    pass

tree = BetterNode(
    10,
    left=BetterNode(
        5,
        left=BetterNode(2),
        right=BetterNode(
            6,
            right=BetterNode(7))),
    right=BetterNode(
        15,
        left=BetterNode(11))
)

print('7의 인덱스:', tree.index(7))
print('10의 개수:', tree.count(10))

