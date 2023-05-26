class Pilha:
    def __init__(self):
        self.items = []

    def vazia(self):
        return not self.items
    
    def push(self, item):
        self.items.append(item)
        print(f'[{item}] foi adicionado')

    def pop(self):
        if self.vazia():
            raise ValueError('a pilha esta vazia')
        item = self.items.pop()
        print(f'[{item}] removido')
        return item
    
    def quantidade(self):
        print('a quantidade atual de items na pilha é', len(self.items), 'items')
    
    def mostra_pilha(self):
        print('estado atual da pilha')
        for item in reversed(self.items):
            print(f'[{item}]')
        
    def menor_valor(self):
        if self.vazia():
            print('a pilha esta vazia')
            return None
        return min(list(self.items))#para o maior valor return max

    def maior_valor(self):
        if self.vazia():
            print('a pila esta vazia')
            return None
        maior = self.items[0]
        for item in self.items:
            if item > maior:
                maior = item
        print(f'o maior valor da pilha é: {maior}')
        return maior
    def menor_valor(self):
        if self.vazia():
            print('a pilha esta vazia')
            return None
        menor = float('inf')
        for item in self.items:
            if item < menor:
                menor = item
        print(f'o menor valor da pilha é: {menor}')
        return menor

pilha1 = Pilha()
pilha1.push(1)
pilha1.push(2)
pilha1.push(3)
pilha1.push(4)
pilha1.maior_valor()
pilha1.menor_valor()