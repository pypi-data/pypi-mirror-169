# __main__.py : le programme principal
"""
L'interface texte (TUI) à la bibliothèque grille qui permet
de jouer au SUDOKU
"""
# V2.0.0 (objectif: V2.0)
import sys
import re
import string
from .grille import Grille, is_value_correcte, CreeGrille
from .deduc import deduc_case, deduc_type_groupe, deduc_ligne_colonne, deduc_multiplet, deduc_seule_possible, get_type_groupe

def aide():
    """
    Affiche l'aide en ligne
    """
    print("quit:    quitter")
    print("help:    aide")
    print("tbug:    Permute le mode DEBUG")
    print("veri:    vérification de la cohérence de la grille")
    print("undo:    on annule la dernière opération")
    print("addc:    Ajoute un(des) candidat(s) à une case, (addc,F4,34)")
    print("rmvc:    Supprime un(des) candidat(s) d'une case, (rmvc,F4,7)")
    print("getc:    Liste les candidats d'une case, (getc,F4)")
    print("dedu:    Réaliser des déductions automatiques")
    print("glog:    Affiche le journal des modifications")
    print("gcan:    Affiche tous les candidats d'un groupe (gcan,<type>,4)")
    print("         Remarque: les types:  ligne | colonne | secteur")

def nouvelle_partie(un_fichier):
    """
    Lit et décode un fichier contenant une Grille
    ...
    Paramètres:
    -----------
    un_fichier: str
        Le chemin du fichier

    Valeur de retour:
    -----------------
    Une instance de Grille

    Exceptions:
    -----------
    - FileNotFoundError
    - Exception si la Grille a un format incorrecte
    """
    handler = open(un_fichier, "r")
    chaine = handler.read()
    lst_cases = []
    for car in chaine:
        if   car == ".":
            lst_cases.append(0)
        elif car.isnumeric():
            lst_cases.append(int(car))
    instance = Grille(lst_cases)
    handler.close()
    return instance

def affiche_grille():
    """
    Affiche la Grille
    """
    value_trouvees = LA_GRILLE.get_value_connu()
    print("    A B C |D E F |G H I", end="")
    if LA_GRILLE.debug:
        print(" (mode DEBUG actif)")
    else: print()
    for i in range(9):
        if (i % 3) == 0:
            print("   ---------------------")
        print("%2d " % (i+1), end="")
        for j in range(9):
            if (j % 3) == 0:
                print("|", end="")
            contenu = LA_GRILLE.get_case(i, j).get_value()
            if contenu == 0:
                contenu = "."
            else:
                contenu = str(contenu)
            print(contenu, end=" ")
        if (i+1) in value_trouvees:
            print("*",end="")
        print()
    print("   ---------------------")
    nbconnu = LA_GRILLE.get_nb_connu()
    nbcandidats = LA_GRILLE.get_nb_candidats()
    print("Nombre de cases connues: %d, candidats: %d" % (nbconnu, nbcandidats))

def gcan(type_groupe, numero):
    """ affiche les candidats d'un groupe """
    les_cases = get_type_groupe(LA_GRILLE, type_groupe, numero)
    if les_cases is None:
        return
    for une_case in les_cases:
        ligne, colonne, _ = une_case.get_coord()
        les_candidats = une_case.get_candidats()
        if len(les_candidats) == 1:
            continue
        print(", [%s%d]: " % (COLONNES[colonne], ligne+1), end="")
        print(les_candidats, end=" ")
    print()

