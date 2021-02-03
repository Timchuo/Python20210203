math=[]
T=0
I=0
M=100
i = int(input('How many paople in this cless?'))
for k in range(i):
    score = int(input('Please input the score:'))
    stuname= int(input('Pleas input the name'))
    T = T +score
    if I < score:
        I = score
    if M > score:
        M = score
    math.append(stuname)
    math.append(score)
for k in range(i):
    if math[i]>I:
        hugh=math[i]
        highname=math[i-1]
for k in range(i):
    if math[i]>I
        I=math[i]
        highname=muth[i-1]
average = T / i
print(math)        
print('average',average)
print('I',I,highname)
print('M',M,lowname)