import pandas as pd msg=pd.read_csv('naivetext1.csv',names=['message','label'])
print('The dimensions of the dataset',msg.shape)
msg['labelnum']=msg.label.map({'pos':1,'neg':0})
X=msg.message y=msg.labelnum print(X)
print(y)

#splitting the dataset into train and test data
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(X,y)
print(xtest.shape)
print(xtrain.shape)
print(ytest.shape)
print(ytrain.shape)
#output of count vectoriser is a sparse matrix
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
xtrain_dtm = count_vect.fit_transform(xtrain) 
xtest_dtm=count_vect.transform(xtest) 
print(count_vect.get_feature_names())

df=pd.DataFrame(xtrain_dtm.toarray(),columns=count_vect.get_feature_names())
print(df)
#tabular representation
print(xtrain_dtm)
#sparse matrix representation

# Training Naive Bayes (NB) classifier on training data. from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(xtrain_dtm,ytrain)
predicted = clf.predict(xtest_dtm)

#printing accuracy metrics from sklearn import metrics print('Accuracy metrics')
print('Accuracy of the classifer is',metrics.accuracy_score(ytest,predicted))
print('Confusion matrix')
print(metrics.confusion_matrix(ytest,predicted))
print('Recall and Precison ')
print(metrics.recall_score(ytest,predicted))
print(metrics.precision_score(ytest,predicted))

'''docs_new = ['I like this place', 'My boss is not my saviour']
X_new_counts = count_vect.transform(docs_new) predictednew = clf.predict(X_new_counts)
for doc, category in zip(docs_new, predictednew):
print('%s->%s' % (doc, msg.labelnum[category]))'''

'''

I love this sandwich,pos This is an amazing place,pos
I feel very good about these beers,pos This is my best work,pos
What an awesome view,pos
I do not like this restaurant,neg I am tired of this stuff,neg
I can't deal with this,neg He is my sworn enemy,neg My boss is horrible,neg
This is an awesome place,pos
I do not like the taste of this juice,neg I love to dance,pos
I am sick and tired of this place,neg What a great holiday,pos
That is a bad locality to stay,neg
We will have good fun tomorrow,pos I went to my enemy's house today,neg

'''


'''

output:

['about', 'am', 'amazing', 'an', 'and', 'awesome', 'beers', 'best', 'boss', 'can', 'deal',
'do', 'enemy', 'feel', 'fun', 'good', 'have', 'horrible', 'house', 'is', 'like', 'love', 'my',
'not', 'of', 'place', 'restaurant', 'sandwich', 'sick', 'stuff', 'these', 'this', 'tired', 'to',
'today', 'tomorrow', 'very', 'view', 'we', 'went', 'what', 'will', 'with', 'work']
about am amazing an and awesome beers best boss can ... today \
0 1 0 0 0 0 0 1 0 0 0 ... 0
1 0 0 0 0 0 0 0 1 0 0 ... 0
2 0 0 1 1 0 0 0 0 0 0 ... 0
3 0 0 0 0 0 0 0 0 0 0 ... 1
4 0 0 0 0 0 0 0 0 0 0 ... 0
5 0 1 0 0 1 0 0 0 0 0 ... 0
6 0 0 0 0 0 0 0 0 0 1 ... 0
7 0 0 0 0 0 0 0 0 0 0 ... 0
8 0 1 0 0 0 0 0 0 0 0 ... 0
9 0 0 0 1 0 1 0 0 0 0 ... 0
10 0 0 0 0 0 0 0 0 0 0 ... 0
11 0 0 0 0 0 0 0 0 1 0 ... 0
12 0 0 0 1 0 1 0 0 0 0 ... 0
	
tomorrow very view we went what will with work
0 0 1 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 0 1
2 0 0 0 0 0 0 0 0 0
3 0 0 0 0 1 0 0 0 0
4 0 0 0 0 0 0 0 0 0
5 0 0 0 0 0 0 0 0 0
6 0 0 0 0 0 0 0 1 0
7 1 0 0 1 0 0 1 0 0
8 0 0 0 0 0 0 0 0 0

'''
