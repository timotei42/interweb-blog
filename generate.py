import time
import os
import shutil
from os.path import exists
#function to get the header part of the site
def get_head():
    file=open('pieces/header.txt')
    header=file.read()
    file.close()
    return header

#function to get the 2 parts of the body to sandwitch the text between
def get_body(Title,Date,Hour):
    file=open('pieces/body.txt')
    content=file.read()
    content=content.replace('$TITLE',Title.replace("_"," "))
    content=content.replace('$DATE',Date)
    content=content.replace('$HOUR',Hour)
    separated=content.split("\n")
    limit_reached=0
    body_1=[]
    body_2=[]
    for i in separated:
        if '$CONTENT' in i:
            limit_reached=1
        if limit_reached==0:
           body_1.append(i+"\n")
        else:
              if limit_reached==1 and not '$CONTENT' in i:
                 body_2.append(i+"\n")
    file.close()
    return body_1,body_2
def main():
 article_name=input("Name the file you want to pass to article:")
 if not exists(article_name):
    print("File not found")
 else:
#getting the content from the written file
  paragraphs=[]
  written_page= open(article_name,'r')
  text=written_page.read()
  separated=text.split("\n")

#variables to replace in the article
  Title=separated[0].replace(" ","_")
  Date=separated[1]
  Time = time.asctime()

#assiging the components to variables
  body1,body2=get_body(Title,Date,Time)
  head=get_head()

#Creating the new html file for the article
  new = open("test.html", "a")
  xml=[]
  new.write("<!DOCTYPE HTML><html lang='en'> \n")
  for i in head:
   new.write(i)
  for i in body1:
   new.write(i)
#function below converts the text form the file to html
#it starts from the second line as it's assumed the first and second line is used for the title and the date
  for paragraph in separated[2:]:
     if paragraph[:4]=="code":
        temp_paragraph=paragraph.split(" ")
        len_of_code=temp_paragraph[1]
        new.write("<pre style=max-width:"+len_of_code+"px;margin:auto;><code> ")
     else:
            if paragraph=="!code":
                new.write("</code></pre> ")
            else:
                  if paragraph=="":
                      new.write("<br> ")
                  else:
                      if paragraph[:6]=="!image":
                         link=paragraph[6:].split()
                         new.write('<img src="'+link[0]+'" style=width:'+link[1]+'px;height:'+link[2]+'px;>')
                      else:
                            temp=paragraph.replace("$COLOR","<span style='color: red'>")
                            temp2=temp.replace("COLOR$","</span>")
                            new.write("<p>"+temp2+"</p>")
                            xml.append("<p>"+temp2+"</p>")
  for i in body2:
   new.write(i)
  new.write("</html>")
  new.flush()
  new.close()

  Unixtime=str(int(time.time())*1000000)
  destination="articles/"+Unixtime
  os.mkdir(destination)
  shutil.copy('pieces/css.css',destination)
  shutil.copy(article_name,destination)
  os.rename("test.html",destination+"/"+Title+".html")
  #returns the paragraphs of written text to be put into the xml file
  return xml
