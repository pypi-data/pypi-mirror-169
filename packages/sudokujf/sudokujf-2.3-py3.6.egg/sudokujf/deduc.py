# deduc.py
"""
Déductions automatiques
"""

def deduc_case(grille, ligne, colonne):
    """
    Déductions réalisées sur une Case
    ...
    Paramètre:
    ----------
    grille: Grille
        La grille sur laquelle on fait des déductions
    ligne, colonne: int
        Les coordonnées de la case (de 0 à 9)
    """
    la_case = grille.get_case(ligne, colonne)
    ligne, colonne, secteur = la_case.get_coord()
    une_valeur = la_case.get_value()
    if une_valeur != 0:
        return
    les_values = []

    for une_case in grille.les_lignes[ligne]:
        if une_case == la_case:
            continue
        une_valeur = une_case.get_value()
        if une_valeur != 0:
            les_values.append(une_valeur)

    for une_case in grille.les_colonnes[colonne]:
        if une_case == la_case:
            continue
        une_valeur = une_case.get_value()
        if une_valeur != 0:
            les_values.append(une_valeur)

    for une_case in grille.les_secteurs[secteur]:
        if une_case == la_case:
            continue
        une_valeur = une_case.get_value()
        if une_valeur != 0:
            les_values.append(une_valeur)

    for une_valeur in les_values:
        if une_valeur in la_case.get_candidats():
            grille.remove_candidat(ligne, colonne, une_valeur)

def deduc_type_groupe(grille, type_groupe, ligne, colonne):
    """
    Déductions réalisées sur une Case. On supprime
    les candidats qui apparaissent sur la même ligne (ou colonne
    ou secteur).
    ...
    Paramètre:
    ----------
    grille: Grille
        La grille sur laquelle on fait des déductions
    type_groupe: (str)
        "ligne" ou "colonne" ou "secteur"
    ligne, colonne: (int)
        Les coordonnées de la case (de 0 à 9)
    """
    la_case = grille.get_case(ligne, colonne)
    _, _, secteur = la_case.get_coord()
    if type_groupe == "ligne":
        numero = ligne
    elif type_groupe == "colonne":
        numero = colonne
    elif type_groupe == "secteur":
        numero = secteur
    else:
        return
    les_cases = get_type_groupe(grille, type_groupe, numero)

    une_valeur = la_case.get_value()
    if une_valeur != 0:
        return
    les_values = []

    for une_case in les_cases:
        if une_case == la_case:
            continue
        une_valeur = une_case.get_value()
        if une_valeur != 0:
            les_values.append(une_valeur)

    for une_valeur in les_values:
        if une_valeur in la_case.get_candidats():
            la_case.remove_candidat(une_valeur)

def deduc_ligne_colonne(grille, secteur, value):
    """
    Réalise des déductions basées sur l'algo "LigneColone"
    ...
    Paramètre:
    ----------
    secteur: int
        Le numéro du secteur
    value: int
        La valeur que l'on veut trouver dans le secteur
    """
    contenu_secteur = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    for une_case in grille.les_secteurs[secteur]:
        une_valeur = une_case.get_value()
        if une_valeur != 0:
            if une_valeur == value:
                return
            else:
                contenu_secteur[i] = 1
        i += 1
    lignes = [[0, 1, 2], [0, 1, 2], [0, 1, 2],
              [3, 4, 5], [3, 4, 5], [3, 4, 5],
              [6, 7, 8], [6, 7, 8], [6, 7, 8]]
    colonnes = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
               [0, 1, 2], [3, 4, 5], [6, 7, 8],
               [0, 1, 2], [3, 4, 5], [6, 7, 8]]
    k = 0
    for i in lignes[secteur]:
        for une_case in grille.les_lignes[i]:
            une_valeur = une_case.get_value()
            if une_valeur == value:
                for j in range(3):
                    contenu_secteur[k*3+j] = 1
        k += 1

    k = 0
    for i in colonnes[secteur]:
        for une_case in grille.les_colonnes[i]:
            une_valeur = une_case.get_value()
            if une_valeur == value:
                for j in range(3):
                    contenu_secteur[j*3+k] = 1
        k += 1

    nb_de_zeros = 0
    coord = 0
    for i in range(9):
        if contenu_secteur[i] == 0:
            nb_de_zeros += 1
            coord = i
    if nb_de_zeros != 1:
        return

    i = coord // 3
    j = coord % 3
    ajout = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
    ligne = i + ajout[secteur][0]
    colonne = j + ajout[secteur][1]
    grille.set_case(ligne, colonne, value)

def get_type_groupe(grille, type_groupe, numero):
    """
    Renvoie un groupe de cases (une ligne, une colonne, un secteur)
    ...
    Paramètres:
    -----------
    grille: Grille
        La grille sur laquelle on fait les déductions
    type_groupe: str
        Le type de groupe ("ligne", "colonne" ou "secteur")
    numero: int
        Le numéro de ligne ou de  colonne  ou de secteur
    """
    if type_groupe == "ligne":
        les_cases = grille.les_lignes[numero]
    elif type_groupe == "colonne":
        les_cases = grille.les_colonnes[numero]
    elif type_groupe == "secteur":
        les_cases = grille.les_secteurs[numero]
    else:
        les_cases = None
    return les_cases

def deduc_multiplet(grille, type_groupe, numero):
    """
    Réalise des déductions basées sur les éliminations des multiplets
    ...
    Paramètre:
    ----------
    type_groupe: str
        Le type de groupe ("ligne", "colonne" ou "secteur")
    numero: int
        Le numéro de ligne ou de  colonne  ou de secteur
    """
    multiplets = {}

    les_cases = get_type_groupe(grille, type_groupe, numero)
    if les_cases is None:
        return

    for une_case in les_cases:
        candidats = une_case.get_candidats()
        cle = str(candidats)
        if cle in multiplets:
            multiplets[cle].append(une_case)
        else:
            multiplets[cle] = [une_case]

    for cle in multiplets.keys():
        objet = eval(cle)
        if len(multiplets[cle]) >= len(objet):
            for une_case in les_cases:
                if une_case in multiplets[cle]:
                    continue
                for un_candidat in objet:
                    une_case.remove_candidat(un_candidat)

def deduc_seule_possible(grille, type_groupe, numero):
    """
    Déductions réalisées sur un groupe (ligne, colonne, secteur)
    On déduit une valeur d'une case si c'est la seule possible pour
    le groupe.
    ...
    Paramètres:
    grille: Grille
        La grille sur laquelle on fait des déductions
    type_groupe: (str)
        "ligne" ou "colonne" ou "secteur"
    numero: int (de 0 à 8)
        Le numéro de la ligne (ou de la colonne ou du secteur) 
    """
    les_cases = get_type_groupe(grille, type_groupe, numero)
    if les_cases is None:
        return

    les_cases_par_valeur = []
    valeurs_trouvees = []

    for une_case in les_cases:
        candidats = une_case.get_candidats()
        if len(candidats) == 1:
            valeurs_trouvees.append( list(candidats)[0] )

    for i in range(10):
        les_cases_par_valeur.append( [] )
    for une_case in les_cases:
        candidats = une_case.get_candidats()
        if len(candidats) == 1: continue
        coord = une_case.get_coord()
        for un_candidat in candidats:
            if un_candidat in valeurs_trouvees:
                continue
            les_cases_par_valeur[un_candidat].append(coord)
    for i in range(1,10):
        if len(les_cases_par_valeur[i]) == 1:
            ligne, colonne, secteur = les_cases_par_valeur[i][0]
            grille.set_case(ligne, colonne, i)
