
from bs4 import BeautifulSoup
import os
topics_list = []
places_list = []
orgs_list = []
exchgs_list = []
companies_list = []
people_list = []
for k in range(21):
    with open("reut2-"+str(k).zfill(3)+".sgm") as fp:
        soup = BeautifulSoup(fp,'html.parser')
    
    
    for i in soup.find_all('reuters'):
        for j in i.topics:
            if j:
                topics_list.append(str(j.text))
        for j in i.places:
            if j:
                places_list.append(str(j.text))
        for j in i.orgs:
            if j:
                orgs_list.append(str(j.text))
        for j in i.exchanges:
            if j:
                exchgs_list.append(str(j.text))
        for j in i.people:
            if j:
                people_list.append(str(j.text))
os.makedirs('Categories')
op = open("Categories/people_list.txt","w")
op.write(str(list(set(people_list))))
op.close()
op = open("Categories/topics_list.txt","w")
op.write(str(list(set(topics_list))))
op.close()
op = open("Categories/orgs_list.txt","w")
op.write(str(list(set(orgs_list))))
op.close()
op = open("Categories/exchgs_list.txt","w")
op.write(str(list(set(exchgs_list))))
op.close()
op = open("Categories/places_list.txt","w")
op.write(str(list(set(places_list))))
op.close()

