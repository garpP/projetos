class Pilha: #criando a classe pilha
    def __init__(self): #fazendo seu inicio padrão
        self.items = [] #self é como se fosse esse == esse items vai receber uma lista

    def vazia(self): #criando metodo para verificar se a pilha esta vazia
        return len(self.items) == 0 #explic vai retornar false se a pillha não estiver vazia
    def vaziona(self):
        return not self.items#jeito mais eficiente
    
#    def push(self, item):# criando metodo para inserir items na pilha
#        self.items.append(item)#append serve para adicionar a pilha
    def push(self, item):
        self.items.append(item)
        print(f'item adicionado: {item}')        

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

    def quantidade_i_pilha(self):#criando metodo para ver a quantidade de items de uma pilha
        return len(self.items) #pedimos que ele nos retorne o len de items na pilha
    def quantidade(self):#o mesmo de cima so que com print  #self.quantidade_i_pilha
        print('a quantidade de items na pilha é', len(self.items), 'items')

    def mostra_pilha(self):#função para mostrar os items da pilha em fromato de pilha
        for item in self.items[::-1]:#a função utiliza o loop for para iterar sobre a lista items da classe pilha em ordem inversa ou seja do ultimo item ao primeiro isso so é possivel graças ao [::-1] slice que inverte a ordem dos elementos na lista e imprime cada elemento na tela usando a função print
            print(item)
    
pilha = Pilha()
pilha.push(1)
pilha.push(2)
pilha.push(3)
pilha.mostra_pilha()
pilha.quantidade()
print(pilha.vazia())

pilha2 = Pilha()
pilha2.push(1)
pilha2.push(2)
pilha2.mostra_pilha()
pilha2.quantidade() #não esqueça dde abrir parentes 
print(pilha2.vaziona())#função mais eficiente