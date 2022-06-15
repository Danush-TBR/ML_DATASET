from google.colab import files
uplaoded=files.upload()

import csv
with open("training_Data_Exp_2.csv") as f:
  csv_file=csv.reader(f)
  data=list(csv_file)
s=data[1][:-1]
g=[['?' for i in range(len(s))]for j in range(len(s))]
print("Specfic Hypothesis:")
print(s)
print("General Hypothesis:")
print(g)
for i in data:
  if i[-1]=='Yes':
    for j in range(len(s)):

      if i[j]!=s[j]:
        s[j]='?'
        g[j][j]='?'
  
  elif i[-1]=='No':
    for j in range(len(s)):
      if i[j]!=s[j]:
        g[j][j]=s[j]
      else:
        g[j][j]=  '?'
  print("\nSteps of Candidate Elimination Algorithm",data.index(i)+1)
  print("S=",s)
  print("G=",g)

gh=[]
for i in g:
  for j in i:
    if j!='?':
      gh.append(i)
      break
print("\nFinal specific hypothesis:\n",s)
print("\nFinal general hypothesis:\n",gh)

''' [('sunny', 'warm', 'normal', 'strong', 'warm','same')]
[('sunny', 'warm', 'normal', 'strong', 'warm','same')]
[('sunny', 'warm', '?', 'strong', 'warm', 'same')]
[('?', '?', '?', '?', '?', '?')]
[('sunny', '?', '?', '?', '?', '?'), ('?', 'warm', '?', '?', '?', '?'), ('?', '?', '?', '?', '?', 'same')]
[('sunny', 'warm', '?', 'strong', 'warm', 'same')]
[('sunny', 'warm', '?', 'strong', '?', '?')]
[('sunny', 'warm', '?', 'strong', '?', '?')]
[('sunny', '?', '?', '?', '?', '?'), ('?', 'warm', '?', '?', '?', '?')] '''
