"""


        
        
        
        
        O 1.PY É O PROGRAMA QUE VOU COLOCAR TODAS AS FUNÇÕES Q EU CONSEGUIR

        




        
"""










class Pilha:
    def __init__(self): 
        self.items = [] 

    def vazia(self): 
        return len(self.items) == 0 
    def vaziona(self):
        return not self.items
    
    def push(self, item):#push mostrando o adicionado
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

    def quantidade_i_pilha(self):
        return len(self.items) 
    def quantidade(self):
        print('a quantidade de items na pilha é', len(self.items), 'items')

#    def mostra_pilha(self):
#        for item in self.items[::-1]:
#            print(item)
    def mostra_pilha(self):#formatado
        print('estado atual da pilha')
        for item in reversed(self.items):
            print(f'[{item}]')

    def mostrar_menor_maior(self):
        if self.vazia():
            print('A pilha está vazia')
            return
        menor = float('inf')
        maior = float('-inf')
        for item in self.items:
            if item < menor:
                menor = item
            if item > maior:
                maior = item
        print(f'O menor valor da pilha é: {menor}')
        print(f'O maior valor da pilha é: {maior}')

    def mostra_par_impar(self):
        if self.vazia():
            print('a pillha esta vazia')
            return
        for item in self.items:
            if item % 2 == 0:
                print(f'[{item}] é par')
            else:
                print(f'[{item}] é impar')
    

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
pilha2.quantidade()
print(pilha2.vaziona())
pilha2.mostrar_menor_maior()
pilha2.mostra_par_impar()

