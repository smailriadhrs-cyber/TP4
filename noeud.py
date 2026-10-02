class Noeud:
    def __init__(self, valeur, enfants=None):
        self.valeur = valeur
        if enfants is None:
            self.enfants = []
        else:
            self.enfants = list(enfants)

    def ajouter_enfant(self, enfant):

        self.enfants.append(enfant)
        
    def notation_polonaise(self):

        elements = [str(self.valeur)]
        for enfant in self.enfants:
            elements.append(enfant.notation_polonaise())
        return " ".join(elements)
    def afficher_polonais(self):
      
        print(self.notation_polonaise())
    def evaluer(self, variables=None):
        if variables is None:
            variables = {}

        # Cas 1 : constante numérique directe
        if isinstance(self.valeur, (int, float)):
            return float(self.valeur)

        # Cas 2 : chaîne de caractères (opérateur ou variable)
        operateurs_connus = {"+", "-", "*", "/", "exp", "log", "sin", "cos"}

        # Si ce n'est pas un opérateur, il s'agit d'une variable
        if self.valeur not in operateurs_connus:
            if self.valeur not in variables:
                raise ValueError(
                    f"Erreur d'évaluation : la variable '{self.valeur}' n'a pas été fournie dans le dictionnaire."
                )
            return float(variables[self.valeur])

        # Si c'est un opérateur, on évalue récursivement tous les sous-arbres enfants
        valeurs_enfants = [e.evaluer(variables) for e in self.enfants]

        # Application des opérateurs binaires
        if self.valeur == "+":
            return valeurs_enfants[0] + valeurs_enfants[1]
        elif self.valeur == "-":
            return valeurs_enfants[0] - valeurs_enfants[1]
        elif self.valeur == "*":
            return valeurs_enfants[0] * valeurs_enfants[1]
        elif self.valeur == "/":
            if valeurs_enfants[1] == 0:
                raise ZeroDivisionError("Division par zéro rencontrée dans l'arbre.")
            return valeurs_enfants[0] / valeurs_enfants[1]

        # Application des opérateurs unaires (facultatif question 5)
        elif self.valeur == "exp":
            return math.exp(valeurs_enfants[0])
        elif self.valeur == "log":
            return math.log(valeurs_enfants[0])
        elif self.valeur == "sin":
            return math.sin(valeurs_enfants[0])
        elif self.valeur == "cos":
            return math.cos(valeurs_enfants[0])

        raise ValueError(f"Opérateur inconnu : {self.valeur}")
    


