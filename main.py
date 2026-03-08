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
    def entervoiture(self,voiture):
        if voiture in self.voiture:
            print("voiture existe")
        elif len(self .voiture):>=self.capacite:
            print("parc est plein")
        else:
            self.voiture.append(voiture)
            print("voiture ajoutee",voiture.affiche())
    def sortirvoiture(self,voiture):
        if voiture in self.voiture:
            self.voiture.remove(voiture)
            print("voiture retiree",voiture.affiche())
            print("places libres:",self.calculerNplaceslibre())
        else:
            print("voiture non existe")
    def calculerNplaceslibre(self):
        return  self.capacite - len(self.voiture)
parc = parc(3)

v1=voiture(marque="toyota",modele="yaris",imatriculation="X50 MPC")
v2=voiture("toyota",modele="corolla",imatriculation="X50 MPC")
v3=voiture("toyota",modele="matryx",imatriculation="X50 MPC" )
v4=voiture("toyota",modele="carmy",imatriculation="X50 MPC" )

parc.entervoiture(v1)
parc.entervoiture(v2)
parc.entervoiture(v3)
parc.entervoiture(v4)

