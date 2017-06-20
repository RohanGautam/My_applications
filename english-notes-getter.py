'''program to get all the "restricted"(lmao) content in the subject 
english from academicseasy.com .
As of today (20/6/17) I'm in 12th grade and this website i go to for notes tells
me that the content is 'protected' and i cant view the page source, even with
the chrome allow copy extension on. So i take it upon myself to get the notes for
every chapter of every english book that i have this year.
To anyone who happens to need this (i dont know why) ,you can use this freely :)

Uncomment the below urls for links to different book chapters
'''

import requests,re
#flamingo
#urls=[r'http://academicseasy.com/2013/10/class-xii-flamingo-last-lesson.html',
#      r'http://academicseasy.com/2016/05/xii-flamingo-lost-spring.html',
#      r'http://academicseasy.com/2013/10/class-xii-flamingo-deep-water.html',
#      r'http://academicseasy.com/2013/10/class-xii-flamingo-rattrap.html',
#      r'http://academicseasy.com/2013/10/class-xii-flamingo-indigo.html',
#      r'http://academicseasy.com/2013/10/class-xii-flamingo-going-places.html',
#      r'http://academicseasy.com/2013/10/class-xii-poetry-my-mother-at-sixty-six.html',
#      r'http://academicseasy.com/2013/10/class-xii-poetry-my-mother-at-sixty-six.html',
#      r'http://academicseasy.com/2013/10/class-xii-poetry-elementary-school.html',
#      r'http://academicseasy.com/2013/10/class-xii-poetry-keeping-quiet.html',
#      r'http://academicseasy.com/2013/10/class-xii-poetry-thing-of-beauty.html',
#      r'http://academicseasy.com/2013/10/aunt-jennifers-tigers-byadrienne-rich.html'
#      ]

#silas marner
#urls=[r'http://academicseasy.com/2016/05/class-xii-novel-silas-marner.html']

#vistas
#urls=[r'http://academicseasy.com/2013/10/class-xii-vistas-tiger-king.html',
#      r'http://academicseasy.com/2013/10/class-xii-vistas-enemy.html',
#      r'http://academicseasy.com/2013/10/class-xii-vistas-should-wizard-hit-mommy.html',
#      r'http://academicseasy.com/2013/10/class-xii-vistas-on-face-of-it.html',
#      r'http://academicseasy.com/2013/10/class-xii-vistas-evans-tries-o-level.html',
#      r'http://academicseasy.com/2013/10/class-xii-vistas-memories-of-childhood.html'
#      ]
for url in urls:
    name=re.findall(r'(?<=\d\/\d\d\/).*(?=\.html$)',url)[0]
    name=re.sub('class-xii-|xii-','',name)
    r=requests.get(url)
    text=(r.text).encode('utf-8')
    pattern1=re.compile(r'.*<div class="entry-content clearfix">',re.DOTALL)
    text=pattern1.sub('',text)
    pattern2=re.compile(r'<div class="post-views.*',re.DOTALL)
    text=pattern2.sub('',text)
    pattern3=re.compile(r"<div class='code-block code-block.*?<\/div>",re.DOTALL)
    text=pattern3.sub('',text)
    with open(r'{}.html'.format(name),'w+') as  f:f.write(text)
