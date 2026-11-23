#gestion simple d'une bibliotheque
titre=input("titre du livre: ")
exemplaires=int(input("nombre d'exemplaires: "))
#Emprunt d'un livre
exemplaires=exemplaires-1

print("livre:",titre)
print("Exemplaires disponibles:",exemplaires)
print("Apres emprunt :",exemplaires,"exemplaire(s) disponible(s)")