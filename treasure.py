# coding=UTF-8

from runnable import *
import mundane
import item

# TODO: colocar os nomes certos das gemas.
gem = choice('Gema valendo ', [(25, GP('d(4,4)')),
                               (50, GP('d(2,4)*10')),
                               (70, GP('d(4,4)*10')),
                               (90, GP('d(2,4)*100')),
                               (99, GP('d(4,4)*100')),
                               (100, GP('d(2,4)*1000'))])

# TODO: colocar nomes certos de obras de arte.
art = choice('Obra de arte valendo ', [(10, GP('d(1,10)*10')),
                                       (25, GP('d(3,6)*10')),
                                       (40, GP('d(1,6)*100')),
                                       (50, GP('d(1,10)*100')),
                                       (60, GP('d(2,6)*100')),
                                       (70, GP('d(3,6)*100')),
                                       (80, GP('d(4,6)*100')),
                                       (85, GP('d(5,6)*100')),
                                       (90, GP('d(1,4)*1000')),
                                       (95, GP('d(1,6)*1000')),
                                       (99, GP('d(2,4)*1000')),
                                       (100, GP('d(2,6)*1000'))])

treasure = (array('Tesouro nível 1', 
                 [choice('Moedas',
                         [(14, 'Nada'),
                          (29, CP('d(1,6)*1000')),
                          (52, SP('d(1,8)*100')),
                          (95, GP('d(2,8)*10')),
                          (100, PP('d(1,4)'))]),
                  choice('Bens',
                         [(90, 'Nada'),
                          (95, mult("Gemas", 1, gem)),
                          (100, mult("Obras de arte", 1, art))]),
                  choice('Itens',
                         [(71, 'Nada'),
                          (95, mult("Itens mundanos", 1, mundane.mundane)),
                          (100, mult("Itens mágicos", 1, item.minor))])])
            # TODO: outros níveis.
            )


