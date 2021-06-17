#Exercice

fawaz={'java':[14,12,15],'uml':[14,10,16],'sda':[15,13,15],'algebre':[17,12,14],'reseaux':[14,14,20]}
notes_java=fawaz['java']
notes_uml=fawaz['uml']
notes_sda=fawaz['sda']
notes_algebre=fawaz['algebre']
notes_reseaux=fawaz['reseaux']
moyenne_java=(notes_java[0]+notes_java[1]+notes_java[2])/3
moyenne_uml=(notes_uml[0]+notes_uml[1]+notes_uml[2])/3
moyenne_reseaux=(notes_reseaux[0]+notes_reseaux[1]+notes_reseaux[2])/3
moyenne_algebre=(notes_algebre[0]+notes_algebre[1]+notes_algebre[2])/3
moyenne_sda=(notes_sda[0]+notes_sda[1]+notes_sda[2])/3
moyenne=(moyenne_java+moyenne_uml+moyenne_reseaux+moyenne_algebre+moyenne_sda)/5
print("La moyenne est :"+ str(moyenne))

 #E0

#1-
x=list(range(1,11))
print(x)
#2-
x[0]=x[0]+11
x[1]=x[1]+11
x[2]=x[2]+11
x[3]=x[3]+11
x[4]=x[4]+11
x[5]=x[5]+11
x[6]=x[6]+11
x[7]=x[7]+11
x[8]=x[8]+11
x[9]=x[9]+11
print(x)   
#3-print(d)
x.append(22)
print(x)
#4
x.extend([23,24])
print(x)
#5
y=list(x[0:13 :2])
z=list(x[1:12 :2])
print(y)
print(z)
#6
x.remove(x[3])
print(x)



#E1
d={'nom':'Dupuis','prenom':'Jacque','age':30}

#a-
d['prenom']='Jacques'
print(d)
#b-
print(d.keys())
#c-
print(d.values())
#d-
print(d)
#e-
print(d['nom']+' ' +d['prenom'] +' a '+str(d['age'])+' ans')
