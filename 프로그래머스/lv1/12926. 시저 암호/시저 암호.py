def solution(s, n):
    answer = ""
    for alp in s:
        if alp == " ":
            answer+=" "
        elif alp.isupper():
            answer+=chr(65+((ord(alp)+n)%65)%26)
        else:
            answer+=chr(97+((ord(alp)+n)%97)%26)

    return answer