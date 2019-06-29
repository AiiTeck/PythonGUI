"""
Fichier contenant les classes et fonctions permettant de gerer un ecran
"""
import pygame
import os

class Ecran:
    def __init__(self, dim = (1280,720), couleurFond = (0,0,0)):
        """
        Cette class permet de definir un ecran a afficher qui occupera les dimensions de la fenetre.
        dim -> (int, int): dimensions
        couleurFond -> (int, int, int): couleur du fond d ecran
        """
        self.dim = dim
        self.surface = pygame.display.set_mode(self.dim)
        self.widgets = [] # on doit initialiser l ecran avant les widgets mais certains widgets on besoin d un ecran def pour etre defini ex : Texte.
        self.couleur = couleurFond
    
    def afficher(self):
        """
        Efface l ecran et affiche la totalite des widgets sur l ecran.
        """
        self.surface.fill(self.couleur)
        for objet in self.widgets:
            objet.afficher() # => tout les objets a afficher auront une methode "afficher()"
        pygame.display.flip()
    
    def effacer(self):
        """
        Efface l ecran en le remplissant avec sa couleur de fond.
        """
        self.surface.fill(self.couleur)
        pygame.display.flip()

    def add(self, widgets):
        """
            Ajouter un widget a l ecran
            widgets -> list de widget ou un widget
        """
        if type(widgets) == type([]):
            for widget in widgets:
                self.widgets.append(widget)
                widget.afficher()
        else:
            self.widgets.append(widgets)
            widgets.afficher()

    def remove(self, widget):
        """
        Permet de supprimer un widget.
        """
        self.widgets.remove(widget)
        self.afficher()
    
    def scroll(self, x, y):
        """
        Permet de scroller dans l ecran pour permettre a l utilisateur de s y deplacer.
        x -> int: deplacement horizontale
        y -> int: deplacement verticale
        """
        for widget in self.widgets:
            widget.pos = (widget.pos[0]+x, widget.pos[1]+y)
        self.surface.scroll(x,y)
        self.afficher()