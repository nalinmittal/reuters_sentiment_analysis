import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
#from sklearn.naive_bayes import MultinomialNB
from random import shuffle
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier


category_list = os.listdir('./train_data')
for category in category_list:
    list1 = os.listdir('./train_data/'+category)
    data = []
    target =[]
    for i in list1:
        list2 = os.listdir('./train_data/'+category+'/'+i)
        for j in list2:
            fp = open('./train_data/'+category+'/'+i+'/'+j,'r')
            data.append(fp.read())
            fp.close()
            target.append(i)
        



    zipped_list = zip(data,target)
    shuffle(zipped_list)
    a = len(zipped_list)
    a = int(a*0.9)
    train  = zipped_list[0:a]
    test = zipped_list[a:]
    train_data = zip(*(train))[0]
    train_target = zip(*(train))[1]
    
    
    
    text_clf_svm = Pipeline([('vect', CountVectorizer(stop_words='english')),('tfidf', TfidfTransformer()),('clf-svm', SGDClassifier(loss='hinge',alpha=1e-3,n_iter=5,random_state=42)),])
    #text_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),('tfidf', TfidfTransformer()),('clf', MultinomialNB()),])
    _ = text_clf_svm.fit(train_data, train_target)
    predicted = text_clf_svm.predict(zip(*test)[0])
    print category+" accuracy : "+str(np.mean(predicted == zip(*test)[1]))