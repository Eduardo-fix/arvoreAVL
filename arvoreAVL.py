class no(object):
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1
 
# Operação de inserção
class ArvoreAVL(object):
    def insercao(self, raiz, chave):
        
        if not raiz:
            print("Comparando valores...")
            return no(chave)
        elif chave < raiz.valor:
            print("Comparando valores...")
            raiz.esquerda = self.insercao(raiz.esquerda, chave)
        else:
            print("Comparando valores...")
            raiz.direita = self.insercao(raiz.direita, chave)

        raiz.altura = 1 + max(self.getAltura(raiz.esquerda),
                           self.getAltura(raiz.direita))
        balanco = self.getBalanco(raiz)
 
        # Caso 1 - Rotação esquerda
        if balanco > 1 and chave < raiz.esquerda.valor:
            print("Efetuando rotação a direita...\n")
            return self.rotacaoDireita(raiz)
 
        # Caso 2 - Rotação direita
        if balanco < -1 and chave > raiz.direita.valor:
            print("Efetuando rotação a esquerda...\n")
            return self.rotacaoEsquerda(raiz)
 
        # Caso 3 - Dupla rotação a esquerda
        if balanco > 1 and chave > raiz.esquerda.valor:
            print("Efetuando rotação dupla a direita...\n")
            raiz.esquerda = self.rotacaoEsquerda(raiz.esquerda)
            return self.rotacaoDireita(raiz)
 
        # Caso 4 - Dupla rotação a direita
        if balanco < -1 and chave < raiz.direita.valor:
            print("Efetuando rotação dupla a esquerda...\n")
            raiz.direita = self.rotacaoDireita(raiz.direita)
            return self.rotacaoEsquerda(raiz)
 
        return raiz
 
    def rotacaoEsquerda(self, z):
 
        y = z.direita
        T2 = y.esquerda

        #Efetua rotação
        y.esquerda = z
        z.direita = T2
        
        #Atualiza altura da árvore
        z.altura = 1 + max(self.getAltura(z.esquerda),
                         self.getAltura(z.direita))
        y.altura = 1 + max(self.getAltura(y.esquerda),
                         self.getAltura(y.direita))
 
        # Retorna novo valor a raiz
        return y
 
    def rotacaoDireita(self, z):
 
        y = z.esquerda
        T3 = y.direita
 
        #Efetua rotação
        y.direita = z
        z.esquerda = T3
 
        #Atualiza altura da árvore
        z.altura = 1 + max(self.getAltura(z.esquerda),
                        self.getAltura(z.direita))
        y.altura = 1 + max(self.getAltura(y.esquerda),
                        self.getAltura(y.direita))
 
        #Retorna novo valor a raiz
        return y
 
    def getAltura(self, raiz):
        if not raiz:
            return 0
 
        return raiz.altura
 
    def getBalanco(self, raiz):
        if not raiz:
            return 0
 
        return self.getAltura(raiz.esquerda) - self.getAltura(raiz.direita)
 
    def exec(self, raiz):
 
        if not raiz:
            return
 
        print("{0} ".format(raiz.valor), end="")
        self.exec(raiz.esquerda)
        self.exec(raiz.direita)
 
 
# Testando o programa
arvore = ArvoreAVL()
raiz = []
        
raiz = arvore.insercao(raiz, 10)
raiz = arvore.insercao(raiz, 20)
raiz = arvore.insercao(raiz, 30)
raiz = arvore.insercao(raiz, 40)
raiz = arvore.insercao(raiz, 50)
raiz = arvore.insercao(raiz, 25)

print("Uso para Demonstração:\n"
      "Números inseridos: 10 - 20 - 30 - 40 - 50 - 25 \n")

print("Organização da árvore em linha:")
arvore.exec(raiz)
 
