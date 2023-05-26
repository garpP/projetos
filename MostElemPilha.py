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

#    def mostra_pilha(self):
#        for item in self.items[::-1]:
#            print(item)
    def mostra_pilha(self):
        print('estado atual da pilha')
        for item in reversed(self.items):
            print(f'[{item}]')
    
pilha = Pilha()
pilha.push(1)
pilha.push(2)
pilha.push(3)
pilha.mostra_pilha()

"""
O método mostra_pilha é responsável por imprimir a pilha atual, ou seja, os itens armazenados nela.

A linha print('estado atual da pilha') imprime a mensagem "estado atual da pilha" no console, para que o usuário saiba qual é a informação que está sendo apresentada.

Em seguida, a linha for item in reversed(self.items): começa um loop que percorre todos os itens armazenados na pilha, na ordem inversa em que foram adicionados. A palavra-chave reversed é usada para inverter a ordem da lista items, de forma que o primeiro item adicionado seja o último a ser impresso.

Dentro do loop, a linha print(f'[{item}]') imprime cada item na pilha, com colchetes em volta para separá-los visualmente e facilitar a leitura. O f-string {item} é usado para inserir o valor de cada item no texto, dentro dos colchetes.

Por fim, quando o loop termina, a função também termina e não retorna nenhum valor. Em vez disso, a saída é impressa diretamente no console.

Assim, quando o método mostra_pilha é chamado, ele exibe a pilha atual, com cada item dentro de colchetes e em ordem inversa de adição.
"""