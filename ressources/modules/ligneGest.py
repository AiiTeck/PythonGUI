import pygame
from ressources.modules.policeGest import * # chemin  d acces depuis le fichier main !!

class Ligne:
    def __init__(self, ecran, text, police, taille, pos = (0,0), couleurText = (0,0,0), couleurFond = (255,255,255)):
        """
            Defini un carre contenant un texte afficher en son centre.
            ecran -> Ecran: ecran sur lequel se colle la ligne
            text -> str: texte de la ligne
            police -> Police: police avec laquelle sera rendue le texte
            taille -> int: taille de la police avec laquelle sera rendue le texte
            pos -> (int, int): position du point en haut a gauche de la ligne
            couleurText -> (int, int, int): couleur du texte
            couleurFond -> (int, int, int): couleur du fond de la ligne
        """
        self.ecran = ecran
        self.txt = text # val String du texte
        self.police = police
        self.taille = taille
        self.pos = pos
        self.couleurText = couleurText
        self.couleurFond = couleurFond
        self.text = Texte(self.ecran, self.txt, self.police, self.taille, self.pos, self.couleurText) # objet Texte
        self.textRect = self.text.textRend.get_rect()
        self.dim = (self.textRect.w + 5, self.textRect.h + 5) # dims -> dimensions du texte + marge de 5px

    def __contains__(self,pos):
        """(int, int) in BoiteTexte -> bool
        Appartenance d un point au rectangle ferme BoiteTexte"""
        # Permet de donner une contenance a l objet
        # Il devient comme une liste de point
        # Ainsi on peut le parcourir comme on le ferai avec une liste
        xmin=self.pos[0]
        xmax=self.pos[0]+self.dim[0]
        ymin=self.pos[1]
        ymax=self.pos[1]+self.dim[1]
        xpt=pos[0]
        ypt=pos[1]
        return (xpt>=xmin and xpt<=xmax and ypt>=ymin and ypt<=ymax)
    
    def afficher(self):
        """
        Affiche la ligne sur son ecran
        """
        self.text = Texte(self.ecran, self.txt, self.police, self.taille, self.pos, self.couleurText) # Actualise
        self.textRect = self.text.textRend.get_rect() # Actualise
        self.dim = (self.textRect.w + 5, self.textRect.h + 5) # Actualise
        self.bordRect = (self.pos[0]-5, self.pos[1]-5, self.dim[0]+5, self.dim[1]+5) # -5 pour le faire partir de plus loin /// +5 pour le faire aller plus loin
        Fond=pygame.draw.rect(self.ecran.surface, self.couleurFond, self.bordRect, 0) # fond
        Bords=pygame.draw.rect(self.ecran.surface, (0,0,0), self.bordRect, 1) # bord
        self.text.afficher() # Affiche le texte
        
    def depassementTest(self):
        """
        Permet de savoir si le texte depasse de l ecran.
        return -> bool : renvoie True si le texte depasse de l ecran
        """
        self.text = Texte(self.ecran, self.txt, self.police, self.taille, self.pos, self.couleurText) # Actualise
        self.textRect = self.text.textRend.get_rect() # Actualise
        self.dim = (self.textRect.w + 5, self.textRect.h + 5) # Actualise
        if self.pos[0]+self.dim[0] >= self.ecran.dim[0] or self.pos[0]+self.dim[0] >= self.ecran.dim[0]: # ou si chevauchement en parcourant la liste des widgets ...
            return True # Renvoie True -> il y a un depassement
            

class Bouton(Ligne):
    def __init__(self, ecran, text, police, taille, pos = (0,0), couleurText = (0,0,0), couleurFond = (255,255,255)):
        """
            Classe symbolique pour permettre au code d etre plus lisible.

            Defini un carre contenant un texte afficher en son centre.
            ecran -> Ecran: ecran sur lequel se colle la ligne
            text -> str: texte de la ligne
            police -> Police: police avec laquelle sera rendue le texte
            taille -> int: taille de la police avec laquelle sera rendue le texte
            pos -> (int, int): position du point en haut a gauche de la ligne
            couleurText -> (int, int, int): couleur du texte
            couleurFond -> (int, int, int): couleur du fond de la ligne
        """
        super().__init__(ecran, text, police, taille, pos, couleurText, couleurFond)


