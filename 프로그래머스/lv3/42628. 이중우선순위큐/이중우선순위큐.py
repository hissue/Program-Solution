def solution(operations):
    deq = []
    for operation in operations:
        op, num = operation.split(" ")
        if op == "I":
            deq.append(int(num))
            deq.sort()
        else:
            if num == "-1":
                deq = deq[1:]
            else:
                deq = deq[:-1]

    return [max(deq),min(deq)] if deq else [0,0] 