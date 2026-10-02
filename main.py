from noeud import Noeud

# Création des nœuds
exponentielle = Noeud("exp")
deux = Noeud("2")
plus = Noeud("+")
y = Noeud("y")

# Construction de l'arbre
plus.ajouter_enfant(deux)
plus.ajouter_enfant(y)

exponentielle.ajouter_enfant(plus)

# Affichage
affichage = exponentielle.notation_polonaise()

print(f"Notation polonaise obtenue : {affichage}")