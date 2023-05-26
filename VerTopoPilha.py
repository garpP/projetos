"""
criar uma função que permita ver qual o item no topo da pilha, você pode acessar o último item na lista items da classe Pilha. Isso pode ser feito com o índice -1, que se refere ao último item na lista.
"""

class Pilha:
    def __init__(self):
        self.items = []

    def vazia(self):
        return not self.items
    
    def push(self, item):
        self.items.append(item)
        print(f'item adicionado: {item}')

    def pop(self):
        if self.vazia():
            raise ValueError('a pilha esta vazia')
        item = self.items.pop()
        print(f'item removido: {item}')
        return item
    
    def tamanho(self):
        print('a pilha tem', len(self.items), 'items')

#    def mostra_pilha(self):
#        for item in self.items[::-1]:
#            print(item)
    def mostra_pilha(self):
        print('estado atual da pilha')
        for item in reversed(self.items):
            print(f'[{item}]')

    def topo(self):
        if self.vazia():
            print('a pilha esta vazia')
            return None
        return self.items[-1]
    
pilha01 = Pilha()
pilha01.push(1)
pilha01.push(2)
pilha01.push(3)
pilha01.push(4)
pilha01.mostra_pilha()
pilha01.tamanho()
pilha01.pop()
pilha01.pop()
pilha01.mostra_pilha()
pilha01.tamanho()
