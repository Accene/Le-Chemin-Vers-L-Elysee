#   permet de faire un choix entre oui et non.
def oui_non():
  print("Choisir oui ou non.")
  urep = input()
  if urep == 'OUI' or urep=='oui':
    return True
  elif urep == 'NON' or urep=='non':
    return False
  while  urep != 'OUI' or urep!='oui' or urep != 'NON' or urep!='non' :
    print('ERREUR ! choisissez oui ou non.')
    urep = input()
    if urep == 'OUI' or urep=='oui':
      return True
    elif urep == 'NON' or urep=='non':
      return False


#   permet de faire un choix entre les chiffres 1 et 2.
def un_deux():
  urep = input()
  if urep == '1' :
    return True
  elif urep == '2' :
    return False
  while  urep != '1' or urep!= '2' :
    print('ERREUR ! choisissez 1 ou 2.')
    urep = input()
    if urep == '1' :
      return True
    elif urep == '2':
      return False

#   permet de faire un choix entre les chiffres 1, 2, 3 ou 4.
def un_quatre():
  urep = input()
  if urep == '1' :
    return 1
  elif urep == '2' :
    return 2
  elif urep == '3' :
    return 3
  elif urep == '4' :
    return 4
  while  urep!='1' or urep!='2' or urep!='3' or urep!='4':
    print('ERREUR ! choisissez 1, 2, 3 ou 4.')
    urep = input()
    if urep == '1' :
      return 1
    elif urep == '2' :
      return 2
    elif urep == '3' :
      return 3
    elif urep == '4' :
      return 4

#   permet de faire un choix entre les chiffres 1, 2, 3, 4 ou 5.
def un_cinq():
  urep = input()
  if urep == '1' :
    return 1
  elif urep == '2' :
    return 2
  elif urep == '3' :
    return 3
  elif urep == '4' :
    return 4
  elif urep == '5' :
    return 5
  while  urep!='1' or urep!='2' or urep!='3' or urep!='4' or urep!='5':
    print('ERREUR ! choisissez 1, 2, 3, 4 ou 5.')
    urep = input()
    if urep == '1' :
      return 1
    elif urep == '2' :
      return 2
    elif urep == '3' :
      return 3
    elif urep == '4' :
      return 4
    elif urep == '5' :
      return 5

#   presentation print rpg.
def presentation_rpg():
  print("___________________________________________________________________________________________")
  print("\n")
  print(
  "#################              ################                 ############################\n"
  "##              ##             ##              ##               ##                        ##\n"
  "##               ##            ##                ##             ##                        ##\n"
  "##                ##           ##                  ##           ##                        ##\n"
  "##                ##           ##                  ##           ##                          \n"
  "##               ##            ##                ##             ##                          \n"
  "##              ##             ##################               ##                          \n"
  "##            ##               ##                               ##                          \n"
  "##          ##                 ##                               ##              ############\n"
  "##        ##                   ##                               ##              ##        ##\n"
  "##          ##                 ##                               ##              ##        ##\n"
  "##            ##               ##                               ##                        ##\n"
  "##              ##             ##                               ##                        ##\n"
  "##                ##           ##                               ############################\n"
  )
  print("\n")
  print("___________________________________________________________________________________________")
  return

