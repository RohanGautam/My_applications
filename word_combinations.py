#This is a program to beat the traditional 'Jumble' newspaper game.
#the user enters the scrambled word, program outputs 
#a word that makes sense(is a part of the english dictionary)
from nltk.corpus import wordnet
import itertools
while True:
    letters=raw_input('Enter the letters:')
    if wordnet.synsets(letters):
        print 'Already a word!!'
    perms=[''.join(i) for i in itertools.permutations(letters) if wordnet.synsets(''.join(i))]
    print 'Possible words are:'
    for y in perms: print y   
    y=raw_input('Do you want to continue?(y/n)')
    if y=='n':
        print 'Thanks for playing!'
        break
print '<------------------------>'