def  deduction():
    """
    Sous-menu associé aux déductions
    """
    old_cmd = "quit"
    LA_GRILLE.set_synchro()
    while True:
        affiche_grille()
        print("===== deductions pour une case ou une ligne, ...  ======")
        print("type:        déduction par ligne/colonne/secteur (type,<type>,F4)")
        print("             Remarque: les types: ligne | colonne | secteur")
        print("case:        déduction pour une case (case,F4)")
        print("multiplet:   (multiplet,<type>,5)")
        print("seule:       Seule possibilité, (seule,<type>,6)") 
        print("ligcol:      Algo Ligne/Colonne, (ligcol,4,5) [secteur,valeur]")
        print("===== deductions évoluées ========")
        print("cases:       idem de candidtat, mais pour toutes les cases")
        print("ligscols:    Idemd de ligcol, mais pour tous les secteurs et valeurs")
        print("seules:      Seule possibilité, mais pour tous les groupes") 
        print("multiplets:  Multiplet pour toutes les cases")
        print("----------------------------------")
        print("TOUT:        Utilise toutes les méthodes")
        print("quit:        QUITTER")
        choix = input("Commande ? ")
        if  choix == "":
            choix = old_cmd
        else:
            old_cmd = choix
        if choix == "quit":
            break
        elif choix[:4] == "type":
            match = re.search(r'^type,(ligne|colonne|secteur),([A-I])([1-9])', choix)
            if match:
                type_groupe = match.group(1)
                colonne = COLONNES.find(match.group(2))
                ligne = int(match.group(3))-1
                LA_GRILLE.set_synchro()
                deduc_type_groupe(LA_GRILLE, type_groupe, ligne, colonne)
        elif choix[:10] == "multiplet,":
            match = re.search('^multiplet,(ligne|colonne|secteur),([1-9])', choix)
            if match:
                type_groupe = match.group(1)
                numero = int(match.group(2))-1
                LA_GRILLE.set_synchro()
                deduc_multiplet(LA_GRILLE, type_groupe, numero)
        elif choix[:5] == "case,":
            match = re.search(r'^case,([A-I])([1-9])', choix)
            if match:
                colonne = COLONNES.find(match.group(1))
                ligne = int(match.group(2))-1
                print("===case===>", ligne, colonne)
                deduc_case(LA_GRILLE, ligne, colonne)
        elif choix[:6] == "seule,":
            match = re.search('^seule,(ligne|colonne|secteur),([1-9])', choix)
            if match:
                type_groupe = match.group(1)
                numero = int(match.group(2))-1
                LA_GRILLE.set_synchro()
                deduc_seule_possible(LA_GRILLE, type_groupe, numero)
        elif choix == "cases":
            for i in range(9):
                for j in range(9):
                    deduc_case(LA_GRILLE, i, j)
        elif choix == "multiplets":
            for type_groupe in ["ligne", "colonne", "secteur"]:
                for i in range(9):
                    deduc_multiplet(LA_GRILLE, type_groupe, i)
        elif choix == "seules":
            for type_groupe in ["ligne", "colonne", "secteur"]:
                for i in range(9):
                    deduc_seule_possible(LA_GRILLE, type_groupe, i)
        elif choix[:7] == "ligcol,":
            match = re.search(r'ligcol,([1-9]),([1-9])')
            if match:
                secteur = match.group(1) - 1
                valeur = match.group(2)
                deduc_ligne_colonne(LA_GRILLE, secteur, valeur)
        elif choix == "ligscols":
            for secteur in range(9):
                for valeur in range(1, 10):
                    deduc_ligne_colonne(LA_GRILLE, secteur, valeur)
        elif choix == "TOUT":
            nbcandidats = LA_GRILLE.get_nb_candidats()
            while True:
                for secteur in range(9):
                    for valeur in range(1, 10):
                        deduc_ligne_colonne(LA_GRILLE, secteur, valeur)
                for i in range(9):
                    for j in range(9):
                        deduc_case(LA_GRILLE, i, j)
                for type_groupe in ["ligne", "colonne", "secteur"]:
                    for i in range(9):
                        deduc_multiplet(LA_GRILLE, type_groupe, i)
                for type_groupe in ["ligne", "colonne", "secteur"]:
                    for i in range(9):
                        deduc_seule_possible(LA_GRILLE, type_groupe, i)
                nbcandidatsnew = LA_GRILLE.get_nb_candidats()
                if nbcandidatsnew < nbcandidats:
                    nbcandidats = LA_GRILLE.get_nb_candidats()
                    continue
                break

