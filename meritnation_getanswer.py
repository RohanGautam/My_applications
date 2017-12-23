'''With this, one can get all the answers to a given question on a site called meritnation.
Meritnation is a student-oriented site where teachers answer questions and stuff.
You need to "log in"(not with facebook, google or anything), and need to give your phone number to access the full answer(s).
This is just a really simple workaround that gets the answer and saves it in an html file and can thus be viewed, including all the mathml formulae.'''
import requests,re
link=raw_input('Enter meritnation answer link:')
pagesrc=requests.get(link)
pattern=r'<div class="ans_text">.*?<\/div>' #non-greedy selection
f=open(r'answer.html','w+')
f.write('\n-------------------------------------------------------------------------------'.join(re.findall(pattern,pagesrc.text)))
print '\n\nAnswer saved in "answer.html" !!'
f.close()