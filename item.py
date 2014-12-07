# coding=UTF-8

from runnable import *
import armor

#TODO: Especificar...
weapon_minor = "Arma mágica menor."
potion_minor = "Poção menor."
ring_minor = "Anel menor."
scroll_minor = "Pergaminho menor."
wand_minor = "Varinha menor."
wonder_minor = "Item maravilhoso menor."

# TODO: incluir item amaldiçoado, inteligente, etc
minor = choice('Menor',
               [(4, armor.minor),
                (9, weapon_minor),
                (44, potion_minor),
                (46, ring_minor),
                (81, scroll_minor),
                (91, wand_minor),
                (100, wonder_minor)])

# TODO: arrumar essas tabelas
medium = 'Item mágico médio.'
major = 'Item mágico maior.'
