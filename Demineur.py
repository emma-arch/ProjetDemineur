import random
import math
INCONNU = '_'
PERDU = '!'
DRAPEAU = '|>'

def genere_plateau(largeur, hauteur, prob_mine): #prob_mine supposer != de 0 et 1
    plateau = []
    c=0
    for i in range(hauteur):
        plateau.append([])
        for j in range(largeur):
                if random.randint(0,1)==0 and c<int(largeur*hauteur*prob_mine):
                    c+=1
                    plateau[i].append({"mine" : True, 
                                        "etat" : INCONNU})         
                else :
                    plateau[i].append({"mine" : False, 
                                        "etat" : INCONNU })
    return plateau


def coup_joueur(plateau):
    #le joueur donne (x,y) ou il met un drapeau
    x = input("Entre une coordonnées selon la verticale ")
    y = input("Entre une coordonnées selon l'horizontale ")
    d = input("Veut tu mettre un DRAPEAU ? ")

    if d == 'oui': 
        plateau[int(x)][int(y)]['etat'] = DRAPEAU
        return (int(x),int(y))

    else : 
        return (int(x),int(y))


def case_voisines(plateau,x,y):
        if plateau[x][y]["etat"] == DRAPEAU:
            return
        hauteur = len(plateau)
        largeur = len(plateau[0])
        l = []
        for i in range(-1,2):  #case restantes au centre du plateau
            for j in range(-1,2):
                l.append([x+i,y+j])   
        l.remove([x,y])
        l2=[]
        for k in l:
            if k[0] >= 0 and k[1] >= 0:
                if k[0] < hauteur and k[1]< largeur:
                    l2.append(k)
        return l2   

def compte_mines_voisines(plateau,x,y):
    compt = 0
    L = case_voisines(plateau,x,y)
    t = len(L)
    for k in range(t):
        if plateau[L[k][0]][L[k][1]]['mine']== True:
            compt+=1
    return compt
    

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
        for i in L:
            composante_connexe(plateau,i[0],i[1])
   
def decouvre_case(plateau,x,y):
    "fonction et procédure a la fois car renvoie un booléen et modifie l'argument plateau. renvoie False si la case contenait une mine et True sinon."
    if plateau[x][y]["mine"] == True and plateau[x][y]["etat"] != DRAPEAU:
        plateau[x][y]["etat"] = PERDU
        print("Tu as perdu")
        return False 
    else :
        composante_connexe(plateau,x,y)
    return True


def compte_mine_solution(plateau):
    h = len(plateau)
    l = len(plateau[0])
    for x in range(h):
        for y in range(l):
            if not plateau[x][y]["mine"]:
                plateau[x][y]["etat"] = compte_mines_voisines(plateau,x,y)
            else : 
                plateau[x][y]["etat"] = PERDU
    return plateau


def total_mines(plateau):
    #Compte le nombre total de mines sur le plateau.
    c = 0
    for i in plateau:
        for j in i:
            if j['mine'] == True:
                c +=1
    return c

def check(plateau):
    #compte le nombre de drapeau et de case inconnue
    c = 0
    for i in plateau:
        for j in i:
            if j['etat'] == -1 or j['etat'] == -3:
                c += 1
    return c

def display(plateau):
    #permet d'afficher la grille
    for ligne in plateau:
        for colonne in ligne:
            print(colonne['etat'], '  ', end="")
        print()
    return None

def level(scores):
    if scores[0] <=  2:
        plateau = genere_plateau(5,5,0.3)
    if   3 <= scores <= 5  :
        plateau = genere_plateau(10,20,0.5)
    else:
        plateau = genere_plateau(30,40,0.6)
    return plateau
    
def write_score(filename, score):
    with open(filename, mode='a', encoding='utf8') as f:
        f.write(str(score))
        f.write('\n')

def read_scores(filename):
    with open(filename, mode='r', encoding='utf8') as f:
        scores = f.readlines()

    return scores

filename = 'scores.txt'
write_score(filename, 0)

scores = read_scores(filename)

print(scores)
#3niveau de jeu: Facile, intermédiaire, expert
plateau=level(scores)

while True:
    display(plateau)
    x,y = coup_joueur(plateau)
    L = case_voisines(plateau,x,y)
    if not decouvre_case(plateau,x,y):   
        plateau = compte_mine_solution(plateau)
        display(plateau)                                                   
        plateau = genere_plateau(20,30,0.5) 
    if total_mines(plateau) == check(plateau):
        print("tu as gagné")
        plateau = genere_plateau(20,30,0.5)
       
    
    
    
        