import collections
def solution(spell, dic):
    temp = collections.Counter(spell)
    for name in dic:
        answer = temp - collections.Counter(name)
        if not answer:
            return 1
    return 2