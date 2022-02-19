import random
paixnidia=0      
scorepirgos=0   
scoreajiomat=0
scoreaspros=0
scorebasilisa=0
scoremauros=0
while paixnidia<100:
    gameend=False
    scorebasilisamax=0
    stili0=[0,0,0,0,0,0,0,0]
    stili1=[0,0,0,0,0,0,0,0]
    stili2=[0,0,0,0,0,0,0,0]
    stili3=[0,0,0,0,0,0,0,0]
    stili4=[0,0,0,0,0,0,0,0]
    stili5=[0,0,0,0,0,0,0,0]
    stili6=[0,0,0,0,0,0,0,0]
    stili7=[0,0,0,0,0,0,0,0]
    matrix=[stili0,stili1,stili2,stili3,stili4,stili5,stili6,stili7]
    x1=random.randint(0,7)
    y1=random.randint(0,7)
    x2=random.randint(0,7)
    y2=random.randint(0,7)
    x3=random.randint(0,7)
    y3=random.randint(0,7)
    while x1==x2 and y1==y2 and x1==x3 and y1==y3 : 
        x1 = random.randint(0,7)
        y1 = random.randint(0,7)
    matrix[x1][y1] = 1  
    matrix[x2][y2] = 2
    matrix[x3][y3] = 3
    if x1 == x3 or y1 == y3 : 
        scorepirgos+=1
        gameend= True
    if (x3+y3==x2+y2) or (x3-y3==x2-y2): 
        scoreajiomat+=1
        gameend=True
    if x3 == x1 or y3 == y1 or x2==x3 or y2==y3 and scorebasilisamax<2:
        scorebasilisa+=1
        scorebasilisamax+=1
        gameend=True
    if gameend== True:
        paixnidia+=1
scoreaspros=scorepirgos+scoreajiomat
print("paixnidia poy paixtikan : " , paixnidia )
print("score tou asprou paixth : " , scoreaspros )
print("score tou mavrou paixth : " , scorebasilisa )
