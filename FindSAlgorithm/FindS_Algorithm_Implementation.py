import csv
from google.colab import files
uploaded=files.upload()

num_attributes = 5
a = []
print("\n The Given Training Data Set \n")
with open('PlayTennis_1.csv', 'r') as csvfile:
 reader = csv.reader(csvfile)
 for row in reader:
  a.append (row)
  print(row)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes
print(hypothesis)
for j in range(0,num_attributes):
  hypothesis[j] = a[1][j];
print(hypothesis)

print("\n Find S: Finding a Maximally Specific Hypothesis\n")
for i in range(1,len(a)):
  if  a[i][4]=='Yes':
    for j in range(0,num_attributes):
      if a[i][j]!=hypothesis[j]:
          hypothesis[j]='?'
      else:
        hypothesis[j]= a[i][j] 
  else:
    pass
    print(" For Training instance No:{0} the hypothesis is".format(i),hypothesis)
print("\n The Maximally Specific Hypothesis for a given Training Examples :\n")
print(hypothesis)
