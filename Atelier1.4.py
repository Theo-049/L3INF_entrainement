impots = int(input("Entrez votre revenu annuel imposable (en euros): "))

def revenu_imposable(revenu: int):
    if revenu <= 11497:
        return "Vous êtes exonéré d'impôt"
    elif revenu <= 29315:
        return f"Votre taux d'imposition est de 11% ", {revenu * 1.11}
    elif revenu <= 83823:
        return f"Votre taux d'imposition est de 30%", {revenu * 1.30}
    elif revenu <= 180294:
        return f"Votre taux d'imposition est de 41%", {revenu * 1.41}
    else:
        return f"Votre taux d'imposition est de 45%", {revenu * 1.45}

print( " Votre revenu imposable est de : " ,revenu_imposable(impots))