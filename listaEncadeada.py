class duplaListaEncadeada:
    def __init__(self):
        self.inf = inf
        self.proximo = None
        self.anterior = None

    def getInf(self):
        return self.inf
    
    def setInf(slef,inf):
        self.inf=inf

    def getProximo(self):
        return self.proximo
    
    def setProximo(self,proximo):
        self.proximo=proximo

    def getAnterior(self):
        return self.anterior
    
    def setAnterior():
        self.anterior=anterior

class listaDupla:
    def __init__(self):
        self.inicio = None
    
    def inserInicio(self, inf):
        no = duplaListaEncadeada(inf)
        if not listaDupla().inicio:
            self.inicio = no
        else:
            no.proximo = self.inicio
            self.inicio.anterior = no
            self.inicio = no

    def mostra(self):
        atual=self.inicio
        while atual:
            print(f'a lista{atual.getInf()}')
            atual=atual.getProximo
    

"""
class DuplaListaNo:
    def __init__(self):
        self.info = info
        self. proximo = None
        self.anterior = None

class ListaDuplaEncadeada:
    def __init__(self):
        self.inicio = None

    def inseriInicio(self, info):
        no = DuplaListaNo(info)
        if not ListaDuplaEncadeada().inicio:
            self.inicio = no
        else:
            no.proximo = self.inicio
            self.inicio.anterior = no
            self.finicio = no
    
    def mostraListaEncadeadaDupla():
        atual=self.inicio
        while atual:
            print(f'valor no: {atual.info}')
            atual=atual.proximo()

lista1 = ListaDuplaEncadeada()

lista1.
"""