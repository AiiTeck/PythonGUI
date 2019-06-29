"""
Memo : Les chemins se definissent en fonction du premier fichier execute (ici main.py)
"""

import pygame
import os
import sys
from ressources.modules.policeGest import * # "." ==> "/", certain systeme utilise "/" ou "\" python s adapte en fonction grace au "."
from ressources.modules.ecranGest import *
from ressources.modules.ligneGest import *


pygame.init()
pygame.font.init()