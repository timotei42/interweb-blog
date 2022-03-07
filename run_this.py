from list_folders import getnames
import generate
import os
import datetime
from os.path import exists
import shutil

#gets the content of paragraph via returned parameter from main function
CONTENT=generate.main()

#writes the index of articles
def make_archive():
    file=open('pieces/blog.txt')
    content=file.read()
    History=str(LIST)
    MAR=""
    for i in History:
        MAR=MAR+i
    MAR=MAR.replace("]","")
    MAR=MAR.replace("[","")
    MAR=MAR.replace(",","")
    MAR=MAR.replace("'","")
    MAR=MAR.replace('"','')
    content=content.replace("$ARTICLE",MAR)
    with open('blog.html','w') as html:
      for i in content:
        html.write(i)
    html.close()
    file.close()
#adds content of article to rss feed of site
def make_rss(name_array,date_array,paragraphs):
    want_rss=input("Refresh RSS feed? y/n ")
    if want_rss == "y":
     RSS=[]
     RSS.append("<!--NEXT_ITEM--> \n")
     RSS.append("<item> \n")
     RSS.append("<title>"+name_array[-1]+"</title> \n")
     RSS.append("<pubDate>"+datetime.datetime.fromtimestamp(int(date_array[-1])/1000000).strftime("%a, %d %b %Y %H:%M:%S %z -0400")+"</pubDate> \n")
     RSS.append("<description><![CDATA[ \n")
     for i in paragraphs:
         RSS.append(i)
     RSS.append("]]></description> \n")
     RSS.append("</item> \n")
     rss_string=""
     for i in RSS:
        rss_string=rss_string+i
     rss_string=rss_string.replace(" ] ","")
     rss_string=rss_string.replace(" [ ","")
     rss_string=rss_string.replace(" , ","")
     rss_string=rss_string.replace(" ' ","")
    # print(rss_string)
     file=open('rss.xml')
     content=file.read()
     content=content.replace('<!--NEXT_ITEM-->',rss_string)
     file.close()
     os.remove("rss.xml")
     new = open("rss.xml", "a")
     new.write(content)
     new.close()
    else:
        print("[*]Article will not be added to rss feed")
    
LIST=[]
links,names,dates=getnames("articles")
for i in range(len(links)):
    temp="<a href="+links[i]+"><h4><p>"+names[i].replace("_"," ")+" "+datetime.datetime.fromtimestamp(int(dates[i])/1000000).strftime('%Y-%m-%d')+"</h4></p></a>"
    LIST.append(temp)
if not exists("blog.html"):
    make_archive()
    make_rss(names,dates,CONTENT)
else:
    os.remove("blog.html")
    make_archive()
    make_rss(names,dates,CONTENT)