"""
\-\-\-\-\-\-\-\-\-\-\\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\
                                  EXPLICANDO
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\-\-\-\-\-\-\-\-\--\-\-\-\-


*
================================================================================
__init__
================================================================================
O método __init__ é um método especial em Python que é executado automaticamente quando um novo objeto é criado a partir da classe. Ele é usado para inicializar o objeto com seus atributos e valores iniciais.

No caso da classe Pilha, o método __init__ cria um novo objeto Pilha com uma lista vazia. A lista é armazenada como um atributo do objeto, chamado items. Isso significa que cada nova instância da classe Pilha terá sua própria lista de itens, que pode ser preenchida e manipulada independentemente de outras instâncias da classe.

A linha self.items = [] cria uma nova lista vazia e a atribui ao atributo items do objeto atual, que é representado pela palavra-chave self. Isso significa que cada nova instância da classe Pilha começará com uma lista vazia, pronta para ser preenchida com itens.

Assim, o método __init__ é usado para inicializar o estado inicial de cada novo objeto Pilha, criando uma lista vazia para armazenar seus itens.



*
================================================================================
vazia/vaziona
================================================================================
O método vazia é uma função da classe Pilha que verifica se a pilha está vazia ou não.

A implementação do método é simples: ele verifica se a lista de itens da pilha (self.items) está vazia ou não. Se a lista estiver vazia, ele retorna True. Caso contrário, ele retorna False.

A expressão not self.items é uma maneira concisa de verificar se a lista self.items está vazia ou não. O operador not inverte o valor booleano de self.items. Se self.items for uma lista vazia, not self.items será True. Se self.items não estiver vazio, not self.items será False.

Assim, o método vazia é útil para verificar o estado da pilha antes de tentar realizar uma operação de remoção (pop) ou para determinar se a pilha está vazia antes de iniciar um loop ou outra operação que dependa do conteúdo da pilha.



*
================================================================================
push
================================================================================
O método push é uma função da classe Pilha que adiciona um item à pilha. Recebe um argumento item que representa o elemento a ser adicionado.

A implementação do método é simples: ele adiciona o item à lista de itens da pilha (self.items) usando o método append. Além disso, ele imprime uma mensagem informando qual item foi adicionado à pilha, utilizando a função print e a formatação de string (f-strings) do Python.

Essa mensagem é útil para fins de depuração e para ajudar o usuário a entender o que está acontecendo com a pilha em um determinado momento.

Assim, o método push é usado para adicionar itens à pilha e pode ser útil para operações que envolvem empilhar elementos em uma pilha, como avaliação de expressões ou processamento de dados em profundidade.



*
================================================================================
pop
================================================================================
O método pop é uma função da classe Pilha que remove o item mais recente (o topo) da pilha e retorna o item removido.

O método começa verificando se a pilha está vazia, o que é feito chamando o método vazia. Se a pilha estiver vazia, o método lança uma exceção ValueError com uma mensagem de erro apropriada.

Se a pilha não estiver vazia, o método continua e usa o método pop da lista de itens da pilha (self.items) para remover o item mais recente (o topo) da pilha e armazená-lo na variável item.

Além disso, ele imprime uma mensagem informando qual item foi removido da pilha, utilizando a função print e a formatação de string (f-strings) do Python.

Essa mensagem é útil para fins de depuração e para ajudar o usuário a entender o que está acontecendo com a pilha em um determinado momento.

Por fim, o método retorna o item removido.

Assim, o método pop é usado para remover o item mais recente da pilha e pode ser útil para operações que envolvem desempilhar elementos em uma pilha, como avaliação de expressões ou processamento de dados em profundidade.



*
================================================================================
quantidade
================================================================================
O método quantidade é responsável por imprimir na saída a quantidade de elementos armazenados na pilha.

Para isso, ele utiliza a função len do Python, que retorna o número de elementos de uma lista, para obter a quantidade de itens da pilha e, em seguida, imprime uma mensagem na saída contendo essa quantidade de elementos.

Por exemplo, se a pilha tiver 3 elementos, o método quantidade irá imprimir a seguinte mensagem: a quantidade de items na pilha é 3 items.



*
================================================================================
mostra_pilha
================================================================================
O método mostra_pilha é responsável por imprimir na saída os elementos da pilha em ordem, começando pelo elemento mais recente (último elemento adicionado) até o mais antigo (primeiro elemento adicionado).

Para isso, ele utiliza o método reversed do Python para percorrer a lista de elementos da pilha de trás para frente, ou seja, começando pelo último elemento adicionado e terminando no primeiro.

A cada iteração do laço for, ele imprime o elemento atual entre colchetes, para indicar que se trata de um elemento da pilha.

Por exemplo, se a pilha tiver os elementos 3, 5 e 7 (nessa ordem), o método mostra_pilha irá imprimir a seguinte mensagem:

estado atual da pilha
[7]
[5]
[3]

Note que a pilha é exibida de forma invertida em relação à ordem em que os elementos foram adicionados, pois o método reversed percorre a lista de trás para frente.



*
================================================================================
maior_valor\menor_valor  \\ mostrar_menor_maior
================================================================================


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

O método maior_valor(self) percorre a pilha (self.items) e compara cada item com uma variável maior, inicializada como o primeiro item da pilha. Se o item atual for maior do que a variável maior, ela é atualizada com o novo valor. No final, o método retorna o valor da variável maior. Se a pilha estiver vazia, o método retorna None.

O método menor_valor(self) também percorre a pilha (self.items), mas, ao invés de comparar com uma variável que inicia com o primeiro item da pilha, ele usa uma variável menor que é inicializada com o valor infinito (usando float('inf')). Isso garante que qualquer item da pilha será menor do que a variável menor. Então, se o item atual for menor do que a variável menor, ela é atualizada com o novo valor. No final, o método retorna o valor da variável menor. Se a pilha estiver vazia, o método retorna None.

MOSTRAR_MENOR_MAIOR
 parte por parte como o método mostrar_menor_maior funciona e como ele foi criado:

Verificação se a pilha está vazia:
if self.vazia():
Verifica se a pilha está vazia usando o método vazia(). Se a pilha estiver vazia, imprime a mensagem "A pilha está vazia" e retorna.
Isso garante que o método não tente encontrar o menor e o maior valor se a pilha estiver vazia.
Inicialização das variáveis menor e maior:

menor = float('inf')
Inicializa a variável menor com um valor infinito positivo. Isso garante que qualquer item da pilha será menor do que menor no início.
maior = float('-inf')
Inicializa a variável maior com um valor infinito negativo. Isso garante que qualquer item da pilha será maior do que maior no início.
Percorrendo a pilha:

for item in self.items:
Percorre cada item na lista items da pilha.
Verificação do menor valor:

if item < menor:
Compara o item atual com a variável menor.
Se o item atual for menor do que menor, atualiza o valor de menor com o valor do item.
Verificação do maior valor:

if item > maior:
Compara o item atual com a variável maior.
Se o item atual for maior do que maior, atualiza o valor de maior com o valor do item.
Impressão do menor e do maior valor:

print(f'O menor valor da pilha é: {menor}')
Imprime o valor armazenado na variável menor indicando que é o menor valor encontrado na pilha.
print(f'O maior valor da pilha é: {maior}')
Imprime o valor armazenado na variável maior indicando que é o maior valor encontrado na pilha.
Espero que isso esclareça o funcionamento e a criação do método mostrar_menor_maior.



*
================================================================================
mostrar_par_impar
================================================================================
parte por parte como o método mostrar_par_impar funciona e como ele foi criado:

Verificação se a pilha está vazia:

if self.vazia():
Verifica se a pilha está vazia usando o método vazia(). Se a pilha estiver vazia, imprime a mensagem "A pilha está vazia" e retorna.
Isso garante que o método não tente verificar se os itens são pares ou ímpares se a pilha estiver vazia.
Percorrendo a pilha:

for item in self.items:
Percorre cada item na lista items da pilha.
Verificação se o item é par ou ímpar:

if item % 2 == 0:
Verifica se o item atual é divisível por 2, ou seja, se ele é par.
Se o item for par, imprime a mensagem indicando que o item é par.
else:
Caso contrário, ou seja, se o item não for divisível por 2, ele é ímpar.
Nesse caso, imprime a mensagem indicando que o item é ímpar.
Impressão do resultado:

print(f'O item {item} é par')
Imprime a mensagem indicando que o item é par.
print(f'O item {item} é ímpar')
Imprime a mensagem indicando que o item é ímpar.
Esse método percorre todos os itens da pilha e verifica se cada item é par ou ímpar, imprimindo a mensagem correspondente para cada item.



*
================================================================================

================================================================================
"""