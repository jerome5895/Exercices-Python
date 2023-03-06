# Function to calcul and list produits consecutive
def produit_consecutif():
    entiers = list(range(2, 22, 2))
    produit = 0
    for produit in entiers: 
        produit = (produit + 2) * produit
        print(produit)

# Call function
produit_consecutif()