# coding=UTF-8

from runnable import *

meelee_common = choice('Comum corpo a corpo',
                       [(4, msized('Adaga')),
                        (14, msized('Machado grande')),
                        (24, msized('Espada larga')),
                        (28, msized('Kama')),
                        (41, msized('Espada longa')),
                        (45, msized('Maça leva')),
                        (50, msized('Maça pesada')),
                        (54, msized('Nunchaku')),
                        (57, msized('Bordão')),
                        (61, msized('Sabre')),
                        (66, msized('Cimitarra')),
                        (70, msized('Lança curta')),
                        (74, msized('Sianghan')),
                        (84, msized('Espada bastarda')),
                        (89, msized('Espada curta')),
                        (100, 'Machado de combate anão')])

uncommon = choice('Incomum',
                  [(3, 'Machado orc duplo'),
                   (7, msized('Machado de combate')),
                   (10, msized('Corrente com cravos')),
                   (12, msized('Clava')),
                   (16, msized('Besta de mão')),
                   (19, msized('Besta de repetição')),
                   (21, msized('Adaga de soco')),
                   (23, msized('Falcione')),
                   (26, msized('Mangual atroz')),
                   (31, msized('Mangual pesado')),
                   (35, msized('Mangual leve')),
                   (37, msized('Manopla')),
                   (39, msized('Manopla com cravos')),
                   (41, msized('Glaive')),
                   (43, msized('Clava grande')),
                   (45, msized('Clava grande')),
                   (45, msized('Guisarme')),
                   (48, msized('Alabarda')),
                   (51, msized('Meia lança')),
                   (54, 'Martelo gnomo com gancho'),
                   (56, msized('Martelo leve')),
                   (58, msized('Machadinha')),
                   (61, msized('Kukri')),
                   (64, msized('Lança montada')),
                   (67, msized('Lança longa')),
                   (70, msized('Maça estrela')),
                   (72, msized('Rede')),
                   (74, msized('Picareta pesada')),
                   (76, msized('Picareta leve')),
                   (78, msized('Ranseur')),
                   (80, msized('Porrete')),
                   (82, msized('Foice longa')),
                   (84, msized('Shuriken')),
                   (86, msized('Foice curta')),
                   (89, msized('Espada de duas lâminas')),
                   (91, msized('Tridente')),
                   (94, 'Urgrosh anão'),
                   (97, msized('Martelo de guerra')),
                   (100, msized('Chicote'))])

# TODO: termonar
distance_common = 'Comum a distância.'

weapon = choice('',
                [(70, meelee_common),
                 (80, uncommon),
                 (100, distance_common)])

# TODO: fazer o tipo (menor, medio, maior) ser passado como um parâmetro
def _weapon():
    distrib = choice('',
                     [(70, name('Melhoria +1', weapon)),
                      (85, name('Melhoria +2', weapon)),
                      (90, specific_weapon_minor),
                      (100, None)])

    def generate():
        count = 0
        weapon = distrib.run()
        while not weapon[1]:
            count = count + 1
            weapon = distrib.run()

        if !count or weapon[1][1][0] == 'Arma':
            return weapon
        else:
            props = apply_hability_hierarchy(
                set(unify(mult('', count, weapon_hability_minor).run())),
                hability_hierarchy)

            return (weapon[1][0], (', '.join(props), weapon[1][1]))

    return callable('Arma', generate)

minor = _weapon()
