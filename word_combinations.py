#this is a program to beat the traditional 'Jumble' newspaper game.
#the user enters the scrambled word, program outputs a word that makes sense(is a part of the english dictionary)
import random
from nltk.corpus import wordnet
while True:
    letters=raw_input('Enter the letters:')
    if wordnet.synsets(letters):
        print 'Already a word!!'
        break
    unique_letters=list(set(letters))    
    def factorial(x):
        ans=1
        while x>0:
            ans*=x
            x-=1
        return ans
    length=len(letters)
    n=factorial(length)
    L=[]
    
    while n<>len(L):
        x=random.sample(range(length),length)
        if x not in L:
            L.append(x)
    
    
    outcomes=[]
    for x in L:
        st=''
        for i in x:
            st+=letters[i]
        if st not in outcomes:
            outcomes.append(st)
    outcomes.sort()
    
    d={}
    for x in unique_letters:
        d[x]=[y for y in outcomes if y[0]==x]
    print 'Possible words are:' 
    for a in d:       
        for i in d[a]:
            if wordnet.synsets(i):
                print i,'\t',    
    print '\n'
    x=raw_input('Do you want to continue?(y/n)')
    if x=='n':
        print 'Thanks for playing!'
        break
print '<------------------------>'


