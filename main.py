class voiture:
    def __init__(self, marque,couleur,imatriculation):
        self.marque = marque
        self.couleur = couleur
        self.imatriculation = imatriculation
    def affiche(self):
        return f"{self.marque} {self.couleur} {self.imatriculation}"

class parc:
    def __init__(self,capacite):
        self.capacite = capacite
        self.voiture = []
    def entervoiture(self,voiture):
        if voiture in self.voiture:
            print("voiture existe")
        elif len(self .voiture) >=self.capacite:
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

v1=voiture(marque="toyota",couleur="noir",imatriculation="X50 MOC")
v2=voiture("toyota",couleur="blanc",imatriculation="O50 MFC")
v3=voiture("toyota",couleur="rouge",imatriculation="X50 PPC" )
v4=voiture("toyota",couleur="maron",imatriculation="X80 MPC" )

parc.entervoiture(v1)
parc.entervoiture(v2)
parc.entervoiture(v3)
parc.entervoiture(v4)

parc.sortirvoiture(v2)


