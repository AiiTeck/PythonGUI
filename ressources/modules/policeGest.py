"""
Fichier contenant les classes concernant la gestion des polices et des textes.
"""
from pickle import Pickler, Unpickler
import pygame
import os


class Police:
    def __init__(self, nom, chemin):
        """
            Class permetant de definir une police.
            (option future : permettre a l utilisateur d ajouter sa propre police)
            nom -> str: nom de la police
            chemin -> str : chemin d acces a la police
        
            /* Alternative : utilisation d un dictionnaire. */
        """
        self.nom = nom
        self.path = chemin
    
    def renderText(self, taille = 24, text = "", couleur = (0,0,0)):
        """
        methode permettant de generer le rendu pygame d un texte en fonction de plusieurs parametres.
        permet de modifier la couleur et la taille sans avoir a en predefinir a l avance!

        taille -> int: taille de la police avec laquelle rendre le texte
        text -> str: texte a rendre via cette methode
        couleur -> (int, int, int): couleur du texte a rendre

        return -> pygame.render() => pygame.Surface
        """
        self.pygamePol = pygame.font.SysFont(self.path, taille)
        textRend = self.pygamePol.render(text, True, couleur)
        return textRend

class Texte:
    def __init__(self, ecran, text, police, taille, pos = (0,0), couleur = (0,0,0)):
        """
            Classe permettant de definir un texte et de l afficher.
            ecran -> Ecran: ecran sur lequel se colle le texte
            text -> str: texte
            police -> Police: police avec laquelle rendre le texte
            taille -> int: taille de la police avec laquelle rendre le texte
            pos -> (int, int): position du point en haut a gauche du texte
            couleur -> (int, int, int): couleur du texte
        """
        self.text = text
        self.pos = pos
        self.police = police
        self.taille = taille
        self.couleur = couleur
        self.ecran = ecran
        self.textRend = self.police.renderText(self.taille, self.text, self.couleur)
    
    def afficher(self):
        """
            methode permettant d afficher un texte.
        """
        self.textRend = self.police.renderText(self.taille, self.text, self.couleur)
        self.ecran.surface.blit(self.textRend,self.pos)