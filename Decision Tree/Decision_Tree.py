#Create Object from LabelEncoder
label_En = LabelEncoder()

X = data_PlayTennis.drop(['play'] , axis=1 )
Y = data_PlayTennis['play']

from sklearn.model_selection import train_test_split
x_train  , x_test, y_train, y_test =train_test_split(X ,Y , test_size=0.3 ,stratify=Y ,random_state=101)

x_train
y_train
x_test
y_test

print(len(X))
print(len(Y))
print(len(x_train))
print(len(y_train))
print(len(x_test))
print(len(y_test))

print(len(X))
print(len(Y))
print(len(x_train))
print(len(y_train))
print(len(x_test))
print(len(y_test))

from sklearn.tree import DecisionTreeClassifier
#Create Object from Decision Tree Classifier
D_T_C_Model =DecisionTreeClassifier(criterion='entropy' ,random_state=10)
D_T_C_Model.fit(x_train , y_train)
D_T_C_Model.score(x_train , y_train)
D_T_C_Model.score(x_test , y_test)
y_pred = D_T_C_Model.predict(x_test)
y_pred
D_T_C_Model.predict_proba(x_test)

#Graphviz
import graphviz
graph_data = tree.export_graphviz(D_T_C_Model, out_file=None) 
graph = graphviz.Source(graph_data) 
graph
#visualize the tree using tree.plot_tree
from sklearn import tree
tree.plot_tree(D_T_C_Model)

#Check Accurcy score(y_test , y_pred)
from sklearn.metrics import accuracy_score
accuracy_score(y_test , y_pred)

'''
outlook
overcast
b'yes'
rain
  wind

    b'strong'
     b'no'
 b'weak'
                b'yes'
          sunny
             humidity
                 b'high'
                   b'no'
          b'normal'
               b'yes
'''
