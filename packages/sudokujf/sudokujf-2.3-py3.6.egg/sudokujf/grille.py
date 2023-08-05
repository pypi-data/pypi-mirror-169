# grille.py
"""
Contient l'API Grille et la classe sous-jacente Case
ainsi que les classes d'exception associées
et des outils vérifie une value ainsi qu'une coordonnée
"""

class CreeGrille(Exception):
    """
    Classe d'exception qui vérifie l'initialisation de la Grille
    """
    def __init__(self, message):
        super().__init__(message)

class ValeurIncorrecte(Exception):
    """
    Classe d'exception qui vérifie si une valeur est valide
    """
    def __init__(self):
        super().__init__("Valeur doit etre un entier valide (dans les bornes")

def is_value_correcte(value, minimum=0, maximum=9):
    """
    Vérifie si value a une valeur correcte (int de minimum à maximum)
    ...
    Paramètres:
    -----------
    value: int
        valeur dont on teste la cohérence (int de minimum à maximum)
    Exceptions:
    -----------
    Lève l'Exception ValeurIncorrecte si valeur est incorrecte
    """
    if not isinstance(value, int):
        print("non entier")
        raise ValeurIncorrecte()
    if value < minimum or value > maximum:
        print("en dehors bornes")
        raise ValeurIncorrecte()

def is_coord_correcte(value):
    """
    Vérifie si value a une valeur correcte (int de 0 à 8)
    ...
    Paramètres:
    -----------
    value: int
        valeur de 0 à 8
    Exceptions:
    - ValeurIncorrecte
    ----------
    Lève l'Exception CoordIncorrecte si valeur incorrecte
    """
    if not isinstance(value, int):
        raise ValueError()
    if value < 0 or value > 8:
        raise ValeurIncorrecte()