def grande_boucle():
    """
    boucle principale du programme. A chaque tour de boucle
    le joueur saisie une hypothèse pour une case ou active
    une des commandes du menu.
    """
    while True:
        affiche_grille()
        saisie = input("Remplir une case: 'F4=4' (saisie vide ou 'help': menu) ? ")
        if saisie == "quit":
            break
        elif saisie == "help" or saisie == "":
            aide()
        elif "=" in saisie:
            print(">>>> Fixe la valeur d'une Case (0: Annule une saisie)")
            match = re.search(r'([A-I])([1-9])=([0-9])', saisie)
            if match:
                ligne = int(match.group(2))-1
                value = int(match.group(3))
                colonne = COLONNES.find(match.group(1))
                LA_GRILLE.set_synchro()
                LA_GRILLE.set_case(ligne, colonne, value)
        elif saisie == "tbug":
            LA_GRILLE.toggle_debug()
        elif saisie[:4] == "gcan":
            match = re.search(r'^gcan,(secteur|colonne|ligne),([1-9])', saisie)
            if match:
                gcan(match.group(1),int(match.group(2))-1)
        elif saisie == "glog":
            LA_GRILLE.get_log()
        elif saisie == "veri":
            if LA_GRILLE.verif():
                print("========> La grille est correcte")
            else:
                print("ERREUR (2 valeurs identiques sur une ligne, colonne, secteur")
        elif saisie == "undo":
            print(">>>> Annule la dernière opération")
            LA_GRILLE.undo()
        elif saisie[:4] == "addc":
            print(">>>> Ajoute un candidat à une Case")
            match = re.search(r'^addc,([A-I])([1-9]),([1-9]+)', saisie)
            if match:
                ligne = int(match.group(2))-1
                colonne = COLONNES.find(match.group(1))
                LA_GRILLE.set_synchro()
                for value in match.group(3):
                    LA_GRILLE.add_candidat(ligne, colonne, int(value))
        elif saisie[:4] == "rmvc":
            print(">>>> Retire un candidat à une Case")
            match = re.search(r'^rmvc,([A-I])([1-9]),([1-9]+)', saisie)
            if match:
                ligne = int(match.group(2))-1
                colonne = COLONNES.find(match.group(1))
                LA_GRILLE.set_synchro()
                for value in match.group(3):
                    LA_GRILLE.remove_candidat(ligne, colonne, int(value))
        elif saisie[:4] == "getc":
            print(">>>> Affiche les candidats d'une Case")
            match = re.search(r'^getc,([A-I])([1-9])', saisie)
            if match:
                ligne = int(match.group(2))-1
                colonne = COLONNES.find(match.group(1))
                print(LA_GRILLE.get_candidats(ligne, colonne))
        elif saisie == "dedu":
            deduction()

    nbconnu = LA_GRILLE.get_nb_connu()
    verification = LA_GRILLE.verif()
    if nbconnu == 81 and verification:
        print("Vous avez réussi, BRAVO!!!")
    return

#========== DEBUT DU PROGRAMME PRINCIPAL ==========================
if len(sys.argv) < 2:
    print(f"Syntaxe: {sys.argv[0]} une_grille")
    print("  Le fichier qui contient une grille est fait de 9 lignes")
    print("  Exemple de ligne:   ..65..7...")
    sys.exit(1)
FICHIER = sys.argv[1]
try:
    LA_GRILLE = nouvelle_partie(FICHIER)
except FileNotFoundError:
    print("ERREUR: le fichier n'existe pas")
    sys.exit(2)
except PermissionError:
    print("ERREUR: vous n'avez pas les droits d'accès au fichier")
    sys.exit(2)
except CreeGrille:
    print("ERREUR: le format du fichier est incorrect")
    sys.exit(2)
#------------------------------------
COLONNES = "ABCDEFGHI"
grande_boucle()
