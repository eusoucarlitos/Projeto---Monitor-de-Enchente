class sensorAgua: 
    def __init__ (self, nome, altAtual, altLimite):
        self._nome = nome
        self._altAtual = altAtual
        self._altLimite = altLimite

    def getNome(self):
        return self._nome
    
    def LerAgua(self):
        return self._altAtual
