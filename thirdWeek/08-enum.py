from enum import Enum


class Supermercados(Enum):
    EXTRA = 'Extra super market'
    ARIES = 'Aries super market'

print(Supermercados.EXTRA.value)