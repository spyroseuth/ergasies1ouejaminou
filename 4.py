import random

xartia = []
figures = ["J", "Q", "K"]
xarti = [i for i in range(1, 11)] + figures
color = ["H", "S", "C", "D"]
player1start=[10]+figures
player2start=random.randint(1,11)
p1w=0
p2w=0
draws=0 #metrites
for i in range(1):
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[random.choice(player1start)]
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        # print (player1)
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
        print(sum1)
    if sum1>21:
        print("P2 wins!")
        p2w+=1
    else:
        '''
        sxolia pollwn
        grammwn
        '''

        print("P2 joins the game") #let me add one more player
        player2=[player2start]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            # print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
            print(sum2)
        if sum2>21:
            sum2=0
        if sum1>sum2:
            print("P1 wins!")
            p1w+=1
        elif sum2>sum1:
            print("P2 wins!")
            p2w+=1
        else:
            print("draw!")
            draws+=1
print p1w,p2w,draws
