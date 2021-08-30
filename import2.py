import csv
f = open(r'/Users/willunt/Downloads/test/16421740 708f93625d0148bd9a33dcc21bcba864/Group Data 0bc905017c2243d7b18fae3ee3cc8955.csv')
csv_f = csv.reader(f)
N =[]
Group = []
Region = []
Stain = []
Measurement = []
Value = []
Neuronal_Type = []
Method = []
Age = []
Stat = []
Value2 = []
Magnification = []
NB = []

for row in csv_f:
   N.append(row[0])
   Group.append(row[1])
   Region.append(row[2])
   Stain.append(row[3])
   Measurement.append(row[4])
   Value.append(row[5])
   Neuronal_Type.append(row[6])
   Method.append(row[7])
   Age.append(row[8])
   Stat.append(row[9])
   Value2.append(row[10])
   Magnification.append(row[11])
   NB.append(row[12])

group0 = [N[0],Group[0],Region[0],Stain[0],Measurement[0],Value[0],Neuronal_Type[0],Method[0],Age[0],Stat[0],Value2[0],Magnification[0],NB[0]]
print(group0)
group1 = [N[1],Group[1],Region[1],Stain[1],Measurement[1],Value[1],Neuronal_Type[1],Method[1],Age[1],Stat[1],Value2[1],Magnification[1],NB[1]]
print(group1)
group2 = [N[2],Group[2],Region[2],Stain[2],Measurement[2],Value[2],Neuronal_Type[2],Method[2],Age[2],Stat[2],Value2[2],Magnification[2],NB[2]]
print(group2)
group3 = [N[3],Group[3],Region[3],Stain[3],Measurement[3],Value[3],Neuronal_Type[3],Method[3],Age[3],Stat[3],Value2[3],Magnification[3],NB[3]]
print(group3)


control = 'Control'
if control in group1:
    control = group1
    disease = group2
print(disease)






#Statistical analysis from here#










