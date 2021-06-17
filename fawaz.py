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