class Grille:
    """
    Cette classe représente une grille de Sudoku
    ...
    Attributs:
    ---------
    lst_cases : list de Case
        L'adresse des 81 cases (de type "Case") qui composent une
        Grille.
    les_lignes, les_colonnes, les_secteurs : list de liste de Case
        L'adresse de groupes de cases. Par exemple, les_lignes
        contient l'adresse de 9 groupes, une par ligne. Chaque
        groupe contenant l'adresses des 9 cases formant une ligne.
    log : list de list
        Contient l'historique des opérations effectuées. Ce qui
        permet de faire une opération "undo".
        enreg: "humain"|"ordi",<operation>,ligne,colonne,oldv,newv
        <operation>::= "setc" | "adc" | "rmc"
    debug: bool
        Permet d'activer le mode verbeux (débogage)
    """
    def __init__(self, les_cases: bool, debug: bool=False):
        """
        Constructeur: Crée une Grille
        ...
        Paramètres:
        -----------
        les_cases: list de int
            La valeur initiale d'une Case. La valeur égale à zéro
            signifie une Case vide.
        debug: bool, par défaut False
            Permet d'activer le Debugging
        Exception:
        ---------
        - Lève l'Exception CreeGrille si la Grille est incorrecte
        - Lève l'Exception ValeurIncorrecte si value n'est pas
          entre 0 et 9
        """
        if len(les_cases) != 81:
            raise CreeGrille("Il faut 81 cases")
        for i in range(81):
            is_value_correcte(les_cases[i])

        self.debug = debug
        self.log = []
        self.lst_cases = []
        self.les_lignes = []
        for i in range(9):
            self.les_lignes.append([])
        self.les_colonnes = []
        for i in range(9):
            self.les_colonnes.append([])
        self.les_secteurs = []
        for i in range(9):
            self.les_secteurs.append([])
        ligne = colonne = secteur = 0
        for i in range(81):
            ligne = i // 9
            colonne = i % 9
            coord_x = colonne // 3
            coord_y = ligne // 3
            secteur = coord_y * 3 + coord_x
            une_case = Case(ligne, colonne, secteur, les_cases[i])
            self.lst_cases.append(une_case)
            self.les_lignes[ligne].append(une_case)
            self.les_colonnes[colonne].append(une_case)
            self.les_secteurs[secteur].append(une_case)

    def toggle_debug(self):
        """
        Permute la valeur du mode debug
        """
        if self.debug:
            self.debug = False
        else:
            self.debug = True

    def get_case(self, ligne, colonne):
        """
        Retrouve une Case par ses coordonnées
        ...
        Paramètres:
        ----------
        ligne, colonne: int
            Les coordonnées d'une Case
        Valeur de retour:
        ----------------
        L'adresse de la Case
        ...
        """
        return self.lst_cases[ligne * 9 + colonne]

    def set_synchro(self):
        """
        Démarre une transaction
        """
        self.log.append(["COMMIT"])

    def set_case(self, ligne, colonne, value):
        """
        Modifie la value d'une Case
        ...
        Paramètres:
        -----------
        ligne, colonne, value: int
            ligne, colonne: coordonnées, value: La nouvelle valeur
        """
        une_case = self.get_case(ligne, colonne)
        if une_case.verrou:
            return    # on log ???
        oldvalue = set(une_case.get_candidats())
        if value == 0:
            newvalue = {1,2,3,4,5,6,7,8,9}
            une_case.set_candidats(newvalue)
        else:
            newvalue = {value}
            une_case.set_candidats(newvalue)
        self.log.append(["modif", ligne, colonne, oldvalue])

    def get_value(self, ligne, colonne):
        """
        Retourne la value d'une case
        ...
        Paramètres:
        -----------
        ligne, colonne:
            Coordonnées d'une case
        Valeur de retour:
        -----------------
        La value d'une Case
        """
        une_case = self.get_case(ligne, colonne)
        return une_case.get_value()

    def get_log(self):
        """ Affiche l'historique des modifications
        (Ne fait pas partie de l'API, utilitaire de Debug)
        """
        print("debug: le journal des modifications")
        for item in self.log:
            print(item)

    def get_nb_connu(self):
        """ Renvoie le nombre de Cases occupées """
        nbconnu = 0
        for une_case in self.lst_cases:
            if une_case.get_value() != 0:
                nbconnu += 1
        return nbconnu

    def get_nb_candidats(self):
        """ Renvoie le nombre de Candidats restants """
        nbcandidats = 0
        for une_case in self.lst_cases:
            nbcandidats += len(une_case.get_candidats())
        return nbcandidats

    def get_value_connu(self):
        """ renvoie le tableau des value connus
        Exemple: si on a trouvé tous les "8", alors le "8"
        fait partie des value connus.
        """
        nb_par_value = [0]*10
        for une_case in self.lst_cases:
            value = une_case.get_value()
            if value != 0:
                nb_par_value[value] += 1
        value_trouvees = []
        for i in range(1,10):
            if nb_par_value[i] == 9:
                value_trouvees.append(i)
        return value_trouvees

    def verif(self):
        """ Vérifie si il y a des incohérences, par exemple
        deux 7 dans la même ligne
        ...
        Valeur de retour: True si le test réussie
        """
        verif_ok = True
        # 1. On vérifie les lignes
        for i in range(9):
            les_valeurs = [0]*10
            for j in range(9):
                index = self.les_lignes[i][j].get_value()
                if index == 0:
                    continue
                if les_valeurs[index] != 0:
                    verif_ok = False
                    if self.debug:
                        print("debug: Verif Ligne ECHOUE")
                else:
                    les_valeurs[index] = 1
        # 2. On vérifie les colonnes
        for i in range(9):
            les_valeurs = [0]*10
            for j in range(9):
                index = self.les_colonnes[i][j].get_value()
                if index == 0:
                    continue
                if les_valeurs[index] != 0:
                    verif_ok = False
                    if self.debug:
                        print("debug: Verif Colone ECHOUE")
                else: les_valeurs[index] = 1
        # 3. On vérifie les secteurs
        for i in range(9):
            les_valeurs = [0]*10
            for j in range(9):
                index = self.les_secteurs[i][j].get_value()
                if index == 0:
                    continue
                if les_valeurs[index] != 0:
                    verif_ok = False
                    if self.debug:
                        print("debug: Verif Secteur ECHOUE")
                else: les_valeurs[index] = 1
        return verif_ok

    def undo(self, snapshot="COMMIT"):
        """
        Annule la dernière action (revient au dernier point de synchro)
        ...
        Paramètres:
        -----------
        snapshot: str
            Jusqu'où on revient en arrière, par défaut la dernière opération.
        """
        while True:
            if len(self.log) >= 1:
                enreg = self.log.pop()
                if enreg[0] == snapshot:
                    break
                if self.debug:
                    print(">>>UNDO: ", enreg)
                else:
                    une_case = self.get_case(enreg[1], enreg[2])
                    une_case.set_candidats(enreg[3])
            else:
                break

    def add_candidat(self, ligne, colonne, value):
        """
        Ajoute un candidat (à priori, provient d'une action "UNDO")
        ...
        Paramètres:
        -----------
        ligne, colonne, value: int
            ligne, colonne: coordonnées, value: La nouvelle valeur
        """
        une_case = self.get_case(ligne, colonne)
        if une_case.verrou:
            return    # on log ???
        oldvalue = set(une_case.get_candidats())
        une_case.add_candidat(value)
        self.log.append(["modif", ligne, colonne, oldvalue])

    def remove_candidat(self, ligne, colonne, value):
        """
        Supprime un candidat (à priori, c'est la base des déductions
        ...
        Paramètres:
        -----------
        ligne, colonne, value: int
            ligne, colonne: coordonnées, value: La nouvelle valeur
        """
        une_case = self.get_case(ligne, colonne)
        if une_case.verrou:
            return    # on log ???
        oldvalue = set(une_case.get_candidats())
        une_case.remove_candidat(value)
        self.log.append(["modif", ligne, colonne, oldvalue])

    def get_candidats(self, ligne, colonne):
        """
        Renvoie la liste des candidats d'une Case
        ...
        Paramètres:
        -----------
        ligne, colonne: int
            Les coordonnées de la case
        Valeur de retour:
        -----------------
        Les candidats de la case
        """
        une_case = self.get_case(ligne, colonne)
        return une_case.get_candidats()

