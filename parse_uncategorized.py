from bs4 import BeautifulSoup
import os
from django.utils.encoding import smart_str

count = 0
os.makedirs('./Uncategorized_data')
os.makedirs('./Uncategorized_data/topics')
os.makedirs('./Uncategorized_data/places')
os.makedirs('./Uncategorized_data/exchgs')
os.makedirs('./Uncategorized_data/people')
os.makedirs('./Uncategorized_data/orgs')

for k in range(21):
    with open("reut2-"+str(k).zfill(3)+".sgm") as fp:
        soup = BeautifulSoup(fp,'html.parser')
    
    for i in soup.find_all('reuters'):
        
        if i.topics.contents:
            pass
        else:
            if i.find('body'):
                data = open('./Uncategorized_data/topics/'+str(count).zfill(5)+'.txt','w')
                data.write(smart_str(i.body.text).replace('\n',' '))
                data.close()
                count = count+1

        if i.places.contents:
            pass
        else:
            if i.find('body'):
                data = open('./Uncategorized_data/places/'+str(count).zfill(5)+'.txt','w')
                data.write(smart_str(i.body.text).replace('\n',' '))
                data.close()
                count = count+1

        if i.exchanges.contents:
            pass
        else:
            if i.find('body'):
                data = open('./Uncategorized_data/exchgs/'+str(count).zfill(5)+'.txt','w')
                data.write(smart_str(i.body.text).replace('\n',' '))
                data.close()
                count = count+1
 
        if i.people.contents:
            pass
        else:
            if i.find('body'):
                data = open('./Uncategorized_data/people/'+str(count).zfill(5)+'.txt','w')
                data.write(smart_str(i.body.text).replace('\n',' '))
                data.close()
                count = count+1
                    

        if i.orgs.contents:
            pass
        else:
            if i.find('body'):
                data = open('./Uncategorized_data/orgs/'+str(count).zfill(5)+'.txt','w')
                data.write(smart_str(i.body.text).replace('\n',' '))
                data.close()
                count = count+1