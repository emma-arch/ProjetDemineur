# projet_python
## informations génerales
le but du jeu du démineur est de découvrir toute les cases vides du plateau sans faire exploser les mines.
***
le plateau est représenté par un liste de liste de dictionnaire.
La case de coordonnée (x,y) est un dictionnaire donc une paire clé valeur.
  - "mine" qui est un booléen et qui indique si la case contient une mine 
  - "etat" indique l'état de la case :
  - INCONNU quand le joueur n'a pas découvert la case
  - un entier compris entre 0 et 8 qui indique le nombre de mines voisines, quand le joueur a decouvert la case.
  - PERDU quand il s'agit d'une case avec une mine, que le joueur a selectionne.
  - DRAPEAU si le joueur a mis un drapeau.

Les 4 des 13 etats possibles sont modelises par les étiquettes suivantes : 

INCONNU = _
PERDU = !
DRAPEAU = |>


### collaboration
le projet à été mené bien par aina ahmed et emma brillat.

### explications des fonctions
La fonction `genere_plateau(largeur,hauteur,prob_mine)` créée un plateau d'une certaine taille et avec une certaine probabilité d'avoir des mines.
la largeur correspond à l'axe vertical et la hauteur à l'axe horizontal.

la fonction `coup-joueur(x,y)` demande au joueur si il veut mettre un drapeau ou de rentrer les coordonnées de la case qu'il veut découvrir.
la fonction `decouvre_case(plateau,x,y)` est a la fois une procédure et une fonction car elle renvoie False si la case contient une mine et True sinon,
 tous ça en changent la variable plateau. En effet si False alors l'état de la case
 devient PERDU et sinon l'état devient égal au nombre de mine qu'il y a autour de la case (grâce à l'execution de la fonction conposante_connexe).
La fonction `composante_connexe(plateau,x,y)` modifie l'état de la case que l'on découvre et celle de ses voisines si elles ne sont inconnues et que la case découverte n'as pas de mine autour d'elle.

idée de se que fait tous notre code
---> genere_plateau
---> coup-joueur : soit on met un drapeau
                   soit on rentre les coordonnées de la case qu'on veut ouvrir
---> check : {si mine alors on a perdu
             sinon nombre de mine dans les cases_voisines }; `decouvre_case`: {si 0 alors on compte le nombre de mine des cases voisines
                                                                             sinon on affiche le nombre de mine qu'il y a autour}; `composante_connexe`
             ---> coup-joueur : si drapeau ---> coup joueur
                                sinon ---> check
             
---> si total_mine == nombre de drapeau + nombre de case non découverte alors on a gagné.


             