class Case:
    """
    Cette classe représente une Case d'une Grille de Sudoku
    ...
    ATTRIBUTS:
    ----------
    ligne, colonne, secteur: int
        Les coordonnées de la Case
    value: int
        Le contenu de la Case. La valeur 0 signifie une Case vide
    verrou: bool
        Si vrai, la Case ne peut pas être modifié
        Elle appartient au problème, ce ne peut être une hypothèse
    candidats: list de int
        Les candidats, ie les valeurs possible de la Case.
        Si il ne reste qu'un seul candidat, celui-ci affecte la value

    """
    def __init__(self, ligne, colonne, secteur, value):
        """
        constructeur
        ...
        Paramètres:
        -----------
        ligne, colonne, secteur, value: int
            Respectivement: ligne, colonne, secteur, value
        """
        self.ligne = ligne
        self.colonne = colonne
        self.secteur = secteur
        self.value = value
        self.candidats = {i for i in range(1, 10)}
        if value > 0:
            self.verrou = True # ce doit etre une methode a part!!!
            self.candidats = {value}
        else:
            self.verrou = False

    def get_value(self):
        """
        Renvoie la value d'une Case
        ...
        Valeur de retour: la value d'une Case (int)
        """
        return self.value

    def add_candidat(self, value):
        """
        Ajoute un candidat à une Case (souvent suite à un "UNDO")
        (éventuellement supprime la value [la remet à zéro] si
        maitenant on a plusieurs [2] candidats).
        ...
        Paramètres:
        -----------
        value: int
            La valeur du candidat que l'on ajoute
        """
        if value not in self.candidats:
            self.candidats.add(value)
            if len(self.candidats) == 2:
                self.value = 0

    def remove_candidat(self, value):
        """
        Retirer un candidat (l'opération de base d'une déduction)
        ...
        Paramètres:
        -----------
        value: int
            La valeur du candidat que l'on retire
        """
        if len(self.candidats) == 1:
            return
        if value in self.candidats:
            self.candidats.remove(value)
        if len(self.candidats) == 1:
            self.value = list(self.candidats)[0]

    def get_candidats(self):
        """
        Renvoie les candidats d'une Case
        ...
        Valeur de retour: les candidats (list d'int)
        """
        return self.candidats

    def get_coord(self):
        """
        Renvoie les coordonnées d'une Case
        ...
        Valeur de retour:
        -----------------
        ligne, colonne, secteur: int
            Les coordonnées de la Case
        """
        return self.ligne, self.colonne, self.secteur

    def set_candidats(self, new_candidats):
        """
        Fixe l'ensemble des candidats
        ...
        Paramètres:
        -----------
        new_candidats: set
            Les nouveaux candidats
        """
        self.candidats = new_candidats
        if len(self.candidats) == 1:
            self.value = list(self.candidats)[0]
        else:
            self.value = 0
