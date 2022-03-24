from Etudiant import *
print("Sérialisation")
#Sérialiser l'objet instancié
etud=Etudiant("1234567","Hasna","informatique")
etud.serialiser("FichierSerialiser.json")

#Désérialisation

etud1 = Etudiant()

etud1.deserialiser("FichierSerialiser1.json")

print(etud1)
