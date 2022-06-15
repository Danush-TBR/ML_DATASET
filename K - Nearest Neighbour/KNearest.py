from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 
from sklearn.model_selection import train_test_split 
import pandas as pd 
dataset=pd.read_csv("iris.csv") 
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0,test_size=0.25) 
             classifier=KNeighborsClassifier(n_neighbors=8,p=3,metric='euclidean')
classifier.fit(X_train,y_train) 
#predict the test resuts 
y_pred=classifier.predict(X_test) 
cm=confusion_matrix(y_test,y_pred) 
print('Confusion matrix is as follows\n',cm) 
print('Accuracy Metrics') 
print(classification_report(y_test,y_pred)) 
print(" correct predicition",accuracy_score(y_test,y_pred)) 
print(" worng predicition",(1-accuracy_score(y_test,y_pred)))


'''
Output
Confusion matrix is as follows 
[[13 0 0] 
[ 0 15 1] 
[ 0 0 9]] 
Accuracy Metrics 
precision recall f1-score support 
Iris-setosa 1.00 1.00 1.00 13 
Iris-versicolor 1.00 0.94 0.97 16 
Iris-virginica 0.90 1.00 0.95 9 
avg / total 0.98 0.97 0.97 38 
correct predicition 0.9736842105263158 
             worng predicition 0.02631578947368418
'''
