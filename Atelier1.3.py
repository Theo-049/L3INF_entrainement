#Ajoute du texte dans la nouvelle branche
unites = {
    "mg": 0.001,
    "cg": 0.01,
    "dg": 0.1,
    "g": 1,
    "dag": 10,
    "hg": 100,
    "kg": 1000,
    "t": 10**4
}

#je ne suis pas la même personne

def conversion_masse(unité_actuelle, nouvelle_unité, poids):
    return poids * unites[unité_actuelle] / unites[nouvelle_unité]

print(conversion_masse("hg", "kg", 1))