class voiture:
    def __init__(self, marque,modele,imatriculation):
        self.marque = marque
        self.modele = modele
        self.imatriculation = imatriculation
    def affiche(self):
        return f"{self.marque} {self.modele} {self.imatriculation}"

class parc:
    def __init__(self,capacite):
        self.capacite = capacite
        self.voiture = []