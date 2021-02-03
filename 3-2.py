math=[]
T=0
I=0
M=100
i = int(input('How many paople in this cless?'))
for k in range(i):
    score = int(input('Please input the score:'))
    T = T +score
    if I < score:
        I = score
    if M > score:
        M = score
    math.append(score)
average = T / i
print(math)        
print('average',average)
print('I',I)
print('M',M)






