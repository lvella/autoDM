# coding=UTF-8

from runnable import *

armor = msized(choice('Armadura',
                      [(1, 'Acolchoada'),
                       (2, 'Corselete de couro'),
                       (17, 'Corselete de couro batido'),
                       (32, 'Camisão de cota de malha'),
                       (42, 'Gibão de peles'),
                       (43, 'Brunea'),
                       (44, 'Cota de malha'),
                       (57, 'Peitoral de aço'),
                       (58, 'Cota de talas'),
                       (59, 'Loriga segmentada'),
                       (60, 'Meia armadura'),
                       (100, 'Armadura de batalha')]))

shield = msized(choice('Escudo',
                       [(10, 'Broquel'),
                        (15, 'Escudo pequeno de madeira'),
                        (20, 'Escudo pequeno de metal'),
                        (30, 'Escudo grande de madeira'),
                        (95, 'Escudo grande de metal'),
                        (100, 'Escudo de corpo')]))

hability_hierarchy = (('Escorregadia maior',
                       'Escorregadia aprimorada',
                       'Escorregadia'),
                      ('Resistência a ácido maior',
                       'Resistência a ácido aprimorada',
                       'Resistência a ácido'),
                      ('Resistência à eletricidade maior',
                       'Resistência à eletricidade aprimorada',
                       'Resistência à eletricidade'),
                      ('Resistência ao fogo maior',
                       'Resistência ao fogo aprimorada',
                       'Resistência ao fogo'),
                      ('Resistência ao frio maior',
                       'Resistência ao frio aprimorada',
                       'Resistência ao frio'),
                      ('Resistência à magia (19)',
                       'Resistência à magia (17)',
                       'Resistência à magia (15)',
                       'Resistência à magia (13)'),
                      ('Resistência sônica maior',
                       'Resistência sônica apromorada',
                       'Resistência sônica'),
                      ('Silenciosa maior',
                       'Silenciosa aprimorada',
                       'Silenciosa'),
                      ('Sombria maior',
                       'Sombria aprimorada',
                       'Sombria'))

def _armor_hability_minor():
    def one_more():
        return [_armor_hability_minor().run(), _armor_hability_minor().run()]

    return choice('Habilidade especial de armadura',
                  [(25, 'Camuflagem'),
                   (32, 'Fortificação leve'),
                   (52, 'Escorregadia'),
                   (72, 'Sombria'),
                   (92, 'Silenciosa'),
                   (96, 'Resistência à magia (13)'),
                   (97, 'Escorregadia aprimorada'),
                   (98, 'Sombria aprimorada'),
                   (99, 'Silenciosa aprimorada'),
                   (100, callable('', one_more))])

armor_hability_minor = _armor_hability_minor()

def _shield_hability_minor():
    def one_more():
        return [_shield_hability_minor().run(), _shield_hability_minor().run()]

    return choice('Habilidade especial de escudo',
                  [(20, 'Apanhador de flechas'),
                   (40, 'Esmagamento'),
                   (50, 'Cegante'),
                   (75, 'Fortificação leve'),
                   (92, 'Deflexão de flechas'),
                   (97, 'Animado'),
                   (99, 'Resistência à magia (13)'),
                   (100, callable('', one_more))])

shield_hability_minor = _shield_hability_minor()

specific_armor_minor = sized(choice('Armadura específica',
                                    [(50, 'Camisão de mitral'),
                                     (80, 'Armadura de couro de dragão'),
                                     (100, 'Cota de malha élfica')]))

specific_shield_minor = sized(choice('Escudo específico',
                                     [(30, 'Broquel de madeira negra'),
                                      (80, 'Escudo de madeira negra'),
                                      (95, 'Escudo grande de mitral'),
                                      (100, choice('Escudo do conjurador',
                                                   [(50, 'Sem magia'),
                                                    #TODO: Especificar
                                                    (90, '1 Magia arcana'),
                                                    (100, '1 Magia divina')]))]))

# TODO: fazer o tipo (menor, medio, maior) ser passado como um parâmetro
def _armor():
    distrib = choice('',
                     [(60, name('Melhoria +1', shield)),
                      (80, name('Melhoria +1', armor)),
                      (85, name('Melhoria +2', shield)),
                      (87, name('Melhoria +2', armor)),
                      (89, specific_armor_minor),
                      (91, specific_shield_minor),
                      (100, None)])

    def generate():
        count = 0
        armor = distrib.run()
        while not armor[1]:
            count = count + 1
            armor = distrib.run()

        if count:
            hab = None
            if armor[1][0] == 'Escudo':
                hab = shield_hability_minor
            elif armor[1][0] == 'Armadura':
                hab = armor_hability_minor
            else:
                return armor

            props = apply_hability_hierarchy(
                set(unify(mult('', count, hab).run())),
                hability_hierarchy)

            return (armor[1][0], (', '.join(props), armor[1][1]))
        else:
            return armor

    return callable('Armadura ou escudo', generate)

minor = _armor()

