from collections import Counter

numTest = int(input())
for i in range(numTest):
    Tshirts = list(map(str,input().split()))
    for i in range(len(Tshirts[0])):
        Tshirt1 = Counter(Tshirts[0])
        Tshirt2 = Counter(Tshirts[1])
        
    if Tshirt1 == Tshirt2:
        print('=')
    elif Tshirt1['S'] == 1 and Tshirt2['M']==1 or Tshirt1['S'] == 1 and Tshirt2['L']==1:
        print('<')  
    elif Tshirt1['L'] == 1 and Tshirt2['M']== 1 or Tshirt1['L'] == 1 and Tshirt2['S']== 1:
        print('>')
    elif Tshirt1['M']== 1 and Tshirt2['L']== 1:
        print('<')
    elif Tshirt1['M']== 1 and Tshirt2['S']== 1:
        print('>')
    elif Tshirt1['S'] == 1 and Tshirt2['S'] == 1  and Tshirt1['X'] < Tshirt2['X']:
        print('>')
    elif Tshirt1['S'] == 1 and Tshirt2['S'] == 1 and Tshirt1['X'] > Tshirt2['X']:
        print('<')
    elif Tshirt1['L'] == 1 and Tshirt2['L'] == 1 and Tshirt1['X'] < Tshirt2['X']:
        print('<')
    elif Tshirt1['L'] == 1 and Tshirt2['L'] == 1 and Tshirt1['X'] > Tshirt2['X']:
        print('>')
    