class BoiteSaisi:
    def __init__(self, ecran, text, police, taille, pos, couleurText = (0,0,0), couleurFond = (255,255,255)):
        """
        Cette classe permet de definir une boite permettant de saisir du texte. Cette boite est composee de plusieurs Ligne.

        ecran -> Ecran: ecran sur lequelle la boite est defini
        text -> str: label de la point de texte
        police -> Police : police avec laquelle rendre le texte
        taille -> int : taille de la police avec laquelle rendre le texte
        pos -> (int, int): tuple permettant de definir le point en haut a gauche de la boite
        couleurText -> (int, int, int): couleur du texte
        couleurFont -> (int, int, int): couleur du fond de la boite
        """
        self.ecran = ecran
        self.police = police
        self.taille = taille
        self.pos = pos
        self.couleurText = couleurText
        self.couleurFond = couleurFond
        self.msg = text
        self.txt = self.msg
        self.lignes = [
            Ligne(self.ecran, self.txt ,self.police, self.taille, self.pos, self.couleurText, self.couleurFond)
        ]
        self.dim = self.lignes[0].dim
        self.actif = False
        self.hLigne = self.dim[1]

    def __contains__(self,pos):
        """(int, int) in BoiteTexte -> bool
        Appartenance d un point au rectangle ferme BoiteTexte"""
        # Permet de donner une contenance a l objet
        # Il devient comme une liste de point
        # Ainsi on peut le parcourir comme on le ferai avec une liste
        xmin=self.pos[0]
        xmax=self.pos[0]+self.dim[0]
        ymin=self.pos[1]
        ymax=self.pos[1]+self.dim[1]
        xpt=pos[0]
        ypt=pos[1]
        return (xpt>=xmin and xpt<=xmax and ypt>=ymin and ypt<=ymax)    
    
    def activer(self):
        """
        Fonction permettant de declarer la boite comme active
        """
        if self.txt == self.msg: self.txt=" " #Efface juste le message de saisie...
        self.actif=True
        self.afficher()

    def desactiver(self):
        """
        Fonction permettant de declarer la boite comme desactive
        """
        self.actif=False
        if self.txt == "":self.txt=self.msg #Permet de remettre l instruction si la zone de saisir est vide...
        self.afficher()

    def correction(self, text, compteur):
        """
        Permet de generer les lignes de la boite pour permettre le retour a la ligne.
        text -> str: texte a couper
        compteur -> int: permet de connaitre le numero de la ligne et le definit sa position correctement
        
        return borneSup -> rang ou le text a ete coupe
        """
        borneInf = 0
        borneSup = len(text)
        pos = (self.pos[0], self.pos[1] + compteur*self.hLigne)

        ligne = Ligne(self.ecran, text, self.police, self.taille, pos) # pos -> seulement pour le test ==> Ne pas peut etre (0,0) il test le depassement de l ecran ...
        while ligne.depassementTest():
            borneSup -= 1
            ligne = Ligne(self.ecran, text[borneInf:borneSup], self.police, self.taille, pos)
        self.lignes.append(Ligne(self.ecran, text[borneInf:borneSup], self.police, self.taille, pos, self.couleurText, self.couleurFond))
        return borneSup

    def afficher(self):
        """
        Affiche la boite de saisi.
        Efface la boite precedente et affiche la nouvelle dessus.
        """
        bordRect = (self.pos[0]-5, self.pos[1]-5, self.dim[0]+5, self.dim[1]+5)
        Fond = pygame.draw.rect(self.ecran.surface, self.ecran.couleur, bordRect, 0) # Efface le precedant text

        rang = 0
        verif = ""
        compteur = 0
        self.lignes = []
        if self.txt == "": self.txt = " "
        
        while verif != self.txt:
            verif =""
            rang += self.correction(self.txt[rang:], compteur)
            compteur += 1
            for k in self.lignes:
                verif += k.txt

        for compteur in range(len(self.lignes)):
            self.lignes[compteur].afficher()

        self.dim = (self.dim[0], self.hLigne*(compteur+1)) # +1 -> Boucle for
        
        pygame.display.flip()

    def saisir(self):
        """
        Permet d activer la saisi. 
        Modifie l attribut txt qui modifiera les lignes lorsqu elles seront recreees
        Actualise l affichage et return-> bool: return True apres une desactivation
        desaction => impossible de saisir : - appui sur Echap
                                            - appui sur entree
                                            - appui en dehors de la zone de saisis
        """
        Caracteres=[chr(k) for k in range(32,254+1)] # Genere la liste des caracteres pouvant etre saisie, 34-> Espace, 254-> Dernier caractere (ASCII Extend)
        self.activer()
        while True:
            for entree in pygame.event.get():
                #Actions Souris
                if entree.type==pygame.MOUSEBUTTONDOWN: 
                    if pygame.mouse.get_pressed()[0]==1: 
                        
                        if not pygame.mouse.get_pos() in self: # Clic en dehors -> Desactivation
                            self.desactiver()
                            return True

                #Actions appuis Clavier
                if entree.type==pygame.KEYDOWN:
                    
                    if entree.unicode in Caracteres: # Permet de saisir les caracteres
                        self.txt+=entree.unicode
                        self.afficher()
                    
                    if entree.key==pygame.K_RETURN: # Appuie sur ENTREE -> Desactivation
                        self.desactiver()
                        return True
                    
                    if entree.key==pygame.K_ESCAPE:
                        self.desactiver()
                        return True
                    
                    if entree.key==pygame.K_BACKSPACE: # Permet d effacer lors de l appuie sur "retour"
                        self.txt=self.txt[:len(self.txt)-1]
                        self.afficher() # Actualise