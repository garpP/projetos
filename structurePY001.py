#criando estrutura pilha padrão utilizando lista
########################################################
class Pilha:                                           #
    def __init__(self):                                #
        self.items = []                                #
                                                       #
    def vazia(self):                                   #
        return len(self.items) == 0                    #
    def vaziona(self):                                 #
        return not self.items#jeito mais eficiente     #
                                                       #
    def push(self, item):                              #
        self.items.append(item)                        #
        print(f'item adicionado: {item}')              #
#    def push(self, item):                             #
#        self.items.append(item)                       #
                                                       #
#   def pop(self):                                     #
#       if self.vazia():                               #
#           raise ValueError('pilha esta vazia')       #
#       return self.items.pop()                        #
    def pop(self):#pop mostrando item que retirou      #
        if self.vazia():                               #
            raise ValueError('a pilha esta vazia')     #
        item = self.items.pop()                        #
        print(f'item removido: {item}')                #
        return item                                    #
########################################################
#__init__ é o construtor da classe, que cria uma lista vazia para armazenar os elementos da pilha. vazia retorna True se a pilha estiver vazia e False caso contrário. push adiciona um elemento ao topo da pilha usando o método append da lista. pop remove o elemento do topo da pilha usando o método pop da lista e retorna esse elemento. Se a pilha estiver vazia, pop levanta uma exceção ValueError.

#UTILIZANDO A CLASSE PILHA
#adicionando items com push                   EXPLO001
pilha = Pilha() #aqui a pilha esta recebendo a classe pilha senddo assim a pilha podera utilizar todos os metodos\funções da classe
pilha.push(1)
pilha.push(2)
pilha.push(3)

#verificando se a pilha esta vazia                                        EXPLO002
print(pilha.vazia())  # False ois acabamos de adicionar 3 items a pilha

#removendo elementos da pilha                            EXPLO003
print(pilha.pop()) #3
print(pilha.pop()) #2
print(pilha.pop()) #1

print(pilha.vazia())######################################################EXPLO002