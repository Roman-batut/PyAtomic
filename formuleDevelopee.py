
#Forule possible
def possible(molecule) :
    
    moleculeOutput = []
    moleculeStr = ""
    
    for i in range(len(molecule)) :
        atome = molecule[i]
        if atome != "H" :
            if i != len(molecule)-1 :
                moleculeStr += atome + "-"
            else : 
                moleculeStr += atome
    
    moleculeOutput.append(moleculeStr)

    #Sortie
    return(moleculeOutput)

#Nombre de liaisons
def liaisons(molecule, moleculeAtomes, moleculeCovalente) :

    moleculeOutput = []

    for j in range(len(molecule)) :
        moleculeList = []
        total = 0
        for i in range(len(molecule[j])) :
            atome = molecule[j][i] 
            liaisons = 0
            if atome in moleculeAtomes :

                if i == 0 :
                    if molecule[j][i+1] == "-" : liaisons += 1
                    elif molecule[j][i+1] == "=" : liaisons += 2

                elif i == len(molecule[j])-1 :
                    if molecule[j][i-1] == "-" : liaisons += 1
                    elif molecule[j][i-1] == "=" : liaisons += 2

                else :
                    if molecule[j][i-1] == "-" : liaisons += 1
                    elif molecule[j][i-1] == "=" : liaisons += 2
                    if molecule[j][i+1] == "-" : liaisons += 1
                    elif molecule[j][i+1] == "=" : liaisons += 2
                    
                moleculeList.append(int(moleculeCovalente[atome]) - liaisons)
                total += int(moleculeCovalente[atome]) - liaisons

        moleculeOutput.append(moleculeList)

    #Sortie
    return(moleculeOutput, total)

#Molécule finale
def final(total, moleculeDecomposee, moleculePossible) :

    moleculeOutput = []
    positions = [i for i, j in enumerate(moleculePossible) if j == "-"]
    
    if total == moleculeDecomposee.count("H") :
        moleculeOutput.append(moleculePossible)
    
    elif total > moleculeDecomposee.count("H") :
        for pos in positions :
            moleculeOutput.append(moleculePossible[:pos] + "=" + moleculePossible[pos+1:])
  
    #Sortie
    return(moleculeOutput)

#Molécule hydrogène
def hydrogene(moleculeFinale, liaisonsFinale, moleculeAtomes) : 
    
    moleculeOutputMachine = []
    moleculeOutputHumain = [] 

    for i in range(len(liaisonsFinale)) : 
        moleculeMachine = ""
        moleculeHumain = ""
        k = 0
        for j in range(len(moleculeFinale[i])) :
            if moleculeFinale[i][j] in moleculeAtomes :
                if liaisonsFinale[i][k] == 0 :
                    moleculeMachine += moleculeFinale[i][j]
                    moleculeHumain += moleculeFinale[i][j]
                elif liaisonsFinale[i][k] == 1 :
                    moleculeMachine += moleculeFinale[i][j] + "H" + str(liaisonsFinale[i][k])
                    moleculeHumain += moleculeFinale[i][j] + "H"     
                else :
                    moleculeMachine += moleculeFinale[i][j] + "H" + str(liaisonsFinale[i][k])    
                    moleculeHumain += moleculeFinale[i][j] + "H" + str(liaisonsFinale[i][k])           
                k += 1 
            
            else : 
                moleculeMachine += moleculeFinale[i][j]
                moleculeHumain += moleculeFinale[i][j]

        moleculeOutputMachine.append(moleculeMachine)
        moleculeOutputHumain.append(moleculeHumain)
    
    #Sortie
    return(moleculeOutputMachine, moleculeOutputHumain)




