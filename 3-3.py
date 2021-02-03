math=[]
name=[]
T=0
I=0
M=100
i = int(input('How many paople in this cless?'))
for k in range(i):
    stuname = input('How many people in cla?')
    score = int(input('Please input the score:'))
    T = T +score
    name.append(stuname)
    math.append(score)
for k in range(i):
    if I < score:
        high = math[k]
        highname = name[k]
        I = score
    if M > score:
        M = score
    math.append(score)
average = T / i
print(math)        
print('average',average)
print('I',I)
print('M',M)



