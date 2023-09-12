def solution(s):
    answer = sorted(list(map(int,s.split(" "))))
    return "{} {}".format(answer[0],answer[-1])