def about(): 
  print(
  "Nom du projet :  Le chemin vers l'elys??e \n"
  "Membres du groupe de 5 ainsi que leurs r??les :\n"
  "                                             HAKIRI Emir --> Chef de projet & rassemblement des parties, parties deplacament_RPG.py, main_RPG.py\n"
  "                                             LIMACO DIEGO --> Gestion de l'inventaire, partie inventaire_RPG.py\n"
  "                                             MUGUET Benoit --> Gestion des combats, partie combat_RPG.py\n"
  "                                             ROY Accene --> Gestion des menus et de la sauvegarde, partie menu_RPG.py\n"
  "                                             FERNANDES Guy --> Assistance et narration (NB : malade au moment du projet)\n"
  "Lieu : HETIC\n"
  "Encadrement : JANIN Lo??c\n"
  "Language de programation : Python\n"
  "Date de rendu limite : 5 janvier 2022\n"
  "But du jeu : Le joueur se met dans la peau d'un candidat ?? la presidentielle, il doit recolt?? le plus d'??l??cteurs et combattre les autre candidat pour gagn?? sa place ?? l'??lys??e.\n"
  "\n"
  "D??roulement du jeu :\n"
  "Le jeu est en 5 ??tapes (ou niveaux), chaqu'un de ces niveau est caract??riser par un candidat ?? la pr??sidentielle qui est mis dans un contexte autour duquel sera form??,\n"
  "au fur et mesure des interactions du joueur, une situation menant ?? un combat.\n"
  "Les personnages cles sont les suivants, dans l'ordre du jeu : -Hidalgo --> La marre de Paris\n"
  "                                                              -Zemmour --> The hummour\n"
  "                                                              -Melanchon --> Melonchaud\n"
  "                                                              -Le Pen --> Pas la peine\n"
  "                                                              -Benalla --> Alexandre\n"
  "\n"
  "\n"
  "Comment gagn?? le jeu ? :\n"
  "Pour gagn?? le jeu il faut reussir ?? arriver ?? la derni??re et 5e ??tape, battre le dernier boss, et tout d'abord avoir recolt?? plus de 60 ??l??cteurs.\n"
  "\n"
  "\n"
  "Comment se d??roule les combats ? :\n"
  "Une fois le cambat d??clancher le joueur ?? le choix de combattre ou de quitter le combat, si le joueur combat jusqu'au bout et gagne le combat,\n"
  "il repare avec 200 points de vie, 100 ??l??cteurs, et l'arme de son adversaire.\n"
  "En revenche si il perd le combat, (c'est ?? dire qu'il n'a plus de points de vie), il repare qu'avec 10 ??l??cteurs, puis il passe au niveau suivant (?? part le 3e combat, si il le perd il perd le jeu).\n"
  "\n"
  "\n"
  "Qu'en est-il des menus ? :\n"
  "dans le jeu nous avons 5 menus diff??rents :\n"
  "Le premier menu :\n"
  "Le premier menu ne s'affiche qu'une seule fois, au lancement du programme, il permet au joueur de : -D??marrer une nouvelle partie\n"
  "                                                                                                    -Reprendre ?? un niveau sauvegarder\n"
  "                                                                                                    -Lire ce que vous lisez ?? linstant\n"
  "                                                                                                    -Quitter le jeu\n"
  "\n"
  "Le menu principale :\n"
  "Le menu principale s'affiche parmis les choix du joystick, une fois selectionner il permet au joueurs de : -Visualiser l'inventaire\n"
  "                                                                                                           -Nettoyer la console\n"
  "                                                                                                           -Lire ce que vous lisez ?? l'instant\n"
  "                                                                                                           -Quitter & sauvegarder le jeu, si vous choisissez quitter une option de sauvegarde s'affichera\n"
  "\n"
  "le joystick :\n"
  "Le joystick s'affiche ?? chaque fois que le joueur est appel?? ?? se d??placer, il permet au joueur de : -Avancer\n"
  "                                                                                                     -Se diriger ?? droite\n"
  "                                                                                                     -Se diriger ?? gauche\n"
  "                                                                                                     -Faire de mis-tour\n"
  "                                                                                                     -Afficher le menu principale\n"
  "(NB : le joystick ?? pour but de cr??e une interraction avec le joueur, de se d??placer d'un niveau ?? un autre et de cr??e un systeme de r??compense au d??placement avec des objets qui apparaisse lorsque le joueur se d??place et qui peuvent ??tre ajouter ?? l'inventaire.)\n"
  "\n"
  "Le menu attaque :\n"
  "Le menu attaque appara??t lorsque le joueur rentre en mode combat, il permet au joueur de : -Attaquer\n"
  "                                                                                           -Afficher l'inventaire\n"
  "                                                                                           -Quitter le combat\n"
  "                                                                                           -Afficher le menu principale\n"
  "\n"
  "L'inventaire :\n"
  "L'inventaire ?? cet ??tape du projet n'ai pas vraiment un menu, il permet seulement de visualiser les objet recolt??s pendant les d??placements, et d'afficher le nombre d'??l??cteurs gagn??.\n"
  "\n"
  "Le vrai but de l'inventaire aurai ??t?? de non seulement voir les objet gagn?? mais en plus de pouvoir les utilis??, mais le temps ne nous ?? pas permis d'appliquer cette fonctionnalit??.\n"
  "\n"
  "autre chose ? :\n"
  "Le fichier fonction.py regroupes les fonctions les plus utilis??es dans le programme.\n"
  )
