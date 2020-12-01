import random
import math
INCONNU = -1
PERDU = -2
DRAPEAU = -3
def genere_plateau(largeur, hauteur, prob_mine): #prob_mine supposer != de 0 et 1
    plateau = []
    c=0
    for i in range(largeur):
        plateau.append([])
        for j in range(hauteur):
                if random.randint(0,1)==0 and c<int(largeur*hauteur*prob_mine):
                    c+=1
                    plateau[i].append({"mine" : True, 
                                        "etat" : INCONNU})         
                else :
                    plateau[i].append({"mine" : False, 
                                        "etat" : INCONNU })
    return plateau

plateau=genere_plateau(5,2,0.5)
print(plateau)

while True:

    def coup_joueur(plateau,x,y):
        #le joueur donne (x,y) ou il met un drapeau
        x = input('entre une coordonnées selon la verticale ')
        y = input('entre une coordonnées selon l horizontale ')
        d = input('veut tu mettre un DRAPEAU')
    
        if d == 'oui': 
            plateau[int(x)][int(y)]['etat'] = DRAPEAU
        else : 
            return (int(x),int(y))
    print(coup_joueur(plateau,1,2)

    def case_voisines(plateau,x,y):
            largeur = len(plateau)
            hauteur = len(plateau[0])
            l = []
            for i in range(-1,2):  #case restantes au centre du plateau
                for j in range(-1,2):
                    l.append([x+i,y+j])   
            l.remove([x,y])
            l2=[]
            for k in l:
                if k[0] >= 0 and k[1] >= 0:
                    if k[0] < largeur and k[1]< hauteur:
                        l2.append(k)
            return l2   
    L= case_voisines(plateau,0,0)[0]
    
    def compte_mines_voisines(plateau,x,y):
        compt = 0
        t = len(L)
        for k in range(t):
            if plateau[L[k][0]][L[k][1]]['mine']== True:
                compt+=1
        return compt
        
    print(compte_mines_voisines(plateau,0,0))  #la variable plateau n'est pas static


    def composante_connexe(plateau,x,y):
        # met le plateau à jour en ouvrant toutes les cases vides à partir de la case (x,y)
        #il d'agit d'une procédure, il s'agir d'un bloc d'instructions qui ne renvoie pas de valeur à la fin.
        #ici la variable plateau est modifié.
        if plateau[x][y]['etat'] != INCONNU:
            return
        plateau[x][y]["etat"] = compte_mines_voisines(plateau, x, y)
        if plateau[x][y]['etat'] > 0:
            return
        else:
            for i in l:
                composante_connexe(plateau,i[0],i[1])
        
    def decouvre_case(plateau,x,y):
        "fonction et procédure a la fois car renvoie un booléen et modifie l'argument plateau. renvoie False si la case contenait une mine et True sinon."
        if plateau[x][y]["mine"]==True:
            plateau[x][y]["etat"] = PERDU
            print("OUPS La case contenait une mine...")
            return False
        composante_connexe(plateau,x,y)
        return True
    print(decouvre_case(plateau,0,0))

    def compte_mine_solution(plateau):
        l = len(plateau)
        h = len(plateau[0])
        for x in range(l):
            for y in range(h):
                if plateau[x][y]["etat"] == INCONNU and not plateau[x][y]["mine"]:
                    plateau[x][y]["etat"] = compte_mines_voisines(plateau,x,y)
        return plateau   #normalement on ne renvoie pas le plateau
    print(compte_mine_solution(plateau))



    """
    def total_mines(plateau):
        #Compte le nombre total de mines sur le plateau.
        c = 0
        for i in plateau:
            for j in i:
                if j['mine'] == True:
                    c +=1
        return c
    print(total_mines(plateau))
"""


    
