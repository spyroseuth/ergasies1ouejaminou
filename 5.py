from collections import Counter
txtopen=open('readme.txt','r')
txt=txtopen.read()
for letter in txt:
    if letter.isupper():
        txt = txt.replace(letter,letter.lower())
splittxt= txt.split()
counter=Counter(splittxt)
popularten=counter.most_common(10)
def split(word):
    return [char for char in word]
print 'Οι δέκα δημοφιλέστερες λέξεις ειναι: ', popularten
letters2listfinal=[]
letters2list=[]
letters2=''
for i in range(len(splittxt)):
    words=split(splittxt[i])
    letters2list=words[:2]
    letters2=''.join(letters2list)
    letters2listfinal.append(letters2)
counter2=Counter(letters2listfinal)
popular2=counter2.most_common(3)
print 'Οι τρεις δημοφιλέστεροι συνδυασμοί δύο πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις είναι: ',popular2

letters3listfinal=[]
letters3list=[]
letters3=''
for i in range(len(splittxt)):
    words=split(splittxt[i])
    letters3list=words[:3]
    letters3=''.join(letters3list)
    letters3listfinal.append(letters3)
counter3=Counter(letters3listfinal)
popular3=counter3.most_common(3)
print 'Οι τρεις δημοφιλέστεροι συνδυασμοί τριών πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις είναι: ', popular3
