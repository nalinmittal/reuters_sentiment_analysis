

from bs4 import BeautifulSoup
import ast
import os
from django.utils.encoding import smart_str

dict1={}
list2 = os.listdir("./Categories")
os.makedirs("./train_data")
for file in list2:
    list_str1 = open("./Categories/"+file,'r')
    dict1[file] = ast.literal_eval(list_str1.read())
    os.makedirs("./train_data/"+file.replace("_list.txt",""))
    for i in dict1[file]:
        os.makedirs('./train_data/'+file.replace("_list.txt","")+"/"+str(i))

for k in range(21):
    with open("reut2-"+str(k).zfill(3)+".sgm") as fp:
        soup = BeautifulSoup(fp,'html.parser')
    count = 0
    for i in soup.find_all('reuters'):
        for j in i.topics:
            if j:
                if i.find('body'):
                    new_data = open("./train_data/topics/"+str(j.text)+"/"+str(count).zfill(5)+".txt",'w')
                    new_data.write(smart_str(i.body.text).replace('\n',' '))
                    new_data.close()
                    count  = count +1
         
        for j in i.places:
            if j:
                if i.find('body'):
                    new_data = open("./train_data/places/"+str(j.text)+"/"+str(count).zfill(5)+".txt",'w')
                    new_data.write(smart_str(i.body.text).replace('\n',' '))
                    new_data.close()
                    count  = count +1
        
        for j in i.exchanges:
            if j:
                if i.find('body'):
                    new_data = open("./train_data/exchgs/"+str(j.text)+"/"+str(count).zfill(5)+".txt",'w')
                    new_data.write(smart_str(i.body.text).replace('\n',' '))
                    new_data.close()
                    count  = count +1        
    
        for j in i.orgs:
            if j:
                if i.find('body'):
                    new_data = open("./train_data/orgs/"+str(j.text)+"/"+str(count).zfill(5)+".txt",'w')
                    new_data.write(smart_str(i.body.text).replace('\n',' '))
                    new_data.close()
                    count  = count +1
    
        for j in i.people:
            if j:
                if i.find('body'):
                    new_data = open("./train_data/people/"+str(j.text)+"/"+str(count).zfill(5)+".txt",'w')
                    new_data.write(smart_str(i.body.text).replace('\n',' '))
                    new_data.close()
                    count  = count +1
    #str(soup.reuters.body.text).replace('\n',' ')
"""
list_str1 = open("topics_list.txt",'r')
topics_list = ast.literal_eval(list_str1.read())

#A directory for "TOPICS" data
os.makedirs('topics')
for i in topics_list:
    os.makedirs('topics/'+str(i))
    
list_str1 = open("places_list.txt",'r')
places_list = ast.literal_eval(list_str1.read())    
#A directory for "PLACES" data
os.makedirs('places')
for i in places_list:
    os.makedirs('places/'+str(i))
    
list_str1 = open("exchgs_list.txt",'r')
exchgs_list = ast.literal_eval(list_str1.read())
#A directory for "EXCHANGES" data
os.makedirs('exchgs')
for i in exchgs_list:
    os.makedirs('exchgs/'+str(i))
"""    