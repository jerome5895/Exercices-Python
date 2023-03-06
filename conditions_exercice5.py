notes = [14, 9, 13, 15, 12]

# Function calcul average
def moyenne_notes():
    total = 0
    for i in notes:
        total = total + i
        moyenne = total / len(notes)
    return moyenne

moyenne = moyenne_notes()

# Function to displays mention
def mention():
    if moyenne >= 10 and moyenne < 12:
        print("Votre mention est : passable")
    elif moyenne >= 12 and moyenne < 14:
        print("Votre mention est : assez bien")
    else:
        print("Votre mention est : bien")

# Print out results
mention()
print(f"La note maximale est de : {max(notes):.2f}")
print(f"La note minimale est de : {min(notes):.2f}")
print(f"La valeur moyenne est de : {moyenne_notes():.2f}")