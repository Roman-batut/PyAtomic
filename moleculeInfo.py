'''Imports'''

#Global Imports
import csv


'''Fonctions'''

#Rewriter
def rewriter(molecule) :
    for i in range(len(molecule)+1) :

        letter = molecule[i]
        
        if letter.isupper() :
            try : 
                if molecule[i+1].isupper() :
                    molecule = molecule[:i+1] + "1" + molecule[i+1:]

            except IndexError :
                molecule = molecule + "1" 

    #Sortie            
    return(molecule)


#Decomposer
def decomposer(molecule) :
    
    moleculeOutput = []

    for i in range(len(molecule)) :

        letter = molecule[i]

        #Vérifier quel atome est mis en jeu
        if letter.isupper() :
            try : 
                if molecule[i+1].islower() :
                    atome = letter + molecule[i+1]
                else : 
                    atome = letter
            
            except IndexError : 
                    atome = letter

        #Vérifier le nombre de l'atome mis en jeu
        elif letter.isnumeric() :
            try :
                if molecule[i+1].isnumeric() :
                    nombre = str(letter) + str(0)
                else :
                    nombre = letter
            
            except IndexError :
                    nombre = letter

            for j in range(int(nombre)) :
                moleculeOutput.append(atome)

    #Sortie
    return moleculeOutput

#Atomes
def atoms(molecule) :

    moleculeOutput = []
    
    for atome in molecule :
        if atome.isupper() and atome not in moleculeOutput :
            moleculeOutput.append(atome)
    
    #Sortie
    return(moleculeOutput)
    
#Numéro Atomique
def numAtomique(moleculeAtomes) : 

    moleculeOutput = {}

    for atom in moleculeAtomes :
        with open("atoms.csv", "r") as atoms :
            content = csv.reader(atoms)
            for row in content :
                if row[2] == atom :
                    moleculeOutput[atom] = row[0]
    #Sortie
    return(moleculeOutput)


#Nombre de Valence
def valence(moleculeAtomes) :

    moleculeOutput = {}

    for atom in moleculeAtomes :
        with open("atoms.csv", "r") as atoms :
            content = csv.reader(atoms)
            for row in content :
                if row[2] == atom :
                    moleculeOutput[atom] = row[6]

    #Sortie
    return(moleculeOutput)

#Nombre de liaisons covalentes
def covalente(moleculeZ, moleculeValence) :
    
    moleculeOutput = {}

    for atom in moleculeZ.keys() :

        if int(moleculeZ[atom]) <= 4 :
            moleculeOutput[atom] = str(2 - int(moleculeValence[atom]))
        else : 
            moleculeOutput[atom] = str(8 - int(moleculeValence[atom]))

    #Sortie
    return(moleculeOutput)

