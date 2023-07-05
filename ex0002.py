class Artigo:
    def __init__ (self,titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def getArtigo(self):
        return f"Título: " + str(self.titulo) + " ; " + "Autor: " + str(self.autor)

class Edicao:
    def __init__ (self, numero, volume, data):
        self.numero = numero
        self.volume = volume
        self.data = data
        self.artigos = [ ] #Artigos da edição

    def addNovoArtigo(self,artigo):
        self.artigos.append(artigo) #append - adiciona ao vetor artigos

    def getEdicao(self): #Retorna as informações da edição
        return f"Edição: " + str(self.numero) + " ; " + "Volume: " + str(self.volume) + " ; " + "Data: " + str(self.data)

    def showArtigos(self): 
        for artigo in self.artigos:
            print(artigo.getArtigo()) 

    def getNumeroDeArtigo(self): #nº de artigos cadastrados
        return len(self.artigos)
    
    def RemoveArtigo(self,titulo):
        for artigo in self.artigos:
            if artigo.titulo == titulo:
                self.artigos.remove(artigo)

class Revista:
    def __init__ (self, titulo, issn, periodicidade):
        self.titulo =  titulo
        self.issn = issn
        self.periodicidade = periodicidade
        self.edicoes = [ ] 
    
    def addNovaEdicao(self, edicao): 
        num_artigos = edicao.getNumeroDeArtigo()
        if (num_artigos>=10 and num_artigos <=15):  #critério: de 10 a 15 artigos em uma edição
            self.edicoes.append(edicao)
            print("Edição lançada com sucesso!") 
        else:
            print("Para lançar uma edição são necessários no mínimo 10 artigos e no máximo 15 artigos.")

    def showEdicoes(self):
        for edicao in self.edicoes:
            print(edicao.getEdicao())




