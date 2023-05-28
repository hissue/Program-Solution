def solution(babbling):
    count = 0
    words = [ "aya", "ye", "woo", "ma" ]
    for b in babbling:
        for word in words:
            if word * 2 not in b:
                b = b.replace(word, ' ')
        if b.strip() == '':
            count += 1
    return count