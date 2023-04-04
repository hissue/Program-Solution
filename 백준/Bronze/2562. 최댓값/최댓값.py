max = 0
m_idx = 0
for i in range(9):
    temp = int(input())
    if temp > max:
        max = temp
        m_idx = i+1
print(max)
print(m_idx)