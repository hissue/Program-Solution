def solution(s):
    stack = []
    answer = ""
    words = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    for w in s:
        word = "".join(stack)
        # 문자인 경우
        if w.isalpha():
            if word+w in list(words.keys()):
                answer+=str(words[word+w])
                stack = []
            else:
                stack.append(w)
            
        # 숫자인 경우
        else:
            answer+=w
    return int(answer)