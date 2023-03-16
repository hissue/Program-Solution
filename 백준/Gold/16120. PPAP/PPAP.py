import sys

words = sys.stdin.readline().rstrip()
stk = []
PPAP = ['P','P','A','P']

for word in words:
    stk.append(word)
    if stk[-4:] == PPAP:
        stk.pop()
        stk.pop()
        stk.pop()
        
if stk[0] != 'A' and len(stk) == 1:
    print('PPAP')

else:
    print('NP')