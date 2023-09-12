def solution(s):
    words = s.split(" ")
    result = []
    for word in words:
        if word and word[0].isalpha():
            result.append(word[0].upper()+word[1:].lower())
        else:
            result.append(word.lower())
    return " ".join(result)