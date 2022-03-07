
# import OS module
import os
#gets a list of the directory location and name of the articles and dates and returns them
#path=articles
def getnames(path):
# Get the list of all files and directories
  dir_list = os.listdir(path)

  articles_links=[]
  articles_names=[]
  articles_dates=[]
  for i in dir_list:
    path_alt=path+"/"+i
    dir=os.listdir(path_alt)
    #print(str(i)+str(dir))# prints all files
    for j in dir:
        if j[-5:]==".html":
            link="articles/"+i+"/"+j
            articles_dates.append(i)
            articles_links.append(link)
            articles_names.append(j[:-5])

  return articles_links,articles_names,articles_dates

