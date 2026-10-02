import math
import matplotlib.pyplot as plt

class Noeud:
    """
    Représente un nœud dans un arbre d'expression mathématique.

    Attributs :
        valeur (str, int, float) : Opérateur, nom de variable ou constante.
        enfants (list) : Liste des nœuds enfants (sous-arbres).
    """

    def __init__(self, valeur, enfants=None):
        self.valeur = valeur
        if enfants is None:
            self.enfants = []
        else:
            self.enfants = enfants

    def ajouter_enfant(self, noeud_enfant):
        """
        Ajoute un nœud enfant à la liste des enfants du nœud courant.
        """
        self.enfants.append(noeud_enfant)

    def afficher_polonais(self):
        """
        Retourne l'expression sous forme de chaîne en notation polonaise (préfixée).
        """
        elements = [str(self.valeur)]
        for enfant in self.enfants:
            elements.append(enfant.afficher_polonais())
        return " ".join(elements)

    def evaluer(self, variables):
        """
        Calcule la valeur numérique de l'expression représentée par l'arbre.

        Lève une ValueError si une variable requise est manquante dans le dictionnaire
        ou si l'opérateur n'est pas reconnu.
        """
        if isinstance(self.valeur, (int, float)):
            return float(self.valeur)

        operateurs = {"+", "-", "*", "/", "exp", "log", "sin", "cos"}
        if self.valeur not in operateurs:
            if self.valeur in variables:
                return float(variables[self.valeur])
            else:
                raise ValueError(f"Variable manquante dans le dictionnaire : '{self.valeur}'")

        if self.valeur in {"+", "-", "*", "/"}:
            gauche = self.enfants[0].evaluer(variables)
            droite = self.enfants[1].evaluer(variables)
            if self.valeur == "+":
                return gauche + droite
            elif self.valeur == "-":
                return gauche - droite
            elif self.valeur == "*":
                return gauche * droite
            elif self.valeur == "/":
                return gauche / droite

        if self.valeur in {"exp", "log", "sin", "cos"}:
            arg = self.enfants[0].evaluer(variables)
            if self.valeur == "exp":
                return math.exp(arg)
            elif self.valeur == "log":
                return math.log(arg)
            elif self.valeur == "sin":
                return math.sin(arg)
            elif self.valeur == "cos":
                return math.cos(arg)

        raise ValueError(f"Opérateur inconnu : {self.valeur}")

    def tracer(self, nom_variable, valeurs):
        """
        Trace la courbe de l'expression mathématique en fonction d'une variable donnée
        sur une liste de valeurs à l'aide de matplotlib.
        """
        images = []
        for v in valeurs:
            y = self.evaluer({nom_variable: v})
            images.append(y)

        plt.figure()
        plt.plot(valeurs, images)
        plt.xlabel(nom_variable)
        plt.ylabel(self.afficher_polonais())
        plt.title(f"Graphe de {self.afficher_polonais()}")
        plt.grid(True)
        plt.show()