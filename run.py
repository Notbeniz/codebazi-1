word=list(input('>>'))
for i in range(len(word)):
    for j in range(i):
        word[j]=word[i]
    print(''.join(word))