class Pilha:
    def __init__(self):
        self.items = []
    
    def vazia(self):
        return len(self.items) == 0
    def vaziona(self):
        return not self.items#jeito mais eficiente

    def push(self, item):
        self.items.append(item)
        print(f'item adicionado: {item}')        
#    def push(self, item):
#        self.items.append(item)
#erro bobo encontre erro bobo encontre
#   def push(self, items):
#       self.items.append(item)

#   def pop(self):
#       if self.vazia():
#           raise ValueError('pilha esta vazia')
#       return self.items.pop()
    def pop(self):#pop mostrando item que retirou
        if self.vazia():
            raise ValueError('a pilha esta vazia')
        item = self.items.pop()
        print(f'item removido: {item}')
        return item
    
    def tamanho(self):                           #EXPLO001
        return len(self.items)
    #ou posso fazer assim
    def mostra_tamanho(self):
        print('a pilha tem', len(self.items), 'items')
        #basicamente o mesmo jeito so que com um print
    
pilha1 = Pilha()                         #EXPLO002
pilha1.push(1)
pilha1.push(2)
pilha1.push(3)
print(pilha1.tamanho())
pilha1.mostra_tamanho()